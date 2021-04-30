import os

class FilePaths:
    """ Class containing class variables for file paths that are used in the app """
    pass

    project_root_path = os.path.dirname(os.path.abspath(__file__))

    base_questions_path = f"{ project_root_path }/data/app_data/base_questions.txt"
