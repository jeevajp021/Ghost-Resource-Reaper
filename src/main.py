from concurrent.futures import ThreadPoolExecutor # MODIFICATION: For performance
from scanner import scan_vms
from reaper import safe_reap
from utils import log_action
from notifier import send_slack_alert

# SAFETY SWITCH
DRY_RUN = False 

def process_zombie(ghost):
    """Handles the lifecycle of a single zombie resource"""
    vm_name = ghost['name']
    creator = ghost['creator']
    rg = ghost['resource_group']
    
    if DRY_RUN:
        print(f" [DRY RUN] Would reap {vm_name} (Owner: {creator})")
        print(f" [DRY RUN] Target Disk: {disk}")
    else:
        # 1. Execution
        success = safe_reap(vm_name, rg, ghost['disk_id'], ghost['location'])
        
        if success:
            # 2. Logging
            log_action(vm_name, creator, "Deallocated & Snapshotted")
            
            # 3. Notification (The UI component)
            send_slack_alert(vm_name, creator, "Resource stopped due to missing tags. Snapshot created for safety.")

def run_orchestrator():
    print(f"--- GHOST RESOURCE REAPER STARTING (DRY_RUN={DRY_RUN}) ---")
    
    zombies = scan_vms()
    
    if not zombies:
        print("No zombies found. Cloud is clean!")
        return

    # MODIFICATION: Use Parallel Processing for efficiency
    print(f"Processing {len(zombies)} targets in parallel...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(process_zombie, zombies)

if __name__ == "__main__":
    run_orchestrator()
