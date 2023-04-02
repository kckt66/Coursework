from utils import sort_executed, format_data, classified_card, get_date


def test_date():
    assert get_date('2019-12-08T22:46:21.935582') == '08.12.2019'
    assert get_date('2020-02-23T22:46:21.935582') == '23.02.2020'


def test_classified_card():
    assert classified_card('MasterCard 6783917276771847') == 'MasterCard 6783 91** **** 1847'
    assert classified_card('Счет 18889008294666828266') == 'Счет **8266'
    assert classified_card('Visa Gold 8326537236216459') == 'Visa Gold 8326 53** **** 6459'
    assert classified_card(None) == ''


def test_format_data():
    data = {
        "id": 490100847,
        "state": "EXECUTED",
        "date": "2018-12-22T02:02:49.564873",
        "operationAmount": {
            "amount": "56516.63",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Gold 8326537236216459",
        "to": "MasterCard 6783917276771847"
    }

    result = '22.12.2018 Перевод с карты на карту\nVisa Gold 8326 53** **** 6459 -> MasterCard 6783 91** **** 1847' \
             '\n56516.63 USD'

    assert format_data(data) == result


def test_sort_executed():
    data = [
        {
            'id': 27192367,
            'state': 'CANCELED'
        },
        {
            'id': 743278119,
            'state': 'EXECUTED',
            "date": "2018-10-15T08:05:34.061711"
        },
        {
            'id': 207126257,
            'state': 'EXECUTED',
            'date': '2019-07-15T11:47:40.496961'
        }
    ]

    result = [
        {
            'id': 207126257,
            'state': 'EXECUTED',
            'date': '2019-07-15T11:47:40.496961'
        },
        {
            'id': 743278119,
            'state': 'EXECUTED',
            "date": "2018-10-15T08:05:34.061711"
        }
    ]

    assert sort_executed(data) == result
