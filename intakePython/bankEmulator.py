import faker

fake = Faker()

# 1. Bank Details
print("--- Bank Details ---")
print("Bank Name:", fake.bank_name())
print("Routing Number (ABA):", fake.aba())
print("SWIFT/BIC Code:", fake.swift())
print("IBAN:", fake.iban())
print("Account Number (BBAN):", fake.bban())

# 2. Credit Card Details
print("\n--- Credit Card Details ---")
print("Full Card Details:", fake.credit_card_full())
print("Card Type:", fake.credit_card_provider())
print("Card Number:", fake.credit_card_number(card_type='visa'))
print("Expiration Date:", fake.credit_card_expire())
print("Security Code (CVV):", fake.credit_card_security_code())