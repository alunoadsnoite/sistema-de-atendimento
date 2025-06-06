
import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

def main():
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:5000'])

if __name__ == '__main__':
    main()
