# from scrapper import *
import logging
import json


def reader(filename: str) -> list:
    """read and return list from json file"""
    with open(filename, "r", encoding="utf-8") as file:
        lst = json.load(file)
    return lst


def add_in_json(filename: str, data: list) -> bool:
    """add list of data in json file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=3)
    return True


def checker() -> bool:
    """check new updates in .json file"""
    info = reader("result.json")
    info1 = reader("last_results.json")
    try:
        if info1:
            if info[0]["#"] == info1[0]["#"]:
                return False
            else:
                add_in_json("last_results.json", [info[-1]])
                add_in_json("result.json", info)
                return True
        else:
            return False

    except Exception as e:
        logging.warning(str(e) + " -- warning in file helper_checker was returned exception --")
        add_in_json("last_results.json", [info[-1]])
        add_in_json("result.json", info)
        return True
