
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

VAR_USER = ""
VAR_PASSWORD = ""

usuario = VAR_USER
contraseña = VAR_PASSWORD
sitio = "https://quantil.co/xmlrpc.php"
cliente = Client(sitio, usuario, contraseña)
nueva_entrada = WordPressPost()
nueva_entrada.title = "El título de la entrada"
nueva_entrada.content = "Hola, yo soy el contenido. Claro que <strong>puedo</strong> llevar contenido HTML"
id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
print("Correcto! Se publicó la entrada, y su id es {}".format(id_entrada_publicada))