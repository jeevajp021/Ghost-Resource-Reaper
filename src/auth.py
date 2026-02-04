import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# 1. Load the secrets from .env
load_dotenv()

def get_azure_client():
    """
    Authenticates securely and returns a Compute client.
    """
    try:
        # 2. DefaultAzureCredential automatically looks for your 
        # AZURE_CLIENT_ID, SECRET, and TENANT environment variables.
        credential = DefaultAzureCredential()
        
        subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        
        # 3. Create the management client
        client = ComputeManagementClient(credential, subscription_id)
        
        print("Successfully authenticated with Azure!")
        return client
    except Exception as e:
        print(f"Authentication Failed: {e}")
        return None

if __name__ == "__main__":
    # Test the connection
    get_azure_client()
