<<<<<<< HEAD
=======
# TODO запустить этот код и сделать коммит на git
>>>>>>> origin/master

import sys
import platform

info = 'OS info is \n{} \n\nPython version is {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)
with open('os_info.txt', 'w') as ff:
    ff.write(info)
