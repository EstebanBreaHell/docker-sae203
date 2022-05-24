## Rendu de projet SAE 2.03 site d'upload de documents.

Ce projet a été fait sous la base d'un docker Debian sur lequel tout les besoins nécessaire au projet s'installe grâce au docker file.

#Site d'upload de Document.

Nous avons décidé de créer un site qui permet de partager des documents et de télécharger les documents que les personnes ont partagé. Nous aurons donc en premier lieu l'endroit ou l'on ajoute les fichiers au site et un autre endroit avec la liste des documents ajoutés que l'on pourra regarder dans le navigateur et télécharger.



### HTML
### Python 
### Flask
### Le docker


-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# HTML

Vu que nous avons créé un projet web, il nous fallait une base de HTML, celle-ci est nommée base.html. Il est alimenté grâce à Python et on se sert du même fichier base.html pour la partie d'upload et la partie où l'on regarde les fichier stockés.

Le CSS est présent, il n'est pas nécessaire au projet mais il rend le site beaucoup plus agréable d'usage.


------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
# Python

Python a été un choix parmis tant d'autres, nous avions de base commencé le projet en PHP mais c'était très compliqué d'apprendre le langage sur une courte durée, donc nous avons opté pour du Python car c'est un language plutôt simple à comprendre. De plus certains membres en avaient déja fait auparavant et ils étaient à l'aise avec la librairie utilisé.
Le code python génère les requêtes et "Crée les pages web" grâce à un module de model, on indique du code HTML et il crée des pages grâce a ce code HTML qu'il peut répéter.
C'est très utile pour générer la liste des fichiers disponibles à chaque fois qu'on crée un nouvel élément dans la liste.

On a aussi pu s'en servir dans la page d'upload du fichier car lorsqu'on ajoute un fichier il faut remettre la page à vide avec aucun fichier de chargé pour éviter les multiples uploads par mégarde.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Flask

Flask est une librairie en Python, elle est utilisée pour le développement web et de notre côté on s'en est servi pour l'interaction avec la page web au niveau de l'upload de documents et de la récupération des documents sur le serveur. Nous nous sommes beaucoup aidés de la documentation et de tutoriels pour arriver à comprendre ce que c'était étant donné que c'était nouveau.

Les avantages de Flask sont sa facilité d'usage et sa lisibilité dans le code, de plus il fait le travail demandé en peu de temps.

Flask fut la librairie que nous avons le plus utilisé mais il y a 2 autres librairies que nous avons utilisé : Wheel et uWSGI sont des packages pour supporter la page web qui tourne sous Flask.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Le docker

Comme demandé, le docker est sous la dernière version de Debian.
Nous n'avons pas apporté beaucoup de modifications au docker, juste mis à jour les packages et installé python3-pip de façon à installer tout ce dont a besoin le programme.

Puis ajouté le code en transférant le fichier "/sae203" et changé le document dans le quel nous agissons grace a WORKDIR pour aller dans "/sae203".

Après cela nous lançons le téléchargement des packages dont Python a besoin pour faire tourner le programme, c'est automatisé grâce au fichier requirement.txt


Et dernière étape, nous lançons le serveur grâce a uWSGI sur le port 80 pour qu'après il s'addapte bien au port demandé par l'utilisateur.
