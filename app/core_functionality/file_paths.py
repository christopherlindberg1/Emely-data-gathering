from pathlib import Path, PurePath


class FilePaths:
    """ Class containing class variables for file paths that are used in the app """

    project_root = Path(__file__).parent.parent

    app_data_folder = PurePath(project_root, "data/app_data")

    base_questions_text_file = PurePath(app_data_folder, "base_questions.txt")

    dialogues_folder = PurePath(project_root, "data/generated_data/dialogues")

