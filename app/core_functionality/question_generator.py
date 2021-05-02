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
        random_question = questions[random.randrange(0, len(questions))]

        # Most questions contain line break when read from file. Remove so they can be stored correctly.
        if random_question[len(random_question) - 1 : len(random_question)] == "\n":
            return random_question[0:len(random_question) - 1]
        
        return random_question


    def get_base_questions(self) -> List[str]:
        """ Returns a list with all base questions """

        try:
            return self.text_file_reader.read_lines(FilePaths.base_questions_text_file)
        except FileNotFoundError:
            return base_questions

