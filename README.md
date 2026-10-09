# descartes-calculator
A virtual calculator to rival the HP Prime Graphing Calculator.

## 🚀 Installation on Linux

This application is distributed as a standalone portable package. It **does not require Python** or any dependencies to be installed on your computer.

### 📥 Step 1: Download the Package

Click the link below to get the latest pre-compiled bundle directly:

➡️ **[Download Latest Release (descartes-calculator-linux.tar.gz)](https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>/releases/latest/download/descartes-calculator-linux.tar.gz)**

---

### ⚙️ Step 2: Install via Terminal

Once downloaded, open your terminal, navigate to your `Downloads` folder, and run the following three commands to install it to your user space:

```bash
# 1. Extract the package
tar -xzf descartes-calculator-linux.tar.gz

# 2. Enter the installation directory
cd descartes-calculator-linux

# 3. Run the automated installer script
./install.sh
```

---

### What the Installer Does
The `install.sh` script automates the desktop setup without requiring administrative (`sudo`) privileges. It performs the following steps:
* **Application Binary:** Copies the standalone executable into `~/.local/share/descartes-calculator/`.
* **System Path Integration:** Generates a system shortcut in `~/.local/bin/` so you can launch the app directly from your terminal by typing `descartes-calculator`.
* **Desktop Environment Launcher:** Creates a native desktop launcher shortcut (`.desktop` entry) inside `~/.local/share/applications/` so the app appears instantly in your system's Application Menu (GNOME, KDE, etc.) with its high-resolution vector icon.

---

### 🖥️ Launching the Application

Once installed, you can launch the application in two ways:
1. **Application Menu:** Open your system’s activities/applications overview, search for **Descartes Calculator**, and click the icon. You can also right-click it to pin it to your desktop dock or favorites sidebar.
2. **Terminal:** Open a terminal and simply type:
   ```bash
   descartes-calculator
   ```
