import mapEngToBraille, mapBrailleToEng,map1

CAPITAL = chr(10272)  # ⠠
NUMBER =  chr(10300) # ⠼

open_quotes = True


def extract_words(string):
    # Split up a sentence based on whitespace (" ") and new line ("\n") chars.
    words = string.split(" ")
    result = []
    for word in words:
        temp = word.split("\n")
        for item in temp:
            result.append(item)
    return result


def is_braille(char):
    # Return true if a char is braille.
    
    return char in mapBrailleToEng.letters \
        or char in mapBrailleToEng.numbers \
        or char in mapBrailleToEng.punctuation \
        or char in mapBrailleToEng.contractions \
        or char == CAPITAL \
        or char == NUMBER


def trim(word):
    # Remove punctuation around a word. Example: cat." becomes cat
    while len(word) is not 0 and not word[0].isalnum():
        word = word[1:]
    while len(word) is not 0 and not word[-1].isalnum():
        word = word[:-1]
    return word


def numbers_handler(word):
    # Replace each group of numbers in a word to their respective braille representation.
    if word == "":
        return word
    result = word[0]
    if word[0].isdigit():
        result = NUMBER + mapEngToBraille.numbers.get(word[0])
    for i in range(1, len(word)):
        if word[i].isdigit() and word[i-1].isdigit():
            result += mapEngToBraille.numbers.get(word[i])
        elif word[i].isdigit():
            result += NUMBER + mapEngToBraille.numbers.get(word[i])
        else:
            result += word[i]
    return result


def capital_letters_handler(word):
    # Put the capital escape code before each capital letter.
    if word == "":
        return word
    result = ""
    for char in word:
        if char.isupper():
            result += CAPITAL + char.lower()
        else:
            result += char.lower()
    return result





def char_to_braille(char):
    # Convert an alphabetic char to braille.
    if is_braille(char):
        return char
    if char == "\"":
        global open_quotes
        if open_quotes:
            open_quotes = not open_quotes
            return mapEngToBraille.punctuation.get("“")
        else:
            open_quotes = not open_quotes
            return mapEngToBraille.punctuation.get("”")
    elif char in mapEngToBraille.letters and char.isupper():
        return CAPITAL + mapEngToBraille.letters.get(char)
    elif char in mapEngToBraille.letters:
        return mapEngToBraille.letters.get(char)
    elif char in mapEngToBraille.punctuation:
        return mapEngToBraille.punctuation.get(char)
   


def word_to_braille(word):
    # Convert an alphabetic word to braille.
    if word in mapEngToBraille.contractions:
        return mapEngToBraille.contractions.get(word)
    else:
        result = ""
        for char in word:
            result += char_to_braille(char)
        return result


def build_braille_word(trimmed_word, shavings, index, braille):
    # Translate a trimmed word to braille then re-attach the shavings.
    if shavings == "":
        braille += word_to_braille(trimmed_word)
    else:
        for i in range(0, len(shavings)):
            if i == index and trimmed_word is not "":
                braille += word_to_braille(trimmed_word)
            braille += word_to_braille(shavings[i])
        if index == len(shavings):  # If the shavings are all at the beginning.
            braille += word_to_braille(trimmed_word)
    return braille



def translate(string):
    # Convert alphabetic text to braille.
    braille =""
    braille1=[]
    braille2=[]
    words = extract_words(string)
    for word in words:
        word = numbers_handler(word)
        word = capital_letters_handler(word)
        trimmed_word = trim(word)  # Remove punctuation (ex: change dog?" to dog)
        untrimmed_word = word
        index = untrimmed_word.find(trimmed_word)
        shavings = untrimmed_word.replace(trimmed_word, "")
        braille = build_braille_word(trimmed_word, shavings, index, braille)+ " "
    braille=braille[:-1].split(" ")
    for word in braille:
        braille1=[]
        for i in range(0,len(word)):
            if word[i] in map1.letters:
               braille1+=[map1.letters.get(word[i])]
            elif word[i] in map1.punctuation:
               braille1+=[map1.punctuation.get(word[i])]
            elif word[i] in map1.numbers:
               braille1+=[map1.numbers.get(word[i])]
            elif word[i] in map1.contractions:
              braille1+=[map1.contractions.get(word[i])]
            elif word[i]==CAPITAL:
               braille1+=[[0, 0, 0, 0, 0, 1]]
            elif word[i]==NUMBER:
               braille1+=[[0, 1, 0, 1, 1, 1]]
        braille2+=[braille1]
    return braille2
               

