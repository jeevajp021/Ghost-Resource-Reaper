import os
import requests

def send_slack_alert(vm_name, creator_email, action_taken):
    """
    Sends a notification to a Slack webhook.
    """
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print(" [!] Slack Webhook not configured, skipping notification.")
        return

    message = {
        "text": "🚨 *Ghost-Resource Reaper Alert* 🚨",
        "attachments": [
            {
                "color": "#ff0000",
                "fields": [
                    {"title": "Resource", "value": vm_name, "short": True},
                    {"title": "Owner", "value": creator_email, "short": True},
                    {"title": "Action", "value": action_taken, "short": False},
                ],
                "footer": "Cloud Cost Optimization Engine"
            }
        ]
    }

    response = requests.post(webhook_url, json=message)
    if response.status_code == 200:
        print(f" [✓] Notification sent to {creator_email} via Slack.")
