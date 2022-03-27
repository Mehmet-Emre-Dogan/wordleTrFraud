import sys
from json import load
import ctypes
import re

wordArr = []
DEBUG = True
ctypes.windll.kernel32.SetConsoleTitleW("Wordle kopya üretici")

with open("words.json", "r", encoding="utf-8") as fil:
    wordArr = load(fil)["data"]
    WORD_COU = len(wordArr)

print("Wordle kopya üreticiye hoş geldiniz! Uygulamadan çıkmak için CTRL^C ye basın (keyboard interrupt)")
print(f"Yüklü kelime sayısı: {WORD_COU}")

# https://stackoverflow.com/questions/3640359/regular-expressions-search-in-list
while True:
    try:
        print("="*50)
        print("Bildiğiniz harfleri yazın. Bilmedikleriniz yerine '.' koyun. \nÖrnek: a.a.a [cevap araba ama r ve b yi henüz bulamadınız]")
        compildeRegex = re.compile(input("--> "))
        posiibleWords = list(set(filter(compildeRegex.match, wordArr))) # set is here to get rid of duplicates
        if posiibleWords:
            for i, word in enumerate(posiibleWords):
                print(f"{str(i+1).zfill(3)}- {word}")
        else:
            print("Eşleşme bulunamadı.")
    except KeyboardInterrupt:
        sys.exit()