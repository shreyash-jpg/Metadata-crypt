from faker import Faker
import json

def obfuscate_metadata(file_path):
    fake = Faker()
    obfuscated = {
        "Author": fake.name(),
        "Company": fake.company(),
        "Location": fake.address()
    }
    with open(file_path + ".obfuscated.json", 'w') as f:
        json.dump(obfuscated, f, indent=4)
    print("Metadata obfuscated and saved.")