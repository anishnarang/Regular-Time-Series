import   numpy
import rad
import sys

a=rad.RandomWalk(int(sys.argv[1]))
numpy.savetxt("q.txt",a,fmt='%.7e',newline="\n")
