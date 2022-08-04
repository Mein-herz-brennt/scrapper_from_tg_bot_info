from scrapper import *
import logging


def checker() -> None:
    """check new updates in .json file"""
    try:
        info = reader("result.json")
        info1 = reader("last_results.json")
        print(info1)
        if info[-1]["#"] == info1[-1]["#"]:
            with open("out_checker.txt", "w", encoding="utf-8") as file:
                file.write("False")
        else:
            print(add_in_json("last_results.json", [info[-1]]))
            info.pop(-1)
            print(add_in_json("result.json", info))
            with open("out_checker.txt", "w", encoding="utf-8") as file:
                file.write("False")
    except Exception as e:
        logging.warning(str(e) + " -- warning in file helper_checker was returned exception --")


