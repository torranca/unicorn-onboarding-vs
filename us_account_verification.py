import requests
from auth import get_access_token

BASE_URL = 'https://api-mock.payments.jpmorgan.com/tsapi/v2/validations/accounts'

def verify_us_account_exists(account_number, routing_number):
    access_token = get_access_token()
    url = BASE_URL
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-client-id': 'CLIENTID',
        'x-program-id': 'VERIAUTH',
        'x-program-id-type': 'AVS'
    }
    payload = [{
        'requestId': '123e4567-e89b-12d3-a456-426614174000',
        'account': {
            'accountNumber': account_number,
            'financialInstitutionId': {
                'clearingSystemId': {
                    'id': routing_number,
                    'idType': 'ABA'
                }
            }
        },
        'entity': {
            'individual': {
                'firstName': 'Jane',
                'lastName': 'Abbot',
                'fullName': 'Jane Abbot'
            }
        }
    }]
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def verify_us_account_debit_return(account_number, routing_number):
    access_token = get_access_token()
    url = BASE_URL
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-client-id': 'CLIENTID',
        'x-program-id': 'VERIAUTH',
        'x-program-id-type': 'AVS'
    }
    payload = [{
        'requestId': '123e4567-e89b-12d3-a456-426614174000',
        'account': {
            'accountNumber': account_number,
            'financialInstitutionId': {
                'clearingSystemId': {
                    'id': routing_number,
                    'idType': 'ABA'
                }
            }
        },
        'entity': {
            'individual': {
                'firstName': 'Jane',
                'lastName': 'Abbot',
                'fullName': 'Jane Abbot'
            }
        }
    }]
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def validate_us_account_status_beneficiary(account_number, routing_number, beneficiary_name):
    access_token = get_access_token()
    url = BASE_URL
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-client-id': 'CLIENTID',
        'x-program-id': 'VERIAUTH',
        'x-program-id-type': 'AVS'
    }
    payload = [{
        'requestId': '123e4567-e89b-12d3-a456-426614174000',
        'account': {
            'accountNumber': account_number,
            'financialInstitutionId': {
                'clearingSystemId': {
                    'id': routing_number,
                    'idType': 'ABA'
                }
            }
        },
        'entity': {
            'individual': {
                'firstName': 'Jane',
                'lastName': 'Abbot',
                'fullName': 'Jane Abbot'
            }
        },
        'beneficiaryName': beneficiary_name
    }]
    response = requests.post(url, json=payload, headers=headers)
    return response.json()