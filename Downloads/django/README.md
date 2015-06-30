A simple Django project starter
===============================

Requires Django 1.4 and higher.

Features
--------
* `modernizr.js`, `respond.js`, `jQuery`
* compass/sass - files are in directory `media/sass`
* css resets are applied
* default database engine is sqlite3, change in settings.py if necessary
* directory project_conf contains settings.py and urls.py
* html5 doctype in the base template with screen, print and IE fixes js files (from sass)
* easy to switch between Django and Jinja2 templates
* the template is based on html5 boilerplate
* base template works both with Django and Jinja2 templates

Installation
------------
* clone git repository
* install compass and run it inside `media` directory
  (requires ruby & rubygems: gem install compass)

Usage
-----
* It is suggested to add custom apps at the root,
  alongside with `project_conf`
  or install them into the virtual environment
* Directory `project_conf` does not need to be renamed
* Default url '/' displays the "base.html" template - extend this template

Authors
-------
* Evgeny Fadeev (evgeny.fadeev@gmail.com)

License
-------
* MIT License
