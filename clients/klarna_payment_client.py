from clients import APIClient

ENDPOINT_PAYMENT_SESSION = "payments/v1/sessions"

class KlarnaPaymentClient():
    """A client for interacting with Klarna Payment API

    Args:+
            logger: Logger object
            payment_config: Config object which contains config data for payment client
    """

    def __init__(self, logger, payment_config):
        self.requests = APIClient(logger)
        self.logger = logger
        self.base_url = payment_config.base_url
        token = payment_config.token
        self.headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}  
    
    def payment_session(self, json_body, headers=None, timeout=10):
        """ Create or update payment session

        Args:
            json_body (dict): The JSON body to send in the request
            headers (dict, optional): Headers to include in the request. Default is None
            timeout (int, optional): Timeout for the request in seconds. Default is 10

        Returns:
            requests.Response: The API response.
        """
        if not headers:
            headers = self.headers

        payment_url = f"{self.base_url}/{ENDPOINT_PAYMENT_SESSION}"
        resp = self.requests.post(payment_url, verify=True, json=json_body, headers=headers, timeout=timeout)
        return resp

