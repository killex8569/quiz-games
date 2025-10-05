from random import *
import json
player_score = 0
player_chance = 3


def main_menu():
    print("Bienvenu dans le Quiz Game ! ")

    # Proposition de la section pour l'utilisateur
    print("Dans qu'elle section voulez vous vous tester ? : ")
    print("1 - Astronomie\n2 - Developpement\n3 - Philo\n4 - Other")
    user_choix_section = int(input("votre choix : "))
    if user_choix_section == 2:
        menu_dev()

def menu_dev():
    global player_score, player_chance
    with open("qst/qst_dev.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    
    q = choice(questions)
    print(q["question"])
    for letter, options in q["options"].items():
        print(f"{letter}: {options}")

    user_answer = str(input("Votre réponse : "))
    if player_chance == 0:
        print("Vous avez perdu !")

    else : 
        if user_answer == q["answer"]:
            print("Oui bien jouer")
            player_score += 1
            print("Vies restante(s) : ", player_chance)
            print("Score actuelle", player_score)
            menu_dev()
        else:
            print("Non, pas cela")
            player_chance -= 1
            print("Vies restante(s) : ", player_chance)
            print("Score actuelle", player_score)
            menu_dev()



main_menu()