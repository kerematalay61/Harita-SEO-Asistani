from faker import Faker
fake = Faker()

def create_business(name, category, city, district):
    address = fake.address().replace("\n", ", ")
    postal_code = fake.postcode()
    return {
        "name": name,
        "category": category,
        "address": f"{district}, {city}, {address}",
        "postal_code": postal_code,
        "hours": "09:00-23:00",
        "photo": f"{name.lower().replace(' ', '_')}_logo.png"
    }
