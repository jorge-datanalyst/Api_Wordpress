from wordpress_xmlrpc import Client, WordPressPost, WordPressPage
from wordpress_xmlrpc.methods import posts

VAR_USER = ""
VAR_PASSWORD = ""

usuario = VAR_USER
contraseña = VAR_PASSWORD
sitio = "https://quantil.co/xmlrpc.php"

client = Client(sitio, usuario, contraseña)

page = WordPressPage()
page.title = 'About Me'
page.content = 'I am an aspiring WordPress and Python developer.'
page.post_status = 'publish'
page.id = client.call(posts.NewPost(page))

# no longer aspiring
page.content = 'I am a WordPress and Python developer.'
client.call(posts.EditPost(page.id, page))
