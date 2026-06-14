import faker
import numpy as np


class myGen:
    def __init__(self):
        self.fake = faker.Faker()
        # self.transactionDistribution = np.random.normal(2, 1, 1000)

    def genBankSending(self):
        # 1. Sending Bank Details
        self.sendingBank = self.fake.bank()
        self.sendingRouting_number = self.fake.aba()
        self.sendingSwift_code = self.fake.swift()
        self.sendingIban = self.fake.iban()
        self.sendingBban = self.fake.bban()

    def genBankReceiving(self):
        # 2. ReceivingBank Details
        self.receivingBank = self.fake.bank()
        self.receivingRouting_number = self.fake.aba()
        self.receivingSwift_code = self.fake.swift()
        self.receivingIban = self.fake.iban()
        self.receivingBban = self.fake.bban()

    def genCreditCard(self):
        # 3. Credit Card Details
        self.credit_card = self.fake.credit_card_full()
        self.card_type = self.fake.credit_card_provider()
        self.card_number = self.fake.credit_card_number(
            card_type="visa"
        )  # Revisit card type
        self.expiration_date = self.fake.credit_card_expire()
        self.security_code = self.fake.credit_card_security_code()

    def genTransaction(self):
        # 4. Transaction Details
        self.transaction_id = self.fake.uuid4()
        self.amount = round(np.random.normal(100, 50), 2)  # Negative possible?
        self.currency = self.fake.currency_code()
        self.date = self.fake.date()
        self.time = self.fake.time()


testValue = np.random.normal(100, 50)
print(round(testValue, 2))
