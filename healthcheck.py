import psycopg2
import requests
from datetime import datetime, timezone, timedelta
import os
# Konfigurasi DB
DB_CONFIG = {
    "host": os.environ.get("HOST", "localhost"),
    "port": os.environ.get("PORT", "5433"),
    "dbname": os.environ.get("DBNAME", "postgres"),
    "user": os.environ.get("USER", "postgres"),
    "password": os.environ.get("PASSWORD", "1234"),
}
# Slack Webhook URL
SLACK_WEBHOOK = "https://hooks.slack.com/services/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"
def send_slack_alert(node_name, last_healthcheck):
    message = {
        "text": f":warning: Node *{node_name}* terakhir healthcheck pada {last_healthcheck}, sudah lebih dari 3 menit!"
    }
    form_data = {
        'payload': message,
    }
    response = requests.post(SLACK_WEBHOOK, data=form_data)
    print(response.status_code)
    
def main():
    print("host", DB_CONFIG["host"])
    print("port", DB_CONFIG["port"])
    print("dbname", DB_CONFIG["dbname"])
    print("user", DB_CONFIG["user"])

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    # Ambil semua node
    cursor.execute("SELECT id, name, last_healthcheck FROM \"public\".\"node\"")
    nodes = cursor.fetchall()
    now = datetime.now(timezone.utc)
    for node_id, name, last_healthcheck in nodes:
        print("node_id", node_id, "name", name, "last_healthcheck", last_healthcheck)
        if last_healthcheck is None:
            send_slack_alert(name, "Belum pernah")
            continue
        # Cek selisih waktu
        if now - last_healthcheck > timedelta(minutes=3):
            send_slack_alert(name, last_healthcheck)
        send_slack_alert(name, last_healthcheck)  # untuk testing uhuy      
    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()











