import sys

from PyQt5.QtWidgets import QApplication

from main import SimpleMusicPlayer


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = SimpleMusicPlayer()
sys.exit(app.exec())


