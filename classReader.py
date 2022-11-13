import re
from Result import Result

def readFile(path: str) -> list[Result]:
    """
    Reads the file path and returns a list of Result objects.
    """

    f = open(path)
    lines = f.readlines()
    currentLine = 0

    resultList = []

    while(currentLine < len(lines)):
        cls = re.search(r"class ([a-zA-Z]+):", lines[currentLine])
        method = re.search(r"def ([a-zA-Z]+)", lines[currentLine])
        if cls != None:
            currentLine += 1
            methods = []
            readMethodsInClass(methods, currentLine, lines)
            resultList.append(Result(cls.group(1), methods))
            break
            
        if method != None:
            resultList.append(Result(None, [method.group(1)]))
        
        currentLine += 1

    return resultList
        
def readMethodsInClass(methods: list[str], currentLine: int, lines: list[str]):
    """
    Reads each method's name of a class and adds them into a list received as a parameter. 
    It also receives the current line from which to start, and updates it as the lines are read.
    """
    linesLeft = lines[currentLine:]

    for line in linesLeft:
        cls = re.search(r"class ([a-zA-Z]+):", line)
        method = re.search(r"def ([a-zA-Z]+)", line)

        if cls != None:
            break

        if(method != None):
            methods.append(method.group(1))

        currentLine += 1

    return methods