import requests
import json
import os

SLACK_WEBHOOK_URL = "your_slack_webhook_url"

def send_slack_notification(message):
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload))

send_slack_notification("🚨 Deployment failed! AI is analyzing the issue...")
    