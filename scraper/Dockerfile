FROM centos:7

MAINTAINER Alastair McClelland <alastair.mcclelland@gmail.com>

RUN yum install -y epel-release http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
RUN yum install -y python-pip vim tree tmux htop wget
RUN yum clean all

RUN pip install --upgrade pip
RUN pip install requests argh

MAINTAINER Alastair McClelland <alastair.mcclelland@gmail.com>
