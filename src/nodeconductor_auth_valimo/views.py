from __future__ import unicode_literals

from rest_framework import viewsets, mixins, response

from nodeconductor.core import mixins as core_mixins

from . import models, serializers, executors


class AuthResultViewSet(core_mixins.CreateExecutorMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = models.AuthResult.objects.filter(visible=True)
    serializer_class = serializers.AuthResultSerializer
    permission_classes = ()
    lookup_field = 'uuid'
    create_executor = executors.AuthExecutor

    def create(self, request, *args, **kwargs):
        """
        To start PKI login process - issue post request with users phone and message.
        Example of a valid request:

        .. code-block:: http

            POST /api/auth-valimo/ HTTP/1.1
            Content-Type: application/json
            Accept: application/json
            Host: example.com

            {
                "phone": "1234567890",
                "message": "Login to example.com"
            }
        """
        return super(AuthResultViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        To get PKI login status and details - issue get request against /api/auth-valimo/<uuid>/

        Warning: success result with token will be returned only once.
        Possible states:
         - Scheduled - login process is scheduled
         - Processing - login is in progress
         - OK - login was successful. Response will contain token.
         - Canceled - login was canceled by user or timed out. Field details will contain additional info.
         - Erred - unexpected exception happened during login process.
        Example of response:

        .. code-block:: javascript

            {
                "url": "http://example.com/api/auth-valimo/e42473f39c844333a80107e139a4dd06/",
                "uuid": "e42473f39c844333a80107e139a4dd06",
                "token": null,
                "state": "Canceled",
                "error_message": "",
                "details": "User cancel."
            }
        """
        auth_result = self.get_object()

        # To prevent brute-force token search - show valid response only once.
        if auth_result.state == models.AuthResult.States.OK:
            auth_result.visible = False
            auth_result.save()

        serializer = self.get_serializer(auth_result)
        return response.Response(serializer.data)
