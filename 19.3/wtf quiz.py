from tkinter import*
from tkinter import ttk
from random import*
from threading import*
from time import*
import pickle
import sys 

#class
class frames:
    def __init__(self, tk):
        
        self.current_user_info = []
        self.score = 0
        self.all_user_info = []
        try:
            with open("quiz_data.txt", "rb") as fp:
                self.all_user_info = pickle.load(fp)
        except:
            print('Critical file "quiz_data.txt" missing.')
            sys.exit()
                
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
        self.response_1 = Label(self.frame1, bg = "light blue", width = 28, padx = 30, pady = 10, text = "Medium", font = ("Times", "14", "bold italic"))
        self.response_1.grid(columnspan = 2)        
        self.rank_button = ttk.Button(self.frame1, text = "Rank", command = self.display_rank)
        self.rank_button.grid(row = 7, column = 0)        
        self.next_button = ttk.Button(self.frame1, text = "Next", command = self.enter_quiz)
        self.next_button.grid(row = 7, column = 1)
        
        #quiz
        self.frame2 = Frame(tk, height = "450", width = "400", bg = "light blue") 
        self.frame2.grid(row = 0, column = 0)         
        self.frame2_label = Label(self.frame2, bg = "black", fg = "white", width = 28, padx = 30, pady = 10, text = "", font = ("Times", "20", "bold italic"))
        self.frame2_label.grid(columnspan = 3)                
        self.question_label = Label(self.frame2, bg = "light blue", text = "", width = 10, font=("Times", "14", "bold italic"))
        self.question_label.grid(row = 1, column = 0)
        self.answer_entry = Entry(self.frame2, width = 20)
        self.answer_entry.grid(row = 1, column = 2)
        self.home_button = ttk.Button(self.frame2, text = "Quit", command = self.quit_quiz)
        self.home_button.grid(row = 2, column = 0) 
        self.give_up_button = ttk.Button(self.frame2, text = "Give up", command = self.refresh_quiz)
        self.give_up_button.grid(row = 2, column = 1)     
        self.check_button = ttk.Button(self.frame2, text = "Check", command = self.check_answer)
        self.check_button.grid(row = 2, column = 2)        
        self.response_2 = Label(self.frame2,  bg = "light blue", text = "Name:", width = 10, font=("Times", "14", "bold italic"))
        self.response_2.grid(columnspan = 2)  
        self.time = Label(self.frame2,  bg = "light blue", text = "", width = 10, font=("Times", "14", "bold italic"))
        self.time.grid(row = 4, column = 0)  
        self.score_label = Label(self.frame2,  bg = "light blue", text = "", width = 10, font=("Times", "14", "bold italic"))
        self.score_label.grid(row = 4, column = 2) 
        
        #rank
        self.frame3 = Frame(tk, height = "450", width = "400", bg = "light blue") 
        self.frame3.grid(row = 0, column = 0)            
        self.frame3_label = Label(self.frame3, bg = "black", fg = "white", width = 28, padx = 30, pady = 10, text = "Ranking", font = ("Times", "20", "bold italic"))
        self.frame3_label.grid(columnspan = 3)    
        self.rank_label = Label(self.frame3, bg = "light blue", text = "Rank: ", width = 10, font=("Times", "14", "bold italic"))
        self.rank_label.grid(row = 1, column = 0)               
        self.username_label = Label(self.frame3, bg = "light blue", text = "Name: ", width = 10, font=("Times", "14", "bold italic"))
        self.username_label.grid(row = 1, column = 1)                     
        self.socre_label = Label(self.frame3, bg = "light blue", text = "Score: ", width = 10, font=("Times", "14", "bold italic"))
        self.socre_label.grid(row = 1, column = 2)    
        
        #start up config
        self.frame2.grid_remove()    
        self.frame3.grid_remove()

    def display_difficulty(self):
        self.response_1.configure(text = self.choice.get())    #------------------------------------------------------------------
    
    def display_rank(self):
        self.frame1.grid_remove()
        self.frame3.grid()        
        for i in range(len(self.all_user_info)):
            temp = self.all_user_info[i]
            for i2 in range(len(temp)):
                self.a_label = Label(self.frame3, bg = "light blue", text = i+1, width = 10, font=("Times", "14", "bold italic"))
                self.a_label.grid(row = 2+i, column = 0)               
                self.b_label = Label(self.frame3, bg = "light blue", text = temp[1], width = 10, font=("Times", "14", "bold italic"))
                self.b_label.grid(row = 2+i, column = 1)                     
                self.c_label = Label(self.frame3, bg = "light blue", text = temp[0], width = 10, font=("Times", "14", "bold italic"))
                self.c_label.grid(row = 2+i, column = 2)                       
        self.return_button = ttk.Button(self.frame3, text = "Back", command = self.quit_rank)
        self.return_button.grid(row = 3+i, column = 2)              
        
    def quit_rank(self):
        self.frame3.grid_remove()
        self.frame1.grid()            
    
    def bonus_timer(self):
        self.t = 6
        for i in range(6):
            if self.answer_correct == False: 
                self.t -= 1
                try:
                    self.time.configure(text = "Time left: " + str(self.t))
                except:
                    pass
                sleep(1)            
                if self.t == 1:
                    self.bonus = False
            else:
                break

    def enter_quiz(self):    
        self.score_label.configure(text = "Score: " + str(self.score))
        if self.name_input_entry.get().strip() != "":
            try:
                int(self.age_input_entry.get())
                self.frame2_label.configure(text = "Quiz for: " + self.name_input_entry.get())
                self.answer_correct = False
                self.refresh_question = False
                self.bonus = True
                self.bonus_timer_thread = Thread(target = self.bonus_timer)
                self.bonus_timer_thread.start()
                self.operators = ["+", "-", "*", "/", "^", "¡Ì"]
                if self.choice.get() == "Easy":
                    self.x = randrange(11)
                    self.y = randrange(11)                     
                    self.operator = self.operators[randrange(2)]
                elif self.choice.get() == "Medium":
                    self.x = randrange(15)
                    self.y = randrange(15)                     
                    self.operator = self.operators[randrange(4)]
                else:
                    self.x = randrange(15)
                    self.y = randrange(15)                     
                    self.operator = self.operators[randrange(6)]
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
                elif self.operator == "^":
                    while self.y > 5:
                        self.y = randrange(5)                
                    self.answer = self.x ** self.y   
                else:
                    while self.x <=1 or self.x > 5:
                        self.x = randrange(5)                
                    self.answer = round(self.y ** float(1/self.x) ,2)
                self.question_label.configure(text = str(self.x) + self.operator + str(self.y) + " = ? ")
                self.frame1.grid_remove()
                self.frame2.grid()
                self.response_2.configure(text = self.answer)    #------------------------------------------------------
            except:
                self.response_1.configure(text = "Age invalid")
                self.age_input_entry.delete(0, END)
        else:
            self.response_1.configure(text = "Name invalid")
            self.name_input_entry.delete(0, END)            
            
    def refresh_quiz(self): 
        timer = Timer(1.0, self.refresh)
        timer.start()          
        self.answer_correct = True 
        
    def quit_quiz(self):
        self.frame2.grid_remove()
        self.frame1.grid()
        self.current_user_info = [self.score, self.name_input_entry.get(), self.age_input_entry.get()]
        print("User: " + self.name_input_entry.get())
        print("Age: " + self.age_input_entry.get())
        print("Score: " + str(self.score))
        with open("quiz_data.txt", "rb") as fp:
            self.all_user_info = pickle.load(fp)
            self.all_user_info.append(self.current_user_info)
            self.all_user_info.sort(reverse=True)
        with open("quiz_data.txt", "wb") as fp:
            pickle.dump(self.all_user_info, fp)
        self.name_input_entry.delete(0, END)
        self.age_input_entry.delete(0, END)
        
    def check_answer(self):
        try:
            float(self.answer_entry.get())
            if float(self.answer) == round(float(self.answer_entry.get()),2):
                self.response_2.configure(text = "Good +1", bg = "light green")   
                if self.bonus == True:
                    self.response_2.configure(text = "Bonus +2", bg = "light green")
                    self.score += 1
                self.frame2.configure(bg = "light green")
                self.question_label.configure(bg = "light green")
                self.time.configure(bg = "light green")
                self.score_label.configure(bg = "light green")
                self.answer_entry.delete(0, END)
                self.answer_entry.focus()        
                self.score += 1             
                timer = Timer(1.0, self.refresh)
                timer.start()          
                self.answer_correct = True
            else:
                self.response_2.configure(text = "LOL", bg = "orange")
                self.frame2.configure(bg = "orange")
                self.question_label.configure(bg = "orange")            
                self.time.configure(bg = "orange")
                self.score_label.configure(bg = "orange")                
                self.answer_entry.focus()   
                timer = Timer(1.0, self.refresh)
                timer.start()
                self.answer_correct = False
        except:
            self.response_2.configure(text = "WTF", bg = "tomato")
            self.frame2.configure(bg = "tomato")
            self.question_label.configure(bg = "tomato")      
            self.time.configure(bg = "tomato")
            self.score_label.configure(bg = "tomato")                 
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
            self.time.configure(bg = "light blue")
            self.score_label.configure(bg = "light blue")                 
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