# Python Service Manager

A generic, self-healing installer for deploying Python scripts as systemd services on Linux.

## Features
* **Interactive Setup:** Prompts for service name, user, and description.
* **Virtual Environments:** Automatically manages `venv` for both testing and production.
* **Secret Management:** Securely handles API keys using `.env.example` templates.
* **Self-Updating:** The installer checks for updates to itself during the upgrade process.
* **Git Integration:** Supports deploying specific branches (Main, Newest, or Custom).

## Prerequisites
* Linux (Mint, Ubuntu, Debian, Raspbian)
* Python 3 installed (`sudo apt install python3-venv`)
* Git

## Quick Start

1.  **Prepare your project:**
    Ensure your folder contains:
    * `upgrade.sh` (The installer)
    * `main.py` (Your python script)
    * `requirements.txt` (Dependencies)
    * `.env.example` (Optional: List of required API keys)

2.  **Make executable:**
    ```bash
    chmod +x upgrade.sh
    ```

3.  **Run the menu:**
    ```bash
    ./upgrade.sh
    ```

## Workflow
1.  **Test:** Select **Run Test**. This creates a temporary local environment and runs your script.
2.  **Cleanup:** Select **Cleanup Test** to remove the temporary files.
3.  **Install:** Select **Install Service**. This requires `sudo`. It will prompt you for configuration and create a persistent service in `/opt`.
4.  **Upgrade:** When you update your code on GitHub, run **Upgrade Service**. It will pull the latest code and restart the service.

## Configuration Files
* `service_config.env`: Stores non-sensitive installation settings (Service Name, Path, User).
* `secrets.env`: Stores sensitive API keys. **This file is never committed to Git.**
* `.env.example`: A template file you create to tell the installer which keys to ask for.

## Uninstalling
Run the script and select **Uninstall**. This will:
1.  Stop the systemd service.
2.  Remove the unit file from `/etc/systemd/system`.
3.  (Optionally) Delete the installation directory and all data.
