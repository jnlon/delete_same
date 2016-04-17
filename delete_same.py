#!/usr/bin/python3

# This script deletes all duplicate files in the current working directory.
# Duplicates are determined based on the sha1 hash of the file's contents,
# and are printed to stdio before being deleted

import os, hashlib, sys

sums = set()
dups = 0

filelist = os.listdir('.')

for filename in filelist:
    if not os.path.isfile(filename):
        continue
    m = hashlib.sha1()
    f = open(filename, "rb")
    m.update(f.read())
    sha = m.digest()
    f.close()
    if sha in sums:
        print(">>>",filename)
        os.remove(filename)
        dups += 1
    else:
        sums.add(sha)

print("Removed", dups, "duplicate files")

