from us_account_verification import (
    verify_us_account_exists,
    verify_us_account_debit_return,
    validate_us_account_status_beneficiary
)
from global_account_verification import (
    verify_global_personal_account,
    verify_global_business_account
)

def main():
    # Example usage for US account verification
    us_account_result = verify_us_account_exists('12345', '122199983')
    print(us_account_result)

    us_debit_return_result = verify_us_account_debit_return('12345', '122199983')
    print(us_debit_return_result)

    us_status_beneficiary_result = validate_us_account_status_beneficiary('12345', '122199983', 'Jane Abbot')
    print(us_status_beneficiary_result)

    # Example usage for Global account verification
    global_personal_result = verify_global_personal_account('12345')
    print(global_personal_result)

    global_business_result = verify_global_business_account('12345')
    print(global_business_result)

if __name__ == "__main__":
    main()