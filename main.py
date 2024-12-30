import characters
import getpass
import big_prints

big_prints.introduction_of_the_game()

jedi = characters.character("","", "","","","","","","")
characters.player_avatar_data_init(jedi)
print("De l'autre coté de l'arene maintenant.")
sith = characters.character("","", "","","","","","","")
characters.player_avatar_data_init(sith)



big_prints .rules_of_the_game()

print("Pour pimenter le combat, nous avons decider de vous donner un choix.")
print("Un choix entre deux drogues. la premiere augmente votre andurance de 20% et l'autre votre santé de 10% aussi")
characters.drug_choice(jedi)
characters.drug_choice(sith)

print("\nCe soir : ".upper())
characters.Introduction(jedi)
characters.Introduction(sith)

print("que le combat proprement parlé commence")
print("pour que votre  adversaire ne vois pas votre descision, vos entrés sont ivisibles sur la consoleb")
i = 0;
while characters.is_alive(jedi) and characters.is_alive(sith) :
    i += 1
    while jedi.choice != "0" and jedi.choice != "1" and jedi.choice != "2" :
        jedi.choice = getpass.getpass("Que choisis "+str(jedi.name)+" ?\n reponse :")
    while sith.choice != "0" and sith.choice != "1" and sith.choice != "2":
        sith.choice = getpass.getpass("Que choisis "+str(sith.name)+"?\n reponse :")
    jedi.choice = int(jedi.choice)
    sith.choice = int(sith.choice)
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
print("\n*** fin du jeu ***\n".upper())

characters.fights_history_register(jedi,sith,i)