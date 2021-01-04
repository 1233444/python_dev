import os
import requests

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")
# assign sensitive information right inside the code, no good practice
# db_password = 'my_db_pass_123!'
print(db_user)
print(db_password)
r = requests.get("https://coreyms.com")
print(r.status_code)
