# cour 03 : 



## 1. 

Pour comprendre le fonctionnement de Git, il est essentiel de comprendre ces trois concepts principaux : le Working Directory (Répertoire de Travail), la Staging Area (Zone de Préparation ou Index), et le Local Repository (Dépôt Local). Ajoutons également le concept de Dépôt Distant pour une vue plus complète :

1. **Working Directory (Répertoire de Travail) :**
   - Le Working Directory est simplement le répertoire sur votre système de fichiers où vous travaillez avec vos fichiers. C'est là que vous créez, modifiez et supprimez des fichiers. Lorsque vous initialisez un nouveau dépôt Git, le contenu de ce répertoire est considéré comme non suivi par Git.

2. **Staging Area (Zone de Préparation ou Index) :**
   - La Staging Area est une zone intermédiaire entre le Working Directory et le Local Repository. Avant qu'un fichier ne soit enregistré dans l'historique du dépôt (commit), il doit être ajouté à la Staging Area. Cela vous permet de sélectionner spécifiquement les modifications que vous souhaitez inclure dans le prochain commit. Vous utilisez la commande `git add` pour déplacer des modifications du Working Directory vers la Staging Area.
   
3. **Local Repository (Dépôt Local) :**
   - Le Local Repository est la base de données Git locale qui stocke l'historique complet des commits et des changements. Lorsque vous effectuez un commit avec `git commit`, les modifications dans la Staging Area sont enregistrées dans le Local Repository. Cela crée une capture instantanée de l'état de votre projet à ce moment-là. Vous pouvez revenir à n'importe quel point dans l'historique à l'aide de commits.

4. **Dépôt Distant :**
   - Le Dépôt Distant est un serveur distant où vous pouvez stocker et partager votre projet Git avec d'autres collaborateurs. Les dépôts distants sont utiles pour la collaboration, la sauvegarde et le déploiement. GitHub, GitLab et Bitbucket sont des exemples de plateformes de dépôts distants populaires. Vous pouvez cloner un dépôt distant sur votre machine locale pour travailler sur le projet, puis pousser vos modifications vers le dépôt distant avec `git push`.

En résumé, le cycle de travail typique avec Git consiste à modifier les fichiers dans le Working Directory, à les ajouter à la Staging Area pour sélectionner les modifications à inclure dans le prochain commit, à effectuer un commit pour enregistrer ces modifications dans le Local Repository, puis à pousser ces commits vers un Dépôt Distant pour la collaboration et le partage avec d'autres. Ces concepts clés sont au cœur du modèle de versionnement décentralisé de Git.