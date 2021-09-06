"""
 AnswerSearchkit strictly defines the relationship between different API
 interfaces and the corresponding table style sheet, which we define as a
 mapping, and the mapping is unique for each API interface.
"""
from .Structs.Mapping import Mapping
from typing import Dict






mapping:Dict[str,bool] = {

    "icodef":Mapping().setting_mapping("icodef",["Number","Question","Option","Content","API InterFace"]),

    # Add the new API-Table mapping rules here

}