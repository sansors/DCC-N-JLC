# Workflow KiCad pour DCC-N-JLC

Pour que nous puissions travailler efficacement ensemble sur le PCB, voici la marche à suivre :

## 1. Initialisation
Clément, tu peux maintenant cloner le dépôt sur ta machine :
`git clone https://github.com/sansors/DCC-N-JLC.git`

## 2. Création du projet
- Ouvre KiCad et crée un nouveau projet dans le dossier `hardware/`.
- Nomme le projet `DCC-N-JLC`.

## 3. Saisie du Schéma
- Utilise les définitions de pins fournies dans le canal `#logs-techniques-dcc`.
- **Propriétés des composants :** Pour chaque composant de la BOM, ajoute un champ `LCSC` avec le numéro de référence (ex: `C432211`). Cela nous permettra de générer la BOM JLCPCB en un clic.

## 4. Synchronisation
- Dès que tu as fini une étape (Schéma fini, Empreintes associées, ou placement partiel) :
  `git add .`
  `git commit -m "Message décrivant ton avancée"`
  `git push`
- Je recevrai une notification et je pourrai vérifier les connexions ou t'aider sur le placement.

## 5. Règles de Design (DRC)
- **Largeur de piste Puissance :** 0.3mm minimum.
- **Largeur de piste Signal :** 0.2mm.
- **Isolement :** 0.2mm.
