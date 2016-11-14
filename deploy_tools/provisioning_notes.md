Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg. on Ubuntu:
 
  sudo apt-get install nginx git python3 python3-pip
  sudo pip3 install vitualenv

## Nginx Virtual Host config

* nginx.template.conf
* replace SITENAME with, eg, tddstage.thezs.net

## VirtualEnv

* virtualenv --python=python3 /home/username/sites/SITENAME/virtualenv
* /home/username/sites/SITENAME/bin/pip3 install gunicorn
## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, tddstage.thezs.net

## Folder structure:
Assume we have a user account at /home/username

/home/username
|___ sites
     |___ SITENAME
          |___ database
          |___ source
          |___ static
          |___ virtualenv


