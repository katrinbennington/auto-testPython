from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Lenina", "1", "123")
from_address = Address("654321", "Saint-Petersburg", "Nevskaya", "2", "456")

mail = Mailing(to_address, from_address, 100, "TRK123456789")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, "
      f"{mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")
