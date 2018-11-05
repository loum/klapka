################################################
Klapka (Kafka pub/sub with SASL over SSL example
################################################

***************
Getting Started
***************
Get the code::

    $ git clone https://github.com/loum/klapka.git

If you have Python 3 available then to build the virtual environment::

    $ cd klapka
    $ make init APP_ENV=dev
    
Source the Python 3 environment::

    $ source 3env/bin/activate
    (3env) $

For Python 2 you will need ``virtualenv``.  Similarly::

    $ make init PYVERSION=2 APP_ENV=dev
    
Source the Python 2 environment::

    $ source 2env/bin/activate
    (2env) $
