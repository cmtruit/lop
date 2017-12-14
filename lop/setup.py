import os
import subprocess

#install the requirements
try:
    r = subprocess.Popen('/bin/pip', 'install', '-r', 'requirements.txt', shell=True)
except:
    print "WARNING: cannot install requirements from pip install"

### Setup the database ###

createdb = '\"CREATE DATABASE lop\;\"'
createdbuser = '\"CREATE USER lopadmin WITH PASSWORD \'lop\'\;\"'
setencode = '\"ALTER ROLE lopadmin  SET client_encoding TO \'utf8\'\;\"'
setisolation = '\"ALTER ROLE lopadmin SET default_transaction_isolation TO \'read committed\'\;\"'
setdbtimezone = '\"ALTER ROLE lopadmin SET timezone TO \'UTC\'\;\"'
giveuserpermission = '\"GRANT ALL PRIVILEGES ON DATABASE lop TO lopadmin\;\"'
allowusertocreatedb = 'psql -c \"ALTER USER lopadmin CREATEDB\;\"'

e = [
     createdb, 
     createdbuser, 
     setencode, 
     setisolation,
     setdbtimezone, 
     giveuserpermission, 
     allowusertocreatedb,
    ]


for x in e:
    #try:
    subprocess.Popen('psql -c', x+' -U postgres', shell=True)
    #except:
    #    print "ERROR: cannot execute ", x 

actions = ['makemigrations', 'migrate', 'test lop']


for action in actions:
    try:
        subprocess.Popen('python manage.py', action, shell=True)
    except:
        print "ERROR: cannot make any migrations or test lop"



