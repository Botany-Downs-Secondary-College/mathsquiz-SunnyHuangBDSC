from tkinter import*
from tkinter import ttk

#class
class frames:
    def __init__(self, tk):
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
        self.value = StringVar()
        self.value.set(0)
       
        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.frame1, variable = self.value, value = self.difficulty[i], text = self.difficulty[i], bg = "light blue", command = self.display_difficulty)
            rb.grid(row = 3+i, column = 0)
        
        self.response = Label(self.frame1, bg = "light blue", width = 28, padx = 30, pady = 10, text = "", font = ("Times", "14", "bold italic"))
        self.response.grid(columnspan = 2)             
        
        self.next_button = ttk.Button(self.frame1, text = "Next", command = self.enter_quiz)
        self.next_button.grid(row = 7, column = 1)
        

   
        
 
        
        
        #quiz
        self.frame2 = Frame(tk, height = "450", width = "400", bg = "light blue") 
        self.frame2.grid(row = 0, column = 0)          
        self.frame2_label = Label(self.frame2, bg = "black", fg = "white", width = 28, padx = 30, pady = 10, text = "Quiz_Page", font = ("Times", "20", "bold italic"))
        self.frame2_label.grid(columnspan = 2)                
        self.home_button = ttk.Button(self.frame2, text = "Home", command = self.quit_quiz)
        self.home_button.grid(row = 1, column = 1)
        self.frame2.grid_remove()
        

       
        
    def enter_quiz(self):
        self.frame1.grid_remove()
        self.frame2.grid()
            
    def quit_quiz(self):
        self.frame2.grid_remove()
        self.frame1.grid()
    
    def display_difficulty(self):
            self.response.configure(text = self.value.get())        
    
#main
root = Tk()
root.title("wtf test")
root.geometry("600x600+300+100")
run = frames(root)
root.mainloop()
