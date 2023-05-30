# Dialog between two users -> make a call , record call, etc...


# URL "http://<FQDN>/finesse/api/User/<id>/Dialogs"  # "POST" with xml body -> Allow user to make call

# URL "http://<FQDN>/finesse/api/Dialog/<dialogId>"  # "PUT" with xml body -> Allow a user to start recording an active call


# Initiate a dialog between two numbers:

import requests

URL = input('Enter the URL in this format -> "http://<FQDN>/finesse/api/User/<id>/Dialogs": ')
OUTGOING = input('Enter outgoing call extension: ')
INCOMING = input('Enter the receiving extension: ')

PAYLOAD = (
    "<Dialog>" +
    "    <requestedAction>MAKE_CALL</requestedAction>" +
    "    <fromAddress>" + OUTGOING + "</fromAddress>" +
    "    <toAddress>" + INCOMING + "</toAddress>" +
    "</User>"
)

HEADERS = {'authorization': "Basic IQUWHEF98EUE8V9VEF9V", 'Content-Type': "application/xml", 'cache-cotrol': "no-cache"}

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)

print (RESPONSE.text)
print (RESPONSE.status_code)
