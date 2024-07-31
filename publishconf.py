# from pelican_settings import *
import logging

PATH = '/Users/tomyates/niche_sites/sites/christianity/content' 
ARTICLE_PATHS = [''] 
ARTICLE_EXCLUDES = ['pages'] 
PAGE_PATHS = ['pages'] 
PAGE_EXCLUDES = [''] 
THEME = '/Users/tomyates/niche_sites/themes/genus' 
OUTPUT_PATH = '/Users/tomyates/niche_sites/sites/christianity/output' 
READERS = {} 
STATIC_PATHS = ['images', 'css', 'misc', 'social-cards', 'extras'] 
STATIC_EXCLUDES = [] 
STATIC_EXCLUDE_SOURCES = True 
THEME_STATIC_DIR = 'theme' 
THEME_STATIC_PATHS = ['static'] 
FEED_ALL_ATOM = 'feeds/all.atom.xml' 
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml' 
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml' 
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml' 
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml' 
FEED_MAX_ITEMS = 100 
RSS_FEED_SUMMARY_ONLY = True 
SITEURL = 'http://127.0.0.1:8000/' 
SITENAME = 'Bible Based Living' 
SITETITLE = 'Bible Based Living'
DISPLAY_PAGES_ON_MENU = True 
DISPLAY_CATEGORIES_ON_MENU = True 
DOCUTILS_SETTINGS = {} 
OUTPUT_SOURCES = False 
OUTPUT_SOURCES_EXTENSION = '.text' 
USE_FOLDER_AS_CATEGORY = True 
DEFAULT_CATEGORY = 'misc' 
WITH_FUTURE_DATES = True 
CSS_FILE = 'main.css' 
CSS_OVERRIDE = ['css/custom.css']

NEWEST_FIRST_ARCHIVES = True 
REVERSE_CATEGORY_ORDER = False 
DELETE_OUTPUT_DIRECTORY = False 
OUTPUT_RETENTION = [] 
INDEX_SAVE_AS = 'index.html' 
ARTICLE_URL = '{slug}/' 
ARTICLE_SAVE_AS = '{slug}.html' 
ARTICLE_ORDER_BY = 'reversed-date' 
ARTICLE_LANG_URL = '{slug}-{lang}.html' 
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html' 
DRAFT_URL = 'drafts/{slug}.html' 
DRAFT_SAVE_AS = 'drafts/{slug}.html' 
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html' 
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html' 
PAGE_URL = 'pages/{slug}' 
PAGE_SAVE_AS = 'pages/{slug}.html' 
PAGE_ORDER_BY = 'basename' 
PAGE_LANG_URL = 'pages/{slug}-{lang}.html' 
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html' 
DRAFT_PAGE_URL = 'drafts/pages/{slug}.html' 
DRAFT_PAGE_SAVE_AS = 'drafts/pages/{slug}.html' 
DRAFT_PAGE_LANG_URL = 'drafts/pages/{slug}-{lang}.html' 
DRAFT_PAGE_LANG_SAVE_AS = 'drafts/pages/{slug}-{lang}.html' 
STATIC_URL = '{path}' 
STATIC_SAVE_AS = '{path}' 
STATIC_CREATE_LINKS = False 
STATIC_CHECK_IF_MODIFIED = False 
CATEGORY_URL = 'category/{slug}.html' 
CATEGORY_SAVE_AS = 'category/{slug}.html' 
TAG_URL = 'tag/{slug}.html' 
TAG_SAVE_AS = 'tag/{slug}.html' 
AUTHOR_URL = 'author/{slug}.html' 
AUTHOR_SAVE_AS = 'author/{slug}.html' 

AUTHOR = 'maisha_johnson'

# PLUGINS = ['more_categories','seo']

SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = False  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = False # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False # Subfeature of SEO enhancer

STORK_OUTPUT_OPTIONS = {
    'excerpts_per_result': 1,
}
EXTRA_PATH_METADATA = {'images': {'path': 'images'}}

DEFAULT_PAGINATION = 7
PAGINATED_DIRECT_TEMPLATES = (('index', 'blog'))

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.6,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "monthly"
    }
}

import yaml

# Load author information
with open('content/authors.yaml', 'r') as f:
    AUTHORS = yaml.safe_load(f)


EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},  # and this
}

CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

SOCIAL_CARDS_TEMPLATE = "content/misc/template.png"

SOCIAL_CARDS_HORIZONTAL_ALIGNMENT = "left"
SOCIAL_CARDS_VERTICAL_ALIGNMENT = "bottom"
SOCIAL_CARDS_FONT_FILL = "#ffffff"
SOCIAL_CARDS_FONT_FILENAME = "LeagueSpartan-Bold.otf"

SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True # Subfeature of SEO enhancer"

METADATA_FIELDS = [
    ('keywords', 'Keywords'),
    ('description', ''),
]

SITEURL = 'https://biblebasedliving.com'
