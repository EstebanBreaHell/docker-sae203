# Projet SAE 2.03 Equipe 26


# Serveur partage de fichier.

# Instalation : 
pour cloner le repertoir il faut faire : 
```
git clone https://github.com/EstebanBreaHell/docker-sae203
```
# Création de l'image docker : 
Une fois dans le dossier 'docker-sae203' il faut crée l'image docker via la commande 

**le nom de l'image doit êtr en minuscule entierement.**
```
docker build -t <choisir-un-nom-pour-l'image> .
```

# Lancement du docker :

```
docker run --name <nom du conteneur de votre choix> -d -p <port au choix>:80 <nom-de-l'image-choisie>
```

# Puis il reste a aller sur le site :) 

pour cela il vous suffit de aller dans votre 'http://localhost:<port choisi au run>'
