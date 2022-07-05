import os

class PathInfo:

    def __init__(self):

        self.cwd = os.getcwd()
        self.path_parent_project = os.path.abspath(os.path.join(self.cwd, os.pardir))

        self._set_folder()

    def _set_folder(self):

        self.folder_GA = self.path_parent_project + "\\GAfig\\"
        if not (os.path.exists(self.folder_GA)):
            os.makedirs(self.folder_GA)
        print("Figure will be saved to: " + self.folder_GA)

    @property
    def GAfig(self):
        return self.folder_GA