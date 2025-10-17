import os
import sys
import re


class RelativeOpener:
    def __new__(cls, __file__, function = True):
        opener = object.__new__(cls)
        if function:
            opener.__init__(__file__, function)
            return opener.open
        else:
            return opener
        
    def __init__(self, __file__, function = True):
        self.__file__ = __file__

    def get_abspath(self, path):
        base_dir = os.path.dirname(os.path.abspath(self.__file__))
        return os.path.join(base_dir, path)

    def open(self, path, *args, **kwargs):
        return open(self.get_abspath(path), *args, **kwargs)


def relative_import(import_statement, folder = None):
    if not folder:
        file = sys._getframe(1).f_globals["__file__"]
        file = os.path.abspath(file)
        folder = os.path.dirname(file)
    else:
        folder = os.path.abspath(folder)
    if import_statement.startswith("from"):
        match = re.search(r"from\s*(\.+.*)", import_statement)
        if match:
            code = match.group(1).removeprefix(".")
            dots_removed = code.lstrip(".")
            go_back = len(code) - len(dots_removed)
            import_statement = "from " + dots_removed
            match = re.search(r"from\s*import (.*)", import_statement)
            if match:
                import_statement = "import " + match.group(1)
            for i in range(go_back):                
                head, _ = os.path.split(folder)                
                folder = head
    sys.path.insert(0, folder)
    exec(import_statement, locals = sys._getframe(1).f_locals)
    del sys.path[0]
