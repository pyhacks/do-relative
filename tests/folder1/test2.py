import do_relative
do_relative.relative_import("import test3")
open = do_relative.RelativeOpener()
open("text.txt", "w").close()
