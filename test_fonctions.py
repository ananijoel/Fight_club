import random

import characters
#from faker import Faker
#fake = Faker()

sexe = ["M","F"]
side = ["gauche","droite"]

object = characters.character("","","","","","","","")
object_2 = characters.character("","","","","","","","")

def testing_object_properties(object):
    object.name = "player"+str(random.randint(0, 60))
    object.sexe = random.choice([sexe[0], sexe[1]])
    object.health = random.randint(50, 60)
    object.min_strength = random.randint(5, 10)
    object.max_strength = random.randint(20, 25)
    object.side = random.choice([side[0], side[1]])
    object.endurance = random.randint(8, 12)
    object.choice = random.randint(0, 2)
    print("Nom : "+object.name)
    print("Sexe : "+object.sexe)
    print("points de vie : "+str(object.health))
    print("force minimale : " + str(object.min_strength))
    print("force maximale : " + str(object.max_strength))
    print("position sur le ring : " + object.side)
    print("quantité d'endurance: "+str(object.endurance))
    print("choix de l'objet : "+str(object.choice))

testing_object_properties(object)
print("-----------------------------")
testing_object_properties(object_2)
print("-----------------------------")

print("santé de "+object.name+": "+str(characters.is_alive(object)))
print("-----------------------------")
print("santé de "+object_2.name+": "+str(characters.is_alive(object_2)))
print("-----------------------------")

print("INTRODUCTION de "+object.name+":")
characters.Introduction(object)
print("-----------------------------")
print("INTRODUCTION de "+object_2.name+":")
characters.Introduction(object_2)
print("-----------------------------")

print("ENDURANCE de "+object.name+" : "+str(object.endurance))
print("-----------------------------")
print("ENDURANCE de "+object_2.name+": "+str(object_2.endurance))
print("******************************************************")
print("ACTIONS")
print(object.name)
characters.defense(object,object_2)
characters.strike(object,object_2)
characters.defense_against_strike(object,object_2)