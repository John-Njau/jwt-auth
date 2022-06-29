serve:	
	python manage.py runserver

minify:
	python manage.py compress

migrations:
	python manage.py makemigrations
	python manage.py migrate

super:
	python manage.py createsuperuser