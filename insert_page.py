from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

VAR_USER = ""
VAR_PASSWORD = ""

usuario = VAR_USER
contraseña = VAR_PASSWORD
sitio = "https://quantil.co/xmlrpc.php"

cliente = Client(sitio, usuario, contraseña)
nueva_entrada = WordPressPost()
nueva_entrada.title = "Soy otra entrada pública"

with open('index.html', 'r') as f:
    conte = f.read()

    nueva_entrada.content = conte
    id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
    print("Correcto! Se guardó la entrada como borrador, y su id es {}".format(id_entrada_publicada))
    print("Publicando entrada...")
    nueva_entrada.post_status = 'publish'
    resultado = cliente.call(posts.EditPost(id_entrada_publicada, nueva_entrada))
    if resultado is True:
        print("Entrada publicada")
    else:
        print("Algo salió mal")

"""Referencias"""
# https://python-wordpress-xmlrpc.readthedocs.io/en/latest/examples/posts.html#pages
# https://parzibyte.me/blog/2018/01/22/gestionando-sitio-blog-api-wordpress-python/


