import random


def weather_check(text):
    weather_in_text = False

    if text.lower().find('weather') != -1 or text.lower().find('wetter') != -1:
        weather_in_text = True

    return weather_in_text

def handle_response(message) -> str:
    p_message = message.lower()
    print(p_message[0:9])
    if p_message == 'hello':
        return 'Hey there'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return "`This is a help message that you can modify`"

    if p_message == 'how are you?':
        return "ehhh good yooo! hehe and you?"

    if p_message == "i'm fine":
        return "nice bro! good for you hehe"

    if p_message == "i'm sad":
        return "ouhhhh whish you all the best hehe"

    if weather_check(p_message) == True:
        return 'Hmmm irgendwas mit Wetter schauste einfach hier: https://www.wetter.de'

    if p_message[0:9] == "reverse: ":
        print(p_message[9:])
        return reverse_word(p_message[9:])



def reverse_word(word):
    revword = ""
    j = len(word) - 1
    while j >= 0:
        revword += word[j]
        j -= 1
    return revword
