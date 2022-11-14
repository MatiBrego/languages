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
        if result.hasClass():
            classCount += 1

        methodCount += result.methodQty()

    writeReportIntoFile(
        directoryCount, len(paths), classCount, methodCount, totalResults
    )


def writeReportIntoFile(
    dirCount: int,
    filesCount: int,
    classCount: int,
    methodCount: int,
    results: list[Result],
) -> None:
    file = open("informe", "w")
    file.write(f"directories: {dirCount}\n")
    file.write(f"files: {filesCount}\n")
    file.write(f"classes: {classCount}\n")
    file.write(f"methods: {methodCount}\n")
    for result in results:
        file.write(result.toString() + "\n")
    file.close()


scanDirectory("testDir")
