from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.users import GetUserInfo

VAR_USER = ""
VAR_PASSWORD = ""

usuario = VAR_USER
contraseña = VAR_PASSWORD
sitio = "https://quantil.co/xmlrpc.php" #Recuerda que debes llamar al archivo xmlrpc.php
cliente = Client(sitio, usuario, contraseña)
datos_usuario = cliente.call(GetUserInfo())
print("Tu nombre de usuario es {}".format(datos_usuario))