from helpers.date_utils import get_future_date

test_data_top = {
    'first_name': 'Алексей',
    'last_name': 'Иванов',
    'address': 'ул. Ленина, д. 10',
    'metro_station': 'Пушкинская',
    'phone_number': '+79991234567',
    'delivery_date': get_future_date(1),
    'rental_period': 'сутки',
    'scooter_color': 'чёрный',
    'comment': 'Доставить утром',
}

test_data_bottom = {
    'first_name': 'Екатерина',
    'last_name': 'Петрова',
    'address': 'пр. Мира, д. 5',
    'metro_station': 'Курская',
    'phone_number': '+79991234568',
    'delivery_date': get_future_date(2),
    'rental_period': 'двое суток',
    'scooter_color': 'серый',
    'comment': 'Позвонить за 30 минут',
}