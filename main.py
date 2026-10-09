import sys
import os
import ctypes
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon

os.environ["GDK_BACKEND"] = "x11"

os.environ["QT_QT_PLUGIN_VERIFY_THEME"] = "0"

if sys.platform.startswith('linux'):
  try:
    ctypes.CDLL('libX11.so.6').XInitThreads()
  except Exception:
    pass

def get_asset_path(relative_path: str) -> str:
  """ Get absolute path to resource, working for dev and PyInstaller"""
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

def main():
  app = QApplication(sys.argv)
  icon_path = get_asset_path("assets/descartes-logo--app.png")
  
  window = QWidget()
  window.setWindowTitle("Descartes Calculator")
  window.setWindowIcon(QIcon(icon_path))

  layout = QVBoxLayout()
  label = QLabel("Welcome to Descartes!", window)
  layout.addWidget(label)
  window.setLayout(layout)

  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()