# TEST SUITE FOR KLARNA PAYMENT SESSION API
This repo contains automated tests for klarna payment session api


#### TEST CASES

| Test Case | Scenario | Expected |
|----------|----------|----------|
| success_payment_session | Happy Path | 200 status code - Payment succeeds |
| invalid_payment_session | Negative Test (negative amount) | 400 status code - BAD_VALUE|
| empty_amount_value | Negative Test (empty amount) | 400 status code - BAD_VALUE |
| unauthorized_access | No Authorization | 401 status code - PERMISSION_DENIED |


#### HOW TO EXECUTE TESTS:

1. Install requirements:
```sh
pip install -r requirements.txt
```


2. Export following variables:
```sh
export PAYMENT_API_HOST=https://api.playground.klarna.com
export KLARNA_USERNAME="405b588d-157c-462a-a052-f282ec3c79f0"
export KLARNA_PASSWORD="************************"
```


2. Execute test:
```sh
pytest -rA -s -v tests/api/test_klarna_payment_api.py
or
cd tests/
pytest -rA -s -v -m "api"

```

#### TEST EXECUTION LOCALLY
![API Test](api_execution.gif)