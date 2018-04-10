************************
User Language Middleware
************************

.. image:: https://travis-ci.org/laura-barluzzi/django-user-language-middleware.svg?branch=master
    :target: https://travis-ci.org/laura-barluzzi/django-user-language-middleware

What's this?
============

This package contains a middleware that activates translations based on the
language field in the user model. This enables easy user-specific localization
of a Django application: just add a language string field to the user model,
install this middleware and you're good to go!

Usage
=====

Add a language field to your user model:

.. code-block:: python

    class User(auth_base.AbstractBaseUser, auth.PermissionsMixin):
        # ...
        language = models.CharField(max_length=10,
                                    choices=settings.LANGUAGES,
                                    default=settings.LANGUAGE_CODE)

Install the middleware from **pip**:

.. code-block:: sh

    pip install django-user-language-middleware

and then add it to your middleware class list to listen to requests:

.. code-block:: python

    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
        ...
        'user_language_middleware.UserLanguageMiddleware',
        ...
    ]

Supported versions
==================

Python:
- 2.7
- 3.4 to 3.6

Django:
- 1.8 to 1.11
- 2.0
