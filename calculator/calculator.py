import tkinter as tk

class Calculator:
   def __init__(self, master):
      self.master = master
      master.title('Calculator by Python')

      self.state = { 'needCalc': False, 'saveValue': 0, 'displayValue': 0, 'operator': '', 'updateDisplay': False }

      # create screen widget
      self.screen = tk.Text(master, state='disabled', width=30, height=3,background="yellow", foreground="blue")

      # position screen in window
      self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
      self.screen.configure(state='normal')

      # create buttons using method createButton
      b1 = self.createButton(7)
      b2 = self.createButton(8)
      b3 = self.createButton(9)
      #self.b4 = self.createButton(u"\u232B",None)
      b5 = self.createButton(4)
      b6 = self.createButton(5)
      b7 = self.createButton(6)
      b8 = self.createButton(u"\u00F7")
      b9 = self.createButton(1)
      b10 = self.createButton(2)
      b11 = self.createButton(3)
      b12 = self.createButton('*')
      b13 = self.ACButton('AC')
      b14 = self.createButton(0)
      b15 = self.createButton('+')
      b16 = self.createButton('-')
      b17 = self.createButton('=',None,34)

      # buttons stored in list
      self.buttons = [b1, b2, b3,b5,b6,b7,b8,b9,
                 b10,b11,b12,b13,b14,b15,b16,b17]

      count=0
      for row in range(1,5):
            for column in range(4):
                if row == 1 and column == 3:
                   continue
                self.buttons[count].grid(row=row,column=column)
                count += 1
      # arrange last button '=' at the bottom
      self.buttons[15].grid(row=5,column=0,columnspan=4)

   def createButton(self, val, write=True, width=7):
      return tk.Button(self.master, text=val,command = lambda:self.click(val,write), width=width)

   def ACButton(self, val):
      return tk.Button(self.master, text=val, command=lambda:self.clearALL(), width=7)

   def click(self, text, write):
      if text == '=':
         if self.state['needCalc'] == False:
            return
         print(self.state['displayValue'])
         self.calculate(self.state['displayValue'])

      elif type(text) == type(1):  # number button clicked
         if self.state['updateDisplay'] == True:
            self.screen.delete('1.0', tk.END)
            self.state['displayValue'] = 0
            self.state['needCalc'] = True
            
         self.screen.insert(tk.END, text)
         self.state['displayValue'] = self.state['displayValue'] *10 + text

         self.state['updateDisplay'] = False

      else: # operator button clicked
         if self.state['needCalc']:
            self.calculate(self.state['displayValue'])
         else:
            self.state['operator'] = text
            self.state['saveValue'] = self.state['displayValue']
            self.state['updateDisplay'] = True

   def calculate(self, value):
      operator = self.state['operator']
      save_value = self.state['saveValue']
      print(save_value)
      result = 0
      if operator == '+' :
         result = value + save_value
      elif operator == '-' :
         result = value - save_value
      elif operator == '*' :
         result = value * save_value
      else:
         result = save_value / value

      self.state['saveValue'] = result
      self.screen.delete('1.0', tk.END)
      self.screen.insert('1.0', result)

   def clearALL(self):
      self.state = { 'needCalc': False, 'saveValue': 0, 'displayValue': 0, 'operator': '', 'updateDisplay': False }
      self.screen.delete('1.0', tk.END)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()