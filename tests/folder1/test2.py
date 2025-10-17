import relative
relative.relative_import("import test3")
open = relative.RelativeOpener(__file__)
open("text.txt", "w").close()
