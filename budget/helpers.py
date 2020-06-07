def should_process_row(description, skip_set):
    if [item for item in skip_set if (item in description)]:
        return False
    return True


def determine_category(description, category_dict):
    for key, value in category_dict.items():
        if key in description:
            return value
    return ''


def toFloat(amt):
    if amt == '':
        return 0
    return float(amt)
