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
- Python 3.12

## How to dev
- Cloner le projet dans PYTHON avec un git clone dans le terminal
  - `git clone https://github.com/VannaEPSI/poec-tp-docker.git`


## How to test
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
   

## Annexe
- Markdown langage : https://www.markdownguide.org/