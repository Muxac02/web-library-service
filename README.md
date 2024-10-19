this is a study project with
back: python sqlalchemy+fastAPI, postgresql
front: next.js


**QUICK START GUIDE**

-install py 3.11.9+
-create venv
-in active venv:
py -m -pip install -r \requirments.txt

download docker and latest postgres image with
docker run --name web-library-service -e POSTGRES_USER=YOURUSERNAME -e POSTGRES_PASSWORD=YOURPASSWORD -p 5432:5432 -d postgres

database/\_\_init\_\_    correct your DATABASEURL with correct username, password and db name

create db in postgres with name that you use in url

create .env file and create in it env variables
SECKRET_KEY
ALGHORITM
ACCESS_TOKEN_EXPIRE_MINUTES
