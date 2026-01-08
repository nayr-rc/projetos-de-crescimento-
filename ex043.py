import sys
from PyQt5.QtWidgets import (
	QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt


# Tela principal do banco
class MainWindow(QWidget):
	def __init__(self, username):
		super().__init__()
		self.setWindowTitle('Banco - Conta do Cliente')
		self.setFixedSize(400, 500)
		self.setStyleSheet('background-color: #f5f6fa; border-radius: 15px;')
		self.username = username
		self.init_ui()

	def init_ui(self):
		title = QLabel(f'Olá, {self.username}!')
		title.setFont(QFont('Segoe UI', 18, QFont.Bold))
		title.setAlignment(Qt.AlignCenter)
		title.setStyleSheet('color: #273c75; margin-bottom: 20px;')

		saldo_label = QLabel('Saldo disponível:')
		saldo_label.setFont(QFont('Segoe UI', 13))
		saldo_label.setStyleSheet('color: #353b48;')
		self.saldo = 3250.75
		saldo_valor = QLabel(f'R$ {self.saldo:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
		saldo_valor.setFont(QFont('Segoe UI', 22, QFont.Bold))
		saldo_valor.setStyleSheet('color: #44bd32; margin-bottom: 25px;')

		extrato_label = QLabel('Extrato recente:')
		extrato_label.setFont(QFont('Segoe UI', 13, QFont.Bold))
		extrato_label.setStyleSheet('color: #353b48; margin-top: 20px;')

		# Simulação de extrato
		extrato = [
			('Depósito', 1000.00, '05/01/2026'),
			('Transferência recebida', 500.00, '03/01/2026'),
			('Pagamento', -200.00, '02/01/2026'),
			('Saque', -50.00, '01/01/2026'),
		]
		extrato_vbox = QVBoxLayout()
		for desc, valor, data in extrato:
			cor = '#44bd32' if valor > 0 else '#e84118'
			item = QLabel(f'{data}  |  {desc:<22}  |  <span style="color:{cor}">R$ {valor:,.2f}</span>'.replace(',', 'X').replace('.', ',').replace('X', '.'))
			item.setFont(QFont('Segoe UI', 11))
			item.setStyleSheet('margin-bottom: 6px;')
			item.setTextFormat(Qt.RichText)
			extrato_vbox.addWidget(item)

		vbox = QVBoxLayout()
		vbox.addWidget(title)
		vbox.addSpacing(10)
		vbox.addWidget(saldo_label)
		vbox.addWidget(saldo_valor)
		vbox.addWidget(extrato_label)
		vbox.addLayout(extrato_vbox)
		vbox.addStretch()
		self.setLayout(vbox)

# Tela de login
class LoginWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Banco - Login')
		self.setFixedSize(350, 400)
		self.setStyleSheet('background-color: #f5f6fa; border-radius: 15px;')
		self.init_ui()

	def init_ui(self):
		title = QLabel('Bem-vindo ao Banco')
		title.setFont(QFont('Segoe UI', 20, QFont.Bold))
		title.setAlignment(Qt.AlignCenter)
		title.setStyleSheet('color: #273c75; margin-bottom: 30px;')

		user_label = QLabel('Usuário:')
		user_label.setFont(QFont('Segoe UI', 12))
		self.user_input = QLineEdit()
		self.user_input.setPlaceholderText('Digite seu usuário')
		self.user_input.setFont(QFont('Segoe UI', 11))
		self.user_input.setStyleSheet('padding: 8px; border-radius: 8px; border: 1px solid #dcdde1;')

		pass_label = QLabel('Senha:')
		pass_label.setFont(QFont('Segoe UI', 12))
		self.pass_input = QLineEdit()
		self.pass_input.setPlaceholderText('Digite sua senha')
		self.pass_input.setEchoMode(QLineEdit.Password)
		self.pass_input.setFont(QFont('Segoe UI', 11))
		self.pass_input.setStyleSheet('padding: 8px; border-radius: 8px; border: 1px solid #dcdde1;')

		login_btn = QPushButton('Entrar')
		login_btn.setFont(QFont('Segoe UI', 12, QFont.Bold))
		login_btn.setStyleSheet('background-color: #273c75; color: white; border-radius: 8px; padding: 10px;')
		login_btn.clicked.connect(self.handle_login)

		vbox = QVBoxLayout()
		vbox.addWidget(title)
		vbox.addSpacing(10)
		vbox.addWidget(user_label)
		vbox.addWidget(self.user_input)
		vbox.addWidget(pass_label)
		vbox.addWidget(self.pass_input)
		vbox.addSpacing(20)
		vbox.addWidget(login_btn)
		vbox.setAlignment(Qt.AlignCenter)

		self.setLayout(vbox)

	def handle_login(self):
		user = self.user_input.text()
		password = self.pass_input.text()
		if user == 'cliente' and password == '1234':
			self.open_main_window(user)
		else:
			QMessageBox.warning(self, 'Erro', 'Usuário ou senha incorretos.')

	def open_main_window(self, username):
		self.main_window = MainWindow(username)
		self.main_window.show()
		self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = LoginWindow()
	window.show()
	sys.exit(app.exec_())
