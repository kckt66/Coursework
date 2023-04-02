def sort_executed(data):
    items = []

    for dt in data:
        if dt.get('state') == 'EXECUTED':
            items.append(dt)

    items.sort(key=lambda x: x.get('date'), reverse=True)

    return items


def format_data(item):
    str_date = get_date(item.get('date'))
    description = item.get('description')
    from_ = classified_card(item.get('from'))
    to_ = classified_card(item.get('to'))
    summ = item.get('operationAmount').get('amount')
    currency = item.get('operationAmount').get('currency').get('name')

    if from_:
        from_ = from_ + " -> "

    return f'{str_date} {description}\n{from_}{to_}\n{summ} {currency}'


def classified_card(card):
    if not card:
        return ''
    card_data = card.split(' ')

    if card_data[0] == 'Счет':
        return card_data[0] + ' **' + card_data[1][-4:]

    card_number = card_data[-1][:4] + ' ' + card_data[-1][4:6] + '** **** ' + card_data[-1][-4:]

    return ' '.join(card_data[:-1]) + ' ' + card_number


def get_date(str_date):
    date = reversed(str_date[:10].split('-'))
    return '.'.join(date)
