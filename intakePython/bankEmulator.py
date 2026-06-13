import faker

class myGen:
    def __init__(self):
        self.fake = faker.Faker()

    def genBank(self):
        # 1. Bank Details
        self.bank = self.fake.bank()
        self.routing_number = self.fake.aba()
        self.swift_code = self.fake.swift()
        self.iban = self.fake.iban()
        self.bban = self.fake.bban()
        
    def genCreditCard(self):
        # 2. Credit Card Details
        self.credit_card = self.fake.credit_card_full()
        self.card_type = self.fake.credit_card_provider()
        self.card_number = self.fake.credit_card_number(card_type='visa') # Revisit card type
        self.expiration_date = self.fake.credit_card_expire()
        self.security_code = self.fake.credit_card_security_code()
        
    def genTransaction(self):
        # 3. Transaction Details
        self.transaction_id = self.fake.uuid4()
        self.amount = self.fake.pydecimal(left_digits=3, right_digits=2, positive=True) # Revisit decimal
        self.currency = self.fake.currency_code()
        self.date = self.fake.date()
        self.time = self.fake.time()