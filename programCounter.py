from register import Register


class ProgramCounter(Register):
    def pc_plus_one(self):
        self.__value = self.__value + 1