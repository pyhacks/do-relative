import relative
relative.relative_import("import test3")
open = relative.RelativeOpener()
open("text.txt", "w").close()
