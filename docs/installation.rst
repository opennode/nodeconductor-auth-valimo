Installation
------------

* `Install Waldur <http://nodeconductor.readthedocs.org/en/latest/guide/intro.html#installation-from-source>`_

* Clone Waldur Auth Valimo repository

  .. code-block:: bash

    git clone https://github.com/opennode/waldur-auth-valimo.git

* Install Waldur Auth Valimo into Waldur virtual environment

  .. code-block:: bash

    cd /path/to/waldur-auth-valimo/
    python setup.py install

* Define settings Valimo parameters in Waldur settings:

  .. code-block:: python

    WALDUR_AUTH_VALIMO = {
        'URL': '<Valimo URL, example: https://example.com>',
        'AP_ID': '<Application provider ID>',
        'AP_PWD': '<Application provider password>',
        'DNSName': '<Name of VSS server, blank by default>',
        'SignatureProfile': '<Signature profile to be used in the transaction processing>'
        'cert_path': '<path to file with SSL certificate>',
        'key_path': '<path to file with SSL key>',
        'message_prefix': '<prefix of message that will be send to user, default "Login code:">'
    }

  Example:

  .. code-block:: python

    WALDUR_AUTH_VALIMO.update({
        'URL': 'https://example.com/',
        'AP_ID': 'https://example/MobilePKI_AP',
        'AP_PWD': 'example_password',
        'DNSName': 'example',
        'SignatureProfile': 'https://example.com/MobilePKI',
        'cert_path': '/home/user/path/to/cert/example.cer',
        'key_path': '/home/user/path/to/key/example.key',
    })
