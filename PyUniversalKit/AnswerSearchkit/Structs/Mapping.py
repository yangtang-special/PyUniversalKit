from PyUniversalKit import CSVkit
from ..error import AdminRunError
import os
PATH = "PyUniversalKit/AnswerSearchkit/Static/Tables"
class Mapping():

    # This method will be loaded every time it is run
    def setting_mapping(self,api_type,header:list) -> bool:
        try:
            CSVkit.write(PATH=os.path.join(PATH,"%s.csv")% api_type, header=header, rows=[[]])
            return True
        except Exception as e:
            raise AdminRunError(api=api_type,detail=str(e))
