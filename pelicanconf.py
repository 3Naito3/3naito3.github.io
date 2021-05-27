#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = 'Naito'
SITENAME = "Horse"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
DISPLAY_CATEGORIES_ON_MENU = True
# MENUITEMS = (
#     ('Home', '/'),
# )

# Blogroll
LINKS = (
    # ('name', 'link'),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'custom.css'},
}
