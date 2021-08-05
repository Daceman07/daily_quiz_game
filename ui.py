THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    # Note: in the init self, quiz_brain: QuizBrain it is casting the type of data passed in

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(bg=THEME_COLOR, fg="white", text="Score: 0")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Test",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_mark = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=check_mark, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)

        x_mark = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=x_mark, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """
        Taps into quiz brain file to retrieve question
        :return: another question
        """
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")

        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
