import time
from auth import get_azure_client

def safe_reap(vm_name, resource_group, os_disk_id, location): # MODIFICATION: Added location
    try:
        client = get_azure_client()
        print(f" [!] Initiating SAFE REAP for {vm_name} in {location}...")

        # 1. Power Off (Deallocate)
        print(f" [1/2] Powering off VM...")
        async_stop = client.virtual_machines.begin_deallocate(resource_group, vm_name)
        async_stop.wait() 

        # 2. Create a Snapshot in the SAME location as the VM
        snapshot_name = f"{vm_name}-backup-{int(time.time())}"
        print(f" [2/2] Creating safety snapshot: {snapshot_name}...")
        
        snapshot_config = {
            "location": location, # MODIFICATION: Dynamic location mapping
            "creation_data": {
                "create_option": "Copy",
                "source_resource_id": os_disk_id
            },
            "tags": {"CreatedBy": "Ghost-Reaper-Automation"} # MODIFICATION: Added audit tags
        }
        
        async_snapshot = client.snapshots.begin_create_or_update(
            resource_group, 
            snapshot_name, 
            snapshot_config
        )
        async_snapshot.wait()

        print(f" [✓] VM {vm_name} is deallocated and backed up.")
        return True
        
    except Exception as e:
        print(f" [X] Error reaping {vm_name}: {str(e)}")
        return False
