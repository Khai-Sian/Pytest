import pytest
import logging

LOGGER = logging.getLogger(__name__)
INFO = LOGGER.isEnabledFor(logging.INFO)


def print_logging():
    if INFO:
        LOGGER.info("logging.INFO is enabled")    
    else:
        LOGGER.critical("logging.INFO is not enabled")  

@pytest.fixture(scope="module")
def pre_run():
    print_logging()

def test_set_verbose(pre_run):
    # verbose_level = request.config.getoption('verbose')

    if INFO:
        LOGGER.info('In test: logging.INFO is enabled')

def test():

    assert INFO

