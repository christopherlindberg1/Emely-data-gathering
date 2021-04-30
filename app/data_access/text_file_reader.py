

class TextFileReader:
    """ Class with methods that read from text files """

    def __init__(self):
        pass

    
    def get_lines(self, file_path):
        """ Reads all lines from a text file and returns them as a list of strings """
        try:
            with open(file_path, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("O noo")


