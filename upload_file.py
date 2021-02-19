from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

VAR_USER = ""
VAR_PASSWORD = ""

usuario = VAR_USER
contraseña = VAR_PASSWORD
sitio = "https://quantil.co/xmlrpc.php"

client = Client(sitio, usuario, contraseña)

# set to the path to your file
filename = '/home/jorgeda/Downloads/Personal/utadeo.jpg'

# prepare metadata
data = {
        'name': 'utadeo.jpg',
        'type': 'image/jpeg',  # mimetype
}

# read the binary file and let the XMLRPC library encode it into base64
with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

response = client.call(media.UploadFile(data))
# for key in response:
#     print(key, '->', response[key])
#     if key == 'link':
#         print(key, '->', response[key])
#     elif key == ''    
print(response['attachment_id'])
