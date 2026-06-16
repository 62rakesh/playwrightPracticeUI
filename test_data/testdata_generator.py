from faker import Faker

faker = Faker()

class TestDataGenerator:

    @staticmethod
    def addNew_customer():
        return {
            "customer_name": faker.first_name()
        }
