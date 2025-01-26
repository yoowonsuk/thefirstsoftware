#pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup #pip install beautifulsoup4
import requests # pip install requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1#google_vignette' # placeholder
    #print(url)
    content = requests.get(url).text # source code = HTML, CSS, JavaScript
    soup = BeautifulSoup(content, 'htmp.parser')
    rate = soup.find('span', class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    print(currency)
    #print(type(currency))
    return rate


def show_currency():
    input_text = float(text.text())
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentTest()
    rate = get_currency(in_cur, target_cur)
    output = round(input_text * rate, 2)
    message = f'{input_text} {in_cur} is {output} {target_cur}'
    output_label.setText(str(message))


app = QApplication([])
window = Widget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()
#layout = QHBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

output_label = QLabel('')
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)


in_combo = QComboBox()
currencies = ['USD', 'EUR', 'INR']
incombo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo = QComboBox()
incombo.addItems(currencies)
layout2.addWidget(target_combo)

text = QLineEdit()
layout3.addWidget(text)

'''
text = QLineEdit()
layout.addWidget(text)
'''

btn = QPushBotton('Converter')
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)

btn.clicked.connect(show_currency)

window.setLayout(layout)
window.show()
app.exec()
