

import requests

url_a_probar= "http://127.0.0.1:8000/comentario/1/"


get_responce = requests.get(url_a_probar)
print(get_responce)