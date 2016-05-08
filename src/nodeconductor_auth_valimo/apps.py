from django.apps import AppConfig


class AuthValimoConfig(AppConfig):
    name = 'nodeconductor_auth_valimo'
    verbose_name = 'AuthValimo'

    def ready(self):
        pass
