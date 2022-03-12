from register import Register
from conditionCode import ConditionCode
from memory import Memory
from programCounter import ProgramCounter


class Architecture:
    def __init__(self):
        self.__GPR0 = Register()
        self.__GPR1 = Register()
        self.__GPR2 = Register()
        self.__GPR3 = Register()
        self.__IXR1 = Register()
        self.__IXR2 = Register()
        self.__IXR3 = Register()
        self.__PC = ProgramCounter(256)
        self.__MAR = Register()
        self.__MBR = Register()
        self.__IR = Register()
        self.__MFR = Register()
        self.__memory = Memory()
        self.__conditioncode = ConditionCode()
        self.__input = 0
        self.__output = 0

    def getMemory(self):
        return self.__memory

    def getOutput(self):
        return self.__output

    def getProgramCounter(self):
        return self.__PC

    def getGPR0(self):
        return self.__GPR0

    def getGPR1(self):
        return self.__GPR1

    def getGPR2(self):
        return self.__GPR2

    def getGPR3(self):
        return self.__GPR3

    def getIXR1(self):
        return self.__IXR1

    def getIXR2(self):
        return self.__IXR2

    def getIXR3(self):
        return self.__IXR3

    def getMAR(self):
        return self.__MAR

    def getMBR(self):
        return self.__MBR

    def getIR(self):
        return self.__IR

    def getMFR(self):
        return self.__MFR

    def instruction_controller(self, instruction: str):
        Opcode = instruction[:6]
        R = instruction[6:8]
        IX = instruction[8:10]
        I = instruction[10]
        Address = instruction[11:]
        A_L = instruction[8]
        L_R = instruction[9]
        count = instruction[12:]
        EA = self.getEA(IX, I, Address)
        if Opcode == '000001':
            self.execute_LDR(R, EA)
        elif Opcode == '000010':
            self.execute_STR(R, EA)
        elif Opcode == '000011':
            self.execute_LDA(R, EA)
        elif Opcode == '100001':
            self.execute_LDX(IX, EA)
        elif Opcode == '100010':
            self.execute_STX(IX, EA)
        #从这开始project2了！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        elif Opcode == '001000':#完成
            self.execute_JZ(R, EA)
        elif Opcode == '001001':#完成
            self.execute_JNE(R, EA)
        elif Opcode == '001010':#完成
            self.execute_JCC(R, EA)
        elif Opcode == '001011':#完成
            self.execute_JMA(EA)
        elif Opcode == '999999':#不知道argument是啥
            self.execute_JSR(EA)
        elif Opcode == '999998':
            self.execute_RFS(Address)
        elif Opcode == '001110':#完成
            self.execute_SOB(R, EA)
        elif Opcode == '001111':#完成
            self.execute_JGE(R, EA)
        elif Opcode == '000100':
            self.execute_AMR(R, EA)
        elif Opcode == '000101':
            self.execute_SMR(R, EA)
        elif Opcode == '000110':
            self.execute_AIR(R, Address)
        elif Opcode == '000111':
            self.execute_SIR(R, Address)
        elif Opcode == '999997':#完成
            self.execute_MLT(R, IX)
        elif Opcode == '999996':#完成
            self.execute_DVD(R, IX)
        elif Opcode == '010010':#完成
            self.execute_TRR(R, IX)
        elif Opcode == '010011':#完成
            self.execute_AND(R, IX)
        elif Opcode == '010100':#完成
            self.execute_ORR(R, IX)
        elif Opcode == '010101':#完成
            self.execute_NOT(R)
        elif Opcode == '011001':#完成
            self.execute_SRC(R, A_L, L_R, count)
        elif Opcode == '011010':#完成
            self.execute_RRC(R, A_L, L_R, count)
        elif Opcode == '110001':#完成
            self.execute_IN(R, Address)
        elif Opcode == '110010':#完成
            self.__output = self.execute_OUT(R, Address)
        elif Opcode == '110011':#完成
            self.execute_CHK(R, Address)
        self.__MAR.setValue(self.convert_binary_to_decimal(Address))
        self.__MBR.setValue(self.__memory.getValue(self.__MAR.getValue()))
        self.__IR.setValue(self.convert_binary_to_decimal(instruction))

    def getEA(self, IX: str, I: str, Address: str) -> int:
        if IX == '00':
            EA = int(Address, 2)
        else:
            EA = self.get_IXR_content(IX) + int(Address, 2)
        if I == '1':
            EA = (self.__memory.getValue(EA))
        return EA

    def convert_binary_to_decimal(self, binary: str) -> int:
        return int(binary, 2)

    def convert_decimal_to_binary(self, integer: int) -> str:
        return bin(integer)[2:].zfill(16)

    def get_GPR_content(self, R: str) -> int:
        if R == '00':
            GPR_value = self.__GPR0.getValue()
        elif R == '01':
            GPR_value = self.__GPR1.getValue()
        elif R == '10':
            GPR_value = self.__GPR2.getValue()
        else:
            GPR_value = self.__GPR3.getValue()
        return GPR_value

    def set_GPR_content(self, R: str, GPR_value: int):
        if R == '00':
            self.__GPR0.setValue(GPR_value)
        elif R == '01':
            self.__GPR1.setValue(GPR_value)
        elif R == '10':
            self.__GPR2.setValue(GPR_value)
        else:
            self.__GPR3.setValue(GPR_value)

    def get_IXR_content(self, IX: str) -> int:
        IXR_value = 0
        if IX == '01':
            IXR_value = self.__IXR1.getValue()
        elif IX == '10':
            IXR_value = self.__IXR2.getValue()
        elif IX == '11':
            IXR_value = self.__IXR3.getValue()
        return IXR_value

    def set_IXR_content(self, IX: str, IXR_value: int):
        if IX == '01':
            self.__IXR1.setValue(IXR_value)
        elif IX == '10':
            self.__IXR2.setValue(IXR_value)
        elif IX == '11':
            self.__IXR3.setValue(IXR_value)

    def setInput(self, input: int):
        self.__input = input

    def execute_LDR(self, R: str, EA: int):  # LDR
        self.set_GPR_content(R, self.__memory.getValue(EA))

    def execute_STR(self, R: str, EA: int):
        self.__memory.setValue(EA, self.get_GPR_content(R))

    def execute_LDA(self, R: str, EA: int):
        self.set_GPR_content(R, EA)

    def execute_LDX(self, IX: str, EA: int):
        self.set_IXR_content(IX, self.__memory.getValue(EA))

    def execute_STX(self, IX: str, EA: int):
        self.__memory.setValue(EA, self.get_IXR_content(IX))

    def execute_JZ(self, R: str, EA: int):
        GPR_value = self.get_GPR_content(R)
        if GPR_value == 0:
            self.__PC.setValue(EA)
        else:
            self.__PC.pc_plus_one()

    def execute_JNE(self, R: str, EA: int):
        GPR_value = self.get_GPR_content(R)
        if GPR_value != 0:
            self.__PC.setValue(EA)
        else:
            self.__PC.pc_plus_one()

    def execute_JCC(self, cc: str, EA: int):
        bit = int(cc, 2)
        if self.__conditioncode.judgeCCBit(bit):
            self.__PC.setValue(EA)
        else:
            self.__PC.pc_plus_one()

    def execute_JMA(self, EA: int):
        self.__PC.setValue(EA)

    def execute_JSR(self, EA: int):
        self.__GPR3.setValue(self.__PC.pc_plus_one())
        self.__PC.setValue(EA)
    #
    # def execute_RFS(self, immed: str):
    #     self.set_GPR_content('0',immed.zfill(16))
    #     self.PC_content['text'] = self.GPR3_content.cget('text')[:12]

    def execute_SOB(self, R: str, EA: int):
        self.set_GPR_content(R, self.get_GPR_content(R) - 1)
        if self.get_GPR_content(R) > 0:
            self.__PC.setValue(EA)
        else:
            self.__PC.pc_plus_one()

    def execute_JGE(self, R: str, EA: int):
        if self.get_GPR_content(R) >= 0:
            self.__PC.setValue(EA)
        else:
            self.__PC.pc_plus_one()

    def execute_AMR(self, R: str, EA: int):
        self.set_GPR_content(R, self.get_GPR_content(R) + self.__memory.getValue(EA))

    def execute_SMR(self, R: str, EA: int):
        print(R)

        self.set_GPR_content(R, self.get_GPR_content(R) - self.__memory.getValue(EA))
        print(self.get_GPR_content(R) - self.__memory.getValue(EA))

    def execute_AIR(self, R: str, Address: str):
        immed = self.convert_binary_to_decimal(Address)
        self.set_GPR_content(R, self.get_GPR_content(R) + immed)

    def execute_SIR(self, R: str, Address: str):
        immed = self.convert_binary_to_decimal(Address)
        self.set_GPR_content(R, self.get_GPR_content(R) - immed)

        # def execute_MLT(self, R, IX):
        #     if R == '00' or R == '10' or IX == '00' or IX == '10':
        #         print("jinlaile", R, IX)
        #         GPR_value1 = self.get_GPR_content(R)
        #         GPR_value2 = self.get_GPR_content(IX)
        #         ac = self.convert_binary_to_decimal(GPR_value1)
        #         bc = self.convert_binary_to_decimal(GPR_value2)
        #         Multiply_result = ac * bc
        #         print(Multiply_result)
        #         if Multiply_result > 65535:
        #             self.set_CC(1,2,2,2)
        #         else:
        #             Multiply_result_binary = self.convert_decimal_to_binary(Multiply_result)
        #             Multiply_result_binary = Multiply_result_binary.zfill(16)
        #             High_order_bit = Multiply_result_binary[:8] + '00000000'
        #             Lower_order_bit = Multiply_result_binary[8:].zfill(16)
        #             if a == 0:
        #                 print(111)
        #                 self.GPR0_content['text'] = High_order_bit
        #                 self.GPR1_content['text'] = Lower_order_bit
        #             elif a == 2:
        #                 print(222)
        #                 print(High_order_bit)
        #                 print(Lower_order_bit)
        #                 self.GPR2_content['text'] = High_order_bit
        #                 self.GPR3_content['text'] = Lower_order_bit
        #
        #
        # def execute_DVD(self, R, IX):
        #     GPR_value = self.get_GPR_content(R)
        #     ac = self.convert_binary_to_decimal(GPR_value)
        #     b = self.convert_binary_to_decimal(IX)
        #     if b == 1:
        #         IX_value = self.IXR1_content.cget('text')
        #     elif b == 2:
        #         IX_value = self.IXR2_content.cget('text')
        #     elif b == 3:
        #         IX_value = self.IXR3_content.cget('text')
        #     bc = self.convert_binary_to_decimal(IX_value)
        #     if bc == 0:
        #         self.Set_CC(2, 2, 1, 2)
        #     else:
        #         Quotient, Reminder = self.Divide(ac, bc)
        #         print(ac, b, Quotient, Reminder)
        #         Quotient_binary = self.convert_decimal_to_binary(Quotient)
        #         Quotient_binary = Quotient_binary.zfill(16)
        #         Reminder_binary = self.convert_decimal_to_binary(Reminder)
        #         Reminder_binary = Reminder_binary.zfill(16)
        #         if a == 0:
        #             self.GPR0_content['text'] = Quotient_binary
        #             self.GPR1_content['text'] = Reminder_binary
        #         elif a == 1:
        #             self.GPR1_content['text'] = Quotient_binary
        #             self.GPR2_content['text'] = Reminder_binary
        #         elif a == 2:
        #             self.GPR2_content['text'] = Quotient_binary
        #             self.GPR3_content['text'] = Reminder_binary
        #         elif a == 3:
        #             self.GPR3_content['text'] = Quotient_binary
        #             self.GPR0_content['text'] = Reminder_binary

    def execute_TRR(self, rx: str, ry: str):
        rx_value = self.get_GPR_content(rx)
        ry_value = self.get_GPR_content(ry)
        if rx_value == ry_value:
            self.__conditioncode.setCCByIndex(3, "1")
        else:
            self.__conditioncode.setCCByIndex(3, "0")

    def execute_AND(self, rx: str, ry: str):
        rx_value = self.convert_decimal_to_binary(self.get_GPR_content(rx))
        ry_value = self.convert_decimal_to_binary(self.get_GPR_content(ry))
        ans = ''
        for i in range(len(rx_value)):
            if rx_value[i] == '1' and ry_value[i] == '1':
                ans += '1'
            else:
                ans += '0'
        self.set_GPR_content(rx, self.convert_binary_to_decimal(ans))

    def execute_ORR(self, rx: str, ry: str):
        rx_value = self.convert_decimal_to_binary(self.get_GPR_content(rx))
        ry_value = self.convert_decimal_to_binary(self.get_GPR_content(ry))
        ans = ''
        for i in range(len(rx_value)):
            if rx_value[i] == '1' or ry_value[i] == '1':
                ans += '1'
            else:
                ans += '0'
        self.set_GPR_content(rx, self.convert_binary_to_decimal(ans))

    def execute_NOT(self, rx: str):
        rx_value = self.convert_decimal_to_binary(self.get_GPR_content(rx))
        ans = ''
        for i in range(len(rx_value)):
            if rx_value[i] == '1':
                ans += '0'
            else:
                ans += '1'
        self.set_GPR_content(rx, self.convert_binary_to_decimal(ans))

    def execute_SRC(self, R: str, A_L: str, L_R: str, count: str):
        GPR_value= self.convert_decimal_to_binary(self.get_GPR_content(R))
        count_int = int(count, 2)
        if A_L == '1' and L_R == '1':
            GPR_value = GPR_value[count_int:]
            for i in range(count_int):
                GPR_value += '0'
            self.set_GPR_content(R, self.convert_binary_to_decimal(GPR_value))
        elif A_L == '1' and L_R == '0':
            GPR_value = GPR_value[:len(GPR_value) - count_int]
            for i in range(count_int):
                GPR_value = '0' + GPR_value
            self.set_GPR_content(R, self.convert_binary_to_decimal(GPR_value))
        elif A_L == '0' and L_R == '1':
            GPR_value = GPR_value[count_int:]
            for i in range(count_int):
                GPR_value += '0'
            self.set_GPR_content(R, self.convert_binary_to_decimal(GPR_value))
        else:
            if GPR_value[0] == '1':
                GPR_value = GPR_value[:len(GPR_value) - count_int]
                for i in range(count_int):
                    GPR_value = '1' + GPR_value
                self.set_GPR_content(R, self.convert_binary_to_decimal(GPR_value))
            else:
                GPR_value = GPR_value[:len(GPR_value) - count_int]
                for i in range(count_int):
                    GPR_value = '0' + GPR_value
                self.set_GPR_content(R, self.convert_binary_to_decimal(GPR_value))

    def execute_RRC(self, R: str, A_L: str, L_R: str, count: str):
        GPR_value = self.convert_decimal_to_binary(self.get_GPR_content(R))
        count_int = int(count, 2)
        if A_L == '1' and L_R == '1':
            GPR_value = GPR_value[count_int:] + GPR_value[:count_int]
            self.set_GPR_content(R, self.convert_binary_to_decimal(GPR_value))
        elif A_L == '1' and L_R == '0':
            GPR_value = GPR_value[len(GPR_value) - count_int:] + GPR_value[:len(GPR_value) - count_int]
            self.set_GPR_content(R, self.convert_binary_to_decimal(GPR_value))

    def execute_IN(self, R: str, address: str):
        if address == '00000':
            self.set_GPR_content(R, self.__input)

    def execute_OUT(self, R: str, address: str) -> int:
        if address == '00001':
            return self.get_GPR_content(R)

    def execute_CHK(self, R: str, address: str) -> bool:
        return True