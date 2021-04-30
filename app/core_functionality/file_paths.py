from pathlib import Path, PurePath


class FilePaths:
    """ Class containing class variables for file paths that are used in the app """

    project_root = Path(__file__).parent.parent

    dialogues_folder = PurePath(project_root, "data/generated_data/dialogues")

