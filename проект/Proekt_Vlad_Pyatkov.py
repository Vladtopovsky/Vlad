import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap

class GuessThePicture(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Угадай, что на картинке")
        self.setGeometry(100, 100, 400, 500)
        
        # Словарь с картинками и ответами
        self.images = {
            "cat.jpg": "кот",
            "dog.jpg": "собака",
            "shawarma.jpg": "шаурма"
            "borsch.jpg" : "Борщ"
            "roses.jpg" : "рози"
            "daisies.jpg" : "рамашки "
        }
        
        # Случайный выбор изображения
        self.current_image, self.current_answer = random.choice(list(self.images.items()))
        
        # Создаем интерфейс
        self.init_ui()
    
    def init_ui(self):
        # Виджет изображения
        self.image_label = QLabel(self)

        pixmap = QPixmap(f"images/{self.current_image}")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(300, 300)
        
        # Поле для ввода текста
        self.answer_input = QLineEdit(self)
        self.answer_input.setPlaceholderText("Введите ваш ответ")
        
        # Кнопка проверки
        self.check_button = QPushButton("Проверить", self)
        self.check_button.clicked.connect(self.check_answer)
        
        # Расположение элементов
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.check_button)
        
        # Центральный виджет
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def check_answer(self):
        # Проверка ответа
        user_answer = self.answer_input.text().strip().lower()
        if user_answer == self.current_answer:
            QMessageBox.information(self, "Результат", "Правильно!")
        else:
            QMessageBox.warning(self, "Результат", f"Неправильно! Правильный ответ: {self.current_answer}")
        
        # Следующее изображение
        self.next_image()
    
    def next_image(self):
        # Случайно выбираем новое изображение
        self.current_image, self.current_answer = random.choice(list(self.images.items()))
        pixmap = QPixmap(f"images/{self.current_image}")
        self.image_label.setPixmap(pixmap)
        self.answer_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Убедитесь, что папка "images" существует и содержит картинки
    window = GuessThePicture()
    window.show()
    sys.exit(app.exec_())
