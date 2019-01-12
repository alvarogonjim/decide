DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'https://cabina-ortosia.herokuapp.com'

APIS = {
    'authentication': 'https://cabina-ortosia.herokuapp.com',
    'base': 'https://cabina-ortosia.herokuapp.com',
    'booth': 'https://cabina-ortosia.herokuapp.com',
    'census': 'https://cabina-ortosia.herokuapp.com',
    'mixnet': 'https://cabina-ortosia.herokuapp.com',
    'postproc': 'https://cabina-ortosia.herokuapp.com',
    'store': 'https://cabina-ortosia.herokuapp.com',
    'visualizer': 'https://cabina-ortosia.herokuapp.com',
    'voting': 'https://cabina-ortosia.herokuapp.com',
}
