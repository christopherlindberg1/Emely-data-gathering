import datetime
import os
from pathlib import Path, PurePath
from random import randrange

from core_functionality.file_paths import FilePaths



class DialogueFileManager:
    """ Class responsible for creating an appropriate file structure for dialogue files """
    
    def __init__(self):
        pass


    def get_unique_file_path(self):
        """ Returns a unique file name for a dialogue """

        folder_path = self.__get_folder_for_today()
        full_file_path = self.__get_unique_file_name(folder_path)

        return full_file_path


    def __get_unique_file_name(self, folder_path):
        """
        Gets a unique file name consisting of date and time, as well as microseconds.
        Makes sure it is unique before returning it.
        """
        
        # file_name = f"{ datetime.datetime.now().strftime('%Y/%m/%d-%I:%M:%S.%f') }-{ randrange(1, 1000) }.txt"
        file_name = f"{ randrange(1, 100000001) }.txt"
        full_file_path = PurePath(folder_path, file_name)

        while os.path.isfile(full_file_path) == True:
            # file_name = f"{ datetime.datetime.now().strftime('%Y/%m/%d-%I:%M:%S.%f') }-{ randrange(1, 1000) }.txt"
            file_name = f"{ randrange(1, 1000001) }.txt"
            full_file_path = PurePath(folder_path, file_name)
        
        return full_file_path


    def __get_folder_for_today(self):
        """ Returns the path to the folder that match the current date """

        date = datetime.datetime.now()
        
        year = date.year
        month = date.month if len(str(date.month)) == 2 else f"0{ date.month }"
        # month = 6 if len(str(6)) == 2 else f"0{ 6 }"
        day = date.day if len(str(date.day)) == 2 else f"0{ date.day }"

        folder_path = PurePath(FilePaths.dialogues_folder, f"{ year }/{ month }/{ day }")

        if os.path.isdir(folder_path) == True:
            return folder_path
        else:
            return self.__create_folder_for_today_and_return_path()


    def __create_folder_for_today_and_return_path(self):
        """ Creates folder for the current day and returns the path """

        date = datetime.datetime.now()
        
        year = date.year
        month = date.month if len(str(date.month)) == 2 else f"0{ date.month }"
        # month = 6 if len(str(6)) == 2 else f"0{ 6 }"
        day = date.day if len(str(date.day)) == 2 else f"0{ date.day }"

        year_folder = PurePath(FilePaths.dialogues_folder, f"{ year }")

        if os.path.isdir(year_folder) == False:
            os.mkdir(year_folder)

        month_folder = PurePath(year_folder, f"{ month }")

        if os.path.isdir(month_folder) == False:
            os.mkdir(month_folder)

        day_folder = PurePath(month_folder, f"{ day }")

        if os.path.isdir(day_folder) == False:
            os.mkdir(day_folder)

        return day_folder


