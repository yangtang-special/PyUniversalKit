import os


__all__ = ["get_all"]

Current = "PyUniversalKit/AnswerSearchkit/API"
def get_all():
    PATH_list = os.listdir(Current)
    return [i.replace(".py","") for i in PATH_list if i != "__pycache__" and i != "__init__.py" and i != "content.csv"]