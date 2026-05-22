RELIGIONS = [
    'Buddhist',
    'Hindu',
    'Islam',
    'RomanCatholic',
    'OtherChristian',
    'Other',
]

RELIGION_LABELS = {
    'Buddhist': 'Buddhist',
    'Hindu': 'Hindu',
    'Islam': 'Islam',
    'RomanCatholic': 'Roman Catholic',
    'OtherChristian': 'Other Christian',
    'Other': 'Other',
}

RELIGION_COLORS = {
    'Buddhist': 'yellow',
    'Hindu': 'orange',
    'Islam': 'teal',
    'RomanCatholic': 'blue',
    'OtherChristian': 'purple',
    'Other': 'grey',
}

POSITIVE_COLOR = 'red'
NEGATIVE_COLOR = 'blue'


def shares(data):
    total = data.get('TotalPopulation') or sum(
        data.get(religion, 0) for religion in RELIGIONS
    )
    if total == 0:
        return {religion: 0.0 for religion in RELIGIONS}
    return {religion: data.get(religion, 0) / total for religion in RELIGIONS}


def triangle(value):
    return ''


def rounded_pp(value):
    rounded = round(value * 100, 1)
    if rounded == -0.0:
        rounded = 0.0
    return rounded


def format_pp(value):
    rounded = rounded_pp(value)
    if rounded == 0:
        return '0.0'
    return f'{rounded:+.1f}'


def format_share(value):
    return f'{value:.1%}'
