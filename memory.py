from cache import Cache
from cacheLine import CacheLine


class Memory:
    def __init__(self):
        self.__memory = [0] * 4096
        self.__cache = Cache()

    def getValue(self, EA):
        if self.__cache.getValue(EA) != -1:
            return self.__cache.getValue(EA)
        self.__cache.setValue(CacheLine(EA, self.__memory[EA]))
        return self.__memory[EA]

    def setValue(self, EA, value):
        self.__memory[EA] = value
        self.__cache.updateValue(EA, value)