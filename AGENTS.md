# AGENTS.md

This file serves as the **Master Instruction Set** for any AI agent working on this project or projects derived from it. You **must** read and follow these directives before making any changes.

## 1. Core Principles

*   **Structure First:** Before writing code, ensure the project structure matches the templates defined here.
*   **Documentation:** Every major component (Python service, Android app, Web app) must have a corresponding README section or file explaining how to run, test, and deploy it.
*   **Safety:** Never commit `secrets.env` or `.env` files. Always use `.env.example` templates.
*   **Consistency:** Use the provided workflows and scripts (`manage_service.sh`) rather than inventing new deployment methods.

## 2. Python Projects (Systemd Services)

When working on a Python backend or systemd service:

### 2.1 Service Management
*   **Mandatory Script:** You **must** use the `manage_service.sh` script (found in `python_tool/`) for service lifecycle management.
    *   It handles: Virtual Environments, Systemd Unit creation, Updates, and Uninstallation.
*   **No Manual Systemd:** Do not write separate `.service` files manually unless strictly necessary. Rely on the script generator.

### 2.2 Port Selection
*   **Check Availability:** Before hardcoding a port or suggesting one to the user, you **must** consult `python_tool/common_ports_do_not_use.csv`.
*   **Avoid Conflicts:** Do not use ports listed in that file (e.g., 5000, 8080, 3000) for production services if possible. Suggest alternatives (e.g., 5001, 8090).
*   **Dynamic Config:** Ports should be configurable via environment variables (`PORT`), not hardcoded.

### 2.3 Secrets & Configuration
*   **Templates:** If your code requires API keys, you **must** update (or create) `.env.example`.
*   **Loading:** Your Python code should load environment variables (e.g., using `python-dotenv` or `os.environ`).
*   **Exclusion:** Ensure `secrets.env` and `.env` are in `.gitignore`.

### 2.4 Backup Policy
*   **Critical Files:** Identify files that store state (databases, JSON storage).
*   **Config:** Add these filenames to the `BACKUP_FILES` variable in `service_config.env` (managed via the script menu) so they are backed up during upgrades.

## 3. Android Projects

When working on Android applications:

### 3.1 Workflows
*   **GitHub Actions:** Ensure the project includes the standard workflows from `workflows_examples/` (specifically `android_build.yml`).
*   **Secrets:** Remind the user to configure `PUSHOVER_APP_TOKEN` and `PUSHOVER_USER_KEY` in GitHub Secrets for build notifications.

### 3.2 Dark Mode
*   **Mandatory:** All Android apps must support Dark Mode.
*   **Specs:** Follow the guidelines in `dark_mode.md` (or the Android equivalent if specified there).
    *   Avoid pure black (`#000000`) for backgrounds; use dark grey (`#121212`).
    *   Use elevation to show depth.

## 4. Web Applications

### 4.1 Dark Mode Implementation
*   **Strict Adherence:** You **must** follow the implementation details in `dark_mode.md`.
*   **Key Rules:**
    *   **No Pure Black:** Use `#121212` for the body background.
    *   **Elevation:** Use lighter greys (e.g., `#1e1e1e`, `#2d2d2d`) for cards and modals.
    *   **Text:** Use white with opacity (87%, 60%) instead of grey hex codes.
    *   **FOUC Prevention:** Include the blocking script in `<head>` to prevent white flashes on load.

## 5. Workflow Automation

*   **Pushover Integration:** Use `notify_new_work.yml` and `branch_pr_alert.yml` to keep the user informed of repository activity.
*   **OpenAPI:** If the project exposes an API, use `update_openapi.yml` to keep documentation in sync.

## 6. Project Setup Checklist

When initializing a new project based on this repo:

1.  [ ] Copy `python_tool/` to the root (if Python).
2.  [ ] Copy relevant workflows from `workflows_examples/` to `.github/workflows/`.
3.  [ ] Create `AGENTS.md` (copy this file or a summarized version).
4.  [ ] Ensure `.gitignore` is set up correctly for the language/framework.
5.  [ ] Verify `dark_mode.md` principles are applied to UI designs.
6.  [ ] If using AI features, consult `AI_IMPLEMENTATION.md`.

## 7. AI Integration

*   **Implementation Guide:** For projects requiring AI capabilities (specifically Gemini), you **must** follow the instructions in `AI_IMPLEMENTATION.md`.
*   **Prompt Management:** Use `prompts_examples/learning.txt` as a template for prompt structure and storage.
*   **Boilerplate:** Use `python_tool/ai_example.py` for correct API client initialization and response handling (especially for `asyncio` compatibility).
