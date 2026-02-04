import logging
import os
from datetime import datetime

# 🔧 Ensure logs directory exists BEFORE logging starts
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename='logs/reaper_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_action(vm_name, user, action):
    msg = f"Target: {vm_name} | User: {user} | Action: {action}"
    logging.info(msg)
    print(f" [Log] {msg}")
