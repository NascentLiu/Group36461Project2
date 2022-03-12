class ProgramCounter:
    def __init__(self, init):
        self.__value = init

    def pc_plus_one(self):
        self.__value = self.__value + 1

    def getValue(self):
        return self.__value

    def setValue(self, value: int):
        self.__value = value