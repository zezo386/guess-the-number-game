import tkinter
import random

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guess the number game")
        screen_width = int((self.winfo_screenheight()/3)*2)
        screen_length = int((self.winfo_screenheight()/3)*2)
        self.geometry(f"{screen_width}x{screen_length}")
        self.max_guesses = 10
        self.background_color = "#f0f0f0"
        self.configure(bg = self.background_color)
        self.reset_button = tkinter.Button(self, text = "Play again", command = self.reset_guesses, fg = "black",bg = self.background_color,padx = 10, pady = 15)
        self.title_label = tkinter.Label(self, text = "Welcome to the guess the number game!",fg = "black",bg = self.background_color,padx = 10, pady = 15)
        self.title_label.pack()
        self.instruction_label = tkinter.Label(self, text = f"Guess a number between 1 and 100 (you have {self.max_guesses} attempts)", fg = "black",bg = self.background_color,padx = 10, pady = 15)
        self.instruction_label.pack()
        self.guess_entry = tkinter.Entry(self, fg = "black",bg = self.background_color,)
        self.guess_entry.pack()
        self.submit_button = tkinter.Button(self, text = "Submit Guess", command = self.check_guess, fg = "black",bg = self.background_color,padx = 10, pady = 15)
        self.submit_button.pack()
        self.result_label = tkinter.Label(self, text = "", fg = "black",bg = self.background_color,padx = 10, pady = 15)
        self.result_label.pack()
        self.reset_guesses()
        

    def reset_guesses(self):
        self.reset_button.pack_forget()
        self.guess_entry.config(state = "normal")
        self.submit_button.config(state = "normal")
        self.result_label.config(text = "")
        self.guesses = 0
        self.number_to_guess = random.randint(1, 100)
        self.max_guesses = 10
    def get_anger_level(self):
        return ["#00FF00", "#33FF00", "#66FF00", "#99FF00", "#CCFF00", "#FFFF00", "#FFCC00", "#FF9900", "#FF6600", "#FF3300", "#FF0000"][self.guesses]
    def check_guess(self):
        if self.guess_entry.get().isdigit():
            user_guess = int(self.guess_entry.get())
            
            if user_guess < self.number_to_guess:
                self.result_label.config(text = "Higher, Try again!", fg = self.get_anger_level())
            elif user_guess > self.number_to_guess:
                self.result_label.config(text = "Lower, Try again!", fg = self.get_anger_level())
            else:
                self.result_label.config(text = f"Congratulations! You've guessed the number {self.number_to_guess} in {self.guesses} attempts.")
                self.guess_entry.config(state = "disabled")
                self.submit_button.config(state = "disabled")
                self.reset_button.pack()
            self.guesses += 1
            if self.guesses >= self.max_guesses:
                self.result_label.config(text = f"Sorry, you've used all attempts. The number was {self.number_to_guess}.",fg = self.get_anger_level())
                self.guess_entry.config(state = "disabled")
                self.submit_button.config(state = "disabled")
                self.reset_button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()