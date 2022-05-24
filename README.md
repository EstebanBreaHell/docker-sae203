## Rendu de projet SAE 2.03 site d'upload de Docuement.

Ce projet a était fait sous la base d'un docker débian sur le quel nous avons installé tout les besoins tel que Python et les librairie python stocker dans un dosser requirement.txt

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




Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/EstebanBreaHell/docker-sae203/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
