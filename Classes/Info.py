import os

class PathInfo:

    def __init__(self):

        self.cwd = os.getcwd()
        self.path_parent_project = os.path.abspath(os.path.join(self.cwd, os.pardir))

        self._set_folder()

    def _set_folder(self):

        self._folder_GA = self.path_parent_project + "\\GAfig\\"
        if not (os.path.exists(self._folder_GA)):
            os.makedirs(self._folder_GA)
        print("Figure will be saved to: " + self._folder_GA)

        self._folder_hist = self.path_parent_project + "\\GAhis\\"
        if not (os.path.exists(self._folder_hist)):
            os.makedirs(self._folder_hist)
        print("History will be saved to: " + self._folder_hist)

    @property
    def folder_GA(self):
        return self._folder_GA

    @property
    def folder_hist(self):
        return self._folder_hist
