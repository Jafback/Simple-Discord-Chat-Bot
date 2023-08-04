import random

def check_for_weather_string(text):
    splittext = text.lower().split()
    isinside = False
    if 'weather' in splittext:
        isinside = True
    if 'wetter' in splittext:
        isinside = True
    return isinside
def handle_response(message) -> str:
    p_message = message.lower()

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

    if check_for_weather_string(p_message):
        return 'Hmmm irgendwas mit Wetter schauste einfach hier: https://www.wetter.de'



