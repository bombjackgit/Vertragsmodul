from docxtpl import DocxTemplate
from num2words import num2words
import locale

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

kv = DocxTemplate("Kaufvertrag_11.docx")
context = {
    "namekp": "Max Mustermann",
    "geburtsdatumkp": "24.10.2001",
    "adressekp": "Reifgasse 10, 3500 Krems",
    "kaufpreis": format_euro(kaufpreis),
    "kaufpreisiw" : euro_in_worten(kaufpreis)
}
kv.render(context)
kv.save("Entwurf.docx")
