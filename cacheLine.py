class CacheLine:
    def __init__(self, address: int, value: int):
        self.__address = address
        self.__value = value

    def getAddress(self):
        return self.__address

    def getValue(self) -> int:
        return self.__value

    def setValue(self, value: int):
        self.__value = value