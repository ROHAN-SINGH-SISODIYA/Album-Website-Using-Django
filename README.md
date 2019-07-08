# Album-Website-Using-Django Framework

### This Project is design and developed using Django Framework 

### with MySQL Connectivity

### In this Website We can create a photo Album 

####Requirements
    
    Python: 3.5, 3.6, 3.7
    Django: 1.11, 2.0, 2.1, 2.2
    MySQL: 5.6, 5.7 / MariaDB: 10.0, 10.1, 10.2, 10.3
    mysqlclient: 1.3

###Run These Commands
      
      $ pip install django
      $ python -m django --version
      $ pip install mysql-python
      $ pip install mysqlclient
      $ python manage.py runserver
      
###Database Setup

      DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'python_django_db',
                'USER': 'root',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '3306',
            }
       }

      
      
