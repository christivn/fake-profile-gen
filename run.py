import requests, json

url = 'https://randomuser.me/api/?nat=es'
x = requests.get(url)
json=json.loads(x.text)["results"][0]

nombre=json["name"]["first"]
apellido=json["name"]["last"]
email=json["email"]
nick=json["login"]["username"]
password=json["login"]["password"]
foto=json["picture"]["large"]
pais=json["location"]["country"]

print("\033[93m+-----------------------------------------+\033[0m")
print("\033[33m\033[01m Nombre:\033[0m "+nombre)
print("\033[33m\033[01m Apellido:\033[0m "+apellido)
print("\033[33m\033[01m Foto:\033[0m "+foto)
print("")
print("\033[33m\033[01m Email:\033[0m "+email)
print("\033[33m\033[01m Nick:\033[0m "+nick)
print("\033[33m\033[01m Contraseña:\033[0m "+password)
print("\033[93m+-----------------------------------------+\033[0m")
