class Result:
    """
    Class that represents the result of a search in a python file. 
    It contains a class name (cls), which might be none if the the method read was not in a class, 
    and a list of methods contained in the class (Or just one if the method was not in a class).
    """

    def __init__(self, cls: str, methods: list[str]):
        self.cls = cls
        self.methods = methods

    def getCls(self):
        return self.cls

    def hasClass(self):
        return self.cls != None

    def methodQty(self):
        return len(self.methods)

    def __repr__(self) -> str:
        if(self.hasClass()):
            r = "class: " + self.cls +" methods:"
        else:
            r = "method: "
        for m in self.methods:
            r += " " + m
        return "{" + r + "}"