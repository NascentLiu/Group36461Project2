import tkinter.filedialog
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

class App(Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title("GUI")
        self.geometry('900x400')
        # Initialize all Windows and buttons
        R = Label(self, text="")
        R.grid(row=0, column=1)
        R = Label(self, text="")
        R.grid(row=0, column=5)
        R = Label(self, text="")
        R.grid(row=0, column=7)
        R = Label(self, text="")
        R.grid(row=0, column=8)
        R = Label(self, text="")
        R.grid(row=0, column=9)
        R = Label(self, text="")
        R.grid(row=0, column=10)
        R = Label(self, text="")
        R.grid(row=0, column=11)
        R = Label(self, text="")
        R.grid(row=0, column=12)
        R = Label(self, text="")
        R.grid(row=0, column=13)
        R = Label(self, text="")
        R.grid(row=0, column=14)
        R = Label(self, text="")
        R.grid(row=0, column=15)
        R = Label(self, text="")
        R.grid(row=0, column=16)
        R = Label(self, text="")
        R.grid(row=0, column=17)
        R = Label(self, text="")
        R.grid(row=0, column=18)
        R = Label(self, text="")
        R.grid(row=0, column=19)
        R = Label(self, text="")
        R.grid(row=0, column=20)
        A = Label(self)

        self.GPR0 = Label(self, text="GPR0")
        self.GPR0.grid(row=5, column=0)
        self.GPR0_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR0_content.grid(row=5, column=1)
        self.button_GPR0 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(1))
        self.button_GPR0.grid(row=5, column=2)

        self.GPR1 = Label(self, text="GPR1")
        self.GPR1.grid(row=6, column=0)
        self.GPR1_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR1_content.grid(row=6, column=1)
        self.button_GPR1 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(2))
        self.button_GPR1.grid(row=6, column=2)

        self.GPR2 = Label(self, text="GPR2")
        self.GPR2.grid(row=7, column=0)
        self.GPR2_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR2_content.grid(row=7, column=1)
        self.button_GPR2 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(3))
        self.button_GPR2.grid(row=7, column=2)

        self.GPR3 = Label(self, text="GPR3")
        self.GPR3.grid(row=8, column=0)
        self.GPR3_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR3_content.grid(row=8, column=1)
        self.button_GPR3 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(4))
        self.button_GPR3.grid(row=8, column=2)

        self.IXR1 = Label(self, text="IXR1")
        self.IXR1.grid(row=10, column=0)
        self.IXR1_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.IXR1_content.grid(row=10, column=1)
        self.button_IXR1 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(5))
        self.button_IXR1.grid(row=10, column=2)

        self.IXR2 = Label(self, text="IXR2")
        self.IXR2.grid(row=11, column=0)
        self.IXR2_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.IXR2_content.grid(row=11, column=1)
        self.button_IXR2 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(6))
        self.button_IXR2.grid(row=11, column=2)

        self.IXR3 = Label(self, text="IXR3")
        self.IXR3.grid(row=12, column=0)
        self.IXR3_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.IXR3_content.grid(row=12, column=1)
        self.button_IXR3 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(7))
        self.button_IXR3.grid(row=12, column=2)

        self.button_Operation1 = Button(self, text="0", command=lambda: self.Switch(1))
        self.button_Operation1.grid(row=14, column=1)
        self.button_Operation1.place(x=10, y=290)
        self.button_Operation2 = Button(self, text="0", command=lambda: self.Switch(2))
        self.button_Operation2.grid(row=14, column=2)
        self.button_Operation2.place(x=52, y=290)
        self.button_Operation3 = Button(self, text="0", command=lambda: self.Switch(3))
        self.button_Operation3.grid(row=14, column=3)
        self.button_Operation3.place(x=94, y=290)
        self.button_Operation4 = Button(self, text="0", command=lambda: self.Switch(4))
        self.button_Operation4.grid(row=14, column=4)
        self.button_Operation4.place(x=136, y=290)
        self.button_Operation5 = Button(self, text="0", command=lambda: self.Switch(5))
        self.button_Operation5.grid(row=14, column=5)
        self.button_Operation5.place(x=178, y=290)
        self.button_Operation6 = Button(self, text="0", command=lambda: self.Switch(6))
        self.button_Operation6.grid(row=14, column=1)
        self.button_Operation6.place(x=220, y=290)
        self.Operation_display = Label(self, text="Operation")
        self.Operation_display.grid(row=15, column=1)
        self.Operation_display.place(x=90, y=320)

        self.button_GPR1 = Button(self, text="0", command=lambda: self.Switch(7))
        self.button_GPR1.grid(row=14, column=6)
        self.button_GPR1.place(x=278, y=290)
        self.button_GPR2 = Button(self, text="0", command=lambda: self.Switch(8))
        self.button_GPR2.grid(row=14, column=7)
        self.button_GPR2.place(x=320, y=290)
        self.GPR_display = Label(self, text="GPR")
        self.GPR_display.grid(row=15, column=2)
        self.GPR_display.place(x=300, y=320)

        self.button_IXR1 = Button(self, text="0", command=lambda: self.Switch(9))
        self.button_IXR1.grid(row=14, column=8)
        self.button_IXR1.place(x=372, y=290)
        self.button_IXR2 = Button(self, text="0", command=lambda: self.Switch(10))
        self.button_IXR2.grid(row=14, column=9)
        self.button_IXR2.place(x=414, y=290)
        self.IXR_display = Label(self, text="IXR")
        self.IXR_display.grid(row=15, column=3)
        self.IXR_display.place(x=400, y=320)

        self.button_I1 = Button(self, text="0", command=lambda: self.Switch(11))
        self.button_I1.grid(row=14, column=10)
        self.button_I1.place(x=466, y=290)
        self.I_display = Label(self, text="I")
        self.I_display.grid(row=15, column=4)
        self.I_display.place(x=482, y=320)

        self.button_Address1 = Button(self, text="0", command=lambda: self.Switch(12))
        self.button_Address1.grid(row=14, column=11)
        self.button_Address1.place(x=518, y=290)
        self.button_Address2 = Button(self, text="0", command=lambda: self.Switch(13))
        self.button_Address2.grid(row=14, column=12)
        self.button_Address2.place(x=560, y=290)
        self.button_Address3 = Button(self, text="0", command=lambda: self.Switch(14))
        self.button_Address3.grid(row=14, column=13)
        self.button_Address3.place(x=602, y=290)
        self.button_Address4 = Button(self, text="0", command=lambda: self.Switch(15))
        self.button_Address4.grid(row=14, column=14)
        self.button_Address4.place(x=644, y=290)
        self.button_Address5 = Button(self, text="0", command=lambda: self.Switch(16))
        self.button_Address5.grid(row=14, column=15)
        self.button_Address5.place(x=686, y=290)
        self.Address_display = Label(self, text="Address")
        self.Address_display.grid(row=15, column=5)
        self.Address_display.place(x=580, y=320)
        #right side buttons
        self.PC_display = Label(self, text="PC")
        self.PC_display.grid(row=5, column=20)
        self.PC_content = Label(self, width=25, bg="white", text="000000000000")
        self.PC_content.grid(row=5, column=21)
        self.button_PC = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(8))
        self.button_PC.grid(row=5, column=22)

        self.MAR_display = Label(self, text="MAR")
        self.MAR_display.grid(row=6, column=20)
        self.MAR_content = Label(self, width=25, bg="white", text="000000000000")
        self.MAR_content.grid(row=6, column=21)
        self.button_MAR = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(9))
        self.button_MAR.grid(row=6, column=22)

        self.MBR_display = Label(self, text="MBR")
        self.MBR_display.grid(row=7, column=20)
        self.MBR_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.MBR_content.grid(row=7, column=21)
        self.button_MBR = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(10))
        self.button_MBR.grid(row=7, column=22)

        self.IR = Label(self, text="IR")
        self.IR.grid(row=8, column=20)
        self.IR_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.IR_content.grid(row=8, column=21)

        self.MFR = Label(self, text="MFR")
        self.MFR.grid(row=9, column=20)
        self.MFR_content = Label(self, bg="white", text="0000")
        self.MFR_content.grid(row=9, column=21)

        self.Privileged = Label(self, text="Privileged")
        self.Privileged.grid(row=10, column=20)
        self.Privileged_content = Label(self, width=2, bg="white", text="")
        self.Privileged_content.grid(row=10, column=21)


        self.CC_display = Label(self, text="CC")
        self.CC_display.grid(row=10, column=22)
        self.CC_content = Label(self, width=5, bg="white", text="0000")
        self.CC_content.grid(row=10, column=23)

        self.button_Store = Button(self, text="Store", padx=5, pady=5, command=lambda: self.LD(11))
        self.button_Store.grid(row=13, column=20)
        self.button_Store.place(x=490, y=200)
        self.button_St = Button(self, text="St+", padx=5, pady=5, command=lambda: self.LD(12))
        self.button_St.grid(row=13, column=22)
        self.button_St.place(x=580, y=200)
        self.button_Load = Button(self, text="Load", padx=5, pady=5, command=lambda: self.LD(13))
        self.button_Load.grid(row=13, column=24)
        self.button_Load.place(x=670, y=200)
        self.button_Init = Button(self, text="Init", padx=5, pady=5, command=lambda: self.LD(14))
        self.button_Init.grid(row=13, column=26)
        self.button_Init.place(x=760, y=200)
        self.button_console = Button(self, text="Console", padx=5, pady=5, command=lambda: self.LD(17))
        self.button_console.grid(row=15, column=20)
        self.button_console.place(x=350, y=240)
        self.button_SS = Button(self, text="SS", padx=3, pady=3, command=lambda: self.LD(15))
        self.button_SS.grid(row=15, column=21)
        self.button_SS.place(x=500, y=240)
        self.button_Run = Button(self, text="Run", padx=3, pady=3, command=lambda: self.LD(16))
        self.button_Run.grid(row=15, column=23)
        self.button_Run.place(x=570, y=240)

        self.Halt_content = Label(self, width=2, bg="white", text="")
        self.Halt_content.grid(row=17, column=21)
        self.Halt_content.place(x=680, y=240)
        self.Halt = Label(self, text="Halt")
        self.Halt.grid(row=17, column=22)
        self.Halt.place(x=700, y=240)
        self.Run_content = Label(self, width=2, bg="white", text="")
        self.Run_content.grid(row=17, column=24)
        self.Run_content.place(x=770, y=240)
        self.Run_label = Label(self, text="Run")
        self.Run_label.grid(row=17, column=25)
        self.Run_label.place(x=790, y=240)

        self.GPR0_value = '0000000000000000'
        self.GPR1_value = '0000000000000000'
        self.GPR2_value = '0000000000000000'
        self.GPR3_value = '0000000000000000'
        self.IXR1_value = '0000000000000000'
        self.IXR2_value = '0000000000000000'
        self.IXR3_value = '0000000000000000'
        self.memory = ['0000000000000000'] * 4096
        self.L_long = 0
        self.L_short = 0
        self.PC_next = 0


    #judge which button is clicked
    def get_value(self, number_LD):
        if number_LD == 1:
            self.GPR0_content['text'] = self.L_long
        elif number_LD == 2:
            self.GPR1_content['text'] = self.L_long
        elif number_LD == 3:
            self.GPR2_content['text'] = self.L_long
        elif number_LD == 4:
            self.GPR3_content['text'] = self.L_long
        elif number_LD == 5:
            self.IXR1_content['text'] = self.L_long
        elif number_LD == 6:
            self.IXR2_content['text'] = self.L_long
        elif number_LD == 7:
            self.IXR3_content['text'] = self.L_long
        elif number_LD == 8:
            self.PC_content['text'] = self.L_short
        elif number_LD == 9:
            self.MAR_content['text'] = self.L_short
        elif number_LD == 10:
            self.MBR_content['text'] = self.L_long
        elif number_LD == 11:
            MAR_value = self.convert_binary_to_decimal(self.MAR_content.cget('text'))
            MBR_value = self.MBR_content.cget('text')
            self.memory[MAR_value] = MBR_value
        elif number_LD == 12:
            MAR_value = self.convert_binary_to_decimal(self.MAR_content.cget('text'))
            MBR_value = self.MBR_content.cget('text')
            self.memory[MAR_value] = MBR_value
            MAR_value = MAR_value + 1
            self.MAR_content['text'] = self.convert_decimal_to_binary(MAR_value).zfill(12)
        elif number_LD == 13:
            MAR_value = self.convert_binary_to_decimal(self.MAR_content.cget('text'))
            self.MBR_content['text'] = self.memory[MAR_value]
        elif number_LD == 14:
            self.GPR0_content['text'] = "0000000000000000"
            self.GPR1_content['text'] = "0000000000000000"
            self.GPR2_content['text'] = "0000000000000000"
            self.GPR3_content['text'] = "0000000000000000"
            self.IXR1_content['text'] = "0000000000000000"
            self.IXR2_content['text'] = "0000000000000000"
            self.IXR3_content['text'] = "0000000000000000"
            self.PC_content['text'] = "000000001000"
            self.MAR_content['text'] = "000000000000"
            self.MBR_content['text'] = "0000000000000000"
            self.IR_content['text'] = "0000000000000000"
            self.Run_content['bg'] = "white"
            self.Halt_content['bg'] = "white"
            self.MFR_content['bg'] = "white"
            self.Privileged_content['bg'] ="white"
            self.load_file("IPL.txt")
        elif number_LD == 15:
            PC_value = self.PC_content.cget("text")
            jj = self.convert_binary_to_decimal(PC_value.zfill(12))#MAR_value
            PC_value = self.convert_decimal_to_binary(self.convert_binary_to_decimal(PC_value) + 1)
            self.PC_content['text'] = PC_value.zfill(12)
            self.instruction_controller(self.memory[jj])

        elif number_LD == 16:
            for iii in range(15):
                if self.PC_next < 14:
                    PC_value = self.PC_content.cget("text")
                    jj = self.convert_binary_to_decimal(PC_value.zfill(12))  # MAR_value
                    PC_value = self.convert_decimal_to_binary(self.convert_binary_to_decimal(PC_value) + 1)
                    self.instruction_controller(self.memory[jj])
                    self.PC_content['text'] = PC_value.zfill(12)
                    self.Halt_content['bg'] = "red"
                else:
                    self.Run_content['bg'] = "white"


        elif number_LD == 17:
            for abccc in range(0, 4095, 4):
                print("Address", abccc, ":", "value:", self.memory[abccc],"Address", abccc+1, ":", "value:", self.memory[abccc+1],"Address", abccc+2, ":", "value:", self.memory[abccc+2],"Address", abccc+3, ":", "value:", self.memory[abccc+3])

    #get the value of 16 binary buttons
    def LD(self, number_LD):
        L1 = self.button_Operation1.cget("text")
        L2 = self.button_Operation2.cget("text")
        L3 = self.button_Operation3.cget("text")
        L4 = self.button_Operation4.cget("text")
        L5 = self.button_Operation5.cget("text")
        L6 = self.button_Operation6.cget("text")
        L7 = self.button_GPR1.cget("text")
        L8 = self.button_GPR2.cget("text")
        L9 = self.button_IXR1.cget("text")
        L10 = self.button_IXR2.cget("text")
        L11 = self.button_I1.cget("text")
        L12 = self.button_Address1.cget("text")
        L13 = self.button_Address2.cget("text")
        L14 = self.button_Address3.cget("text")
        L15 = self.button_Address4.cget("text")
        L16 = self.button_Address5.cget("text")
        self.L_long = f"{L1}{L2}{L3}{L4}{L5}{L6}{L7}{L8}{L9}{L10}{L11}{L12}{L13}{L14}{L15}{L16}"
        self.L_short = f"{L5}{L6}{L7}{L8}{L9}{L10}{L11}{L12}{L13}{L14}{L15}{L16}"
        self.get_value(number_LD)



    def Switch(self, number):
        if number == 1:
            self.button_Operation1['text'] = 1 - int(self.button_Operation1.cget("text"));
        elif number == 2:
            self.button_Operation2['text'] = 1 - int(self.button_Operation2.cget("text"));
        elif number == 3:
            self.button_Operation3['text'] = 1 - int(self.button_Operation3.cget("text"));
        elif number == 4:
            self.button_Operation4['text'] = 1 - int(self.button_Operation4.cget("text"));
        elif number == 5:
            self.button_Operation5['text'] = 1 - int(self.button_Operation5.cget("text"));
        elif number == 6:
            self.button_Operation6['text'] = 1 - int(self.button_Operation6.cget("text"));
        elif number == 7:
            self.button_GPR1['text'] = 1 - int(self.button_GPR1.cget("text"));
        elif number == 8:
            self.button_GPR2['text'] = 1 - int(self.button_GPR2.cget("text"));
        elif number == 9:
            self.button_IXR1['text'] = 1 - int(self.button_IXR1.cget("text"));
        elif number == 10:
            self.button_IXR2['text'] = 1 - int(self.button_IXR2.cget("text"));
        elif number == 11:
            self.button_I1['text'] = 1 - int(self.button_I1.cget("text"));
        elif number == 12:
            self.button_Address1['text'] = 1 - int(self.button_Address1.cget("text"));
        elif number == 13:
            self.button_Address2['text'] = 1 - int(self.button_Address2.cget("text"));
        elif number == 14:
            self.button_Address3['text'] = 1 - int(self.button_Address3.cget("text"));
        elif number == 15:
            self.button_Address4['text'] = 1 - int(self.button_Address4.cget("text"));
        elif number == 16:
            self.button_Address5['text'] = 1 - int(self.button_Address5.cget("text"));

    #back-end
    def instruction_controller(self, instruction: str):
        Opcode = instruction[:6]
        R = instruction[6:8]
        IX = instruction[8:10]
        I = instruction[10]
        Address = instruction[11:]
        Count = self.convert_binary_to_decimal(instruction[12:])
        AL = self.convert_binary_to_decimal(instruction[8])
        LR = self.convert_binary_to_decimal(instruction[9])
        print("Count,LR, AL",Count,LR, AL)
        EA = self.getEA(IX, I, Address)
        print(Opcode, R, IX, I, Address)
        if Opcode == '000000':
            Halt_content = Label(self, width=2, bg="red", text="")
            Halt_content.grid(row=17, column=21)
            Halt_content.place(x=680, y=240)
        elif Opcode == '000001':
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
        elif Opcode == '000100':
            self.execute_AMR(R, EA)
        elif Opcode == '000101':
            self.execute_SMR(R, EA)
        elif Opcode == '000110':
            self.execute_AIR(R, Address)
        elif Opcode == '000111':
            self.execute_SIR(R, Address)
        elif Opcode == '001000':#完成
            self.execute_JZ(R, EA)
        elif Opcode == '001001':#完成
            self.execute_JNE(R, EA)
        elif Opcode == '001010':#完成
            self.execute_JCC(R, EA)
        elif Opcode == '001011':#完成
            self.execute_JMA(EA)
        elif Opcode == '001100':#不知道argument是啥
            self.execute_JSR(EA)
        elif Opcode == '001101':
            self.execute_RFS(Address)
        elif Opcode == '001110':#完成
            self.execute_SOB(R, EA)
        elif Opcode == '001111':#完成
            self.execute_JGE(R, EA)
        elif Opcode == '010000':#完成
            self.execute_MLT(R, IX)
        elif Opcode == '010001':#完成
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
            self.execute_SRC(R, Count, LR)
        elif Opcode == '011010':#完成
            self.execute_RRC(R, Count, LR, AL)
        elif Opcode == '110001':#完成
            self.execute_IN(R, Address)
        elif Opcode == '110010':#完成
            self.execute_OUT(R, Address)
        elif Opcode == '110011':#完成
            self.execute_CHK(R, Address)
        self.MAR_content['text'] = Address.zfill(12)
        self.MAR_value = self.MAR_content.cget('text')
        cc = self.convert_binary_to_decimal(self.MAR_value)
        dd = self.memory[cc]
        self.MBR_content['text'] = dd
        self.IR_content['text'] = instruction


    def getEA(self, IX: str, I: str, Address: str) -> int:
        EA = 0
        if IX == '00':
            EA = self.convert_binary_to_decimal(Address)
        else:
            EA = self.get_content_from_IX(IX) + self.convert_binary_to_decimal(Address)
        if I == '1':
            if self.memory[EA] != None:
                EA_possible = self.convert_binary_to_decimal(self.memory[EA])
                if EA_possible <= 4095:
                    EA = EA_possible
        return EA


    def get_content_from_IX(self, IX: str) -> int:
        IXR_value, a = self.get_IXR_content(IX)
        IX_decimal = self.convert_binary_to_decimal(IXR_value)
        return IX_decimal


    def convert_binary_to_decimal(self, binary: str) -> int:
        return int(binary, 2)


    def convert_decimal_to_binary(self, integer: int) -> str:
        return bin(integer)[2:]

    def execute_LDR(self, R: str, EA: int):  # LDR
        GPR_value = self.memory[EA].zfill(16)
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR0_content['text'] = GPR_value
        elif a == 1:
            self.GPR1_content['text'] = GPR_value
        elif a == 2:
            self.GPR2_content['text'] = GPR_value
        elif a == 3:
            self.GPR3_content['text'] = GPR_value

    def execute_STR(self, R: str, EA: int):
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR0_value = self.GPR0_content.cget('text')
            self.memory[EA] = self.GPR0_value
        elif a == 1:
            self.GPR1_value = self.GPR1_content.cget('text')
            self.memory[EA] = self.GPR1_value
        elif a == 2:
            self.GPR2_value = self.GPR2_content.cget('text')
            self.memory[EA] = self.GPR2_value
        elif a == 3:
            self.GPR3_value = self.GPR3_content.cget('text')
            self.memory[EA] = self.GPR3_value


    def execute_LDA(self, R: str, EA: int):
        GPR_value = self.convert_decimal_to_binary(EA).zfill(16)
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR0_content['text'] = GPR_value
        elif a == 1:
            self.GPR1_content['text'] = GPR_value
        elif a == 2:
            self.GPR2_content['text'] = GPR_value
        elif a == 3:
            self.GPR3_content['text'] = GPR_value


    def execute_LDX(self, IX: str, EA: int):
        a = self.convert_binary_to_decimal(IX)
        IXR_value = self.memory[EA].zfill(16)
        if a == 1:
            self.IXR1_content['text'] = IXR_value
        elif a == 2:
            self.IXR2_content['text'] = IXR_value
        elif a == 3:
            self.IXR3_content['text'] = IXR_value

    def execute_STX(self, IX: str, EA: int):
        if IX == '01':
            self.IXR1_value = self.IXR1_content.cget('text')
            self.memory[EA] = self.IXR1_value
        elif IX == '10':
            self.IXR2_value = self.IXR2_content.cget('text')
            self.memory[EA] = self.IXR2_value
        elif IX == '11':
            self.IXR3_value = self.IXR3_content.cget('text')
            self.memory[EA] = self.IXR3_value

    def execute_AMR(self, R: str, EA: int):
        if R == '00':
            self.GPR0_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR0_content.cget('text')) +
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)
        elif R == '01':
            self.GPR1_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR1_content.cget('text')) +
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)
        elif R == '10':
            self.GPR2_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR2_content.cget('text')) +
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)
        else:
            self.GPR3_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR3_content.cget('text')) +
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)

    def execute_SMR(self, R: str, EA: int):
        if R == '00':
            self.GPR0_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR0_content.cget('text')) -
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)
        elif R == '01':
            self.GPR1_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR1_content.cget('text')) -
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)
        elif R == '10':
            self.GPR2_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR2_content.cget('text')) -
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)
        else:
            self.GPR3_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR3_content.cget('text')) -
                self.convert_binary_to_decimal(self.memory[EA])).zfill(16)

    def execute_AIR(self, R: str, Address: str):
        immed = self.convert_binary_to_decimal(Address)
        if R == '00':
            self.GPR0_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR0_content.cget('text')) + immed).zfill(16)
        elif R == '01':
            self.GPR1_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR1_content.cget('text')) + immed).zfill(16)
        elif R == '10':
            self.GPR2_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR2_content.cget('text')) + immed).zfill(16)
        else:
            self.GPR3_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR3_content.cget('text')) + immed).zfill(16)

    def execute_SIR(self, R: str, Address: str):
        immed = self.convert_binary_to_decimal(Address)
        if R == '00':
            self.GPR0_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR0_content.cget('text')) - immed).zfill(16)
        elif R == '01':
            self.GPR1_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR1_content.cget('text')) - immed).zfill(16)
        elif R == '10':
            self.GPR2_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR2_content.cget('text')) - immed).zfill(16)
        else:
            self.GPR3_content['text'] = self.convert_decimal_to_binary(
                self.convert_binary_to_decimal(self.GPR3_content.cget('text')) - immed).zfill(16)

    def load_file(self, file_name: str):
        # global location, instruction
        file_name = tkinter.filedialog.askopenfilename()
        with open(file_name) as file:
            # reading each line
            for line in file:
                words = line.split()
                # Convert to Integer
                location = int(words[0], base=16)
                # Convert hexadecimal to a binary string
                instruction = str(bin(int(words[1], base=16)))[2:].zfill(16)
                self.memory[location] = instruction


    def PC_plus_one (self):
        PC_value = self.PC_content.cget('text')
        PC_value = self.convert_decimal_to_binary(self.convert_binary_to_decimal(PC_value) + 1)
        self.PC_content['text'] = PC_value.zfill(12)

    def get_GPR_content(self, R):
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            GPR_value = self.GPR0_content.cget('text')
        elif a == 1:
            GPR_value = self.GPR1_content.cget('text')
        elif a == 2:
            GPR_value = self.GPR2_content.cget('text')
        elif a == 3:
            GPR_value = self.GPR3_content.cget('text')
        return GPR_value, a

    def set_GPR_content(self, R, GPR_value):
        a = self.convert_binary_to_decimal(R)
        GPR_value = GPR_value.zfill(16)
        if a == 0:
            self.GPR0_content['text'] = GPR_value
        elif a == 1:
            self.GPR1_content['text'] = GPR_value
        elif a == 2:
            self.GPR2_content['text'] = GPR_value
        elif a == 3:
            self.GPR3_content['text'] = GPR_value

    def get_IXR_content(self, IX):
        a = self.convert_binary_to_decimal(IX)
        if a == 1:
            IXR_value = self.IXR1_content.cget('text')
        elif a == 2:
            IXR_value = self.IXR2_content.cget('text')
        elif a == 3:
            IXR_value = self.IXR3_content.cget('text')
        return IXR_value, a

    def Set_CC(self, Overflow, Underflow, DivZero, EqualOrNot):
        CC_value_list = list(self.CC_content.cget('text'))
        print(Overflow, Underflow, DivZero, EqualOrNot)
        if Overflow == 1:
            CC_value_list[0] = '1'
        elif Overflow == 0:
            CC_value_list[0] = '0'
        if Underflow == 1:
            CC_value_list[1] = '1'
        elif Underflow == 0:
            CC_value_list[1] = '0'
        if DivZero == 1:
            CC_value_list[2] = '1'
        elif DivZero == 0:
            CC_value_list[2] = '0'
        if EqualOrNot == 1:
            CC_value_list[3] = '1'
        if EqualOrNot == 0:
            CC_value_list[3] = '0'
        print(type(CC_value_list),CC_value_list)
        CC_value = ''.join(CC_value_list)
        print(type(CC_value), CC_value)
        self.CC_content['text'] = CC_value

    def Divide(self, number_first, number_second):
        Quotient = number_first // number_second
        Reminder = number_first % number_second
        return Quotient, Reminder

    def execute_JZ(self, R: str, EA: int):
        print(EA, R)
        GPR_value, a = self.get_GPR_content(R)
        b = self.convert_binary_to_decimal(GPR_value)
        if b == 0:
            c = self.convert_decimal_to_binary(EA)
            self.PC_content['text'] = c.zfill(12);
            print("c:",c.zfill(12))
        else:
            self.PC_plus_one()
            print("PC_value:")

    def execute_JNE(self, R: str, EA: int):
        GPR_value, a = self.get_GPR_content(R)
        b = self.convert_binary_to_decimal(GPR_value)
        if b != 0:
            c = self.convert_decimal_to_binary(EA)
            self.PC_content['text'] = c.zfill(12)
        else:
            self.PC_plus_one()

    def execute_JCC(self, CC: str, address: int):
        a = self.convert_binary_to_decimal(CC)
        flag = 0
        if a == 0:
            if self.CC_value[0] == 1:
                flag = 1
        elif a == 1:
            if self.CC_value[1] == 1:
                flag = 1
        elif a == 2:
            if self.CC_value[2] == 1:
                flag = 1
        elif a == 3:
            if self.CC_value[3] == 1:
                flag = 1
        if flag == 1:
            self.PC_content['text'] = (self.convert_decimal_to_binary(address)).zfill(12)
        else:
            self.PC_plus_one()


    def execute_JMA(self, address):
        a = address
        c = self.convert_decimal_to_binary(a)
        self.PC_content['text'] = c.zfill(12)

    def execute_JSR(self, address):
        a = address + 1
        c = self.convert_decimal_to_binary(a)
        self.GPR3_content['text'] = c.zfill(16)
        b = self.convert_decimal_to_binary(address)
        self.PC_content['text'] = b.zfill(12)

    def execute_RFS(self, address):
        self.set_GPR_content('0',address.zfill(16))
        self.PC_content['text'] = self.GPR3_content.cget('text')[:12]

    def execute_SOB(self, R, address):
        GPR_value, a = self.get_GPR_content(R)
        b = self.convert_binary_to_decimal(GPR_value) - 1
        if b > 0:
            c = self.convert_decimal_to_binary(address)
            self.PC_content['text'] = c.zfill(12)
        else:
            self.PC_plus_one()

    def execute_JGE(self, R, address):
        GPR_value, a = self.get_GPR_content(R)
        b = self.convert_binary_to_decimal(GPR_value)
        if b >= 0:
            print(111111)
            c = self.convert_decimal_to_binary(address)
            self.PC_content['text'] = c.zfill(12)
        else:
            print(222222)
            self.PC_plus_one()

    def execute_MLT(self, R, IX):
        if R == '00' or R == '10' or IX == '00' or IX == '10':
            print("jinlaile", R, IX)
            GPR_value1, a = self.get_GPR_content(R)
            GPR_value2, b = self.get_GPR_content(IX)
            ac = self.convert_binary_to_decimal(GPR_value1)
            bc = self.convert_binary_to_decimal(GPR_value2)
            Multiply_result = ac * bc
            print(Multiply_result)
            if Multiply_result > 65535:
                self.Set_CC(1,2,2,2)
            else:
                Multiply_result_binary = self.convert_decimal_to_binary(Multiply_result)
                Multiply_result_binary = Multiply_result_binary.zfill(16)
                High_order_bit = Multiply_result_binary[:8] + '00000000'
                Lower_order_bit = Multiply_result_binary[8:].zfill(16)
                if a == 0:
                    print(111)
                    self.GPR0_content['text'] = High_order_bit
                    self.GPR1_content['text'] = Lower_order_bit
                elif a == 2:
                    print(222)
                    print(High_order_bit)
                    print(Lower_order_bit)
                    self.GPR2_content['text'] = High_order_bit
                    self.GPR3_content['text'] = Lower_order_bit


    def execute_DVD(self, R, IX):
        GPR_value, a = self.get_GPR_content(R)
        ac = self.convert_binary_to_decimal(GPR_value)
        b = self.convert_binary_to_decimal(IX)
        if b == 1:
            IX_value = self.IXR1_content.cget('text')
        elif b == 2:
            IX_value = self.IXR2_content.cget('text')
        elif b == 3:
            IX_value = self.IXR3_content.cget('text')
        bc = self.convert_binary_to_decimal(IX_value)
        if bc == 0:
            self.Set_CC(2, 2, 1, 2)
        else:
            Quotient, Reminder = self.Divide(ac, bc)
            print(ac, b, Quotient, Reminder)
            Quotient_binary = self.convert_decimal_to_binary(Quotient)
            Quotient_binary = Quotient_binary.zfill(16)
            Reminder_binary = self.convert_decimal_to_binary(Reminder)
            Reminder_binary = Reminder_binary.zfill(16)
            if a == 0:
                self.GPR0_content['text'] = Quotient_binary
                self.GPR1_content['text'] = Reminder_binary
            elif a == 1:
                self.GPR1_content['text'] = Quotient_binary
                self.GPR2_content['text'] = Reminder_binary
            elif a == 2:
                self.GPR2_content['text'] = Quotient_binary
                self.GPR3_content['text'] = Reminder_binary
            elif a == 3:
                self.GPR3_content['text'] = Quotient_binary
                self.GPR0_content['text'] = Reminder_binary

    def execute_TRR(self, R, IX):
        GPR_value, a = self.get_GPR_content(R)
        ac = self.convert_binary_to_decimal(GPR_value)
        b = self.convert_binary_to_decimal(IX)
        if b == 1:
            IX_value = self.IXR1_content.cget('text')
        elif b == 2:
            IX_value = self.IXR2_content.cget('text')
        elif b == 3:
            IX_value = self.IXR3_content.cget('text')
        bc = self.convert_binary_to_decimal(IX_value)
        if ac == bc:
            self.Set_CC(2, 2, 2, 1)
        else:
            self.Set_CC(2, 2, 2, 0)

    def execute_AND(self, EA, R, IX):
        GPR_value, a = self.get_GPR_content(R)
        b = self.convert_binary_to_decimal(IX)
        if b == 1:
            IXR_value = self.IXR1_content['text']
        elif b == 2:
            IXR_value = self.IXR2_content['text']
        elif b == 3:
            IXR_value = self.IXR3_content['text']
        new_rx = ''
        for i in range(16) :
            if GPR_value[i] == '1' and IXR_value[i] == '1':
                new_rx= new_rx+'1'
            else:
                new_rx= new_rx+'0'
        self.set_GPR_content(a, new_rx)

    def execute_ORR(self, R, IX):
        GPR_value, a = self.get_GPR_content(R)
        b = self.convert_binary_to_decimal(IX)
        if b == 1:
            IXR_value = self.IXR1_content['text']
        elif b == 2:
            IXR_value = self.IXR2_content['text']
        elif b == 3:
            IXR_value = self.IXR3_content['text']
        new_rx = ''
        for i in range(16):
            if GPR_value[i] == '1' or IXR_value[i] == '1':
                new_rx = new_rx + '1'
            else:
                new_rx = new_rx + '0'
        print("new_rx:" + new_rx)
        self.set_GPR_content(a, new_rx)

    def execute_NOT(self, R):
        GPR_value, a = self.get_GPR_content(R)
        new_rx = ''
        print("GPR" + GPR_value)
        for i in range(16):
            if GPR_value[i] == '1':
                new_rx = new_rx + '0'
            else:
                new_rx = new_rx + '1'
        print("~GPR" + new_rx)
        self.set_GPR_content(a, new_rx)

    def execute_SRC(self, R: str, Count: int, LR: int):
        GPR_value, a = self.get_GPR_content(R)
        if Count == 0:
            return
        if LR == 1:
            content_list = list(GPR_value[16 - Count:])
            for i in range(16 - Count):
                content_list.append('0')
            GPR_value = ''.join(content_list)
            self.set_GPR_content(R, GPR_value)
            print(1)
        elif LR == 0:
            print(2)
            self.set_GPR_content(R, GPR_value[:16 - Count].zfill(16))

    def execute_IN(self, R, address):
        answer = simpledialog.askinteger("Input", "please enter an integer")
        self.set_GPR_content(R, self.convert_decimal_to_binary(answer))

    def execute_OUT(self, R, address):
        GPR_value, a = self.get_GPR_content(R)
        messagebox.showinfo("Information", GPR_value)






if __name__ == "__main__":
    app = App()
    app.mainloop()