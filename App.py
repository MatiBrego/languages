from Result import Result
from classReader import readFile
from pyFilesReader import getAllFilePaths

def scanDirectory(dir: str):
    paths = []

    directoryCount = getAllFilePaths(dir, paths)

    totalResults = []

    for path in paths:
        totalResults.extend(readFile(path))

    classCount = 0

    methodCount = 0
    
    for result in totalResults:
        if(result.hasClass()): classCount += 1

        methodCount += result.methodQty()

    writeReportIntoFile(classCount, methodCount, totalResults)

    # print(classCount)
    # print(methodCount)
    # print(totalResults) 

def writeReportIntoFile(classCount: int, methodCount: int, results: list[Result]) -> None:
    #ToDo
    pass
        

scanDirectory("testDir")