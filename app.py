import os
from flask import Flask, render_template, request, flash, redirect, send_from_directory

#Code venant de la doc officiel ici on determine juste ou vont finir les fichier upload et les extension autorisé
UPLOAD_FOLDER = 'media'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#Les paramètre de base de flask l'utilitaire de python pour faire du web réactif
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Ici c'est juste une verification de l'extension du fichier pour voir si elle est accéptable
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Ici la "route" principal c'est globalement la page d'acceuil du site la ou on upload les fichier et ou on sera renvoyé si il y a un problème
@app.route("/", methods=["GET"])
def upload_form():
    #Ici on se sert de la méthode template de Flask qui permet de faire des site facilement en python
    return render_template("upload_form.html")

#Voila la méthode d'upload qui fait toute les vérification pour l'ajout du fichier 
#renvoie vers la route "/" si jamais il y a une erreur.
#Et renvois
@app.route("/upload", methods=["POST"])
def upload_file():

    if 'file' not in request.files:
        flash('No file part')
        return redirect("/")

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect("/")

    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect("/files")

#Ici on accède au fichier qui sont sur le site et on 
@app.route("/files", methods=["GET"])
def file_list():

    _list = os.listdir(UPLOAD_FOLDER)

    return render_template("file_list.html", list=_list)
#Ici on accède au fichier demander par l'utilisateur quand il clique dessu
@app.route("/media/<path:path>", methods=["GET"])
def serve_media(path):
    return send_from_directory(UPLOAD_FOLDER, path)