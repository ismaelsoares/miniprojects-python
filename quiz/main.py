import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar o arquivo do Excel
df = pd.read_excel('questions.xlsx')

# Pegar as perguntas aleatoriamente
questions = df.sample(n=10).values.tolist()

# print(questions)
# variáveis globais
score = 0
current_question = 0

# função para verificar se a resposta está correta


def check_answer(answer):
    global score, current_question

    if answer == correct_answer.get():
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_result()


# funcao para exibir a proxima perguntaS


def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL,
                       command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL,
                       command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL,
                       command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL,
                       command=lambda: check_answer(4))

    correct_answer.set(answer)


# função para exibir o resultado final
def show_result():
    messagebox.showinfo(
        "Quiz finalizado!", f"Parabéns! Você completou o quiz:\n\n Pontuação final: {score}/{len(questions)} pontos")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)


# importando biblioteca tk e configurando a janela
main_window = tk.Tk()
main_window.title("Quiz")
main_window.geometry("500x550")

# definindo cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

main_window.config(bg=background_color)
main_window.option_add('*Font', 'Arial')

# Definindo icone da tela
app_icon = PhotoImage(file="./quiz/src/logo.png")
app_label = tk.Label(main_window, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Componentes da interface
question_label = tk.Label(main_window, text="", wraplength=380,
                          bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

# Botões de perguntas
option1_btn = tk.Button(main_window, text="", width=30,
                        bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(main_window, text="", width=30,
                        bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(main_window, text="", width=30,
                        bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(main_window, text="", width=30,
                        bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(main_window, text="Jogar Novamente", width=30,
                           bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
# play_again_btn.pack(pady=20)

display_question()
main_window.mainloop()
