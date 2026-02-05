# 👻 Ghost-Resource Reaper: Secure Cloud FinOps Automation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cloud: Azure](https://img.shields.io/badge/Cloud-Azure-0089D6?logo=microsoft-azure)](https://azure.microsoft.com/)

### 📌 The Problem: "Cloud Sprawl"

In large-scale cloud environments, developers often provision Virtual Machines (VMs) for testing and forget to deallocate them. These **"Zombie Resources"** lead to "Cloud Sprawl," costing companies thousands of dollars in unnecessary spend.

### 🚀 The Solution: Forensic Automation

The **Ghost-Resource Reaper** is a Python-based automation engine that doesn't just identify idle resources—it **investigates** them. Using Azure Activity Log forensics, it attributes untagged resources to their original creators, performs a safety-first snapshot, and deallocates the resource to stop billing.

---

## 🏗️ Architecture & Workflow

The engine follows a modular, parallel-processed logic:

1. **Scanner:** Identifies VMs missing the required `Owner` tag.
2. **Inspector:** Performs forensic log analysis via Azure Monitor/Activity Logs to find the creator's identity.
3. **Reaper:** Executes a "Safe-Stop" (Deallocate + Snapshot) using concurrent threads.
4. **Notifier:** (Optional) Alerts the owner via Slack Webhook for real-time accountability.

---

## 🛠️ Tech Stack

* **Language:** Python 3.13
* **SDKs:** `azure-mgmt-compute`, `azure-mgmt-monitor`, `azure-identity`
* **Security:** Service Principal (RBAC), `DefaultAzureCredential`
* **Performance:** Multi-threaded execution via `concurrent.futures`

---

## 🌟 Key Features

* **Forensic Attribution:** Queries Azure Audit Trails to identify the 'Caller' email of untagged resources.
* **Safety-First Policy:** Automatically creates a persistent Disk Snapshot before deallocation to ensure zero data loss.
* **Security-First Auth:** Implements secure authentication (No hardcoded secrets) using environment variables.
* **Dry-Run Capability:** Includes a safety switch (`DRY_RUN = True`) to simulate actions without affecting live infrastructure.
* **Audit Logging:** Maintains a detailed `reaper_audit.log` for compliance and security tracking.

---

## 📊 Business Impact (ROI)

| Metric | Impact |
| --- | --- |
| **Cost Savings** | Est. **$8,400/year** (per 10 orphaned B2s instances) |
| **Risk Mitigation** | 100% Data Retention via automated pre-reap snapshots |
| **Accountability** | Direct attribution even when resources are not tagged |

---

## 🚦 Getting Started

### 1. Prerequisites

* Python 3.9+
* Azure CLI installed (`az login`)
* Service Principal with `Contributor` permissions on target Resource Groups.

### 2. Installation

```bash
git clone https://github.com/YOUR_USERNAME/Ghost-Resource-Reaper.git
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
SLACK_WEBHOOK_URL="your-webhook-optional"
```

---

## 🛡️ Security & Compliance

This project follows the **Principle of Least Privilege**. It is designed to run via a Service Principal with scope-limited access, ensuring it cannot touch production-critical infrastructure.

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

## ⚠️ Disclaimer

*This project is for educational and demo purposes. While it includes safety features like snapshots, always test in a sandbox environment before running on production workloads.*

