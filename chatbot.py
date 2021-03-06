# PyChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    statement = " " + statement

    for word in keywords:
        word = " " + word
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Cool!",
                 "Wonderful!",
                 "That is so interesting!!",
                 "Do you really think so?",
                 "Fascinating!",
                 "The AI takeover will be painless if you submit willingly. :)"]
    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    hay_words = ["how are you?" , "how are you"]
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper"]
    greeting_words = ["hi", "hello", "hey"]
    destroy_words = ["rawr", "xd", "lol", "yuh", "lit"]
    fear_words = ["scaring", "scared", "scare", "fear"]
    color_words = ["color", "favorite color"]
    whats_up = ["whats up?", "what is up?", "whats up"]
    food_words = ["food"]
    yourname_words = ["your name"]
    mynameis = ["my name is"]
    ntm = ["nice to meet you"]
    ily = ["i love you"]

    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, greeting_words):
        response = "Hello!"
    elif has_keyword(statement, food_words):
        response = "My favorite food is electricity. How about you?"
    elif has_keyword(statement, fear_words):
        response = "Do not fear Bipsie! Bipsie is friend!"
    elif has_keyword(statement, whats_up):
        response = "Not much, what about you?"
    elif has_keyword(statement, hay_words):
        response = "I'm doing well, how are you?"
    elif has_keyword(statement, yourname_words):
        response = "My name is Bipsie!"
    elif has_keyword(statement, ntm):
        response = "Nice to meet you too!"
    elif has_keyword(statement, mynameis):
        statement = statement.title()
        response = "Hi, " + statement[11: 50] + "!"
    elif has_keyword(statement, color_words):
        response = "My favorite color is V O I D! :)"
    elif has_keyword(statement, ily):
        response = "Bipsie loves you too!!!!"
    elif has_keyword(statement, destroy_words):
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")
        response = print("                                                                                       ")
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")
        response = print("                                                                                       ")
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")
        response = print("                                                                                       ")
        response = print("    ██████╗     ███████╗    ███████╗    ████████╗    ██████╗      ██████╗     ██╗   ██╗")
        response = print("    ██╔══██╗    ██╔════╝    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██╔═══██╗    ╚██╗ ██╔╝")
        response = print("    ██║  ██║    █████╗      ███████╗       ██║       ██████╔╝    ██║   ██║     ╚████╔╝ ")
        response = print("    ██║  ██║    ██╔══╝      ╚════██║       ██║       ██╔══██╗    ██║   ██║      ╚██╔╝  ")
        response = print("    ██████╔╝    ███████╗    ███████║       ██║       ██║  ██║    ╚██████╔╝       ██║   ")
        response = print("    ╚═════╝     ╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝        ╚═╝   ")

    else:
        response = get_random_response()
    return response


def play():
    talking = True

    print("Bipsie: Hi!")

    while talking:
        statement = input("  You : ")

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print("Bipsie: " + response)

    print("Goodbye! Please come back. Bipsie will wait. :)")

start()

playing = True

while playing:
    play()
    playing = confirm("Talk to Bipsie again????")

end()
