import os
import sys
for (dirpath, dirnames, filenames) in os.walk('./'):
    for filename in filenames:
        print "process {}".format(filename)
        f = open(filename, 'r')
        content = []
        for line in f:
            newl = line.replace('\n', '').replace(chr(13), '')
            if len(newl) > 0:
                content.append(newl)
        f.close()
        f = open(filename, 'w')
        f.write('\n'.join(content))
        f.close()