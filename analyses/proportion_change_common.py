RELIGIONS = [
    'Buddhist',
    'Hindu',
    'Islam',
    'RomanCatholic',
    'OtherChristian',
    'Other',
]


def shares(data):
    total = data.get('TotalPopulation') or sum(
        data.get(religion, 0) for religion in RELIGIONS
    )
    if total == 0:
        return {religion: 0.0 for religion in RELIGIONS}
    return {religion: data.get(religion, 0) / total for religion in RELIGIONS}


def triangle(value):
    if value > 0:
        return '🟩 '
    if value < 0:
        return '🟥 '
    return ''
