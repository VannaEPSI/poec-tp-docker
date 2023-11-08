# TP DOCKER
### Doc version : v1 - 08/11/2023
## Project description
Calculer un nouveau prix avec la TVA

## Technical info / folder architecture
- infra : every files linked to deployment in test/production (devops only.)
- src : source code
- ...

## Prerequisites
- Docker
- Python 3.12

## How to dev

- Lancer un docker build du projet
  - `docker build -t tp-docker .`
- Lancer un docker run du projet
  - `docker run -it tp-docker python src/main.py A B`
  - Avec A le prix et B la TVA
- 


## How to test
- ...
   

## Annex
- Markdown langage : https://www.markdownguide.org/