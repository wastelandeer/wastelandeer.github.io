import os
import sys
sys.path.append(os.curdir)
from pdfgen import (NAME, TAGLINE, PIC, EMAIL, LINKEDIN, GITHUB, TELEGRAM,
    EDUCATIONS, LANGUAGES, INTERESTS, EXPERIENCES, SKILLS, THEME)

AUTHOR = 'wastelandeer'
SITENAME = 'Resume project'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'images/resume.pdf': {'path': 'static/resume.pdf'},
}

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),) 

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Hold theme folder inside "content" folder
IGNORE_FILES = ['theme']

PDF = 'resume.pdf'
OPEN_TO_WORK = True