import inspect
import logging
import softest


class Utils(softest.TestCase):

    @staticmethod
    def custom_logger(loglevel=logging.DEBUG):

        # Get calling method name
        logger_name = inspect.stack()[1][3]

        # Create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)

        # Prevent duplicate handlers
        if not logger.handlers:
            fh = logging.FileHandler("automation.log", mode="a")
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger
