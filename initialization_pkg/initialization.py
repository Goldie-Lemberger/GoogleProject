import pickle

from trie_pkg.trie import Trie
from pathlib import Path

#
# The initialization class, occurs only once & write the suffix tree to file
#
class Initialization:
    __instance = None
    tree = Trie()
    def __new__(cls, *args, **kwargs):
        if not Initialization.__instance:
            Initialization.__instance = object.__new__(cls)
        return Initialization.__instance

    def get_tree(self):
        return self.tree

    def __add_file_to_tree(self, file):
        try:
            with open(file,'r',encoding="utf8") as file_:
                lines = file_.readlines()
                for index,line in enumerate(lines):
                    line = line.replace('\n','')
                    if line == '\n':
                        continue
                    self.tree.insert(line,file,index)
        except IOError:
             return IOError
    def write_tree_to_file(self):
        data=self.get_tree()
        fileObject = "data_file.txt"
        with open(fileObject, "wb") as f:
            pickle.dump(data, f)

    def load_file(self):
        fileObject = "data_file.txt"
        with open(fileObject, "rb") as f:
            som = pickle.load(f)
            self.tree=som

    def get_directory_files(self,dir):
        p = Path(dir)
        for i in p.glob('**/*'):

            if i.is_file():
                self.__add_file_to_tree(i)
            if i.is_dir():
                self.get_directory_files(i)

        self.write_tree_to_file()


