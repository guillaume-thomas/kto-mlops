# Troubleshooting

Cette page vous permettra de répondre à certains problèmes que vous pourriez rencontrer pendant la réalisation de ce projet.
Voici les problèmes connus et les moyens de les résoudre.

## Erreur 401 sur openshift dans mes github actions, que faire ?

Il n'est pas impossible que certaines fois, quand on lance la github action, l'erreur suivante apparaisse :

HTTP response body:
```json 
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "Unauthorized",
  "reason": "Unauthorized",
  "code": 401
}
```

Il s'agit de votre jeton OnpenShift qui n'est plus valide. Il faut donc le [renouveler](07_ci.md). Reprenez l'étape
des variables d'environnement et les secrets dans GitHub, et renseignez un nouveau jeton dans le secret OPENSHIFT_TOKEN.
Vous trouverez le lien vers ce jeton ici, puis Display token :

![create_secrets_and_variables.png](00_materials/07_ci/create_secrets_and_variables.png)


## Les 30 jours de ma Sandbox sont passés, il n'y a plus rien, que faire ?

"Malheureusement", pas le choix, il faut [réactiver votre Sandbox](01_intro.md#création-de-notre-compte-red-hat-et-provisionnement-de-notre-red-hat-developer-sandbox), réinstaller [kto-mlops](04_scoping_data_prep_label.md#installation-de-kto-mlflow-et-présentation-de-minio-et-dailyclean) 
et enregistrez [de nouveau les données dans minio](04_scoping_data_prep_label.md#versionning-de-la-donnée-et-stockage). 
Pour vous éviter de tout refaire à la main, il existe un script de réinitialisation.

## Red Hat Developer Sandbox est lent, ça ne fonctionne pas ... Que faire ?

Malheureusement, cela peut arriver et ce n'est pas illogique. Il s'agit d'un cluster partagé pour expérimenter la solution.
Il ne s'agit en aucun cas d'une plateforme de production avec garantie de disponibilité. N'oubliez pas, cette Sandbox est 
gratuite.