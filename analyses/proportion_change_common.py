RELIGIONS = [
    'Buddhist',
    'Hindu',
    'Islam',
    'RomanCatholic',
    'OtherChristian',
    'Other',
]

RELIGION_COLORS = {
    'Buddhist': 'yellow',
    'Hindu': 'orange',
    'Islam': 'teal',
    'RomanCatholic': 'blue',
    'OtherChristian': 'purple',
    'Other': 'grey',
}

POSITIVE_COLOR = 'green'
NEGATIVE_COLOR = 'red'


def shares(data):
    total = data.get('TotalPopulation') or sum(
        data.get(religion, 0) for religion in RELIGIONS
    )
    if total == 0:
        return {religion: 0.0 for religion in RELIGIONS}
    return {religion: data.get(religion, 0) / total for religion in RELIGIONS}
