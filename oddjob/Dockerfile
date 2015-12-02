FROM centos:7

MAINTAINER Alastair McClelland <alastair.mcclelland@gmail.com>

RUN yum install -y epel-release http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
RUN yum install -y gcc python-devel python-pip vim tree tmux htop wget postgresql postgresql-devel
RUN yum clean all

RUN pip install --upgrade pip
RUN pip install Django django-cors-headers django-filter djangorestframework rest-framework-ember django-crispy-forms psycopg2 gunicorn

MAINTAINER Alastair McClelland <alastair.mcclelland@gmail.com>

EXPOSE 8000
