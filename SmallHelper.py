import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QSpinBox, QComboBox, QTextEdit
)

class DiceRoller(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DnD Würfelrechner")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Auswahl: Würfeltyp
        dice_layout = QHBoxLayout()
        dice_layout.addWidget(QLabel("Würfeltyp:"))
        self.dice_box = QComboBox()
        self.dice_box.addItems(["d4", "d6", "d8", "d10", "d12", "d20"])
        dice_layout.addWidget(self.dice_box)
        layout.addLayout(dice_layout)

        # Anzahl der Würfel
        count_layout = QHBoxLayout()
        count_layout.addWidget(QLabel("Anzahl Würfel:"))
        self.count_box = QSpinBox()
        self.count_box.setMinimum(1)
        self.count_box.setMaximum(100)
        count_layout.addWidget(self.count_box)
        layout.addLayout(count_layout)

        # Bonus
        bonus_layout = QHBoxLayout()
        bonus_layout.addWidget(QLabel("Bonus:"))
        self.bonus_box = QSpinBox()
        self.bonus_box.setRange(-100, 100)
        bonus_layout.addWidget(self.bonus_box)
        layout.addLayout(bonus_layout)

        # Button zum Würfeln
        self.roll_button = QPushButton("Würfeln")
        self.roll_button.clicked.connect(self.roll_dice)
        layout.addWidget(self.roll_button)

        # Ergebnisanzeige
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def roll_dice(self):
        dice_type = int(self.dice_box.currentText()[1:])  # z.B. "d6" -> 6
        count = self.count_box.value()
        bonus = self.bonus_box.value()

        rolls = [random.randint(1, dice_type) for _ in range(count)]
        total = sum(rolls) + bonus

        result_text = f"Würfel: {count}x d{dice_type} + {bonus}\n"
        result_text += f"Einzelwürfe: {rolls}\n"
        result_text += f"Gesamt: {total}"
        self.result_display.setText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiceRoller()
    window.show()
    sys.exit(app.exec_())
