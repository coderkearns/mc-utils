#!/usr/bin/env python
# A bunch of function to help with minecraft addons.

import argparse
import zipfile
import os


# There are two expected arguments: filename and operation.
# filename is the name of the file to be operated on.
# operation is the operation to be performed, and is one of ["archive", "unarchive"]
# When operation is "archive", there is also a third argument: type. It will be one of ["world", "addon"]

argparser = argparse.ArgumentParser(description="Archive or unarchive a minecraft world, resource pack, or behavior pack.")
argparser.add_argument("filename", help="The name of the file to be operated on.")
argparser.add_argument("operation", help="The operation to be performed, and is one of ['archive', 'unarchive'].")
argparser.add_argument("type", help="The type of file to be operated on, and is one of ['world', 'addon'].")
args = argparser.parse_args()

def archive(filename, type):
    # Step 1: zip the file
    zf = zipfile.ZipFile(filename + ".zip", "w")
    zf.write(filename, filename)
    zf.close()
    # Step 2: rename the file extension.
    # a. strip the extension from the filename
    # b. add the extension ".mcworld" for world, ".mcaddon" for behaviors and resource packs
    # c. rename the file
    if type == "world":
        new_filename = filename[:-4] + ".mcworld"
    elif type == "addon":
        new_filename = filename[:-4] + ".mcaddon"
    else:
        print("Error: Unknown file type.")
        return
    # Step 3: rename the file
    os.rename(filename + ".zip", new_filename)

def unarchive(filename):
    # Step 1: unzip the file
    zf = zipfile.ZipFile(filename)
    zf.extractall()
    zf.close()

if args.operation == "archive":
    archive(args.filename, args.type)
elif args.operation == "unarchive":
    unarchive(args.filename)
else:
    print("Error: Unknown operation.")

