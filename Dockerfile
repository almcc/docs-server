FROM almcc/base-image:0.1.1

RUN pip install Django django-cors-headers django-filter djangorestframework rest-framework-ember django-bootstrap-form requests

MAINTAINER Alastair McClelland <alastair.mcclelland@gmail.com>

EXPOSE 80
