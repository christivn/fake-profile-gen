import requests, json

url = 'https://randomuser.me/api/?nat=es'
x = requests.get(url)
json=json.loads(x.text)

nombre=json["results"][0]["name"]["first"]
apellido=json["results"][0]["name"]["last"]
email=json["results"][0]["email"]
nick=json["results"][0]["login"]["username"]
password=json["results"][0]["login"]["password"]
foto=json["results"][0]["picture"]["large"]
pais=json["results"][0]["location"]["country"]

print("\033[93m+-----------------------------------------+\033[0m")
print("\033[33m\033[01m Nombre:\033[0m "+nombre)
print("\033[33m\033[01m Apellido:\033[0m "+apellido)
print("\033[33m\033[01m Foto:\033[0m "+foto)
print("")
print("\033[33m\033[01m Email:\033[0m "+email)
print("\033[33m\033[01m Nick:\033[0m "+nick)
print("\033[33m\033[01m Contraseña:\033[0m "+password)
print("\033[93m+-----------------------------------------+\033[0m")
