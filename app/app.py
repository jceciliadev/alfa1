from types import MethodDescriptorType
from flask import Flask,render_template,config,request,redirect,url_for,flash,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
@app.route("/<path:path>")
def static_file(path):
    return app.send_static_file(path)

#configurar DB mysql
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
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
    return render_template("/contact.html")
    

@app.route("/add_contact",methods=['GET',"POS"])
def  Concertar_Cita():
    if request.method == " POST ":
        nombre= request.form['nombre']
        Apellido= request.form['Apellido']
        email=request.form["email"]
        phone=request.form["phone"]
        print(nombre)
        print(Apellido)
        print(email)
        print(phone)
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO Usuarios(nombre,Apellido,email,phone) VALUES (%s,%s,%s,%s)",(nombre,Apellido,email,phone))
        mysql.connection.commit()
        flash("Contacto agregado satisfatoriaamente")
        return redirect(url_for("/index"))
    else:
        return 'Error al agregar usuario'
 


	



if __name__ == "__main__":
    app.run( port=3000,debug=True)
    
    
    
    # mysql -u root -p
