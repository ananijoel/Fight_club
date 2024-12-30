import random
#from faker import Faker
#fake = Faker()
from datetime import datetime

sexe = ["M","F"]
side = ["gauche","droit"]

class character :
    def __init__(self, name, sexe, health, min_strength,max_strength, side, endurance,score, choice=None):
        self.name = name.capitalize()
        self.sexe = sexe.capitalize()
        self.health = health
        self.min_strength = min_strength
        self.max_strength = max_strength
        self.is_alive = is_alive
        self.side = side
        self.endurance = endurance
        self.choice = choice
        self.score = score

def fights_history_register(character,character_2,i):
    date_actuelle = datetime.now()
    date_formatee = date_actuelle.strftime("%Y-%m-%d %H:%M:%S")
    with open('fights_history.txt', 'a') as fights_history:
        fights_history.write("||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        fights_history.write("--------------------------------------------------------\n")
        fights_history.write(f'score final de la partie du : {date_formatee}\n')
        #fights_history.write(character.name+" "+str(character_score)+":"+str(chracter_2_score)+" "+str(chracter_2.name))
        fights_history.write(character.name+" ")
        fights_history.write(str(character.score) + ":" + str(character_2.score) + " ")
        fights_history.write(character_2.name + " \n")
        fights_history.write("la partie a durée "+str(i)+" tours \n")
        fights_history.write("--------------------------------------------------------\n")
        fights_history.write("||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

def player_avatar_data_init(character):
    character.name = input("Quel est votre nom ?\nreponse : ")
    character.sexe = input("ca peut paraitre indiscret " + character.name + " mais quel est votre sexe ? On ne sait plus trop qui est qui aujourd'hui\nreponse (M:masulin/F:feminin): ").capitalize()
    while character.sexe != "M" and character.sexe != "F":
        character.sexe = input(character.name + " CHOISIS ENTRE UN HOUMME OU UNE FEMME. (M/m pour masculin  ou F/f pour feminin.)\nquel est votre sexe ?(M/F)\nreponse : ").capitalize()
    character.health = 30
    character.min_strength = 5
    character.max_strength = 15
    character.side = random.choice([side[0], side[1]])
    character.endurance = 4
    character.score = 0

def object_hasard_config(object):
    object.name = "player"+str(random.randint(0, 60))
    object.sexe = random.choice([sexe[0], sexe[1]])
    object.health = random.randint(50, 60)
    object.min_strength = random.randint(5, 10)
    object.max_strength = random.randint(20, 25)
    object.side = random.choice([side[0], side[1]])
    object.endurance = random.randint(8, 12)
    object.choice = random.randint(0, 2)
    object.score = 0

def drug_choice(character) :
    drug_choice = input("0.Rien du tout \n1.Gain d'endurance \n2.Gain de vitalité. \n Que choisissez vous  "+character.name+" ? : ")
    while drug_choice !="0" and drug_choice !="1" and drug_choice !="2" :
        drug_choice = input("0.Rien du tout \n1.Gain d'enrance \n2.Gain de vitalité. \n Que choisissez vous  " + character.name + " ? : ")
    if drug_choice =="2" :
        character.health = character.health + int(character.health/10)
    elif drug_choice == "1":
        character.endurance = character.endurance + int(character.endurance/20)+1
    elif drug_choice == "0":
        print()


def is_alive(character) :
    if character.health > 0:
        character.is_alive = True
        return character.is_alive
    else:
        character.is_alive = False
        return character.is_alive

def Introduction(character) :
    print("Dans le coin "+str(character.side)+" du ring nous avons :")
    print(character.name + " avec une force de frappe maximale de " + str(character.max_strength) + " points.")
    print("Une endurance de "+str(character.endurance)+" points")
    print("Et une santé s'elevant a " + str(character.health) + " points\n")

def endurance_state(character):
    passif = 1
    defense = 0.5
    actif = 1
    if character.choice == 0 :
        character.endurance += passif
    elif character.choice  == 1 :
        character.endurance -= defense
    elif character.choice == 2 :
        character.endurance -= actif


def welcome_message(character) :
    if character.sexe == "M"  or character.sexe == "m" :
        print("bienvenu sir "+character.name)
    elif character.sexe == "F" or character.sexe == "f" :
        print("bienvenu dame "+character.name)

def strike(character,character_2):
    endurance_state(character)
    if character.endurance > 0 :
        damage = random.randrange(character.min_strength, character.max_strength)
        character_2.health = character_2.health - damage
        print("----------------")
        print(str(character.name)+" a infligé "+str(damage)+" de degat a "+str(character_2.name))
        print(str(character.name) + " a perdu 1 de son endurance. Maintenant, son endurance est de " + str(character.endurance))
    else :
        character.endurance = 0
        print(str(character.name)+" n'a plus assez d'endurance pour defendre")


def defense (character,character_2) :
    endurance_state(character)
    if character.endurance > 0 :
        print("----------------")
        print(str(character.name) + " a choisi la defense.")
        print(str(character.name) + " a perdu 0.5 de son endurance. Maintenant, son endurance est de " + str(character.endurance))
        print(str(character.name)+" n'a recu aucun degat pv = "+str(character.health)+"\n")
    else :
        character.endurance = 0
        print(str(character.name)+" n'a plus assez d'endurance pour defendre")
def defense_against_strike(character,character_2) :
    endurance_state(character)
    endurance_state(character_2)
    if character.endurance >= 0 :
        print("----------------")
        print(str(character.name) + " a choisi la defense.")
        print(str(character.name) + " a perdu 0.5 de son endurance. Maintenant, son endurance est de " + str(character.endurance))
        print(str(character_2.name)+" a attaqué "+str(character.name)+" ")
        print(str(character_2.name)+" a perdu 1 point de son endurance. Maintenant, son endurance est de " + str(character_2.endurance))
        print(str(character.name)+" n'a recu aucun degat pv = "+str(character.health)+"\n")
    else:
        character.endurance =0
        strike(character_2,character)
        defense(character,character_2)


def passivity(character):
    endurance_state(character)
    print("----------------")
    print(str(character.name) + " a choisi la passivité.")
    print(str(character.name) + " a gagné 1 d'endurance. Maintenant, son endurance est de " + str(character.endurance))
def health_printer(character,character_2):

    if is_alive(character) and is_alive(character_2) :
        print("*** Etat des joueurs a la fin du tour ***")
        print(str(character.name)+" a "+str(character.health)+" de point de vie restant")
        print(str(character_2.name) + " a " + str(character_2.health) + " de point de vie restant")
        print("*************************************************************************")


    elif is_alive(character) and not is_alive(character_2) :
        print("\n")
        print("\n")

        print("*************************************************************************")
        print("*************************************************************************")

        print(str(character.name)+" a gagné")
        print("Félicitations à " + character.name + " pour cette victoire dans l'arène du Fight Club!")
        print("*************************************************************************")
        print("*************************************************************************")
        character.score = 1
        character_2.score = 0


    elif  not is_alive(character) and is_alive(character_2) :
        print("\n")
        print("\n")

        print("*************************************************************************")
        print("*************************************************************************")

        print(str(character_2.name) + " a gagné")
        print("Félicitations à " + character_2.name + " pour cette victoire dans l'arène du Fight Club!")
        print("*************************************************************************")
        print("*************************************************************************")
        character.score = 0
        character_2.score = 1

    elif not is_alive(character) and  not is_alive(character_2):
        print("\n")
        print("\n")

        print("*************************************************************************")
        print("*************************************************************************")

        print("Match null")
        print("*************************************************************************")
        print("*************************************************************************")
        character.score = 1
        character_2.score = 1