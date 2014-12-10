DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'Localhost',
        'PORT': '8000',
    }
}

-------

'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),