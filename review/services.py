def is_valid_request(data):
    return data.get('name') and data.get('review') and data.get('rating')