from helpers.date_utils import get_future_date

test_data = [
    {
        'first_name': 'Алексей',
        'last_name': 'Смирнов',
        'address': 'ул. Ленина, д. 10',
        'metro_station': 'Черкизовская',
        'phone_number': '+79005551111',
        'delivery_date': get_future_date(1),  # Завтрашняя дата
        'rental_period': 'трое суток',
        'scooter_color': 'чёрный',
        'comment': 'Доставить утром',
        'order_button': 'top'
    },
    {
        'first_name': 'Екатерина',
        'last_name': 'Васильева',
        'address': 'пр. Мира, д. 5',
        'metro_station': 'Преображенская площадь',
        'phone_number': '+79007772222',
        'delivery_date': get_future_date(2),  # Послезавтрашняя дата
        'rental_period': 'сутки',
        'scooter_color': 'серый',
        'comment': 'Позвонить за 30 минут',
        'order_button': 'bottom'
    }
]