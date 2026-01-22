from clients import APIClient

ENDPOINT_PAYMENT_SESSION = "payments/v1/sessions"

class KlarnaPaymentClient():
    def __init__(self, logger, payment_config):
        """Init for payment client

        Args:
            logger: Logger object
            payment_config: Config object which contains config data for payment client
        """
        self.requests = APIClient(logger)
        self.logger = logger
        self.base_url = payment_config.base_url
        token = payment_config.token
        self.headers = {"Authorization": f"Basic {token}", "Content-Type": "application/json"}  
    
    def payment_session(self, json_body, headers=None, timeout=10):
        """ Create or update payment session

        Args:
            json_body (dict): The JSON body to send in the request.

        Returns:
            requests.Response: The API response.
        """
        if not headers:
            headers = self.headers

        payment_url = f"{self.base_url}/{ENDPOINT_PAYMENT_SESSION}"
        resp = self.requests.post(payment_url, verify=True, json=json_body, headers=headers, timeout=timeout)
        return resp

