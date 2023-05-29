from bs4 import BeautifulSoup
import requests
import random
import re

# ******** START JOC ********************
def header():
    print("******* FAZAN *********")
    print("******* RULES *********")
    print("****** DACA TE DAI BATUT, INTRODU F ******")
    print("******************* HAVE FUN ***************************")
    print("")

def joc(ul2litere):
    # *********  URL & COMMANDS *********** #
    url = "https://www.cuvintecare.ro/cuvinte-care-incep-cu-{}.html".format(ul2litere)
    result = requests.get(url)
    doc = BeautifulSoup(result.content.decode('utf-8'), "html.parser")
    cuvantBotDiv = doc.find('div', class_ = "lista-cuvinte").text

    # ********** Amestecare cuvant de la bot *********
    listacuvinte = [word.strip() for word in cuvantBotDiv.split('\n') if word.strip()]
    if listacuvinte:
        regex = r"\b{}\w*\b".format(ul2litere)
        matches = [word.strip() for word in listacuvinte if re.search(regex, word)]
        if matches:
            random_word = random.choice(matches)
            print("Un cuvant aleator: ", random_word)
            return random_word
        else:
            print("Nu am gasit cuvinte care incep cu '{}'".format(ul2litere), "M-ai facut, fraiere.")
            print("")


header()
cuvant = str(input('Introdu cuvantul: '))
ul2litere = cuvant[-2:].lower()
random_word = joc(ul2litere)
fazanbot = 0
fazanjucator = 0


while True:
    if random_word is None:
        fazanbot += 1
        if fazanbot == 1:
            print("M-ai facut F")
        elif fazanbot == 2:
            print("M-ai facut FA")
        elif fazanbot == 3:
            print("M-ai facut FAZ")
        elif fazanbot == 4:
            print("M-ai facut FAZA")
        elif fazanbot == 5:
            print("M-ai facut FAZAN")
            print("Se incheie jocul! Felicitari!")
            break

        cuvant = str(input('Introdu un alt cuvant: '))
        ul2litere = cuvant[-2:].lower()
        random_word = joc(ul2litere)

    ul2bot = random_word[-2:].lower()
    cuvptbot = str(input("Introdu un cuvant care sa inceapa cu: **"+ul2bot+"**: ".lower()))
    if cuvptbot == "0":
        break
    elif cuvptbot == "F":
        print("Te-am inchis!") #e.g you lost
        fazanjucator += 1
        if fazanjucator == 1:
            print("M-ai facut F")
        elif fazanjucator == 2:
            print("M-ai facut FA")
        elif fazanjucator == 3:
            print("M-ai facut FAZ")
        elif fazanjucator == 4:
            print("M-ai facut FAZA")
        elif fazanjucator == 5:
            print("M-ai facut FAZAN")
            print("Se incheie jocul! Felicitari!")
            break


        cuvant = str(input('Introdu un alt cuvant: '))
        ul2litere = cuvant[-2:].lower()
        random_word = joc(ul2litere)

    cuvantokptbot = cuvptbot.startswith((ul2bot))
    ul2bot2 = cuvptbot[-2:].lower()
    if cuvantokptbot:
        print('')
    else:
        print('Introdu un cuvant corespunzator!')

    random_word = joc(ul2bot2)







