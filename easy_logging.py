import sys
import logging
from humanfriendly.terminal import terminal_supports_colors


def get_logger(name: str, level: str = logging.DEBUG):
    fmt = {'fmt': '{asctime} {name} {levelname} {message}',
           'datefmt': '%H:%M:%S',
           'style': '{'
           }
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    try:
        import coloredlogs
        coloredlog_usable = True
    except ModuleNotFoundError:
        coloredlog_usable = False

    formatter = (coloredlogs.ColoredFormatter if coloredlog_usable and terminal_supports_colors()
                 else logging.Formatter)(**fmt)

    handler.setFormatter(formatter)
    if isinstance(level, str):
        level = getattr(logging, level)
    logger.setLevel(level)

    if not coloredlog_usable:
        logger.info('coloredlogs not installed. colored logging will not be populated.')
    return logger


def set_color_trackback(color_scheme: str = 'Neutral'):
    try:
        from IPython.core.ultratb import AutoFormattedTB
        sys.excepthook = AutoFormattedTB(color_scheme=color_scheme)
    except ModuleNotFoundError:
        print('IPython not installed. Colored Traceback will not be populated.')


__all__ = ['get_logger', 'set_color_trackback']
