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

  
## How to test
Dans le terminal
- Accéder au dossier du projet
- Lancer un docker build
  - `docker build -t tp-docker .`
- Tester les différents prix et les différents pourcentages en modifiant A et B
  - `docker run -it tp-docker python src/test_calc.py`


## Annexe
- Markdown langage : https://www.markdownguide.org/