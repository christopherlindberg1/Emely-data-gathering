from core_functionality.dialogue_file_manager import DialogueFileManager
from data_access.text_file_writer import TextFileWriter


class DialogueSaver:
    """ Class that handles the opreations of writing user generated dialogues to the file system """
    
    def __init__(self):
        self.dialogue_file_manager = DialogueFileManager()
        self.text_file_writer = TextFileWriter()


    def save_dialogue(
        self,
        base_question: str,
        answer_one: str,
        follow_up_one: str,
        answer_two: str,
        follow_up_two: str):
        """ Formats dialogue data and saves it in a file """
        
        dialogue_lines = [
            "episode_start\n",
            f"emely: { base_question }\n",
            f"user: { answer_one }\n",
            f"emely: { follow_up_one }\n",
            f"user: { answer_two }\n",
            f"emely: { follow_up_two }\n",
            "episode_done"
        ]

        file_path = self.dialogue_file_manager.get_file_path()

        self.text_file_writer.write_lines(file_path, dialogue_lines)