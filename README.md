LOP
---

[![Travis](https://api.travis-ci.org/cmtruit/lop.svg?branch=master)](https://travis-ci.org/cmtruit/lop)

Lights-Out Patching is a Django app that manages Linux system patching


Quick start
-----------

1. Download or clone repo.
```
git clone https://github.com/cmtruit/lop.git
```

2. source the virtualenv.
```
cd lop
source env/bin/activate
```
3. Run `python manage.py makemigrations` to pre-setup the app.
4. Run `python manage.py migrate` to setup the app.
5. Run `python manage.py test lop` to start the tests.
6. Run `python manage.py createsuperuser` to create the admin login username/password (for administration)

7. Start the development server and visit http://127.0.0.1:8000/admin/
```
python manage.py runserver 0.0.0.0:8000 and visit http://127.0.0.1:8000/admin/
```
6. Use the username/password from Step 6 to login to the admin section of the app.

7. Add a user (This will be used to log into the app.)

8. Visit http://127.0.0.1:8000/

-----------------
