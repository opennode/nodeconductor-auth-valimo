from __future__ import unicode_literals

from rest_framework import serializers

from . import models


class AuthResultSerializer(serializers.HyperlinkedModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:
        model = models.AuthResult
        fields = ('url', 'uuid', 'token', 'phone', 'message', 'state', 'error_message', 'details')
        write_only_fields = ('message', 'phone')
        read_only_fields = ('url', 'uuid', 'token', 'state', 'error_message', 'details')
        extra_kwargs = {
            'url': {'lookup_field': 'uuid', 'view_name': 'auth-valimo-detail'},
        }

    def get_token(self, auth_result):
        if auth_result.user:
            return auth_result.user.auth_token.key
        return None
