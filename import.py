import requests
from datetime import datetime, timedelta

# Contoh node list (nanti bisa diganti query DB)
nodes = {
    "10.90.0.23": datetime.now() - timedelta(minutes=4),
    "10.90.0.90": datetime.now() - timedelta(minutes=1)
}

# Slack webhook
SLACK_WEBHOOK = "https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX"

def send_slack_alert(node_ip, last_check):
    msg = {"text": f":rotating_light: Node {node_ip} tidak update >3 menit!\nLast check: {last_check}"}
    try:
        requests.post(SLACK_WEBHOOK, json=msg, timeout=1)  # timeout 1s
    except requests.exceptions.Timeout:
        print(f"Slack timeout untuk node {node_ip}")

for ip, last_check in nodes.items():
    delta = (datetime.now() - last_check).total_seconds()
    if delta > 180:
        send_slack_alert(ip, last_check)
    else:
        print(f"Node {ip} OK")
