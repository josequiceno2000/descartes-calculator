import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

os.environ["GDK_BACKEND"] = "x11"

def main():
  app = QApplication(sys.argv)

  window = QWidget()
  window.setWindowTitle("Descartes Calculator")
  window.resize(400, 300)

  layout = QVBoxLayout()
  label = QLabel("Welcome to Descartes!", window)
  layout.addWidget(label)
  window.setLayout(layout)

  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()