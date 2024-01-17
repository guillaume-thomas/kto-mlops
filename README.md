# Projet support du cours API & Cloud for Data Business

## Introduction

Ce projet est initialement destiné à servir de support de cours pour la matière **API & Cloud for Data Business**, à destination de la promotion **M2 Data & IA** de l'**Université Catholique de Lille**.</p>
On y retrouve l'intégralité d'un projet de ML temps réel, son encapsulation en Webservice et son déploiement dans le Cloud.
Toutes les étapes élémentaires des pratiques de MLOps sont représentées.
Ce projet ainsi que l'intégralité des supports de cours sont **open sources**.

Ce cours a été construit avec Guillaume Chervet que je remercie ici au passage.

C'est une version revue et corrigée de son itération précédente que vous trouverez [ici](https://github.com/guillaume-thomas/MLOpsPython-2022-2023)

La partie pratique de ce cours ne nécessite pas d'installation particulière sur votre machine, à l'exception de [Bruno](https://www.usebruno.com/)
pour tester des webservices. Nous utiliserons GitHub Codespaces pour développer, les GitHub Actions pour automatiser nos pipelines de CI/CD
et Red Hat Developer Sandbox pour entraîner nos modèles et héberger nos Webservices. Nous utiliserons MLFlow pour tracer nos
expériences et sauvegarder nos modèles. Tous ces éléments seront expliqués pendant ce cours et les protocoles d'inscriptions et 
installations détaillés.


## Programme

1. [Intro: MLOPs](./courses/01_intro.md)
    - Présentation du cours
    - Tour de table
    - Présentation de la structure des cours
    - Règles de vie 
    - Notations
    - Présentation du MLOps
    - Mise en place de l'environnement de travail
    - Présentation de la cible à atteindre
2. [Git, GitHub, OpenSource et licencing](./courses/02_git.md)
    - Introduction
    - Git en quelques mots ?
    - Comment collaborer et partager des fichiers ?
    - Les différences entre chaque type de gestionnaire
    - Les avantages du développement distribué
    - Les branches
    - Quelques mots sur GitHub
    - Comment installer Git ?
    - Les commandes de base
    - Comment revenir en arrière ?
    - Merger
    - Modifier l'historique (commandes avancées)
    - Bonnes pratiques
    - L'Open Source
    - Les points d'attention sur le Licensing
3. [Python, Unit Test & Clean code](./courses/03_python_unit_tests_clean_code)
    - Bases de Python
    - Les tests unitaires et TDD
    - Clean code, les principes fondamentaux
4. [Scoping, Data préparation et Annotations](./courses/04_scoping_data_prep_label)
    - Présentation du projet
    - Présentation du dataset
    - Préparation de la donnée
    - Présentation et installation d'ecotag
    - Annotations des images
    - Versioning de la donnée et stockage
5. [Train dans un notebook](./courses/05_train_in_a_notebook.md)
    - Installation et présentation de JupyterLab
    - Training de notre modèle dans un Notebook
    - Les limites de la démarche
    - Proposition d'alternative à notre Notebook
6. [Les plateformes de ML sur le Cloud](./courses/06_ml_platforms.md)
    - Présentation du cloud et ses avantages
    - Présentation des solutions du marché
        - Databricks / MLFlow
        - OpenShift DataScience
        - Azure ML
    - Présentation de kto-mlflow
    - Training avec MlFlow
7. [Continuous Integration](./courses/07_ci.md)
    - A quoi ça sert ?
    - Publier un package pour commencer
    - Mise en place de nos github actions
    - Lancer une expérimentation de manière continue
8. [Création d'API avec FastAPI](./courses/08_fastapi_and_webservices.md)
    - FastAPI
    - OpenAPI / Swagger et la documentation
    - Sécurité avec oAuth2
9. [Docker](./courses/09_docker.md)
    - Qu'est-ce que c'est ?
    - A quoi ça sert ?
    - Comment ça fonctionne ?
    - Manipulation de Docker
10. [Kubernetes](./courses/10_kubernetes.md)
    - Qu'est-ce que c'est ?
    - A quoi ça sert ?
    - Comment ça fonctionne ?
    - Manipulation sur OpenShift 
    - Cloud act, cloud souverain et reversibilité
11. [Continuous deployment](./courses/11_cd.md)
    - Les principes
    - GitOps
        - Argo CD
        - FluxCD
    - Mise en place simple pour notre projet
12. [Les tests d'intégration](./courses/12_integration_tests)
13. [Mesurer la performance de notre solution (bonus)](./courses/13_measure_performance.md)

## En cas de pépins

Pas de panique, certaines limitations avec les outils que l'on utilise peuvent amener à des erreurs ou à la disparition
du travail effectué (notamment sur la SandBox Openshift). C'est normal, nous sommes sur des environnements de test et de 
développement. Une section [Troubleshooting](./courses/99_troubleshooting.md) est disponible pour recenser ces éventualités
et proposer une solution. Merci donc de vous y reporter.

## Bibliographie et remerciements

Bibliographie : 
- [Le MLOps est une aventure humaine](https://github.com/guillaume-chervet/Les-Minutes-MLOps/blob/main/Le%20MLOps%20est%20une%20aventure%20humaine.pptx) de Guillaume Chervet
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://ieeexplore.ieee.org/document/10081336)
D. Kreuzberger, N. Kühl and S. Hirschl, "Machine Learning Operations (MLOps): Overview, Definition, and Architecture," in IEEE Access, vol. 11, pp. 31866-31879, 2023, doi: 10.1109/ACCESS.2023.3262138.
- [Pro Git](https://git-scm.com/book/fr/v2) de Scott Chacon, Ben Straub
- [Page Wikipédia sur Git](https://fr.wikipedia.org/wiki/Git)
- Page de Tortoise sur [Les Concepts de base du contrôle de version](https://tortoisesvn.net/docs/release/TortoiseSVN_fr/tsvn-basics-versioning.html)
- [Licences open source : types et comparaison](https://snyk.io/fr/learn/open-source-licenses/) de Snyk
- Licensing de [MuPdf](https://mupdf.com/licensing/index.html)
- [L'Open Source, qu'est-ce que c'est ?](https://www.redhat.com/fr/topics/open-source/what-is-open-source) de Red Hat
- Les cours de MLOps de DeepLearning.AI (pour l'illustration de la Timeline MLOps et pour m'avoir formé à la discipline)

Remerciements : 

Je voudrais tout d'abord remercier ma Compagne pour son soutien de tous les jours, ma Famille que j'aime et qui me définit, 
Guillaume Chervet pour son aide et le partage de ce cours et enfin, AXA France, mon équipe, Red Hat et L'Université Catholique 
de Lille pour leurs confiances toujours renouvelées.

Et un grand merci par avance à mes étudiantes et mes étudiants, pour leur confiance, leur attention et leur compréhension.

# Bon courage et bon cours !!!
![FUN](https://media.giphy.com/media/lmv5aDvwOgTmby3a13/giphy.gif)