# 👻 Ghost-Resource Reaper: Secure Cloud FinOps Automation

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Azure](https://img.shields.io/badge/cloud-Azure-0089D6)

### 📌 The Problem: "Cloud Sprawl"
In large-scale cloud environments, developers often provision Virtual Machines (VMs) for testing and forget to deallocate them. These **"Zombie Resources"** continue to accrue costs, often totaling thousands of dollars in wasted monthly spend.

### 🚀 The Solution: Forensic Automation
The **Ghost-Resource Reaper** is a Python-based automation engine that doesn't just identify idle resources—it **investigates** them. Using Azure Activity Log forensics, it attributes untagged resources to their original creators, performs a safety-first snapshot, and deallocates the resource to stop billing.

---

## 🛠️ Key Features
* **Forensic Attribution:** Queries Azure Monitor/Activity Logs to identify the 'Caller' (Email/SPN) of untagged resources.
* **Safety-First Policy:** Automatically creates a persistent Disk Snapshot before deallocation to ensure zero data loss.
* **Security-First Auth:** Implements `DefaultAzureCredential` for secure, certificate-based or environment-based authentication (No hardcoded secrets).
* **Dry-Run Capability:** Includes a safety switch to simulate actions before making live changes to infrastructure.
* **Audit Logging:** Maintains a detailed `reaper_audit.log` for compliance and security tracking.

---

## 📊 Business Impact (ROI)
| Metric | Impact |
| :--- | :--- |
| **Cost Savings** | Est. **$8,400/year** (per 10 orphaned B2s instances) |
| **Risk Mitigation** | 100% Data Retention via automated pre-reap snapshots |
| **Accountability** | Direct Slack/Email notification to the resource owner |

---

## 🏗️ Architecture
The engine follows a modular event-driven logic:
1. **Scanner:** Identifies VMs missing the `Owner` tag.
2. **Inspector:** Performs forensic log analysis to find the creator's identity.
3. **Reaper:** Executes deallocation and safety snapshotting.
4. **Notifier:** (Optional) Alerts the owner via Slack Webhook.



---

## 🚦 Getting Started

### 1. Prerequisites
* Python 3.9+
* Azure CLI (`az login`)
* An Azure Service Principal with `Contributor` permissions.

### 2. Installation
```bash
git clone [https://github.com/YOUR_USERNAME/Ghost-Resource-Reaper.git](https://github.com/YOUR_USERNAME/Ghost-Resource-Reaper.git)
cd Ghost-Resource-Reaper
pip install -r requirements.txt

```

### 3. Configuration

Create a `.env` file in the root directory:

```text
AZURE_CLIENT_ID="your-app-id"
AZURE_CLIENT_SECRET="your-password"
AZURE_TENANT_ID="your-tenant-id"
AZURE_SUBSCRIPTION_ID="your-sub-id"

```

---

## 🛡️ Security & Compliance

This project follows the **Principle of Least Privilege**. It is designed to run via a Service Principal with scope-limited access to specific Resource Groups, ensuring it cannot touch production-critical infrastructure.

```

