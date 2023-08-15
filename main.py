import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plastic Pollution Quiz")
        self.root.configure(bg="blue")  # Set the background color to blue
        self.root.geometry("600x400")  # Set the width and height of the window

        self.questions = [
            "Question 1: How many tons of plastic enter the ocean each year?",
            "Question 2: What percentage of plastic in the ocean comes from land-based sources?",
            "Question 3: Which type of plastic is the most commonly found in marine environments?",
            "Question 4: What is the estimated time for a plastic bag to decompose in the ocean?",
            "Question 5: How many marine species are affected by plastic pollution?"
        ]

        self.answers = [
            ["A. 10,000 tons", "B. 100,000 tons", "C. 1 million tons", "D. 8 million tons"],
            ["A. 20%", "B. 50%", "C. 80%", "D. 90%"],
            ["A. Polyethylene", "B. Polypropylene", "C. Polystyrene", "D. Polyethylene terephthalate"],
            ["A. 10 years", "B. 50 years", "C. 200 years", "D. 500 years"],
            ["A. 500", "B. 1000", "C. 1500", "D. 2000"]
        ]

        self.correct_choices = ["D", "C", "A", "C", "D"]

        self.current_question = 0
        self.score = 0

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 12), bg="blue", fg="white")
        self.score_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="blue", fg="white")
        self.question_label.pack(pady=10)

        self.choice_var = tk.StringVar()
        self.choice_var.set("")

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.choice_var, value="", font=("Helvetica", 14), bg="blue", fg="white", selectcolor="yellow", indicatoron=0)
            rb.pack(pady=5)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Helvetica", 14))
        self.submit_button.pack(pady=10)

    def display_question(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.question_label.config(text=self.questions[self.current_question])

        choices = self.answers[self.current_question]
        for i in range(4):
            self.radio_buttons[i].config(text=choices[i], value=chr(65 + i))

    def check_answer(self):
        selected_choice = self.choice_var.get()
        correct_choice = self.correct_choices[self.current_question]

        if selected_choice == correct_choice:
            self.score += 1

        # Reset the highlight for all radio buttons
        for rb in self.radio_buttons:
            rb.config(bg="blue")

        # Highlight the selected radio button
        selected_index = ord(selected_choice) - ord('A')
        self.radio_buttons[selected_index].config(bg="yellow")

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Quiz completed!\nYour Score: {self.score} out of {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

