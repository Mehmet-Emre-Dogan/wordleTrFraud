import sys
from json import load
import ctypes
import re

DEBUG = False

wordArr = []
ctypes.windll.kernel32.SetConsoleTitleW("Wordle kopya üretici++")

# https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
def naturalSort(arr): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(arr, key=alphanum_key)

with open("words.json", "r", encoding="utf-8") as fil:
    wordArr = load(fil)["data"]
    WORD_COU = len(wordArr)

print("Wordle kopya üreticiye hoş geldiniz! Uygulamadan çıkmak için CTRL^C ye basın (keyboard interrupt)")
print(f"Yüklü kelime sayısı: {WORD_COU}")

# https://stackoverflow.com/questions/3640359/regular-expressions-search-in-list
# https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
while True:
    try:
        print("="*50)
        print("Bildiğiniz harfleri yazın. Bilmedikleriniz yerine '.' koyun. \nSonra bir boşluk bırakıp engelli harfleri yan yana yazın. \nSonra bir boşluk daha bırakıp sarı harfleri yazın. \nÖzellik kullanmak istemiyorsanız '*' yazın. \nÖrnek: a.a.a şkl b [cevap araba ama r yi henüz hiç bulamadınız ve b yi de sarı olarak buldunuz; ş k ve l nin de olmadığı ortaya çıktı] \nÖrnek2: a.a.a şkl * [cevap araba ama r ve b yi henüz hiç bulamadınız; ş k ve l nin de olmadığı ortaya çıktı; sarı harf çıkmadı]")
        myStrArr = input("--> ").split()

        if DEBUG:
            print(myStrArr)
        compildeRegex = re.compile(myStrArr[0])
        posiibleWords = list(set(filter(compildeRegex.match, wordArr))) # set is here to get rid of duplicates

        if myStrArr[1] != '*':
            prohibitedLetters = list(myStrArr[1])
        else:
            prohibitedLetters = []

        if myStrArr[2] != '*':
            existingLetters = list(myStrArr[2])
        else:
            existingLetters = []    

        if DEBUG:
            print(prohibitedLetters)
        posiibleWords = naturalSort([word for word in posiibleWords if ( (not any(letter in word for letter in prohibitedLetters)) and all(letter in word for letter in existingLetters) )])
        if posiibleWords:
            for i, word in enumerate(posiibleWords):
                print(f"{str(i+1).zfill(3)}- {word}")
        else:
            print("Eşleşme bulunamadı.")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as ex:
        print("Bir hata oluştu:")
        print(ex)