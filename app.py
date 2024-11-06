import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

from main import draw_image

class FileDialogExample(QMainWindow):

    def __init__(self):
        super().__init__()
        self.desktop = QDesktopWidget()
        screen_rect = self.desktop.screenGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()

        self.setWindowTitle("Pics GridLayout")
        self.setGeometry(100, 100, int(screen_width / 2), int(screen_height / 2))
        self.setStyleSheet("background-color: #424141; color: white;")

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        mainLayout = QVBoxLayout(central_widget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(10)

        # Header label with increased font size and centered text
        headerLabel = QLabel("Pics GridLayout")
        headerLabel.setStyleSheet("background-color: #424141; color: white; font-size: 24px; padding: 10px;")
        headerLabel.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(headerLabel)

        # Create a grid layout for the buttons
        buttonLayout = QGridLayout()
        buttonLayout.setContentsMargins(40, 40, 40, 40)
        buttonLayout.setSpacing(20)

        # Define the button size
        button_size = QSize(150, 150)  # Size for each button

        # Create buttons with icons and set size
        buttonLayout1 = QPushButton()
        buttonLayout1.setIcon(QIcon(self.resource_path("buttonLayout1.jpg")))
        buttonLayout1.setIconSize(button_size)
        buttonLayout1.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        buttonLayout1.setFixedSize(button_size)
        buttonLayout1.clicked.connect(lambda: self.open_file_dialog("Layout 1"))  # Pass a parameter

        buttonLayout2 = QPushButton()
        buttonLayout2.setIcon(QIcon(self.resource_path("buttonLayout2.jpg")))
        buttonLayout2.setIconSize(button_size)
        buttonLayout2.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        buttonLayout2.setFixedSize(button_size)
        buttonLayout2.clicked.connect(lambda: self.open_file_dialog("Layout 2"))  # Pass a parameter

        # Repeat for other buttons...
        buttonLayout3 = QPushButton()
        buttonLayout3.setIcon(QIcon(self.resource_path("buttonLayout3.png")))
        buttonLayout3.setIconSize(button_size)
        buttonLayout3.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        buttonLayout3.setFixedSize(button_size)
        buttonLayout3.clicked.connect(lambda: self.open_file_dialog("Layout 3"))

        buttonLayout4 = QPushButton()
        buttonLayout4.setIcon(QIcon(self.resource_path("buttonLayout4.png")))
        buttonLayout4.setIconSize(button_size)
        buttonLayout4.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        buttonLayout4.setFixedSize(button_size)
        buttonLayout4.clicked.connect(lambda: self.open_file_dialog("Layout 4"))

        buttonLayout6 = QPushButton()
        buttonLayout6.setIcon(QIcon(self.resource_path("buttonLayout6.png")))
        buttonLayout6.setIconSize(button_size)
        buttonLayout6.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        buttonLayout6.setFixedSize(button_size)
        buttonLayout6.clicked.connect(lambda: self.open_file_dialog("Layout 6"))

        buttonLayout8 = QPushButton()
        buttonLayout8.setIcon(QIcon(self.resource_path("buttonLayout8.png")))
        buttonLayout8.setIconSize(button_size)
        buttonLayout8.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        buttonLayout8.setFixedSize(button_size)
        buttonLayout8.clicked.connect(lambda: self.open_file_dialog("Layout 8"))

        buttonLayout9 = QPushButton()
        buttonLayout9.setIcon(QIcon(self.resource_path("buttonLayout9.png")))
        buttonLayout9.setIconSize(button_size)
        buttonLayout9.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        buttonLayout9.setFixedSize(button_size)
        buttonLayout9.clicked.connect(lambda: self.open_file_dialog("Layout 9"))

        # Add buttons to the grid layout
        buttonLayout.addWidget(buttonLayout1, 0, 0)
        buttonLayout.addWidget(buttonLayout2, 0, 1)
        buttonLayout.addWidget(buttonLayout3, 1, 0)
        buttonLayout.addWidget(buttonLayout4, 1, 1)
        buttonLayout.addWidget(buttonLayout6, 2, 0)
        buttonLayout.addWidget(buttonLayout8, 2, 1)
        buttonLayout.addWidget(buttonLayout9, 3, 0)

        # Add the button layout to the main layout
        mainLayout.addLayout(buttonLayout)

    def open_file_dialog(self, layout):
        options = QFileDialog.Options()
        # Allow multiple file selection
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, f"Select images for {layout}", "", "Images (*.jpg *.png);;All Files (*)", options=options
        )

        if file_paths:
            # Collecting titles from the user
            title1, ok1 = QInputDialog.getText(self, "Input Dialog", "Please enter first title:")
            title2, ok2 = QInputDialog.getText(self, "Input Dialog", "Please enter second title:")

            # Check if both dialogs were confirmed
            if ok1 and ok2:
                titles = [title1, title2]
                # Call the draw_image function with the selected layout, titles, and file paths
                draw_image(layout, titles, file_paths)
            else:
                QMessageBox.warning(self, "Input Canceled", "Operation canceled by the user.")
        else:
            QMessageBox.warning(self, "No Selection", "No files were selected.")

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temporary folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDialogExample()
    window.show()
    sys.exit(app.exec_())
