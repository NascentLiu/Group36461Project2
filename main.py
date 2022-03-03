import tkinter.filedialog
from tkinter import *


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

        GPR0 = Label(self, text="GPR0")
        GPR0.grid(row=5, column=0)
        self.GPR0_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR0_content.grid(row=5, column=1)
        self.button_GPR0 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(1))
        self.button_GPR0.grid(row=5, column=2)

        GPR1 = Label(self, text="GPR1")
        GPR1.grid(row=6, column=0)
        self.GPR1_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR1_content.grid(row=6, column=1)
        self.button_GPR1 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(2))
        self.button_GPR1.grid(row=6, column=2)

        GPR2 = Label(self, text="GPR2")
        GPR2.grid(row=7, column=0)
        self.GPR2_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR2_content.grid(row=7, column=1)
        self.button_GPR2 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(3))
        self.button_GPR2.grid(row=7, column=2)

        GPR3 = Label(self, text="GPR3")
        GPR3.grid(row=8, column=0)
        self.GPR3_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.GPR3_content.grid(row=8, column=1)
        self.button_GPR3 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(4))
        self.button_GPR3.grid(row=8, column=2)

        IXR1 = Label(self, text="IXR1")
        IXR1.grid(row=10, column=0)
        self.IXR1_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.IXR1_content.grid(row=10, column=1)
        self.button_IXR1 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(5))
        self.button_IXR1.grid(row=10, column=2)

        IXR2 = Label(self, text="IXR2")
        IXR2.grid(row=11, column=0)
        self.IXR2_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.IXR2_content.grid(row=11, column=1)
        self.button_IXR2 = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(6))
        self.button_IXR2.grid(row=11, column=2)

        IXR3 = Label(self, text="IXR3")
        IXR3.grid(row=12, column=0)
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
        IXR_display = Label(self, text="IXR")
        IXR_display.grid(row=15, column=3)
        IXR_display.place(x=400, y=320)

        self.button_I1 = Button(self, text="0", command=lambda: self.Switch(11))
        self.button_I1.grid(row=14, column=10)
        self.button_I1.place(x=466, y=290)
        I_display = Label(self, text="I")
        I_display.grid(row=15, column=4)
        I_display.place(x=482, y=320)

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
        Address_display = Label(self, text="Address")
        Address_display.grid(row=15, column=5)
        Address_display.place(x=580, y=320)
        #right side buttons
        PC_display = Label(self, text="PC")
        PC_display.grid(row=5, column=20)
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

        MBR_display = Label(self, text="MBR")
        MBR_display.grid(row=7, column=20)
        self.MBR_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.MBR_content.grid(row=7, column=21)
        self.button_MBR = Button(self, text="LD", padx=2, pady=2, command=lambda: self.LD(10))
        self.button_MBR.grid(row=7, column=22)

        IR = Label(self, text="IR")
        IR.grid(row=8, column=20)
        self.IR_content = Label(self, width=25, bg="white", text="0000000000000000")
        self.IR_content.grid(row=8, column=21)

        MFR = Label(self, text="MFR")
        MFR.grid(row=9, column=20)
        MFR_content = Label(self, bg="white", text="0000")
        MFR_content.grid(row=9, column=21)

        Privileged = Label(self, text="Privileged")
        Privileged.grid(row=10, column=20)
        Privileged_content = Label(self, width=2, bg="white", text="")
        Privileged_content.grid(row=10, column=21)

        CC_display = Label(self, text="CC")
        CC_display.grid(row=10, column=22)
        self.CC_content = Label(self, width=4, bg="white", text="0000")
        self.CC_content.grid(row=10, column=23)
        self.CC_value = self.CC_content.cget("text")

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

        Halt_content = Label(self, width=2, bg="white", text="")
        Halt_content.grid(row=17, column=21)
        Halt_content.place(x=680, y=240)
        Halt = Label(self, text="Halt")
        Halt.grid(row=17, column=22)
        Halt.place(x=700, y=240)
        Run_content = Label(self, width=2, bg="white", text="")
        Run_content.grid(row=17, column=24)
        Run_content.place(x=770, y=240)
        Run_label = Label(self, text="Run")
        Run_label.grid(row=17, column=25)
        Run_label.place(x=790, y=240)

        self.MAR = 4095
        self.GPR0_value = '0000000000000000'
        self.GPR1_value = '0000000000000000'
        self.GPR2_value = '0000000000000000'
        self.GPR3_value = '0000000000000000'
        self.IXR1_value = '0000000000000000'
        self.IXR2_value = '0000000000000000'
        self.IXR3_value = '0000000000000000'
        self.j = 0
        self.GPR0_value = None
        self.GPR1_value = None
        self.GPR2_value = None
        self.GPR3_value = None
        self.IXR1_value = None
        self.IXR2_value = None
        self.IXR3_value = None
        self.memory = ['0000000000000000'] * 4096


    #judge which button is clicked
    def get_value(self, number_LD):
        abccc = 0
        if number_LD == 1:
            self.GPR0_content = Label(self, width=25, bg="white", text=L_long)
            self.GPR0_content.grid(row=5, column=1)
            self.GPR0_value = self.GPR0_content.cget('text')
        elif number_LD == 2:
            self.GPR1_content = Label(self, width=25, bg="white", text=L_long)
            self.GPR1_content.grid(row=6, column=1)
            self.GPR1_value = self.GPR1_content.cget('text')
        elif number_LD == 3:
            self.GPR2_content = Label(self, width=25, bg="white", text=L_long)
            self.GPR2_content.grid(row=7, column=1)
            self.GPR2_value = self.GPR2_content.cget('text')
        elif number_LD == 4:
            self.GPR3_content = Label(self, width=25, bg="white", text=L_long)
            self.GPR3_content.grid(row=8, column=1)
            self.GPR3_value = self.GPR3_content.cget('text')
        elif number_LD == 5:
            self.IXR1_content = Label(self, width=25, bg="white", text=L_long)
            self.IXR1_content.grid(row=10, column=1)
            self.IXR1_value = self.IXR1_content.cget('text')
        elif number_LD == 6:
            self.IXR2_content = Label(self, width=25, bg="white", text=L_long)
            self.IXR2_content.grid(row=11, column=1)
            self.IXR2_value = self.IXR2_content.cget('text')
        elif number_LD == 7:
            self.IXR3_content = Label(self, width=25, bg="white", text=L_long)
            self.IXR3_content.grid(row=12, column=1)
            self.IXR3_value = self.IXR3_content.cget('text')
        elif number_LD == 8:
            self.PC_content = Label(self, width=25, bg="white", text=L_short)
            self.PC_content.grid(row=5, column=21)
            self.PC_value = self.PC_content.cget("text")
        elif number_LD == 9:
            self.MAR_content = Label(self, width=25, bg="white", text=L_short)
            self.MAR_value = L_short
            self.MAR_content.grid(row=6, column=21)
        elif number_LD == 10:
            self.MBR_value = L_long
            self.MBR_content = Label(self, width=25, bg="white", text=L_long)
            self.MBR_content.grid(row=7, column=21)
        elif number_LD == 11:
            self.MAR_value = self.MAR_content.cget('text')
            self.MAR = self.convert_binary_to_decimal(self.MAR_value)
            self.MBR_value = self.MBR_content.cget('text')
            self.memory[self.MAR] = self.MBR_value
        elif number_LD == 12:
            self.MAR_value = self.MAR_content.cget('text')
            self.MAR = self.convert_binary_to_decimal(self.MAR_value)
            self.MBR_value = self.MBR_content.cget('text')
            self.memory[self.MAR] = self.MBR_value
            self.MAR = self.MAR + 1
            self.MAR_binary = self.convert_decimal_to_binary(self.MAR)
            self.MAR_content = Label(self, width=25, bg="white", text=self.MAR_binary.zfill(12))
            self.MAR_content.grid(row=6, column=21)
            self.MAR_value = self.MAR_content.cget('text')
        elif number_LD == 13:
            self.MAR_value = self.MAR_content.cget('text')
            self.MAR = self.convert_binary_to_decimal(self.MAR_value)
            self.MBR_content = Label(self, width=25, bg="white", text=self.memory[self.MAR])
            self.MBR_content.grid(row=7, column=21)
        elif number_LD == 14:
            self.PC_value = "000000001000"
            self.GPR0_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.GPR0_content.grid(row=5, column=1)
            self.GPR1_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.GPR1_content.grid(row=6, column=1)
            self.GPR2_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.GPR2_content.grid(row=7, column=1)
            self.GPR3_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.GPR3_content.grid(row=8, column=1)
            self.IXR1_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.IXR1_content.grid(row=10, column=1)
            self.IXR2_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.IXR2_content.grid(row=11, column=1)
            self.IXR3_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.IXR3_content.grid(row=12, column=1)
            self.PC_content = Label(self, width=25, bg="white", text=self.PC_value)
            self.PC_content.grid(row=5, column=21)
            self.MAR_content = Label(self, width=25, bg="white", text="000000000000")
            self.MAR_content.grid(row=6, column=21)
            self.MBR_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.MBR_content.grid(row=7, column=21)
            self.IR_content = Label(self, width=25, bg="white", text="0000000000000000")
            self.IR_content.grid(row=8, column=21)
            Run_content = Label(self, width=2, bg="white", text="")
            Run_content.grid(row=17, column=24)
            Run_content.place(x=770, y=240)
            Halt_content = Label(self, width=2, bg="white", text="")
            Halt_content.grid(row=17, column=21)
            Halt_content.place(x=680, y=240)
            MFR_content = Label(self, bg="white", text="0000")
            MFR_content.grid(row=9, column=21)
            Privileged_content = Label(self, width=2, bg="white", text="")
            Privileged_content.grid(row=10, column=21)
            self.load_file("IPL.txt")
            self.PC_next = 0
            self.PC_value = self.PC_content.cget("text")
        elif number_LD == 15:
            self.PC_value = self.PC_content.cget("text")
            print("当前的PC_value是",self.PC_value)
            self.jj = self.convert_binary_to_decimal(self.PC_value[:].zfill(12))#current PC_value
            self.PC_next = self.convert_binary_to_decimal(self.PC_value) + 1
            self.PC_value = self.convert_decimal_to_binary(self.PC_next)
            self.PC_content = Label(self, width=25, bg="white", text=self.PC_value.zfill(12))
            self.PC_content.grid(row=5, column=21)
            Halt_content = Label(self, width=2, bg="white", text="")
            Halt_content.grid(row=17, column=21)
            Halt_content.place(x=680, y=240)
            self.instruction_controller(self.memory[self.jj])

        elif number_LD == 16:
            Run_content = Label(self, width=2, bg="red", text="")
            Run_content.grid(row=17, column=24)
            Run_content.place(x=770, y=240)

            for iii in range(15):
                if self.PC_next < 14:
                    self.PC_value = self.PC_content.cget("text")
                    self.jj = self.convert_binary_to_decimal(self.PC_value[7:].zfill(12))  # MAR_value
                    self.PC_next = self.convert_binary_to_decimal(self.PC_value)
                    self.instruction_controller(self.memory[self.jj])
                    self.PC_next = self.PC_next + 1
                    self.PC_value = self.convert_decimal_to_binary(self.PC_next)
                    self.PC_content = Label(self, width=25, bg="white", text=self.PC_value.zfill(12))
                    self.PC_content.grid(row=5, column=21)
                    Run_content = Label(self, width=2, bg="red", text="")
                    Run_content.grid(row=17, column=24)
                    Run_content.place(x=770, y=240)
                    Halt_content = Label(self, width=2, bg="red", text="")
                    Halt_content.grid(row=17, column=21)
                    Halt_content.place(x=680, y=240)
                else:
                    Run_content = Label(self, width=2, bg="white", text="")
                    Run_content.grid(row=17, column=24)
                    Run_content.place(x=770, y=240)



        elif number_LD == 17:
            for abccc in range(0, 4095, 4):
                print("Address", abccc, ":", "value:", self.memory[abccc],"Address", abccc+1, ":", "value:", self.memory[abccc+1],"Address", abccc+2, ":", "value:", self.memory[abccc+2],"Address", abccc+3, ":", "value:", self.memory[abccc+3])

    #get the value of 16 binary buttons
    def LD(self, number_LD):
        global L_long, L_short
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
        L_long = f"{L1}{L2}{L3}{L4}{L5}{L6}{L7}{L8}{L9}{L10}{L11}{L12}{L13}{L14}{L15}{L16}"
        L_short = f"{L5}{L6}{L7}{L8}{L9}{L10}{L11}{L12}{L13}{L14}{L15}{L16}"
        self.get_value(number_LD)



    def Switch(self, number):
        if number == 1:
            if int(self.button_Operation1.cget("text")) == 0:
                self.button_Operation1 = Button(self, text="1", command=lambda: self.Switch(1))
                self.button_Operation1.grid(row=14, column=1)
                self.button_Operation1.place(x=10, y=290)
            else:
                self.button_Operation1 = Button(self, text="0", command=lambda: self.Switch(1))
                self.button_Operation1.grid(row=14, column=1)
                self.button_Operation1.place(x=10, y=290)
        elif number == 2:
            if int(self.button_Operation2.cget("text")) == 0:
                self.button_Operation2 = Button(self, text="1", command=lambda: self.Switch(2))
                self.button_Operation2.grid(row=14, column=2)
                self.button_Operation2.place(x=52, y=290)
            else:
                self.button_Operation2 = Button(self, text="0", command=lambda: self.Switch(2))
                self.button_Operation2.grid(row=14, column=2)
                self.button_Operation2.place(x=52, y=290)
        elif number == 3:
            if int(self.button_Operation3.cget("text")) == 0:
                self.button_Operation3 = Button(self, text="1", command=lambda: self.Switch(3))
                self.button_Operation3.grid(row=14, column=3)
                self.button_Operation3.place(x=94, y=290)
            else:
                self.button_Operation3 = Button(self, text="0", command=lambda: self.Switch(3))
                self.button_Operation3.grid(row=14, column=3)
                self.button_Operation3.place(x=94, y=290)
        elif number == 4:
            if int(self.button_Operation4.cget("text")) == 0:
                self.button_Operation4 = Button(self, text="1", command=lambda: self.Switch(4))
                self.button_Operation4.grid(row=14, column=4)
                self.button_Operation4.place(x=136, y=290)
            else:
                self.button_Operation4 = Button(self, text="0", command=lambda: self.Switch(4))
                self.button_Operation4.grid(row=14, column=4)
                self.button_Operation4.place(x=136, y=290)
        elif number == 5:
            if int(self.button_Operation5.cget("text")) == 0:
                self.button_Operation5 = Button(self, text="1", command=lambda: self.Switch(5))
                self.button_Operation5.grid(row=14, column=5)
                self.button_Operation5.place(x=178, y=290)
            else:
                self.button_Operation5 = Button(self, text="0", command=lambda: self.Switch(5))
                self.button_Operation5.grid(row=14, column=5)
                self.button_Operation5.place(x=178, y=290)
        elif number == 6:
            if int(self.button_Operation6.cget("text")) == 0:
                self.button_Operation6 = Button(self, text="1", command=lambda: self.Switch(6))
                self.button_Operation6.grid(row=14, column=1)
                self.button_Operation6.place(x=220, y=290)
            else:
                self.button_Operation6 = Button(self, text="0", command=lambda: self.Switch(6))
                self.button_Operation6.grid(row=14, column=1)
                self.button_Operation6.place(x=220, y=290)
        elif number == 7:
            if int(self.button_GPR1.cget("text")) == 0:
                self.button_GPR1 = Button(self, text="1", command=lambda: self.Switch(7))
                self.button_GPR1.grid(row=14, column=6)
                self.button_GPR1.place(x=278, y=290)
            else:
                self.button_GPR1 = Button(self, text="0", command=lambda: self.Switch(7))
                self.button_GPR1.grid(row=14, column=6)
                self.button_GPR1.place(x=278, y=290)
        elif number == 8:
            if int(self.button_GPR2.cget("text")) == 0:
                self.button_GPR2 = Button(self, text="1", command=lambda: self.Switch(8))
                self.button_GPR2.grid(row=14, column=7)
                self.button_GPR2.place(x=320, y=290)
            else:
                self.button_GPR2 = Button(self, text="0", command=lambda: self.Switch(8))
                self.button_GPR2.grid(row=14, column=7)
                self.button_GPR2.place(x=320, y=290)
        elif number == 9:
            if int(self.button_IXR1.cget("text")) == 0:
                self.button_IXR1 = Button(self, text="1", command=lambda: self.Switch(9))
                self.button_IXR1.grid(row=14, column=8)
                self.button_IXR1.place(x=372, y=290)
            else:
                self.button_IXR1 = Button(self, text="0", command=lambda: self.Switch(9))
                self.button_IXR1.grid(row=14, column=8)
                self.button_IXR1.place(x=372, y=290)
        elif number == 10:
            if int(self.button_IXR2.cget("text")) == 0:
                self.button_IXR2 = Button(self, text="1", command=lambda: self.Switch(10))
                self.button_IXR2.grid(row=14, column=9)
                self.button_IXR2.place(x=414, y=290)
            else:
                self.button_IXR2 = Button(self, text="0", command=lambda: self.Switch(10))
                self.button_IXR2.grid(row=14, column=9)
                self.button_IXR2.place(x=414, y=290)
        elif number == 11:
            if int(self.button_I1.cget("text")) == 0:
                self.button_I1 = Button(self, text="1", command=lambda: self.Switch(11))
                self.button_I1.grid(row=14, column=10)
                self.button_I1.place(x=466, y=290)
            else:
                self.button_I1 = Button(self, text="0", command=lambda: self.Switch(11))
                self.button_I1.grid(row=14, column=10)
                self.button_I1.place(x=466, y=290)
        elif number == 12:
            if int(self.button_Address1.cget("text")) == 0:
                self.button_Address1 = Button(self, text="1", command=lambda: self.Switch(12))
                self.button_Address1.grid(row=14, column=11)
                self.button_Address1.place(x=518, y=290)
            else:
                self.button_Address1 = Button(self, text="0", command=lambda: self.Switch(12))
                self.button_Address1.grid(row=14, column=11)
                self.button_Address1.place(x=518, y=290)
        elif number == 13:
            if int(self.button_Address2.cget("text")) == 0:
                self.button_Address2 = Button(self, text="1", command=lambda: self.Switch(13))
                self.button_Address2.grid(row=14, column=12)
                self.button_Address2.place(x=560, y=290)
            else:
                self.button_Address2 = Button(self, text="0", command=lambda: self.Switch(13))
                self.button_Address2.grid(row=14, column=12)
                self.button_Address2.place(x=560, y=290)

        elif number == 14:
            if int(self.button_Address3.cget("text")) == 0:
                self.button_Address3 = Button(self, text="1", command=lambda: self.Switch(14))
                self.button_Address3.grid(row=14, column=13)
                self.button_Address3.place(x=602, y=290)
            else:
                self.button_Address3 = Button(self, text="0", command=lambda: self.Switch(14))
                self.button_Address3.grid(row=14, column=13)
                self.button_Address3.place(x=602, y=290)
        elif number == 15:
            if int(self.button_Address4.cget("text")) == 0:
                self.button_Address4 = Button(self, text="1", command=lambda: self.Switch(15))
                self.button_Address4.grid(row=14, column=14)
                self.button_Address4.place(x=644, y=290)
            else:
                self.button_Address4 = Button(self, text="0", command=lambda: self.Switch(15))
                self.button_Address4.grid(row=14, column=14)
                self.button_Address4.place(x=644, y=290)
        elif number == 16:
            if int(self.button_Address5.cget("text")) == 0:
                self.button_Address5 = Button(self, text="1", command=lambda: self.Switch(16))
                self.button_Address5.grid(row=14, column=15)
                self.button_Address5.place(x=686, y=290)
            else:
                self.button_Address5 = Button(self, text="0", command=lambda: self.Switch(16))
                self.button_Address5.grid(row=14, column=15)
                self.button_Address5.place(x=686, y=290)

    #back-end
    def instruction_controller(self, instruction: str):
        Opcode = instruction[:6]
        R = instruction[6:8]
        IX = instruction[8:10]
        I = instruction[10]
        Address = instruction[11:]
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
        elif Opcode == '001000':#完成
            self.execute_JZ(R, EA)
        elif Opcode == '001001':#完成
            self.execute_JNE(R, EA)
        elif Opcode == '001010':#完成
            self.execute_JCC(self.CC_value, EA)
        elif Opcode == '001011':#完成
            self.execute_JMA(EA)
        elif Opcode == '001100':#完成
            self.execute_JSR(EA)
        elif Opcode == '001101':
            self.execute_RFS(EA)
        elif Opcode == '001110':#完成
            self.execute_SOB(R, EA)
        elif Opcode == '001111':#完成
            self.execute_JGE(R, EA)






        self.MAR_content = Label(self, width=25, bg="white", text=Address.zfill(12))
        self.MAR_content.grid(row=6, column=21)
        self.MAR_value = self.MAR_content.cget('text')

        rr = self.convert_binary_to_decimal(self.MAR_value)
        dd = self.memory[rr]
        self.MBR_content = Label(self, width=25, bg="white", text=dd)
        self.MBR_content.grid(row=7, column=21)

        self.IR_content = Label(self, width=25, bg="white", text=instruction)
        self.IR_content.grid(row=8, column=21)


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
        IX_decimal = self.convert_binary_to_decimal(IX)

        return IX_decimal


    def convert_binary_to_decimal(self, binary: str) -> int:
        return int(binary, 2)


    def convert_decimal_to_binary(self, integer: int) -> str:
        return bin(integer)[2:]

    def execute_LDR(self, R: str, EA: int):  # LDR
        GPR_value = self.memory[EA].zfill(16)
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR0_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR0_content.grid(row=5, column=1)
        elif a == 1:
            self.GPR0_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR0_content.grid(row=6, column=1)
        elif a == 2:
            self.GPR0_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR0_content.grid(row=7, column=1)
        elif a == 3:
            self.GPR0_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR0_content.grid(row=8, column=1)

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
            self.GPR0_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR0_content.grid(row=5, column=1)
        elif a == 1:
            self.GPR1_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR1_content.grid(row=6, column=1)
        elif a == 2:
            self.GPR2_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR2_content.grid(row=7, column=1)
        elif a == 3:
            self.GPR3_content = Label(self, width=25, bg="white", text=GPR_value)
            self.GPR3_content.grid(row=8, column=1)


    def execute_LDX(self, IX: str, EA: int):
        a = self.convert_binary_to_decimal(IX)
        IXR_value = self.memory[EA-1].zfill(16)
        if a == 1:
            self.IXR1_content = Label(self, width=25, bg="white", text=IXR_value)
            self.IXR1_content.grid(row=10, column=1)
        elif a == 2:
            self.IXR2_content = Label(self, width=25, bg="white", text=IXR_value)
            self.IXR2_content.grid(row=11, column=1)
        elif a == 3:
            self.IXR3_content = Label(self, width=25, bg="white", text=IXR_value)
            self.IXR3_content.grid(row=12, column=1)

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

    def execute_JZ(self, R: str, EA: int):
        print(EA, R)
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR_value = self.GPR0_content.cget('text')
        elif a == 1:
            self.GPR_value = self.GPR1_content.cget('text')
        elif a == 2:
            self.GPR_value = self.GPR2_content.cget('text')
        elif a == 3:
            self.GPR_value = self.GPR3_content.cget('text')
        b = self.convert_binary_to_decimal(self.GPR_value)
        if b == 0:
            c = self.convert_decimal_to_binary(EA)
            self.PC_content = Label(self, width=25, bg="white", text=c.zfill(12))
            self.PC_content.grid(row=5, column=21)
            print("c:",c.zfill(16))
        else:
            future_PC_value = self.convert_binary_to_decimal(self.PC_value) + 1
            self.PC_value = (self.convert_decimal_to_binary(future_PC_value)).zfill(12)
            self.PC_content = Label(self, width=25, bg="white", text=self.PC_value)
            self.PC_content.grid(row=5, column=21)
            print("PC_value:",self.PC_value)

    def execute_JNE(self, R: str, EA: int):
        print(EA, R)
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR_value = self.GPR0_content.cget('text')
        elif a == 1:
            self.GPR_value = self.GPR1_content.cget('text')
        elif a == 2:
            self.GPR_value = self.GPR2_content.cget('text')
        elif a == 3:
            self.GPR_value = self.GPR3_content.cget('text')
        b = self.convert_binary_to_decimal(self.GPR_value)
        if b != 0:
            c = self.convert_decimal_to_binary(EA)
            self.PC_content = Label(self, width=25, bg="white", text=c.zfill(12))
            self.PC_content.grid(row=5, column=21)
            print("c:", c.zfill(16))
        else:
            future_PC_value = self.convert_binary_to_decimal(self.PC_value) + 1
            self.PC_value = (self.convert_decimal_to_binary(future_PC_value)).zfill(12)
            self.PC_content = Label(self, width=25, bg="white", text=self.PC_value)
            self.PC_content.grid(row=5, column=21)
            print("PC_value:", self.PC_value)

    def execute_JCC(self, CC: str, address: int):
        if CC == "0000":
            c = self.convert_decimal_to_binary(address)
            self.PC_content = Label(self, width=25, bg="white", text=c.zfill(12))
            self.PC_content.grid(row=5, column=21)
        else:
            future_PC_value = self.convert_binary_to_decimal(self.PC_value) + 1
            self.PC_value = (self.convert_decimal_to_binary(future_PC_value)).zfill(12)
            self.PC_content = Label(self, width=25, bg="white", text=self.PC_value)
            self.PC_content.grid(row=5, column=21)

    def execute_JMA(self, address):
        a = address
        c = self.convert_decimal_to_binary(a)
        self.PC_content = Label(self, width=25, bg="white", text=c.zfill(12))
        self.PC_content.grid(row=5, column=21)

    def execute_JSR(self, address):
        a = address + 1
        c = self.convert_decimal_to_binary(a)
        self.GPR3_content = Label(self, width=25, bg="white", text=c.zfill(16))
        self.GPR3_content.grid(row=8, column=1)
        b = self.convert_decimal_to_binary(address)
        self.PC_content = Label(self, width=25, bg="white", text=b.zfill(12))
        self.PC_content.grid(row=5, column=21)

    def execute_SOB(self, R, address):
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR_value = self.GPR0_content.cget('text')
        elif a == 1:
            self.GPR_value = self.GPR1_content.cget('text')
        elif a == 2:
            self.GPR_value = self.GPR2_content.cget('text')
        elif a == 3:
            self.GPR_value = self.GPR3_content.cget('text')
        b = self.convert_binary_to_decimal(self.GPR_value) - 1
        if b > 0:
            c = self.convert_decimal_to_binary(address)
            self.PC_content = Label(self, width=25, bg="white", text=c.zfill(12))
            self.PC_content.grid(row=5, column=21)
        else:
            future_PC_value = self.convert_binary_to_decimal(self.PC_value) + 1
            self.PC_value = (self.convert_decimal_to_binary(future_PC_value)).zfill(12)
            self.PC_content = Label(self, width=25, bg="white", text=self.PC_value)
            self.PC_content.grid(row=5, column=21)

    def execute_JGE(self, R, address):
        a = self.convert_binary_to_decimal(R)
        if a == 0:
            self.GPR_value = self.GPR0_content.cget('text')
        elif a == 1:
            self.GPR_value = self.GPR1_content.cget('text')
        elif a == 2:
            self.GPR_value = self.GPR2_content.cget('text')
        elif a == 3:
            self.GPR_value = self.GPR3_content.cget('text')
        b = self.convert_binary_to_decimal(self.GPR_value)
        if b >= 0:
            print(111111)
            c = self.convert_decimal_to_binary(address)
            self.PC_content = Label(self, width=25, bg="white", text=c.zfill(12))
            self.PC_content.grid(row=5, column=21)
        else:
            print(222222)
            future_PC_value = self.convert_binary_to_decimal(self.PC_value) + 1
            self.PC_value = (self.convert_decimal_to_binary(future_PC_value)).zfill(12)
            self.PC_content = Label(self, width=25, bg="white", text=self.PC_value)
            self.PC_content.grid(row=5, column=21)


if __name__ == "__main__":
    app = App()
    app.mainloop()
