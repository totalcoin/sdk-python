====================
TotalCoin Python SDK
====================

Instalación
===========

Para instalar la libreria:

::

   [foo@host]$ python setup.py install 


Documentación
=============

Puedes trabajar con el API de TotalCoin instanciando la 
clase Api, para ello vas a precisar un email y api_key:

::

    >>> import totalcoin
    >>> email = 'username@domain.com'
    >>> api_key = 'secret'
    >>> api = totalcoin.Api(email, api_key)

    
Puedes acceder al token de tu usuario de la siguiente forma:

::

    >>> api.access_token
    u'secret'


En caso que las credenciales sean incorrectas (email, api_key), 
vas a obtener una excepción HTTP, ej:

:: 

    (traceback)
    HTTPError: 401 Client Error: Unauthorized


Puedes hacer checkout de una operación de la siguiente forma:

::

    >>> params = {
    ...    "Amount" => 100,
    ...    "Country" => "ARG",
    ...    "Currency" => "ARS",
    ...    "Description" => "Zapatillas adidas",
    ...    "PaymentMethods" => "CREDITCARD|CASH|BANK|TOTALCOIN",
    ...    "Reference" => "0129618531",
    ...    "Site" => "WordPress"
    ... }
    >>> api.perform_checkout(params)
    {...}


Puedes correr los tests de la libreria de la siguiente forma:

::

   [foo@host]$ python tests/test_api.py 
