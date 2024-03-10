import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

# Create the main application
app = QApplication(sys.argv)

# Create a main window
window = QWidget()
window.setWindowTitle("My GUI")

# Create a label and a button
label = QLabel("Hello, World!")
button = QPushButton("Click me")

# Use a vertical layout to add the widgets to the main window
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

# Show the main window
window.show()

# Run the PyQt event loop
sys.exit(app.exec_())




