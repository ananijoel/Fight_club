import characters
import random
import getpass

print("*** Bienvenu dans le jeu fight club ***\n")

jedi = characters.character("","","","","","","","")
sith = characters.character("","","","","","","","")

characters.object_hasard_config(jedi)
characters.object_hasard_config(sith)
print("\nMedames et messieur bienvenus dans l'arene du fight club . Ce soir : \n".upper())
characters.Introduction(jedi)
characters.Introduction(sith)

print("Voici les mecaniques du jeu".upper())
print("A  chaque tour, vous pouvez choisir entre 0,1, et 2")
print("avec 0 vous pouvez rester passif  et vous gagnez un point (1) d'endurance mais vous prenez de plein fouet le coup enemi. ")
print("Avec 1, vous optez pour une defense qui vous permet d'encaiiser le coup enemie sans perdre en point de vie mais vous perdez O.5 points en endurance ")
print("Avec 2, vous optez pour une attaque dont le force sera compris au hazard entre la valeur de frappe minimale et maximale de votre avatar")
print("le premier joueur a O point de vie aura perdu le combat")



while characters.is_alive(jedi) and characters.is_alive(sith) :
    jedi.choice = random.randint(0, 2)
    sith.choice = random.randint(0, 2)
    if jedi.choice == 0 and sith.choice == 0:
        characters.passivity(jedi)
        characters.passivity(sith)
        characters.health_printer(jedi,sith)
    elif jedi.choice == 0 and sith.choice == 1:
        characters.passivity(jedi)
        characters.defense(sith,jedi)
        characters.health_printer(jedi,sith)
    elif jedi.choice == 0 and sith.choice == 2:
        characters.passivity(jedi)
        characters.strike(sith,jedi)
        characters.health_printer(jedi,sith)


    elif jedi.choice == 1 and sith.choice == 0:
        characters.defense(jedi,sith)
        characters.passivity(sith)
        characters.health_printer(jedi,sith)

    elif jedi.choice == 1 and sith.choice == 1:
        characters.defense(jedi, sith)
        characters.defense(sith, jedi)
        characters.health_printer(jedi,sith)

    elif jedi.choice == 1 and sith.choice == 2:
        #characters.strike(sith,jedi)
        characters.defense_against_strike(jedi,sith)
        characters.health_printer(jedi,sith)


    elif jedi.choice == 2 and sith.choice == 0:
            characters.strike(jedi,sith)
            characters.passivity(sith)
            characters.health_printer(jedi, sith)

    elif jedi.choice == 2 and sith.choice == 1:
        characters.defense_against_strike(sith, jedi)
        characters.health_printer(jedi,sith)

    elif jedi.choice == 2 and sith.choice == 2:
        characters.strike(jedi,sith)
        characters.strike(sith,jedi)
        characters.health_printer(jedi,sith)

print("\n*** fin du jeu ***\n")