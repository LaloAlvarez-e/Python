import os
import re
import argparse

#absolute path of a file
currentFilePathName = r""
newFilePathName = r""


def main():
    errorCode = 0
    FilesRename = 0
    regex = re.compile(r'^(.*)\s.*\{.*\}\s(.*)\s\[(.*)\s(\d+).*\.(.*)$', flags = re.I)
    regex2 = re.compile(r'^(.*)\.(.*)$', flags = re.I)
    sub_name = regex.sub
    sub_name2 = regex2.sub
    
    argParser = argparse.ArgumentParser(description= "Rename Files")
    argParser.add_argument("-p","--path", help= "Path of the files to rename")
    
    arguments = argParser.parse_args()
    pathDirFiles = arguments.path
    
    isPathDirValid = os.path.isdir(pathDirFiles)
    print ("File names in progress..")
    if isPathDirValid is True:
        for filename in os.listdir(pathDirFiles):
            pathFile = os.path.join(pathDirFiles, filename)
            isPathFileValid = os.path.isfile(pathFile)
            if isPathFileValid is True:
                match = bool(regex.match(filename))
                if match is True:
                    newFileName = sub_name("[\\4]_-_\\2_-_\\3_-_\\1.\\5",filename)
                    newFileName = newFileName.replace(" ","_")
                    newFileName = newFileName.replace(",_","__")
                    newPathFile = os.path.join(pathDirFiles, newFileName)
                    isNewPathFileExist = os.path.exists(newPathFile)
                    while isNewPathFileExist is True:
                        newFileName = sub_name2("\\1_.\\2",newFileName)
                        newPathFile = os.path.join(pathDirFiles, newFileName)
                        isNewPathFileExist = os.path.exists(newPathFile)
                        print(newPathFile)
                    print(newPathFile)
                    FilesRename = FilesRename + 1
                    os.rename(pathFile, newPathFile)
            else:
                errorCode = 1
                print("File path invalid")
    else:
        errorCode = 2
        print ("Dir Path is invalid")
    
    errorString = "Successfull"
    if errorCode != 0:
        errorString = "Error"
    
    print ("File names completed, Files rename {} -- {}".format(FilesRename, errorString))


if __name__ == "__main__":
    main()