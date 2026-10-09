# create_launcher.py
import os

def create_desktop_file():
    # Get absolute paths to your project files
    current_dir = os.path.abspath(".")
    exec_path = os.path.join(current_dir, "dist", "main")
    
    # Try PNG first, fallback to SVG if that's what you have on disk
    icon_path = os.path.join(current_dir, "assets", "descartes-logo--app.svg")
    
    desktop_content = f"""[Desktop Entry]
Type=Application
Version=1.0
Name=Descartes Calculator
Comment=Standalone Geometry & Math Calculator
Exec={exec_path}
Icon={icon_path}
Terminal=false
Categories=Utility;Math;Development;
StartupNotify=true
"""

    # Linux standard path for user application shortcuts
    launcher_dir = os.path.expanduser("~/.local/share/applications")
    os.makedirs(launcher_dir, exist_ok=True)
    launcher_path = os.path.join(launcher_dir, "descartes-calculator.desktop")

    with open(launcher_path, "w") as f:
        f.write(desktop_content)

    # Give the launcher execution permissions
    os.chmod(launcher_path, 0o755)
    print(f"🎉 Launcher created successfully at: {launcher_path}")
    print("✨ You can now search for 'Descartes Calculator' in your system app menu!")

if __name__ == "__main__":
    create_desktop_file()
