# DriveDuWish
DriveDuWish est une application web permettant aux utilisateurs de gérer leurs fichiers et dossiers sur un drive en ligne, avec des fonctionnalités d'authentification, de téléchargement, de navigation et de visualisation.


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

# Comment lancer DriveDuWish ?

## Méthode 1 : docker 🐬

### Ressources nécessaires :
>Docker Desktop <br>
>Invite de Commande

### Tutoriel :
Dans votre invite de commande tapez ces deux commandes depuis la racine de l'application :
>docker-compose build <br>
>docker-compose up

Docker se chargera ensuite du reste et vous pourrez accéder à DriveDuWish depuis<br>
>http://127.0.0.1:8000/<br>
ou<br>
>http://localhost:8000/

### Par défaut il existe un compte user:admin | password:admin mais libre à vous d'en créer d'autres! 

## Méthode 2

