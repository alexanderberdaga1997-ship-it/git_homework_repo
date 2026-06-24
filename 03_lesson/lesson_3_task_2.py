from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 16", "+79111111111"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79222222222"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79333333333"))
catalog.append(Smartphone("Honor", "90", "+79444444444"))
catalog.append(Smartphone("Huawei", "P60", "+79555555555"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")