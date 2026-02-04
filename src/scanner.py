from auth import get_azure_client
from inspector import get_vm_creator

def scan_vms():
    client = get_azure_client()
    if not client:
        return

    print("--- Starting Resource Scan ---")
    
    # 1. List all VMs in the subscription
    vms = client.virtual_machines.list_all()
    
    zombies = []

    for vm in vms:
        print(f"Checking VM: {vm.name}...")
        
        # 2. Extract Tags
        tags = vm.tags if vm.tags else {}
        owner = tags.get('Owner') or tags.get('owner')

        if not owner:
            print(f" [!] Alert: {vm.name} has NO Owner tag.")
            
            # 3. GET THE DISK ID (Crucial for the Reaper to create snapshots)
            # We drill down into the storage profile to find the managed disk ID
            disk_id = vm.storage_profile.os_disk.managed_disk.id
            
            # 4. CALL THE INSPECTOR for log-based attribution
            actual_creator = get_vm_creator(vm.id)
            print(f" [*] Evidence Found: Last active user appears to be {actual_creator}")
            
            zombies.append({
                "name": vm.name,
                "id": vm.id,
                "disk_id": disk_id,        # Added this field
                "location": vm.location,
                "reason": "Missing Owner Tag",
                "creator": actual_creator,
                "resource_group": vm.id.split('/')[4]
            })
            
    return zombies

if __name__ == "__main__":
    found = scan_vms()
    for z in found:
        print(f"\nTarget: {z['name']} | Disk: {z['disk_id']}")
    print(f"\nScan complete. Found {len(found)} zombie resources.")
