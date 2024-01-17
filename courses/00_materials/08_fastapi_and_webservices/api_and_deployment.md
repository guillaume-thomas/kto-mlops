1 - Faire des APIS REST avec FastAPI

                a - C'est quoi une API REST ? Une requête HTTP ? Les verbs GET/PUT/POST/DELETE

                b - Faire une première route simple : /health

                c - Exposer notre model

                d - Mise en place des tests unitaires

                e - Tester notre service en local avec Postman

                f - La documentation avec Swagger

2 - Sécuriser notre API REST avec oAuth

                a - Les principes d'oAuth

                b - Configurer notre server d'authentification

                c - Sécuriser notre route de prediction

                d - Http / https + TLS (pour aller plus loin)

3 - La conteneurisation avec Docker

                a - C'est quoi ? En quoi c'est différent de la virtualisation ?

                b - Pourquoi c'est pertinent dans un projet ML ?

                c - Les fondamentaux du client docker (quelques commandes simples)

                d - Ecriture d'un premier Dockerfile

                e - Construire les Dockerfile de nos services

                f - Premier test en local avec docker compose

                g - Enregistrement de notre image dans DockerHub

4 - L'orchestration de conteneurs avec Kubernetes

                a - Pourquoi Kubernetes ?

                b - C'est quoi OpenShift ?

                c - Comment fonctionne Kubernetes ?

                d - Mise en place de nos manifestes de déploiements de nos images

                e - Déploiement dans notre Sandbox Openshift (via le client ou via ArgoCD ?)

                f - Tests de masse de notre service avec MLCli

5 - Le monitoring de notre service (Bonus en fonction du temps)

                a - En quoi c'est important ?

                b - Qu'est-ce que la boucle de feedback ? Rappel du Data drift et concept drift.

                c - Que sont Prometheus et Graphana ?

                d - Mise en place des métriques de base de FastApi dans notre API

                e - Configurer Prometheus et Graphana

                f - Notre premier Dashboard

                g - Mettre en place des métriques ayant un sens métier