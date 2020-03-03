from MyUtils import EnvConfs
import logging
from Gui.MainGui import TestApp
from MyUtils.LogHelper import set_logger


if __name__ == '__main__':
    app = TestApp()
    set_logger(log_level=logging.WARNING)
    logger = logging.getLogger("APP")
    try:
        app.run()
    except Exception as ex:
        logger.error(ex, exc_info=True)
        raise ex
