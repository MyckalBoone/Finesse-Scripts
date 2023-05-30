# Generate Base64 Encoding

import base64

ENCODED = base64.b64encode('devasc:strongpassword'.encode('UTF-8'))
print (ENCODED.decode('utf-8'))
