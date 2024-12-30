# Fight Club

**Fight Club** est un jeu de combat Python pour deux joueurs où chaque joueur incarne un personnage avec des attributs spécifiques. Le but est d'éliminer l'adversaire en réduisant ses points de vie à zéro tout en gérant son endurance et en faisant des choix stratégiques.

---

## Fonctionnalités

- Combat à deux joueurs (humains ou IA).
- Gestion des points de vie, endurance, et force de frappe.
- Historique des combats enregistré dans un fichier texte.
- Mode test pour automatiser les combats entre deux personnages aléatoires.
- Méchanismes de choix : passivité, défense ou attaque.

---

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/votre-utilisateur/fight_club.git
cd fight_club
```

---

## Lancer le Jeu

Pour jouer au jeu interactif :

```bash
python main.py
```

Pour lancer un combat automatisé (mode test) :

```bash
python hard_test.py
```

Pour tester les fonctions du jeu :

```bash
python test_fonctions.py
```

---

## Règles du Jeu

- **Choix à chaque tour :**
    
    - `0` : Passivité - Gagne 1 point d'endurance mais subit les attaques adverses.
    - `1` : Défense - Encaisse les attaques sans perdre de points de vie, mais perd 0.5 points d'endurance.
    - `2` : Attaque - Inflige des dégâts aléatoires à l'adversaire (basé sur les forces minimale et maximale).
- Le premier joueur à atteindre 0 points de vie perd la partie.
    

---

## Historique des Combats

Un historique des combats est enregistré dans le fichier `fights_history.txt`, incluant :

- Les noms des joueurs.
- Le score final.
- La durée en nombre de tours.
- La date et l'heure de la partie.

---

## Développement

### Fichiers Principaux

- `main.py` : Jeu principal en mode interactif.
- `hard_test.py` : Mode de test avec des combats automatisés.
- `test_fonctions.py` : Test des fonctionnalités et propriétés des personnages.
- `characters.py` : Définition et gestion des personnages, ainsi que des mécaniques de combat.

---

## Contributeurs

Créé par **[anani joel/ananijoel]**. Contributions et suggestions sont les bienvenues ! 🎉

---