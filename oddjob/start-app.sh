sleep 1
python manage.py migrate
python manage.py loaddata fixtures/*
gunicorn -c gunicorn_conf.py oddjob.wsgi:application --reload
