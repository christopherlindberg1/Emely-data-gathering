

class TextFileWriter:
    """ Class with methods for writing to text files """

    def __init__(self):
        pass

    
    def write_lines(self, file_path, lines):
        """ Writes lines from a list of strings to a text file """
        
        try:
            with open(file_path, "w") as file:
                file.writelines(lines)
        except:
            raise