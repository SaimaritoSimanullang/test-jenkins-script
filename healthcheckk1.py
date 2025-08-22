import psycopg2
import requests
import os
from datetime import datetime, timezone, timedelta

# DB Config ambil dari env juga
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": os.environ.get("DB_PORT", "5432"),
    "dbname": os.environ.get("DB_NAME", "nodes_db"),
    "user": os.environ.get("DB_USER", "postgres"),
    "password": os.environ.get("DB_PASS", "postgres")
}

# Slack Webhook dari env
SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK")

def send_alert(node_id, last_check):
    message = f":rotating_light: Node {node_id} last healthcheck {last_check}, lebih dari 3 menit!"
    requests.post(SLACK_WEBHOOK, json={"text": message})

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT id, last_healthcheck FROM public.node;")
    nodes = cur.fetchall()

    now = datetime.now(timezone.utc)

    for node_id, last_check in nodes:
        if last_check is None or now - last_check > timedelta(minutes=3):
            send_alert(node_id, last_check)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
