#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import exists

from logging import exception



def openCSVFile(fname_str: str) -> str:
    """loads a file, returns csv string"""
    # print("openCSVFile()")
    if not exists(fname_str):  # no file found?
        print(f"\t [-] No file by that name: {fname_str}")
        exit()  # end program if no file has been found.
    try:
        data_str = open(fname_str, "r").read()
    except exception:
        print("\t [-] Something has gone wrong. Correct filename?")
        return None
    if len(data_str) > 0 and "," in data_str:  # commas in this loaded file?
        return data_str
    return None


# end of openCSVFile()


def iterateData(in_str: str) -> dict:
    """Function to output the data in tidy lines. Place data into dictionary."""
    contact_dict = {}
    for line in in_str.splitlines():
        # print(line)
        name_str = line[: line.find(",")]  # get the name, located before first comma
        service_str = line[line.find(",") + 1 :].replace('"', "")
        contact_dict[name_str] = service_str
    return contact_dict


# end of iterateData()


def main() -> None:
    """driver function"""
    prompt_str = "\t Enter the CSV filename : "
    myFile_str = input(prompt_str)
    # print(f"\t [+] You entered file : {myFile_str}")
    myCSV_str = openCSVFile(myFile_str)
    # print(f"Main() {myCSV_str}")
    myContact_dict = iterateData(myCSV_str)  # print out in tidy lines
    # print(f"Dictionary of names: {myContact_dict}")
    for i in myContact_dict: print(f"\t [+] {i} : {myContact_dict[i]}")

# end of main()



main()  ## call the driver function of the program
