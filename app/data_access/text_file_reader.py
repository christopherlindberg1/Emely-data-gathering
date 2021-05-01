from typing import List


class TextFileReader:
    """ Class with methods for reading from text files """

    def __init__(self):
        pass

    
    def read_lines(self, file_path: str) -> List[str]:
        """ Reads all lines from a text file and returns them as a list of strings """

        try:
            with open(file_path, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            raise

