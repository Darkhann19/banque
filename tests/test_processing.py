import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state1():
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'}]) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_filter_by_state2():
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_descending():
    transactions = [
        {'id': 1, 'date': '2023-01-01T00:00:00'},
        {'id': 2, 'date': '2023-01-03T00:00:00'},
        {'id': 3, 'date': '2023-01-02T00:00:00'},
    ]
    sorted_transactions = sort_by_date(transactions, reverse=True)
    assert [t['id'] for t in sorted_transactions] == [2, 3, 1]


def test_sort_by_date_ascending():
    transactions = [
        {'id': 1, 'date': '2023-01-01T00:00:00'},
        {'id': 2, 'date': '2023-01-03T00:00:00'},
        {'id': 3, 'date': '2023-01-02T00:00:00'},
    ]
    sorted_transactions = sort_by_date(transactions, reverse=False)
    assert [t['id'] for t in sorted_transactions] == [1, 3, 2]


def test_sort_by_date_same_dates():
    transactions = [
        {'id': 1, 'date': '2023-01-01T00:00:00'},
        {'id': 2, 'date': '2023-01-01T00:00:00'},
        {'id': 3, 'date': '2023-01-01T00:00:00'},
    ]
    sorted_transactions = sort_by_date(transactions, reverse=True)
    assert [t['id'] for t in sorted_transactions] == [1, 2, 3]