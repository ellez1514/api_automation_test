from pathlib import Path

from helpers.utils import load_json

BASE_PAYLOAD = Path(__file__).resolve().parents[1] / "payloads" / "payment_session.json"

class PaymentSessionPayload:
    """Class to build payment session payloads"""

    def __init__(self):
        self.payment_session_json = load_json(BASE_PAYLOAD)

    def construct_payment_session_json(self, logger, values: dict= None) :
        """ Construct payment session json payload """

        if values is None:
            values = {}

        logger.info("Constructing json for payment session")

        self.payment_session_json["intent"] = values.get("intent", "buy")
        self.payment_session_json["purchase_country"] = values.get("purchase_country", "SE")
        self.payment_session_json["purchase_currency"] = values.get("purchase_currency", "SEK")
        self.payment_session_json["locale"] = values.get("locale", "en-SE")
        self.payment_session_json["order_amount"] = values.get("order_amount", 10000)
        self.payment_session_json["order_tax_amount"] = values.get("order_tax_amount", 2000)
        
        self.payment_session_json["order_lines"][0].update({
            "type": values.get("type", "physical"),
            "reference": values.get("reference", "123456789"),
            "name": values.get("name", "Test Product"),
            "quantity": values.get("quantity", 1),
            "unit_price": values.get("unit_price", 10000),
            "tax_rate": values.get("tax_rate", 2000),
            "total_amount": values.get("total_amount", 10000),
            "total_tax_amount": values.get("total_tax_amount", 2000),
            "total_discount_amount": values.get("total_discount_amount", 0),
            "image_url": values.get("image_url", "https://example.com/product.jpg"),
            "product_url": values.get("product_url", "https://example.com/product")
        })

        self.payment_session_json["merchant_urls"]["authorization"] = values.get(
            "authorization_url",
            "https://example.com/authorization"
        )
        

        logger.debug("Constructed json: %s", self.payment_session_json)
        return self.payment_session_json

