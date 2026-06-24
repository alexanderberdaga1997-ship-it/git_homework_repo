from address import Address
from mailing import Mailing

to_address = Address(
    "123456",
    "Москва",
    "Ленина",
    "10",
    "15"
)

from_address = Address(
    "654321",
    "Санкт-Петербург",
    "Пушкина",
    "20",
    "5"
)

mailing = Mailing(
    to_address,
    from_address,
    500,
    "ABC123456"
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.city} в "
    f"{mailing.to_address.city}. "
    f"Стоимость {mailing.cost} рублей."
)