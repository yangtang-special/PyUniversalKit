from .models import CSVobjects,WriteCSVobject
from datetime import datetime
import csv,os
from typing import Union

class Operate():

    @staticmethod
    def return_file_message(PATH:str) -> dict:
        this_file_message_objects = os.stat(PATH)
        st_size = this_file_message_objects.st_size # File size
        st_mtime = str(datetime.fromtimestamp(this_file_message_objects.st_mtime))  # Modify time
        st_ctime = str(datetime.fromtimestamp(this_file_message_objects.st_ctime))  # Create time
        file_message = {"size": st_size, "mtime": st_mtime, "ctime": st_ctime}
        return file_message


    def read(self,PATH:str,Reading_method:str) -> CSVobjects:
        with open(PATH,Reading_method) as this_file_read:
            csv_reader = csv.reader(this_file_read)
            _content_List_:[[str]] = []

            for i in csv_reader:
                _content_List_.append(i)

            return CSVobjects(_content=_content_List_,_fileMessage=self.return_file_message(PATH))


    def write(self,PATH:str,header:Union[list,bool],rows:[[]],Writing_method:str) -> WriteCSVobject:
        with open(PATH, Writing_method) as f:
            f_csv = csv.writer(f)
            if type(header) == bool:
                pass
            else:
                f_csv.writerow(header)
            f_csv.writerows(rows)
            # csv op is end
        return WriteCSVobject(_content=self.read(PATH, "r")._content,_fileMessage=self.return_file_message(PATH),_path=PATH)




