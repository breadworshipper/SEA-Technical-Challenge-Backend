from .models import Reservation

def is_valid_request(data):
    return data.get('name') and data.get('phone_number') and data.get('type_of_service') and data.get('date') and data.get('time')

