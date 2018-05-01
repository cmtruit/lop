#!/usr/bin/bash


#install:
#pip install coverage
#pip install -r requirements.txt

#before_script:
   psql -c "CREATE DATABASE lop;" -U postgres
   psql -c "CREATE USER lopadmin WITH PASSWORD 'lop';" -U postgres
   psql -c "ALTER ROLE lopadmin  SET client_encoding TO 'utf8';" -U postgres
   psql -c "ALTER ROLE lopadmin SET default_transaction_isolation TO 'read committed';" -U postgres
   psql -c "ALTER ROLE lopadmin SET timezone TO 'UTC';" -U postgres
   psql -c "GRANT ALL PRIVILEGES ON DATABASE lop TO lopadmin;" -U postgres
   psql -c "ALTER USER lopadmin CREATEDB;" -U postgres

#script:
#   cd ./lop/
#   python manage.py makemigrations
#   python manage.py migrate
#   python manage.py test lop

