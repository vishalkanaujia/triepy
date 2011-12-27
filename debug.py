import sys
import tokenize

class pydbg:
    def __init__(self, modname=None):
        self.level = 0
        self.modname = modname

    def DLOG(self, lvl=None, fmt=None, *args):
        self.level = lvl

        if 0 == self.level:
            return

        print '%s ' %self.modname
      
        fmtlist = fmt.split()

        #Disabling new line of print python
        sys.stdout.write("%s:" %(self.modname))

        i = 0
        for arg in args:
            sys.stdout.write(fmtlist[i] %(arg))
            sys.stdout.write(" ")
            i = i + 1

        print ""

    def DLOG2(self, lvl=None, fmt=None, **args):
        self.level = lvl
