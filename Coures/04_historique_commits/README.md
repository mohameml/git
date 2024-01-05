# cour 04 : **l'historique des commits**


## 1. **`git log`:**

- **Description:**
  
  La commande ``git log`` en Git est utilisée pour afficher l'historique des commits dans un dépôt. C'est l'une des commandes les plus fréquemment utilisées pour examiner les changements apportés au fil du temps dans un projet. 


- **les options:**

1. **`git log`**
  - Affiche l'historique des commits, avec des informations telles que l'auteur, la date, et le message de chaque commit.
    ```bash
    git log
    ```

2. **`git log --oneline` :**
   - Affiche l'historique des commits de manière condensée, chaque commit sur une seule ligne.
   ```bash
   git log --oneline
   ```

3. **`git log --graph` :**
   - Affiche l'historique des commits sous forme de graphique, montrant les branches et les fusions.
   ```bash
   git log --graph --oneline --all
   ```

4. **`git log --stat` :**
   - Affiche des statistiques pour chaque commit, montrant les fichiers modifiés et le nombre de lignes ajoutées/supprimées.
   ```bash
   git log --stat
   ```

5. **`git log --author="Nom de l'Auteur"` :**
   - Filtre les commits par auteur spécifié.
   ```bash
   git log --author="John Doe"
   ```

6. **`git log --since="date"` :**
   - Affiche les commits effectués depuis la date spécifiée.
   ```bash
   git log --since="2022-01-01"
   ```

7. **`git log --until="date"` :**
   - Affiche les commits effectués jusqu'à la date spécifiée.
   ```bash
   git log --until="2022-12-31"
   ```

8. **`git log --grep="motif"` :**
   - Filtre les commits en fonction d'un motif dans le message de commit.
   ```bash
   git log --grep="Correction de bug"
   ```


9. **`git log --follow nom_du_fichier` :**
    - Affiche l'historique des commits pour un fichier spécifique, même s'il a été renommé.
    ```bash
    git log --follow nom_du_fichier
    ```

10. **`git log -p` :**
    - Affiche les différences introduites dans chaque commit (un patch) en plus des informations standard.
    ```bash
    git log -p
    ```
    - ou pour un ficher spécifique :

    ```bash
    git log -p <nom_fichier>
    ```


11.  **``git log -n``:**

   - L'option `-n` dans la commande `git log` spécifie le nombre de commits à afficher dans les résultats. Elle limite la sortie aux `n` commits les plus récents. 


   ```bash
   git log -n <nombre>
   ```


12. **`git shortlog` :**
    - Affiche un résumé des commits par auteur.
    ```bash
    git shortlog
    ```



   



