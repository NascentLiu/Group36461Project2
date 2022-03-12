class Memory:
    def __init__(self):
        self.__memory = [0] * 4096

    def getValue(self, EA):
        return self.__memory[EA]

    def setValue(self, EA, value):
        self.__memory[EA] = value