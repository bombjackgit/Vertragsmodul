from docxtpl import DocxTemplate
from num2words import num2words
import locale
import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_mainwindow import Ui_Form

kaufpreis = 562800

# Deutsche Formatierung aktivieren
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

def format_euro(kaufpreis):
    return locale.format_string('%.2f', kaufpreis, grouping=True)

def euro_in_worten(kaufpreis):
    euro = int(kaufpreis)
    cent = int(round((kaufpreis - euro) * 100))

    euro_wort = num2words(euro, lang='de')
    cent_wort = num2words(cent, lang='de')

    if cent == 0:
        return f"{euro_wort} Komma null Euro"
    else:
        return f"{euro_wort} Komma {cent_wort} Euro"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.entwurf)

    def entwurf(self):
        kaufpreis_text = self.ui.textEdit_11.toPlainText()
        try:
            kaufpreis = float(kaufpreis_text.replace(",", "."))
        except ValueError:
            print("Ungültiger Kaufpreis – bitte Zahl eingeben.")
            return

        kv = DocxTemplate("Kaufvertrag_11.docx")
        context = {
            "namekp": self.ui.textEdit.toPlainText(),
            "geburtsdatumkp": self.ui.textEdit_2.toPlainText(),
            "adressekp": self.ui.textEdit_3.toPlainText(),
            "kaufpreis": format_euro(kaufpreis),
            "kaufpreisiw": euro_in_worten(kaufpreis),
            "namevp": self.ui.textEdit_4.toPlainText(),
            "geburtsdatumvp": self.ui.textEdit_6.toPlainText(),
            "adressevp": self.ui.textEdit_8.toPlainText(),
            "ez": self.ui.textEdit_5.toPlainText(),
            "kg": self.ui.textEdit_9.toPlainText(),
            "beschreibung": self.ui.textEdit_7.toPlainText(),
            "übergabetag": self.ui.textEdit_13.toPlainText(),
        }
        kv.render(context)
        kv.save("Entwurf.docx")
        print("Dokument erfolgreich erstellt.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
