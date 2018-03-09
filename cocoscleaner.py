#!/usr/bin/env python

import os
from pprint import pprint

def main(args):
    print("代码目录:\t " + args.src)
    print("CocoStudio目录:\t " + args.csd)

    luaFiles = GetFilesInDirWithExt(args.src, "lua")
    csdFiles = GetFilesInDirWithExt(args.csd, "csd")
    pngFiles = GetPngsIndependent(args.res)    # 单独的png文件
    plistFiles = GetPlistIndependent(args.res) #单独的plist文件

    # pprint(luaFiles)
    # pprint(csdFiles)
    # pprint(pngFiles)
    pprint(plistFiles)


def GetFilesInDirWithExt(directory, ext):
    allfiles = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith("." + ext):
                allfiles.append(os.path.join(root, filename))

    return allfiles

def GetPngsIndependent(directory):
    pngfiles = GetFilesInDirWithExt(directory, "png")

    independent = []

    for png in pngfiles:
        plist = png.replace(".png", ".plist")
        if not os.path.exists(plist):
            independent.append(png)

    return independent

def GetPlistIndependent(directory):
    plistfiles = GetFilesInDirWithExt(directory, "plist")

    independent = []

    for plist in plistfiles:
        png = plist.replace(".plist", ".png")
        if os.path.exists(png):
            independent.append(plist)

    return independent

def CheckPythonVersion():
    import sys

    print("Python Version: " + str(sys.version_info.major))

def InitOptions():
    import argparse

    parser = argparse.ArgumentParser()

    # parser.add_argument("-cfg", "--config", default = "config.py", help = "配置文件路径")
    parser.add_argument("--src", help = "src代码目录")
    parser.add_argument("--res", help = "res资源目录")
    parser.add_argument("--csd", help = "cocosstudio目录")

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    CheckPythonVersion()

    args = InitOptions()

    main(args)
