import os
from pathlib import Path


class TextFileReader:
    """ Class with methods that read from text files """

    def __init__(self):
        pass

    
    def get_lines(self):
        """ Reads all lines from a text file and returns them as a list of strings """
        # pass
        try:
            with open("./data/app_data/base_qugestions.txt", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            raise

