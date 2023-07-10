import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar o arquivo do Excel
df = pd.read_excel('questions.xlsx')

# Pegar as perguntas aleatoriamente
questions = df.sample(n=10).values.tolist()

#variáveis globais 
score = 0
current_question = 0







# importando biblioteca tk e configurando a janela
main_window = tk.Tk()
main_window.title("Quiz")
main_window.geometry("400x450")

# definindo cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

main_window.config(bg=background_color)
main_window.option_add('*Font', 'Arial')

# Definindo icone da tela
app_icon = PhotoImage(file="./src/logo.png")
app_label = tk.Label(main_window, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Componentes da interface
question_label = tk.Label(main_window, text="Pergunta", wraplength=380,
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
play_again_btn.pack(pady=20)

main_window.mainloop()
