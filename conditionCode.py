class ConditionCode:
    def __init__(self):
        self.__code = "0000" # overflow, underflow, division by zero, equal-or-not

    def getCode(self):
        return self.__code

    def setCode(self, code):
        self.__code = code

    def judgeCCBit(self, bit):
        if self.__code[(3 - bit)] == 1:
            return True
        return False

    def setCCByIndex(self, index: int, cc_value: str):
        cc_list = []
        for cc in self.__code:
            cc_list.append(cc)
        cc_list[index] = cc_value
        self.__code = ''.join(cc_list)