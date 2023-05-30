# Various methods and user APIs to perform operations with the user such as loggin in, listing, and changing properties


# URL "http://<FQDN>/finesse/api/User"  # GET -> List of all users

# URL "http://<FQDN>/finesse/api/User/<id>"  # GET -> copy of the user object | "PUT" with xml body -> sign in or change the user state(ready,not_ready,logout)

# URL "http://<FQDN>/finesse/api/User/<id>/Phonebooks"  # GET -> Get a list of phonebooks and the first 1500 associated contacts for that user

# User login below:

import requests

URL = input('Enter the URL in this format -> "http://<FQDN>/finesse/api/User/<id>": ')

PAYLOAD = (
    "<User>" +
    "    <state>LOGIN</state>" +
    "    <extension>6001</extension>" +
    "</User>"
)

HEADERS = {'authorization': "Basic IQUWHEF98EUE8V9VEF9V", 'Content-Type': "application/xml"}

RESPONSE = requests.request("PUT", URL, data=PAYLOAD, headers=HEADERS)

print (RESPONSE.text)
print (RESPONSE.status_code)
