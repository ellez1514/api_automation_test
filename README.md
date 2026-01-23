# TEST SUITE FOR KLARNA PAYMENT SESSION API
This repo contains automated tests for klarna payment session api


#### TEST CASES

| Test Case                 | Scenario                         | Expected Outcome                      |
|---------------------------|----------------------------------|---------------------------------------|
| `success_payment_session` | Happy Path                       | 200 status code – Payment succeeds    |
| `invalid_payment_session` | Negative Test (negative amount)  | 400 status code – BAD_VALUE           |
| `empty_amount_value`      | Negative Test (missing amount)   | 400 status code – BAD_VALUE           |
| `unauthorized_access`     | No Authorization                 | 401 status code – PERMISSION_DENIED   |


#### REPO STRUCTURE DESCRIPTION

| Folder / Subfolder | File                        | Description                                              |
|--------------------|-----------------------------|----------------------------------------------------------|
| `clients/`         | `__init__.py`               | Marks the clients dir as a python package                |
| `clients/`         | `api_client.py`             | API client logic for payments client                     |
| `clients/`         | `klarna_payment_client.py`  | Klarna-specific payment client                           |
| `configuration/`   | `__init__.py`               | Marks configuration directory as a python package        |
| `configuration/`   | `payment_configuration.py`  | Payment-related configuration variables                  |
| `helpers/`         | `utils.py`                  | Helper functions                                         |
| `models/`          | `__init__.py`               | Marks models directory as a python package               |
| `models/`          | `payment_sessions.py`       | Data models for payment sessions                         |
| `payloads/`        | `payment_session.json`      | JSON payload for klarna payment session                  |
| `tests/api/`       | `test_klarna_payment_api.py`| API test cases for Klarna payment session APIs           |
| `/`                | `conftest.py`               | General configuration and fixtures for the whole project |
| `/`                | `pytest.ini`                | Pytest  configuration file                               |
| `/`                | `README.md`                 | Project documentation                                    |
| `/`                | `requirements.txt`          | Python package dependencies                              |
| `/`                | `api_execution.gif`         | GIF of test execution                                    |



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
![API Test](api_test_execution.gif)
