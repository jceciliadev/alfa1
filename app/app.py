from types import MethodDescriptorType
from flask import Flask,render_template,config,request,redirect,url_for,flash,jsonify
from flask.templating import render_template_string
from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path='/static')
#configurar DB mysql
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "barber"
app.config["MYSQL_PASSWORD"] = "Password123$"
app.config["MYSQL_DB"] = "shop_barber"
mysql = MySQL(app)
app.secret_key = ""

# inicializar la app
def inicializarApp(config):
    app.config.from_object(config)
    return app 



@app.route("/")

@app.route("/index" )
def main():
  return render_template("index.html")
 

@app.route("/Estilo_de_Corte")
def estilos_corte():
    return render_template("Estilo_de_Corte.html")


@app.route("/glob",methods =["POST", "GET"])
def glob():
      if request.method == 'POST':
        return render_template ("glob.html")



@app.route("/about",methods =["POST", "GET"])
def about():
    return render_template("about.html")

@app.route("/contact",methods =["POST", "GET"])
def contact():
    return render_template("contact.html")
    

@app.route("/add_contact",methods=['GET',"POS"])
def Concertar_Cita():
    if request.method == " POST":
        nombre= request.form['nombre']
        apellido= request.form['apellido']
        telefono=request.form['telefono']
        email=request.form['email']
        
    return render_template("/add_contact.html")


	



if __name__ == "__main__":
    app.run( port=3000,debug=True)