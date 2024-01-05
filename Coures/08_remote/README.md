

## 1. Remote : dépot distante 

Pour connaître le nom du dépôt distant associé à votre dépôt Git local, vous pouvez utiliser la commande suivante :

```bash
git remote -v
```

Cette commande affiche les noms des dépôts distants configurés et leurs URL associées. Elle liste également les dépôts distants pour lesquels vous avez la permission de pousser (`fetch` et `push`). L'option `-v` signifie "verbeux", ce qui signifie qu'elle affiche plus d'informations.

Par exemple, si vous avez un dépôt distant appelé "origin", vous verrez quelque chose comme ceci :

```bash
origin  https://github.com/utilisateur/nom_du_depot.git (fetch)
origin  https://github.com/utilisateur/nom_du_depot.git (push)
```

Dans cet exemple, "origin" est le nom du dépôt distant, et les URLs indiquent les adresses du dépôt à partir desquelles vous pouvez tirer (`fetch`) et pousser (`push`). Vous pouvez avoir plusieurs dépôts distants configurés, et chacun d'eux sera répertorié avec son nom associé.

Si vous voulez juste le nom du dépôt distant (sans les URLs), vous pouvez utiliser la commande suivante :

```bash
git remote
```

Cela affichera simplement les noms des dépôts distants, un par ligne.



   - *Description :* Pousse les changements locaux vers un dépôt distant, généralement après un commit local.
   - *Exemple :* `git push origin master`
   - *Options :* 
     - `<remote>` : Nom du dépôt distant.
     - `<branch>` : Nom de la branche.