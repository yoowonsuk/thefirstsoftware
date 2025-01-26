#pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize() + '.')


app = QApplication([])
window = Widget()
window.setWindowTitle('Sentence Maker')

layout = QVBoxLayout()
#layout = QHBoxLayout()

text = QLineEdit()
layout.addWidget(text)

'''
text = QLineEdit()
layout.addWidget(text)
'''

btn = QPushBotton('Make')
layout.addWidget(btn)

btn.clicked.connect(make_sentence)

output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
