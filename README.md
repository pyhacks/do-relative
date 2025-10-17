# do-relative
Open and import relatively. 
Open files relative to the module you are in, instead of \_\_main__ module. 
Import modules relatively, directly using ```import module``` syntax, without using the ```from .``` syntax. 
Or use ```from .``` even if you are not in a package.
Import relative to given custom paths, including root directory so you can do an absolute import.

# Installation
```pip install do-relative```

# Api Reference
_class_ do_relative.**RelativeOpener**()

Constructor of this class returns an ```open``` function, instead of its instance. 
The paths you give to this function will be treated as relative to the directory calling module resides in. 

do_relative.**relative_import**(import_statement, folder = None)

Executes the _import_statement_ in caller's scope and relative to the calling module's location. 
Calling this function from another function is not supported. 
In that case, no new names will be introduced to caller's scope. 
_import_statement_ must be a string. Examples: "import module", "from module import func" or "from .. import module".
As a side note, you don't have to be in a package to use the syntax shown in the last example.
If supplied, _folder_ must be a path string. If _folder_ is provided import will be relative to that path instead of calling module's location.
_folder_ can either be relative to current working directory or absolute.
You can pass "/" as the _folder_ and make an absolute import. On windows "/" will be converted to the root directory of some drive.
Drive is determined by the current working directory.
