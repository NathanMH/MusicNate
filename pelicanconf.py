#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan Mador-House'
SITENAME = u'MusicNate'
SITEURL = 'https://www.musicnate.ca'

#PATH = '/home/musicnate/Documents/MusicNate/content/'
#PATH = 'C:\\Users\\natha\\Documents\\MusicNate\\content\\'
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
LINKS = (('Pronto Musica', 'http://www.prontomusica.org/'),
         ('Lara Deutsch', 'http://www.laradeutsch.ca/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = ("theme")
THEME_COLOR = 'cyan'

STATIC_PATHS = ['assets']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
