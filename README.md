# DriveDuWish
DriveDuWish est une application web permettant aux utilisateurs de gérer leurs fichiers et dossiers sur un drive en ligne personnel, avec des fonctionnalités d'authentification, de téléchargement, de navigation et de visualisation.

<br>

# Cahier des charges de l'application

* Authentification et création de compte ✔️
* Navigation dans les fichiers et dossiers ✔️
* Affichage des propriétés et métadonnées ✖️
* Téléchargement de fichiers ✔️
* Création de dossiers ✔️
* Déplacement et copie ✔️
* Limite de stockage par utilisateur de 100 MB ✔️
* Taille maximale de téléchargement de 40 MB ✔️
* Statistiques et graphiques sur l'espace de stockage ✔️
* Prévisualisation de formats connus ✔️
* Base de données SQLite ✔️
* Expérience utilisateur (UX) agréable et responsive ✔️
* Support pour l'affichage de texte, images, et lecture de vidéos (bonus) ✔️
  * Sauf PDF ✖️

### Quelques fonctionnalités supplémentaires 🔝
* Suppression de compte
* Drag and drop pour déplacer les fichiers
  * Instable mais codé

<br>

# Comment lancer DriveDuWish ?

## Méthode 1 : docker 🐬

### Ressources nécessaires :
>Docker Desktop <br>
>Invite de Commande

### Tutoriel :
Dans votre invite de commande tapez ces deux commandes depuis la racine de l'application :
```
> docker-compose build
> docker-compose up
```

Docker se chargera ensuite du reste et vous pourrez accéder à DriveDuWish depuis<br>
>http://127.0.0.1:8000/<br>
ou<br>
>http://localhost:8000/

*Par défaut il existe un compte user:admin | password:admin mais libre à vous d'en créer d'autres!*

<br>

## Méthode 2 : rustique 🔧

### Ressources nécessaires :
>Python <br>
>SQLParse & Django <br>
>Invite de Commande

### Tutoriel :
Dans votre invite de commande tapez ces deux commandes depuis la racine de l'application :
```
> python manage.py migrate
> python manage.py runserver
```

Ainsi votre application Django se lancera et sera accessible aux mêmes adresses que la méthode 1 <br>
>http://127.0.0.1:8000/<br>
ou<br>
>http://localhost:8000/

*Par défaut il existe un compte user:admin | password:admin mais libre à vous d'en créer d'autres!*