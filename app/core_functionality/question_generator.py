import random

from data_access.text_file_reader import TextFileReader
from data.app_data.base_questions import base_questions
# from core_functionality.file_paths import FilePaths


class QuestionGenerator:
    """ Handles all operations related to generating a question """

    def __init__(self):
        self.text_file_reader = TextFileReader()


    def get_random_question(self):
        questions = self.get_questions()
        return questions[random.randrange(0, len(questions))]


    def get_questions(self):
        """ Gets all questions. Gets them from a source code file if it fails to read from file """
        try:
            return self.text_file_reader.read_lines()
        except FileNotFoundError:
            return base_questions

