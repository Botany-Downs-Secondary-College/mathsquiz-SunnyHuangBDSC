from tkinter import*
from tkinter import ttk
from random import*
from threading import Timer
from time import sleep
from threading import Thread


#class
class frames:
    def __init__(self, tk):
        self.score = 0
        #start
        self.frame1 = Frame(tk, height = "450", width = "400", bg = "light blue") 
        self.frame1.grid(row = 0, column = 0)   
        self.frame1_label = Label(self.frame1, bg = "black", fg = "white", width = 28, padx = 30, pady = 10, text = "Welcome", font = ("Times", "20", "bold italic"))
        self.frame1_label.grid(columnspan = 2)         
        self.name_input_label = Label(self.frame1, bg = "light blue", text = "Name:", width = 10, font=("Times", "14", "bold italic"))
        self.name_input_label.grid(row = 1, column = 0)
        self.name_input_entry = Entry(self.frame1, width = 20)
        self.name_input_entry.grid(row = 1, column = 1)
        self.age_input_label = Label(self.frame1, bg = "light blue", text = "Age:", width = 10, font=("Times", "14", "bold italic"))
        self.age_input_label.grid(row = 2, column = 0)    
        self.age_input_entry = Entry(self.frame1, width = 20)
        self.age_input_entry.grid(row = 2, column = 1)
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.choice = StringVar()
        self.choice.set("Medium")
        for i in range(len(self.difficulty)):
            self.rb = Radiobutton(self.frame1, variable = self.choice, value = self.difficulty[i], text = self.difficulty[i], bg = "light blue", command = self.display_difficulty)
            self.rb.grid(row = 3+i, column = 0)       
        self.response_1 = Label(self.frame1, bg = "light blue", width = 28, padx = 30, pady = 10, text = "", font = ("Times", "14", "bold italic"))
        self.response_1.grid(columnspan = 2)             
        self.next_button = ttk.Button(self.frame1, text = "Next", command = self.enter_quiz)
        self.next_button.grid(row = 7, column = 1)
        
        #quiz
        self.frame2 = Frame(tk, height = "450", width = "400", bg = "light blue") 
        self.frame2.grid(row = 0, column = 0)          
        self.frame2_label = Label(self.frame2, bg = "black", fg = "white", width = 28, padx = 30, pady = 10, text = "Quiz_Page", font = ("Times", "20", "bold italic"))
        self.frame2_label.grid(columnspan = 3)                
        self.question_label = Label(self.frame2, bg = "light blue", text = "", width = 10, font=("Times", "14", "bold italic"))
        self.question_label.grid(row = 1, column = 0)
        self.answer_entry = Entry(self.frame2, width = 20)
        self.answer_entry.grid(row = 1, column = 1)
        self.home_button = ttk.Button(self.frame2, text = "Quit", command = self.quit_quiz)
        self.home_button.grid(row = 2, column = 0) 
        self.give_up_button = ttk.Button(self.frame2, text = "Give up", command = self.refresh_quiz)
        self.give_up_button.grid(row = 2, column = 1)     
        self.check_button = ttk.Button(self.frame2, text = "Check", command = self.check_answer)
        self.check_button.grid(row = 2, column = 2)        
        self.response_2 = Label(self.frame2, bg = "light blue", width = 28, padx = 30, pady = 10, text = "", font = ("Times", "14", "bold italic"))
        self.response_2.grid(columnspan = 2)  
        self.time = Label(self.frame2, bg = "light blue", width = 28, padx = 30, pady = 10, text = "", font = ("Times", "14", "bold italic"))
        self.time.grid(columnspan = 2)  
        
        #start up config
        self.frame2.grid_remove()

    def display_difficulty(self):
        self.response_1.configure(text = self.choice.get())    #------------------------------------------------------------------
   
    def bonus_timer(self):
        self.t = 6
        for i in range(6):
            if self.answer_correct == False: 
                self.t -= 1
                try:
                    self.time.configure(text = self.t)
                except:
                    pass
                print(self.t)
                sleep(1)            
                if self.t == 0:
                    self.bonus = False
            else:
                break

    def enter_quiz(self):
        self.answer_correct = False
        self.refresh_question = False
        self.bonus = True
        self.bonus_timer_thread = Thread(target = self.bonus_timer)
        self.bonus_timer_thread.start()
        self.operators = ["+", "-", "*", "/"]
        self.operator = self.operators[randrange(4)]
        self.x = randrange(11)
        self.y = randrange(11)      
        if self.operator == "+":
            self.answer = self.x + self.y
        elif self.operator == "-":
            self.answer = self.x - self.y
        elif self.operator == "*":
            self.answer = self.x * self.y        
        elif self.operator == "/":
            while self.y == 0:
                self.y = randrange(11)
            self.answer = round(self.x / self.y, 2)
        self.question_label.configure(text = str(self.x) + self.operator + str(self.y))
        self.frame1.grid_remove()
        self.frame2.grid()
        self.response_2.configure(text = self.answer)    #------------------------------------------------------
   
    def refresh_quiz(self): 
        timer = Timer(1.0, self.refresh)
        timer.start()          
        self.answer_correct = True 
        
    def quit_quiz(self):
        self.frame1.grid()
    
    def check_answer(self):
        try:
            float(self.answer_entry.get())
            if float(self.answer) == round(float(self.answer_entry.get()),2):
                self.response_2.configure(text = "Good", bg = "light green")   
                if self.bonus == True:
                    self.response_2.configure(text = "Bonus", bg = "light green")
                self.frame2.configure(bg = "light green")
                self.question_label.configure(bg = "light green")
                self.answer_entry.delete(0, END)
                self.answer_entry.focus()        
                self.score += 1
                print("score: " + str(self.score))                
                timer = Timer(1.0, self.refresh)
                timer.start()          
                self.answer_correct = True
            else:
                self.response_2.configure(text = "LOL", bg = "orange")
                self.frame2.configure(bg = "orange")
                self.question_label.configure(bg = "orange")                
                self.answer_entry.focus()   
                timer = Timer(1.0, self.refresh)
                timer.start()
                self.answer_correct = False
        except:
            self.response_2.configure(text = "WTF", bg = "tomato")
            self.frame2.configure(bg = "tomato")
            self.question_label.configure(bg = "tomato")             
            self.answer_entry.delete(0, END)
            self.answer_entry.focus()      
            timer = Timer(1.0, self.refresh)
            timer.start() 
            self.answer_correct = False

    def refresh(self):
        try:
            self.response_2.configure(text = self.answer, bg = "light blue")   #------------------------------------------------------
            self.frame2.configure(bg = "light blue")
            self.question_label.configure(bg = "light blue") 
            if self.answer_correct == True:
                self.enter_quiz()
        except:
            pass
        
        
#main
root = Tk()
root.title("wtf test")
root.geometry("600x600+300+100")
run = frames(root)
root.mainloop()
