#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import plumage

AUTHOR = 'Naito'
SITENAME = 'LovasBlog'
SITESUBTITLE = 'Egy lóimádó blogja'
SITEURL = ''
# LEFT_SIDEBAR = '<div>potatoes</div>'
SITE_THUMBNAIL = 'https://i2.lensdump.com/i/Z05svz.png'

THEME = plumage.get_path()
PLUGINS = ['pelican_webassets']

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
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Főoldal', '/category/fooldal.html'),
    ('Alapszínek', '/category/alapszinek.html'),
    ('Kevert színek', '/category/kevert-szinek.html'),
    ('Fehér mintázatok', '/category/feher-mintazatok.html'),
    ('Más mintázatok', '/category/mas-mintazatok.html'),
    ('Blog', '/'),
 ) 

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
    # 'extra/custom.css': {'path': 'theme/css/custom.css'},
    'extra/googleb5a40eb476852296.html': {'path': 'googleb5a40eb476852296.html'},
}

# CSS_FILE = 'custom.css'
