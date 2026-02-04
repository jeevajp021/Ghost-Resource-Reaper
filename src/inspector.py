import os
from datetime import datetime, timedelta
from azure.mgmt.monitor import MonitorManagementClient
from auth import get_azure_client

def get_vm_creator(resource_id):
    """
    Queries Activity Logs to find the email of the user who created the VM.
    """
    # We need a different client for Logs/Monitoring
    from azure.identity import DefaultAzureCredential
    credential = DefaultAzureCredential()
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    monitor_client = MonitorManagementClient(credential, subscription_id)

    # Define the time range (looking back 7 days)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=7)
    
    # Filter for the specific resource and the 'Write' (Create/Update) operation
    filter_str = (f"eventTimestamp ge '{start_time.isoformat()}' and "
                  f"eventTimestamp le '{end_time.isoformat()}' and "
                  f"resourceId eq '{resource_id}'")

    print(f" [?] Investigating logs for creator...")

    logs = monitor_client.activity_logs.list(filter=filter_str)

    for event in logs:
        # We look for the 'Administrative' event that indicates a resource write
        if event.submission_timestamp and event.caller:
            return event.caller  # This is usually the email address
            
    return "Unknown (Log expired or Service Principal)"

if __name__ == "__main__":
    # Test it with a dummy ID or a real one from your scanner
    print("Testing Inspector...")
    # example_id = "/subscriptions/.../resourceGroups/.../providers/Microsoft.Compute/virtualMachines/test"
    # print(f"Creator: {get_vm_creator(example_id)}")
