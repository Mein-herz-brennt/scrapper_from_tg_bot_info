from scrapper import *
import logging


def checker() -> bool:
    """check new updates in .json file"""
    try:
        info = reader("result.json")
        info1 = reader("last_result.json")
        if info[-1]["#"] == info1[-1]["#"]:
            return False
        else:
            add_in_json("last_results.json", [info[-1]])
            info.pop(-1)
            add_in_json("result.json", info)
            return True
    except Exception as e:
        logging.warning(str(e) + " -- warning in file helper_checker was returned exception --")


