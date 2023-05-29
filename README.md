# Fazan
Classic romanian word game

you input a random word, the program extracts the last 2 letters of your word (e.g CAMERA -> (RA)) and will form a new word starting with them (e.g RAmadan). Then you have to form a word with
the last two letters and so on.

e.g
persON -> ONliNE -> NEuroloGY -> GYroscoPE .. and so on

it uses web-scraping to collect new appropriate words from a website where you can input two letters and will form a word with them, then it will prompt you to form a new word using that word's last letters.
the game ends when a player loses 5 times. each time a round is lost, he gains a new letter, (F-A-Z-A-N), you lose once, you "are F", when you lose twice, you "are FA", and so on until the word FAZAN forms.

the program will check if your input is legitimate (if it truly starts with the letter required) but it will not verify if your word is real, because there is no romanian dictionary available in python.
