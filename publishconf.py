import logging

PATH = '/Users/tomyates/niche_sites/sites/christianity/content' 
ARTICLE_PATHS = [''] 
ARTICLE_EXCLUDES = ['pages'] 
PAGE_PATHS = ['pages'] 
PAGE_EXCLUDES = [''] 
THEME = '/Users/tomyates/niche_sites/themes/genus' 
OUTPUT_PATH = '/Users/tomyates/niche_sites/sites/christianity/output' 
READERS = {} 
STATIC_PATHS = ['images', 'css'] 
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
SITEURL = 'https://christianity-e51.pages.dev/'
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
ARTICLE_URL = '{slug}.html' 
ARTICLE_SAVE_AS = '{slug}.html' 
ARTICLE_ORDER_BY = 'reversed-date' 
ARTICLE_LANG_URL = '{slug}-{lang}.html' 
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html' 
DRAFT_URL = 'drafts/{slug}.html' 
DRAFT_SAVE_AS = 'drafts/{slug}.html' 
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html' 
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html' 
PAGE_URL = 'pages/{slug}.html' 
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

AUTHOR = 'Tom'

# PLUGINS = ['more_categories','seo']

SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = False  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = False # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False # Subfeature of SEO enhancer

STORK_OUTPUT_OPTIONS = {
    'excerpts_per_result': 1,
}