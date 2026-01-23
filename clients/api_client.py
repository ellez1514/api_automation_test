import requests


class APIClient:
    def __init__(self, logger):
        self.logger = logger

    def _request(self, method, url, **kwargs):
        """ Generic method to perform HTTP requests 
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE, etc.)
            url (str): The URL to send the request to.
            **kwargs: Additional arguments to pass to requests.request()

        Returns:
            requests.Response: The API response.
        """
        self.logger.debug("Executing HTTP %s method with url: %s, kwargs: %s", method, url, kwargs)
        try:
            resp = requests.request(method, url, **kwargs)
        except Exception as e:
            self.logger.error("Error on HTTP request call: %s:%s", type(e), e)
            raise e

        self.logger.debug(
            "Response code: %s, Response text: %s", resp.status_code, resp.text
        )
        return resp
    

    def post(self, url, **kwargs):
        """ Perform a POST request """
        return self._request("POST", url, **kwargs)

    def get(self, url, **kwargs):
        """ Perform a GET request """
        return self._request("GET", url, **kwargs)