
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPage

VAR_USER = ""
VAR_PASSWORD = ""

usuario = VAR_USER
contraseña = VAR_PASSWORD
sitio = "https://quantil.co/xmlrpc.php"
cliente = Client(sitio, usuario, contraseña)
entradas = cliente.call(posts.GetPosts({'post_type': 'page'}, results_class=WordPressPage))
print(type(entradas))
if len(entradas) > 0:
    for entrada in entradas:
        print(entrada)
else:
    print("No hay entradas para mostrar")