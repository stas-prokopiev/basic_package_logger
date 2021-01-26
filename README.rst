=======================
package_logger_set_up
=======================

.. contents:: **Table of Contents**

Overview.
=========================
| This is a one file library with only one function get_logger
| which can be used as first logger set up for new py packages


Usage
============================

Whenever you are creating a new python library or package just and this file **logger.py** into the root of it.

1) Then in the root __init__.py add following code

.. code-block:: python

    from . import logger

    LOGGER = logger.get_logger(__name__, path_dir_where_to_store_logs=".")

2) And after the imports in every python module add following lines

.. code-block:: python

    import logging

    LOGGER = logging.get_logger(__name__)


3) Now you have perfectly set up logger for new library or package use it as shown below

.. code-block:: python

    LOGGER.info("hihi")

Contacts
========

    * Email: stas.prokopiev@gmail.com
    * `vk.com <https://vk.com/stas.prokopyev>`_
    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.

