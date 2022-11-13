import os

def getAllFilePaths(dir: str, filePaths: list[str]) -> int:
    """
        Adds all the paths to files inside the given directory path, 
        into a list received as a parameter. 
        It also counts all subdirectories in it and returns the count as an int.
    """
    currentDirList: list[str] = os.listdir(dir)
    subDirs: int = 0
    
    for path in currentDirList:
        completePath: str = dir + "\\" + path
        if os.path.isdir(completePath):
            subDirs += 1
            subDirs += getAllFilePaths(completePath, filePaths)
        
        elif os.path.isfile(completePath):
            filePaths.append(completePath)
    

    return subDirs
