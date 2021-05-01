import random
from typing import List

from data_access.text_file_reader import TextFileReader
from data.app_data.base_questions import base_questions
from core_functionality.file_paths import FilePaths


class QuestionGenerator:
    """ Handles all operations related to generating a question """

    def __init__(self):
        self.text_file_reader = TextFileReader()


    def get_random_base_question(self) -> str:
        """ Returns a random question """

        questions = self.get_base_questions()
        return questions[random.randrange(0, len(questions))]


    def get_base_questions(self) -> List[str]:
        """ Returns a list with all base questions """

        try:
            return self.text_file_reader.read_lines(FilePaths.base_questions_text_file)
        except FileNotFoundError:
            return base_questions

