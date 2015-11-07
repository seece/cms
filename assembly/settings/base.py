# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

gettext = lambda s: s
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')

from datetime import timedelta
import djcelery

djcelery.setup_loader()

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

CELERY_TIMEZONE = 'UTC'

# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'filebrowser',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'djcelery',
    'rest_framework',
    'reversion',
    'treebeard',
    'menus',
    'sekizai',
    'ckeditor',
    'djangocms_siteselector',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_link',
    'djangocms_text_ckeditor',
    'cms',
    'assembly.core',
    'blog',
    'tweetembly',
    'opbeat.contrib.django',
    # Uncomment when schedule models are ready
    'schedule'
)

CKEDITOR_SETTINGS = {
    'toolbar_CMS': [
        ['cmsplugins'],
        ['Source', 'Maximize', 'ShowBlocks', 'Templates'],
        ['CreatePlaceholder', 'Image', 'Flash', 'Table', 'HorizontalRule', 'SpecialChar', 'PageBreak', 'InsertPre'],
        ['Link', 'Unlink', 'Anchor'],
        ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', 'Undo', 'Redo'],
        ['Find', 'Replace', 'SelectAll', 'Scayt'],
        ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'TextColor', 'BGColor',
         'RemoveFormat', 'Styles'],
        ['NumberedList', 'BulletedList', 'Outdent', 'Indent', 'Blockquote', 'CreateDiv', 'JustifyLeft', 'JustifyCenter',
         'JustifyRight', 'JustifyBlock']
    ],
    'skin': 'moono'
}

MIDDLEWARE_CLASSES = (
    'djangocms_siteselector.middlewares.SiteSelectorMiddleware',
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'assembly.core.middlewares.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

MIGRATION_MODULES = {
    # Add also the following modules if you're using these plugins:
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
}

ROOT_URLCONF = 'assembly.urls'

WSGI_APPLICATION = 'assembly.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = (
    ('en', gettext('English')),
    ('fi', gettext('Finnish')),
)

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

OPBEAT = {
    'ORGANIZATION_ID': '#########',
    'APP_ID': '#########',
    'SECRET_TOKEN': '#########',
}

MODELTRANSLATION_TRANSLATION_FILES = (
    'blog.translation',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':
                (
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.template.context_processors.csrf',
                    'django.template.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                    'sekizai.context_processors.sekizai',
                    'cms.context_processors.cms_settings',
                )
        }
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = "uploads/"

CMS_PLACEHOLDER_CONF = {
    # General
    'footer_links': {'plugins': ['LinkPlugin']},

    # Frontpage
    'call_for_action': {'plugins': ['LinkPlugin']},
    'main_sponsors': {'plugins': ['PicturePlugin']},
    'quick_links': {'plugins': ['LinkPlugin']},

    # Article page
    'article_header_image': {'plugins': ['PicturePlugin']}
}
