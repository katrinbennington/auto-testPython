from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone X", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S20", "+79987654321"))
catalog.append(Smartphone("Xiaomi", "Mi 10", "+79012345678"))
catalog.append(Smartphone("Huawei", "P30 Pro", "+79876543210"))
catalog.append(Smartphone("OnePlus", "7T Pro", "+79123456780"))

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")
