import pytest
from models import PaymentSessionPayload

__author__ = "Eleni Kamara"
__email__ = "elenidespinakamara@gmail.com"


invalid_token_header = {"Authorization": f"Basic Invalid_Token", "Content-Type": "application/json"}  
success_response_fields = ["session_id", "client_token", "payment_method_categories"]
error_response_fields = ["correlation_id", "error_code", "error_messages"]
unauthorized_response_fields = ["error_code", "error_message"]

# Parametrize: (scenario, headers, values_dict, expected_status_code, expected_resp_fields, expected_error_code)
# NOTE: If headers is None, default valid headers will be used
# NOTE: If values_dict is {}, default valid payload values will be used
# NOTE: If expected_error_code is None, no error code validation will be performed
test_data = [
    ("success_payment_session", None, {}, 200, success_response_fields, []),
    ("invalid_payment_session", None, {"order_amount": -1000}, 400, error_response_fields, "BAD_VALUE"),
    ("empty_amount_value", None, {"order_amount": ""}, 400, error_response_fields, "BAD_VALUE"),
    ("unauthorized_access", invalid_token_header, {}, 401, unauthorized_response_fields, "PERMISSION_DENIED"),
]


@pytest.mark.api
class TestKlarnaPaymentAPI:
    """@brief Test suite for Klarna Payment API tests
    """

    @pytest.mark.parametrize(
        "scenario, headers, values_dict, expected_status_code, expected_resp_fields, expected_error_code", test_data
    )
    def test_payment_session(
        self,
        klarna_payment_client,
        logger,
        scenario,
        headers,
        values_dict,
        expected_status_code,
        expected_resp_fields,
        expected_error_code
    ):
        """
        Test the creation of a payment session
        """
        logger.info(f"Executing test scenario: {scenario}")

        # Get payment session payload with default values and create session
        payload = PaymentSessionPayload().construct_payment_session_json(logger, values=values_dict)
        result = klarna_payment_client.payment_session(json_body=payload, headers=headers)
        assert result.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, got {result.status_code}"
        )
        
        data = result.json()
        # Assert existence of required fields in the response
        for field in expected_resp_fields:
            assert field in data, f"Response does not contain '{field}'"

        # If there are expected error messages, validate them
        if expected_error_code:
            assert data["error_code"] == expected_error_code, (
                f"Expected error code '{expected_error_code}', got '{data['error_code']}'"
            )
