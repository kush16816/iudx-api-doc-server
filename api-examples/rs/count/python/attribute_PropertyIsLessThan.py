import requests

url = "https://localhost/resource-server/pscdcl/v1/count"

payload = "{\n\t\"id\" : \"rbccps.org/aa9d66a000d94a78895de8d4c0b3a67f3450e531/pscdcl/aqm-bosch-climo/Ambedkar society circle_29\",\n\t\"attribute-name\" : \"LIGHT\",\n\t\"attribute-value\": \"2900\",\n\t\"comparison-operator\": \"propertyislessthan\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

