python manage.py syncdb --noinput
python manage.py loaddata fixtures/*
python manage.py runserver 0.0.0.0:8000
