Installation
------------

* `Install NodeConductor <http://nodeconductor.readthedocs.org/en/latest/guide/intro.html#installation-from-source>`_

* Clone NodeConductor ValimoAuth repository

  .. code-block:: bash

    git clone https://github.com/opennode/nodeconductor-valimo-auth.git

* Install NodeConductor ValimoAuth into NodeConductor virtual environment

  .. code-block:: bash

    cd /path/to/nodeconductor-valimo-auth/
    python setup.py install

* Define settings Valimo parameters in NodeConductor settings:

  .. code-block:: python

    NODECONDUCTOR_VALIMO_AUTH = {
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

    NODECONCUTOR_AUTH_VALIMO.update({
        'URL': 'https://example.com/',
        'AP_ID': 'https://example/MobilePKI_AP',
        'AP_PWD': 'example_password',
        'DNSName': 'example',
        'SignatureProfile': 'https://example.com/MobilePKI',
        'cert_path': '/home/user/path/to/cert/example.cer',
        'key_path': '/home/user/path/to/key/example.key',
    })
