def determine_category(description, category_dict):
    for key, value in category_dict.items():
        if key in description:
            return value
    return ''


def toFloat(amt):
    if amt == '':
        return 0
    return float(amt)
