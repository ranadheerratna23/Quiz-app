import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Blue Whale", "Lion"],
                "correct_answer": "Blue Whale"
            }
        ]

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            self.answer_buttons.append(button)
            button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack()
        
        self.load_question(0)

    def load_question(self, question_number):
        if question_number < len(self.questions):
            self.current_question = question_number
            question_data = self.questions[question_number]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.answer_buttons[i].config(text=question_data["options"][i])
        else:
            self.show_score()

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        selected_option_text = self.questions[self.current_question]["options"][selected_option]
        
        if selected_option_text == correct_answer:
            self.score += 1

        if self.current_question < len(self.questions) - 1:
            self.next_question()
        else:
            self.show_score()

    def next_question(self):
        self.load_question(self.current_question + 1)

    def show_score(self):
        messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
