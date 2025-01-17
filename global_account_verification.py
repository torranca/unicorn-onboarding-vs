import requests
from auth import get_access_token

BASE_URL = 'https://api-mock.payments.jpmorgan.com/tsapi/v2/validations/accounts'

def verify_global_personal_account(iban):
    access_token = get_access_token()
    url = BASE_URL
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-client-id': 'CLIENTID',
        'x-program-id': 'VERIAUTHNONUS',
        'x-program-id-type': 'AVS'
    }
    payload = [{
        'requestId': '123e4567-e89b-12d3-a456-426614174000',
        'account': {
            'accountNumber': iban,
            'financialInstitutionId': {
                'clearingSystemId': {
                    'id': 'PARBDEFFZZZ',
                    'idType': 'SWIFT'
                },
                'postalAddress': {
                    'country': 'AT'
                }
            },
            'accountNumberType': 'IBAN'
        },
        'entity': {
            'individual': {
                'firstName': 'Jane',
                'lastName': 'Abbot',
                'fullName': 'Jane Abbot',
                'identification': [{
                    'idType': 'TAX_ID',
                    'id': '111223333'
                }]
            }
        },
        'transactions': []
    }]
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def verify_global_business_account(iban):
    access_token = get_access_token()
    url = BASE_URL
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-client-id': 'CLIENTID',
        'x-program-id': 'VERIAUTHNONUS',
        'x-program-id-type': 'AVS'
    }
    payload = [{
        'requestId': '123e4567-e89b-12d3-a456-426614174000',
        'account': {
            'accountNumber': iban,
            'financialInstitutionId': {
                'clearingSystemId': {
                    'id': 'PARBDEFFZZZ',
                    'idType': 'SWIFT'
                },
                'postalAddress': {
                    'country': 'AT'
                }
            },
            'accountNumberType': 'IBAN'
        },
        'entity': {
            'organization': {
                'name': 'Global Corp',
                'alternateName': 'Global Corporation'
            }
        },
        'transactions': []
    }]
    response = requests.post(url, json=payload, headers=headers)
    return response.json()