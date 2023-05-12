import json

datos = '{"nombre": "Rodri", "Edad": "16", "Año": "2006"}'
leerFormato = json.loads(datos)

print(leerFormato["nombre"])