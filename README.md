# TP DOCKER
### Doc version : v1 - 08/11/2023
## Project description
Calculer un nouveau prix avec la TVA

## Technical info / folder architecture
- src :
  - calc.py
  - main.py
  - test_calc.py
- Dockerfile

## Prerequisites
- Docker

## How to dev
- Cloner le projet avec un git clone dans le terminal
  - `git clone https://github.com/VannaEPSI/poec-tp-docker-vannaly.git`

## How to use
Dans le terminal
- Lancer un docker build du projet
  - `docker build -t tp-docker .`
- Tester les différents prix et les différents pourcentages en modifiant A et B
  - `docker run -it tp-docker python src/main.py A B`
    - Avec A le prix et B le pourcentage de la TVA
- Exemple :
  - `docker run -it tp-docker python src/main.py 100 20`
  - `docker run -it tp-docker python src/main.py 'ABC' 20`
  - `docker run -it tp-docker python src/main.py -10 20`
  - `docker run -it tp-docker python src/main.py 100 -10`
  - `docker run -it tp-docker python src/main.py 100 110`
  
## How to test
Dans le terminal
- Accéder au dossier du projet
- Lancer un docker build
  - `docker build -t tp-docker .` (si le build n'a pas été lancé avant)
- Lancer le fichier test_calc.py pour lancer les tests
  - `docker run -it tp-docker python src/test_calc.py`


## Annexe
- Markdown langage : https://www.markdownguide.org/