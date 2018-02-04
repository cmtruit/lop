import os
import subprocess

#install the requirements
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

command = 'source ' + BASE_DIR + '/lop/env/bin/activate'
subprocess.Popen(command, shell=True).wait()

print BASE_DIR
PROJECT = '/lop'
TEMPLATE = '/template/pg_hba.conf'
packages = ["epel-release", "postgresql-server", "postgresql-devel", "postgresql-contrib", "python-pip"]
for p in packages: 
    command = '/usr/bin/yum -y install ' + p
    subprocess.Popen(command, shell=True).wait()

command = '/bin/pip install -r requirements.txt'
subprocess.Popen(command, shell=True).wait()

command = 'sudo postgresql-setup initdb'
subprocess.Popen(command, shell=True).wait()

command = '/usr/bin/systemctl enable postgresql'
subprocess.Popen(command, shell=True).wait()

command = '/usr/bin/systemctl start postgresql'
subprocess.Popen(command, shell=True).wait()

postgresconfig = '/var/lib/pgsql/data/pg_hba.conf'

command = '/usr/bin/cp ' + str(BASE_DIR + PROJECT+TEMPLATE + " " + postgresconfig)
subprocess.Popen(command, shell=True).wait()

command = '/usr/bin/systemctl restart postgresql'
subprocess.Popen(command, shell=True).wait()

### Setup the database ###

command = '/usr/bin/cat lop/setup.sh | /usr/bin/sh'
subprocess.Popen(command, shell=True).wait()


actions = ['makemigrations', 'migrate', 'test lop']


for action in actions:
    try:
        subprocess.Popen('python manage.py', action, shell=True)
    except:
        print "ERROR: cannot make any migrations or test lop"



