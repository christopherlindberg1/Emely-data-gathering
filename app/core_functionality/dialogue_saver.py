from core_functionality.dialogue_file_manager import DialogueFileManager
from data_access.text_file_writer import TextFileWriter

class DialogueSaver:
    """ Class that handles the opreations of writing user generated dialogues to the file system """
    
    def __init__(self):
        self.dialogue_file_manager = DialogueFileManager()
        self.text_file_writer = TextFileWriter()


    def save_dialogue(self, base_question, a_one, f_one, a_two, f_two):
        """ Formats dialogue data and saves it in a file """
        
        dialogue_lines = [
            "episode_start\n",
            f"emely: { base_question }\n",
            f"user: { a_one }\n",
            f"emely: { f_one }\n",
            f"user: { a_two }\n",
            f"emely: { f_two }\n",
            "episode_done\n"
        ]

        file_path = self.dialogue_file_manager.get_unique_file_path()

        self.text_file_writer.write_lines(file_path, dialogue_lines)