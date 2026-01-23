import base64
import os


class PaymentConfig():
    """PaymentConfig defines a configuration object to be used for payments client

     Args:
            url (str, optional): Base URL for the payment API. Default value is "".
    """
    def __init__(self, url=""):
        self.base_url = os.getenv("PAYMENT_API_URL", url)
        if not self.base_url:
            raise RuntimeError(
                "Klarna payment url was not provided. Cannot proceed with testing."  
            )

        user = os.getenv("KLARNA_USERNAME")
        pwd = os.getenv("KLARNA_PASSWORD")
        if not user or not pwd:
            raise RuntimeError(
                "Klarna username or password not set. Cannot proceed without token for Klarna Payment Client"
            )
        
        self.token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
