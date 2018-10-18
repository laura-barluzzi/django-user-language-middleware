import django
from django.utils import translation


def is_django_greater_than_1_10():
    main_version = django.VERSION[0]
    if main_version > 1:
        return True

    sub_version = django.VERSION[1]
    if main_version == 1 and sub_version >= 10:
        return True

    return False


if is_django_greater_than_1_10():
    from django.utils.deprecation import MiddlewareMixin
    superclass = MiddlewareMixin
else:
    superclass = object


class UserLanguageMiddleware(superclass):
    def process_response(self, request, response):
        user = getattr(request, 'user', None)
        if not user:
            return response

        if not user.is_authenticated:
            return response

        user_language = getattr(user, 'language', None)
        if not user_language:
            return response

        current_language = translation.get_language()
        if user_language == current_language:
            return response

        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        return response
