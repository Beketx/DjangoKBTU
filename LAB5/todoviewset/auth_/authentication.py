import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import User

class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        """
        Etot method vyzyvaetsya kazhdy raz ne zavisimo
        ot trebuet li kone4naya to4ka authentifikacii
        est dva varianta returna
        1 - None = esli ne authentificiruet. Vsegda eto chto fail. Takoe byvaet kogda
        ne vkluchauyt token v headersah
        :param request:
        2 - '(user,token)' - Eto kogda successfull.
        V ostalnyh sluchaeh owibok prosto raise 'AuthenticationFailed'
        :return:
        """
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            """
            INVALID TOKEN HEADER. NO REKVIZITS PROVIDED. DO NOT AUTHETICATE
            """
            return None

        elif len(auth_header) > 2:
            """
            Invalid token header. Token header should not contain spaces
            Do not authenticate
             Библиотека JWT, которую мы используем,
            не может обрабатывать тип байта, который
             обычно используется стандартными библиотеками в Python 3. Чтобы обойти это,
            нам просто нужно декодировать prefix и token. Это не делает для 
            чистый код, но это хорошее решение, 
            потому что мы получим ошибку # если мы не декодировали эти значения.
            """
            prefix = auth_header[0].decode('utf-8')
            token = auth_header[1].decode('utf-8')

            if prefix.lower() != auth_header_prefix:
                return None

            # By now, we are sure there is a *chance* that authentication will
            # succeed. We delegate the actual credentials authentication to the
            # method below.
            return self._authenticate_credentials(request, token)

        def _authenticate_credentials(self, request, token):
            """
            Try to authenticate the given credentials. If authentication is
            successful, return the user and token. If not, throw an error.
            """
            try:
                payload = jwt.decode(token, settings.SECRET_KEY)
            except:
                msg = 'Invalid authentication. Could not decode token'
                raise exceptions.AuthenticationFailed(msg)

            try:
                user = User.objects.get(pk=payload['id'])
            except User.DoesNotExist:
                msg = 'No user matching this token was found'
                raise exceptions.AuthenticationFailed(msg)
            if not user.is_active:
                msg = 'This user has been deactivated'

                raise exceptions.AuthenticationFailed(msg)
            return (user, token)