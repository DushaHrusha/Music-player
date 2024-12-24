import sys

from main import SimpleMusicPlayer
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = SimpleMusicPlayer()
sys.exit(app.exec())


