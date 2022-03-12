from register import Register


class ProgramCounter(Register):
    def __init__(self, init):
        self.__value = init

    def pc_plus_one(self):
        self.__value = self.__value + 1