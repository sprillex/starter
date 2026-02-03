# map
These are instructions for AI or human developers to ensure projects are started with a consistent workflow.
This was put together to speed up testing and as a base for multiple project formats.
Currently, I am focusing on Android and web service projects.
This project can be forked and used as desired.

All projects with a visible element should have a dark mode option.
See here for dark mode specifications dark_mode.md
All projects should have a method to back up configurations and databases. This has saved me a ton of time in testing.

## Android Projects

Android apps should use the workflows in the `workflows_examples` folder and modify them as needed to work for the specific project.

### GitHub Secrets for Workflows
The included workflows (e.g., `android_build.yml`, `branch_pr_alert.yml`) require the following secrets to be configured in your GitHub repository settings:

*   `PUSHOVER_APP_TOKEN`: Your Pushover Application Token.
*   `PUSHOVER_USER_KEY`: Your Pushover User Key.

These are used to send notifications about build status and repository activity.

## Python Projects

I have included a robust script management tool in the `python_tool` folder.

*   `python_tool/manage_service.sh`: A comprehensive lifecycle manager for Python systemd services. It handles testing, installation, upgrading, uninstallation, status checks, and logs.

### Usage
1.  Copy the contents of `python_tool` to your project root.
2.  Make the script executable: `chmod +x manage_service.sh`
3.  Run the script: `./manage_service.sh`

The script will guide you through creating a configuration file (`service_config.env`) and managing secrets (`secrets.env` based on `.env.example`).

**Advanced Features:**
*   **Dynamic Port Selection:** Automatically checks availability and recommends ports. Uses `common_ports_do_not_use.csv` to avoid conflicts.
*   **Automated Backups:** Specify files to back up automatically before every upgrade.
*   **Appliance Mode:** Optional "Git Force Reset" mode to ensure the deployed code always exactly matches the repository (discarding local changes).
*   **Health Checks:** Optional configuration to automatically verify service connectivity (via curl) after restart.

See `python_tool/install.md` for more detailed instructions.
