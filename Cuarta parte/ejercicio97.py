import json

datosJson = {"nombre": "Rodri", "Edad": 16, "Año": 2006}
conversionjson = json.dumps(datosJson)
print(conversionjson)