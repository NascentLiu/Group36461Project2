import tkinter.filedialog
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from architecture import Architecture
from register import Register
from memory import Memory
import tkinter as tk
import tkinter.scrolledtext as st

class App(Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title("GUI")
        self.geometry('900x900')
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

        self.L_long = 0
        self.L_short = 0
        self.PC_next = 0
        self.architecture = Architecture()
        self.isActivateInputDialog = True
        self.text_area = st.ScrolledText(self, width=50, height=10, font=("Times New Roman", 15))
        self.text_area.grid(row=7, column=20)
        self.text_area.place(x=200, y=350)




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
            MAR_value = self.architecture.getMAR()
            MBR_value = self.architecture.getMBR()
            self.memory.setMemory(MAR_value, MBR_value)
        elif number_LD == 12:
            MAR_value = self.architecture.getMAR()
            MBR_value = self.architecture.getMBR()
            self.memory.setValue(MAR_value, MBR_value)
            self.MAR_content['text'] = MAR_value + 1
        elif number_LD == 13:
            MAR_value = self.architecture.getMAR()
            MBR_value = self.memory.getValue(MAR_value)
            self.MBR_content['text'] = MBR_value
        elif number_LD == 14:
            self.showMessage()
            self.load_file("IPL.txt")
        elif number_LD == 15:
            instruction = self.architecture.getMemory().getValue(self.architecture.getProgramCounter().getValue())
            self.executeInstruction(instruction)
            opcode = self.convert_decimal_to_binary(instruction)[0:6]
        elif number_LD == 16:
            while True:
                instruction = self.architecture.getMemory().getValue(self.architecture.getProgramCounter().getValue())
                self.executeInstruction(instruction)
                opcode = self.convert_decimal_to_binary(instruction)[0:6]
                if opcode == '000000':
                    return
        elif number_LD == 17:
            for abccc in range(2000):
                # print("Address", abccc, ":", "value:", self.architecture.getMemory().getValue(abccc),"Address", abccc+1, ":", "value:", self.architecture.getMemory().getValue(abccc+1),"Address", abccc+2, ":", "value:", self.self.architecture.getMemory().getValue(abccc+3),"Address", abccc+3, ":", "value:", self.architecture.getMemory().getValue(abccc+3))
                print(abccc, self.architecture.getMemory().getValue(abccc))
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

    def convert_binary_to_decimal(self, binary: str) -> int:
        return int(binary, 2)

    def convert_decimal_to_binary(self, integer: int) -> str:
        return bin(integer)[2:].zfill(16)

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
                instruction = int(words[1], base=16)
                self.architecture.getMemory().setValue(location, instruction)

    def executeInstruction(self, instruction: int):
        instruction = self.convert_decimal_to_binary(instruction)
        opcode = instruction[0:6]
        if opcode == "000000":
            self.execute_HLT()
        elif opcode == "110001":
            if self.isActivateInputDialog == True:
                answer = simpledialog.askstring("Input", "please enter an integer")
                self.architecture.setInput(answer)
                self.isActivateInputDialog = False
            self.architecture.instruction_controller(instruction)
            if self.architecture.getGPR0().getValue() == 0:
                self.isActivateInputDialog = True
        elif opcode == "110010":
            self.architecture.instruction_controller(instruction)
            # messagebox.showinfo("Information", self.architecture.getOutput())
            self.text_area.insert(tk.INSERT, self.architecture.getOutput())
        else:
            self.architecture.instruction_controller(instruction)
        self.showMessage()

    def execute_HLT(self):
        self.button_SS.config(state=tkinter.DISABLED)
        self.button_Run.config(state=tkinter.DISABLED)
        self.Halt_content['bg'] = 'red'

    def showMessage(self):
        self.GPR0_content['text'] = self.showMessageOfRegister(self.architecture.getGPR0())
        self.GPR1_content['text'] = self.showMessageOfRegister(self.architecture.getGPR1())
        self.GPR2_content['text'] = self.showMessageOfRegister(self.architecture.getGPR2())
        self.GPR3_content['text'] = self.showMessageOfRegister(self.architecture.getGPR3())
        self.IXR1_content['text'] = self.showMessageOfRegister(self.architecture.getIXR1())
        self.IXR2_content['text'] = self.showMessageOfRegister(self.architecture.getIXR2())
        self.IXR3_content['text'] = self.showMessageOfRegister(self.architecture.getIXR3())
        self.PC_content['text'] = bin(self.architecture.getProgramCounter().getValue())[2:].zfill(12)
        self.MAR_content['text'] = self.showMessageOfRegister(self.architecture.getMAR())
        self.MBR_content['text'] = self.showMessageOfRegister(self.architecture.getMBR())
        self.IR_content['text'] = self.showMessageOfRegister(self.architecture.getIR())
        self.CC_content['text'] = self.architecture.getConditionCode().getCode()
        self.Run_content['bg'] = "white"
        self.Halt_content['bg'] = "white"
        self.MFR_content['bg'] = "white"
        self.Privileged_content['bg'] = "white"

    def showMessageOfRegister(self, register: Register) -> str:
        if register.getValue() >= 65535:
            return bin(register.getValue())[-16:]
        elif register.getValue() >= 0:
            return bin(register.getValue())[2:].zfill(16)
        else:
            return bin(register.getValue())[3:].zfill(16)

if __name__ == "__main__":
    app = App()
    app.mainloop()