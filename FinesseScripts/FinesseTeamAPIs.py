# FinesseTeamAPI to access the team object and list all team messages.


# URL "http://<FQDN>/finesse/api/Team/<id>?includeLoggedOutAgents=true"  # GET -> allow user to get a copy of the team object

# URL "http://<FQDN>/finesse/api/User/<Teamid>/TeamMessages"  # GET -> Get a list of all active team messages for a particular team

# GET Finesse team details below:

import requests

URL = input('Enter the URL in this format -> "http://<FQDN>/finesse/api/Team/2": ')

HEADERS = {'authorization': "Basic IQUWHEF98EUE8V9VEF9V", "Cache-control": "no-cache"}

RESPONSE = requests.request("GET", URL, headers=HEADERS)

print (RESPONSE.text)
