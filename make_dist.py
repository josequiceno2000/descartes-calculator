# make_dist.py
import os
import shutil
import tarfile

def build_distribution():
    dist_name = "descartes-calculator-linux"
    build_dir = os.path.abspath(f"./{dist_name}")
    
    # 1. Clean previous build folders
    print("🧹 Cleaning up old artifacts...")
    for path in [build_dir, "./build", "./dist", f"./{dist_name}.tar.gz"]:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    # 2. Compile the binary using PyInstaller
    print("📦 Compiling standalone binary with PyInstaller...")
    pyinstaller_cmd = (
        "./descartes/bin/python -m PyInstaller --onefile --windowed "
        '--add-data "assets:assets" main.py'
    )
    if os.system(pyinstaller_cmd) != 0:
        print("❌ PyInstaller compilation failed!")
        return

    # 3. Create the structure for the distribution bundle
    print("📁 Creating distribution structure...")
    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(os.path.join(build_dir, "assets"), exist_ok=True)

    # Copy files into the bundle folder
    shutil.copy("./dist/main", os.path.join(build_dir, "descartes-calculator"))
    shutil.copy("./assets/descartes-logo--app.svg", os.path.join(build_dir, "assets"))

    # 4. Generate a smart client-side installer script
    print("📝 Writing installer script...")
    installer_content = """#!/usr/bin/env bash
# Installer for Descartes Calculator
set -e

APP_DIR="$HOME/.local/share/descartes-calculator"
BIN_DIR="$HOME/.local/bin"
LAUNCHER_DIR="$HOME/.local/share/applications"

echo "🚀 Installing Descartes Calculator..."

# Create necessary directories
mkdir -p "$APP_DIR/assets"
mkdir -p "$BIN_DIR"
mkdir -p "$LAUNCHER_DIR"

# Copy binary and icon assets
cp descartes-calculator "$APP_DIR/"
cp assets/descartes-logo--app.svg "$APP_DIR/assets/"
chmod +x "$APP_DIR/descartes-calculator"

# Create a symlink in user's local path
ln -sf "$APP_DIR/descartes-calculator" "$BIN_DIR/descartes-calculator"

# Generate the .desktop menu launcher entry dynamically
cat << EOF > "$LAUNCHER_DIR/descartes-calculator.desktop"
[Desktop Entry]
Type=Application
Version=1.0
Name=Descartes Calculator
Comment=Standalone Geometry & Math Calculator
Exec=$APP_DIR/descartes-calculator
Icon=$APP_DIR/assets/descartes-logo--app.svg
Terminal=false
Categories=Utility;Math;Development;
StartupNotify=true
EOF

chmod +x "$LAUNCHER_DIR/descartes-calculator.desktop"

# Force desktop manager to refresh its menu icons
touch "$LAUNCHER_DIR/descartes-calculator.desktop"

echo "🎉 Installation complete!"
echo "✨ You can now open 'Descartes Calculator' directly from your system app menu."
"""
    
    installer_path = os.path.join(build_dir, "install.sh")
    with open(installer_path, "w") as f:
        f.write(installer_content)
    os.chmod(installer_path, 0o755) # Make installer executable

    # 5. Compress everything into a tarball archive
    tarball_name = f"{dist_name}.tar.gz"
    print(f"🗜️  Archiving bundle into {tarball_name}...")
    with tarfile.open(tarball_name, "w:gz") as tar:
        tar.add(build_dir, arcname=os.path.basename(build_dir))

    # Clean up temporary build structure folder, leaving only the package
    shutil.rmtree(build_dir)
    print(f"\n✅ Done! Your distribution file is ready: {os.path.abspath(tarball_name)}")

if __name__ == "__main__":
    build_distribution()
