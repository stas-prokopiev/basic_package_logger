=========================
The Perfect First LOGGER
=========================

.. contents:: **Table of Contents**

Overview.
=========================
| This is a one file (**logger.py**) library with only one function (**get_logger**)
| which returns a LOGGER that can be used as first logger in many cases

How to use
============================

| Whenever you are creating a new python library or package
| just add the file **logger.py** from this repo into the root of you project

1) Then in the root __init__.py add following lines

.. code-block:: python

    from . import logger

    LOGGER = logger.getLogger(
        name=__name__,
        path_dir_where_to_store_logs="",
        is_stdout_debug=False,
        is_to_propagate_to_root_logger=False,
    )

2) And after imports in every python module add following lines

.. code-block:: python

    import logging

    LOGGER = logging.get_logger(__name__)


Now you have perfectly set up logger for the new library or package

.. code-block:: python

    LOGGER.info("hihi")

What this LOGGER is doing?
============================

In the default set up shown above all log messages are sent to stdout and stderr streams.

This is what user can expect to see for every message level
--------------------------------------------------------------

Stdout:

- LOGGER.debug("hi") -> Not printed
- LOGGER.info("hi") -> "hi"
- LOGGER.warning("hi") -> [WARNING]: hi
- LOGGER.error("hi") -> Not printed
- LOGGER.critical("hi") -> Not printed

Stderr:

- LOGGER.error("hi") -> [Long description of where and when error occured]: hi
- LOGGER.critical("hi") -> [Long description of where and when critical error occured]: hi

Additional arguments
============================

path_dir_where_to_store_logs=""
----------------------------------------

If argument is given with non zero value then in the asked directory will be created folder **Logs** with 2 files:

- **Logs/debug.log** - To contain all messages starting from debug level
- **Logs/errors.log** - To contain all errors and critical messages

For both these files every line of them contain one sent message in a dict format so you can easily parse it

| Both files are rotating when size is bigger than 10 Mb.
| At that moment backup file is created by appending the extensions .1 (Logs/debug.log.1)
| and main file is cleared and used for next messages

is_stdout_debug=False
----------------------------------------

If set to **True** then debug messages also sent to stdout stream in the format: *[DEBUG]: msg*

*Can be useful while you debugging your library or application*

is_to_propagate_to_root_logger=False
----------------------------------------

If set to **True** then LOGGER messages will propagate to parent loggers until root logger

*Can be used if you expect that user will want to read logs in user own format.*

Contacts
========

    * Email: stas.prokopiev@gmail.com
    * `vk.com <https://vk.com/stas.prokopyev>`_
    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.

