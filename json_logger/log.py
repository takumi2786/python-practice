import logging
import logging.config
from logging import StreamHandler, Formatter
from sys import stdout, stderr

from pythonjsonlogger.jsonlogger import JsonFormatter


def setup_logging():
    """
    Overwrite default logger of uvicorn: 
    https://github.com/encode/uvicorn/blob/b5af1049e63c059dc750a450c807b9768f91e906/uvicorn/config.py
    """
    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {# デフォルトのFormatterの設定
                "()": logging.Formatter,
                "fmt": "%(asctime)s %(levelname)s: %(pathname)s: %(message)s",
            },
            "json": {# デフォルトのFormatterの設定
                "()": JsonFormatter,
                "fmt": "%(asctime)s, %(levelname)s, %(pathname)s, %(message)s, %(context)s",
            },
        },
        "handlers": {
            "default": {
                "()": logging.StreamHandler,
                "formatter": "default",
                "stream": "ext://sys.stdout",
            },
            "json": {
                "()": logging.StreamHandler,
                "formatter": "json",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            # apprication log
            "app": {"handlers": ["default"], "level": "INFO", "propagate": False},
            "json": {"handlers": ["json"], "level": "INFO", "propagate": False},
        },
        "root": { # default logger setting
            "level": "WARNING",
            "handlers": ["default"],
        },
    })
