## Rendu de projet SAE 2.03 site d'upload de Docuement.

Ce projet a était fait sous la base d'un docker débian sur le quel tout les besoins nécessaire au projet 

#Site d'upload de Document.

Nous avons décidé de crée un site qui permet de partagé des document et de téléchargé les document que les personne on partagé. nous aurons donc en premier lieu l'endroit ou l'on ajoute les fichier au site et un autre endroit avec la liste des document ajouter que l'on pourra regarder dans le navigateur et téléchargé.



### Html
### Python 
### Flask
### Le docker


-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Html

Vus que nous avons crée un projet web il nous fallait une base de html, cette base html éxiste elle est nommé base.html. il est alimenté grace a python et on se sert du meme fichier base.html pour la partie d'upload et la partie ou on regarde les fichier stocker.

Le css est présent mais n'est pas nécessaire au projet mais il rend le site beaucoup plus agréable d'usage.


------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Python

Python a était un choix parmis tant d'autre nous avions de base commencer le projet en php mais c'était très compliquer d'apprendre le language durant un peu court de temps donc nous avons opté pour du python car c'est un language plutot simple a comprendre de plus certain membre en avait déja fait au par avant et ils était a l'aise avec la librairie utilisé.

Le code python génère les requette et "Crée les pages web" grace a un module de model, on indique du code html et il crée des page grace a ce code html que il peut répété.
c'est très utile pour généré la liste des fichier disponible a chaque fois on crée un nouvelle élément dans la liste.

On a aussi pus s'en servire dans la page d'upload du fichier car l'orsque l'on ajoute un fichier il faut remetre la page a vide avec aucun fichier de charger pour évité les multiple upload par mégarde.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Flask

Flask est une librairie en python elle est utilisé pour le développement web et de notre coté on s'en ait servie pour l'interaction avec la page web au niveau de l'upload de document et de la récupération des document sur le serveur. Nous nous somme beaucoup aidé de la documentation et de tutoriel pour arrivé a comprendre ce que c'était étant donnée que c'était nouveau.

Les avantage de Flask sont sa facilité d'usage et sa lisibilité dans le code , de plus il fait le travail demandé sans trop de temps.

Flask fut la librairie que nous avons le plus utilisé mais il y a 2 autre librairie que nous avons utilisé : Wheel et uwsgi sont des package pour supporter la page web qui tourne sous Flask.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Le docker

Comme demandé le docker est sous la dernier version de débian.
Nous n'avons pas apporté beaucoup de modification au docker juste mis a jour les package et installé python3-pip de façon a installé tout ce dont a besoins le programme.

Puis ajouté le code en transferant le fichier "/sae203" et changer le document dans le quel nous agissont grace a WORKDIR pour aller dans "/sae203".

Après cela nous lançon le téléchargement des package dont python a besoins pour faire tournée le programme, c'est automatisé grace au fichier requirement.txt


Et dernier étape nous lançons le serveur grace a uwsgi sur le port 80 pour que après il s'addapte bien au port demandé par l'utilisateur.
