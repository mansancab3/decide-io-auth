% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && python manage.py makemigrations && python manage.py && migrate python manage.py loaddata data'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'

