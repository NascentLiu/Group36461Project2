from cacheLine import CacheLine


class Cache:
    def __init__(self):
        self.__cache: list[CacheLine] = []

    def getValue(self, EA: int):
        for i in range(len(self.__cache)):
            if self.__cache[i].getAddress() == EA:
                return self.__cache[i].getValue()
        return -1

    def setValue(self, cacheLine):
        self.__cache.append(cacheLine)
        if len(self.__cache) > 16:
            del self.__cache[0]

    def updateValue(self, EA: int, value: int):
        for i in range(len(self.__cache)):
            if self.__cache[i].getAddress() == EA:
                self.__cache[i].setValue(value)