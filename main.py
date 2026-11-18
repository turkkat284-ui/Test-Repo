import time as t
def welcome_ritual():
    print(60 * "=")
    t.sleep(1)
    print(20 * "=", "GEN-Z KELIME SÖZLÜGÜ", 20 * "=")
    t.sleep(1)
    print(60 * "=")
    t.sleep(1)
    print("GenZ sözlügüne hosgeldiniz ! 😊")
    print(" ")
    t.sleep(1)
    print("anlamadiginiz bir kelime varsa burda aratabilirsiniz.")
    print(" ")
    print(" ")
    t.sleep(1)
    

dict = {
    "CRINGE": "Garip yada utandirici birsey",
    "LOL": "komik birseye verilen cevap",
    "ROFL": "bir sakaya karsilik cevap",
    "SHEESH": "onaylamak",
    "CREEPY": "korkunc",
    "AGGRO": "agresiflesmek/sinirlenmek"
}

welcome_ritual()
while True:
    word = input("anlamadiginiz kelimeyi burda aratin (lütfen büyük harflerle yaziniz) : ")
    print(" ")

    if word in dict: 
        print("aradiginiz kelimenin anlami:", dict[word])
        print(" ")
    else:
        print("aradiginiz kelime malesef bulunamadi")
