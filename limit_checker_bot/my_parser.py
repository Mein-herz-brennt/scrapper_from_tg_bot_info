import openpyxl
import json


def parse(filename: str) -> list:
    """function for parse data from xlsx to json file"""
    book = openpyxl.load_workbook(filename=filename).active
    lst = []
    for row in book.values:
        lst.append(list(row))
    last_lst = []
    for name in range(len(lst[0]) - 1):
        dct = {}
        if lst[0][name] is not None:
            dct[lst[0][name]] = []
            for lst_cards_index in range(1, len(lst)):
                # for card in lst[lst_cards_index]:
                if lst[lst_cards_index][name] is not None:
                    dct[lst[0][name]].append(lst[lst_cards_index][name])
        dct["limit"] = 30000
        last_lst.append(dct)
    with open('result.json', "w", encoding="utf-8") as file:
        json.dump(last_lst, file, indent=3)

    return last_lst


def card_string_generator(cards: list) -> str:
    cards_str = ""
    for i in range(len(cards)):
        if len(cards) != i:
            cards_str += cards[i] + "\n\n"
        else:
            cards_str += cards[i]
    return cards_str
