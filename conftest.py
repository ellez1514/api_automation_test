import logging
import pytest

from clients import KlarnaPaymentClient
from configuration import PaymentConfig


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)-15s - %(levelname)s - [%(filename)-.20s | L%(lineno)d] - %(message)s"
)
logging.getLogger("urllib3").setLevel(logging.WARNING)


@pytest.fixture(scope="session")
def logger():
    """Logging fixture to allow across-the-board logging"""
    return logging.getLogger(__name__)

@pytest.fixture(scope="session")
def payment_configuration(url="https://api.playground.klarna.com"):
    payment_config = PaymentConfig(url=url)
    return payment_config

@pytest.fixture(scope="session")
def klarna_payment_client(logger, payment_configuration):
    """Klarna Payment API client fixture"""
    client = KlarnaPaymentClient(logger, payment_configuration)
    return client