#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan Mador-House'
SITENAME = u'MusicNate'
SITEURL = ''

PATH = '/home/musicnate/Documents/MusicNate/content/'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = ("pelican-themes-master/bricks")
THEME_COLOR = 'cyan'
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
SIDEBAR_ABOUT = "Musician, Programmer and Amateur Powerlifter."
# MENUITEMS = (('HELP', '/pages/HELP'), ('Projects', '/pages/projects.html'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
