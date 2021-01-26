"""This is a one file library with main function get_logger
which can be used as first logger set up for new py packages"""
import sys
import os
import logging

STR_DEBUG_FORMAT = '[%(levelname)s: %(asctime)s:%(filename)s:%(name)s:%(funcName)s:%(lineno)d] %(message)s'
STR_INFO_FORMAT = '%(message)s'
STR_WARNING_FORMAT = '[%(levelname)s] %(message)s'
STR_ERROR_FORMAT = STR_DEBUG_FORMAT


class OnlyLowerLevelFilter():
    """Define filter to show only logs with level lower than given level
    """
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno < self.level


def get_logger(name, path_dir_where_to_store_logs="", int_min_stdout_level=20):
    """function returns a perfectly set up logger for the new package"""
    # Create and set basic settings for logger
    LOGGER = logging.getLogger(name)
    LOGGER.setLevel(0)
    LOGGER.propagate = False
    #####
    # 1) Set up stdout logs
    # 1.1) Add info handler
    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(level=int_min_stdout_level)
    info_handler.setFormatter(logging.Formatter(STR_INFO_FORMAT))
    info_handler.addFilter(OnlyLowerLevelFilter(30))
    LOGGER.addHandler(info_handler)
    # 1.2) Add warning handler
    warning_handler = logging.StreamHandler(sys.stdout)
    warning_handler.setLevel(level=int_min_stdout_level)
    warning_handler.setFormatter(logging.Formatter(STR_WARNING_FORMAT))
    warning_handler.addFilter(OnlyLowerLevelFilter(30))
    LOGGER.addHandler(warning_handler)
    # 1.3) Add error handler
    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(level=int_min_stdout_level)
    error_handler.setFormatter(logging.Formatter(STR_ERROR_FORMAT))
    LOGGER.addHandler(error_handler)
    if not path_dir_where_to_store_logs:
        return LOGGER
    #####
    # 2) Set up file handlers for logger
    # Create folder for Logs
    str_path_to_logs_dir = os.path.join(path_dir_where_to_store_logs, "Logs")
    if not os.path.isdir(str_path_to_logs_dir):
        os.makedirs(str_path_to_logs_dir)
    # 2.1) Debug handler
    debug_file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(str_path_to_logs_dir, "debug.log"),
        maxBytes=10000,
        backupCount=1
    )
    debug_file_handler.setLevel(level=0)
    debug_file_handler.setFormatter(logging.Formatter(STR_DEBUG_FORMAT))
    LOGGER.addHandler(debug_file_handler)
    # 2.1) Warnings and above handler
    warnings_file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(str_path_to_logs_dir, "errors.log"),
        maxBytes=10000,
        backupCount=1
    )
    warnings_file_handler.setLevel(level=0)
    warnings_file_handler.setFormatter(logging.Formatter(STR_DEBUG_FORMAT))
    LOGGER.addHandler(warnings_file_handler)
    #####
    return LOGGER
