import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
#Título do programa
root.title("Relógio pessoal")
#Tamanho da aba do programa
root.geometry("600x320")
#Tamanho inalteravel do programa, minimo e maximo
root.maxsize(600, 320)
root.minsize(600, 320)
#Cor de fundo do programa, background
root.configure(background = '#1d1d1d')

#Função que exibi o nome do usuário a partir do sistema operacional logado
def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.configure(text = 'Olá, ' + nome_usuario)
#Função que puxa a data atual e exibe no programa  
def get_data():
    data_atual = strftime(' %a, %d %b %Y')
    data.config(text = data_atual)
#Função que exibi horas, minutos e segundos
def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text = hora_atual)
    horas.after(1000, get_horas)

margem = tk.Canvas(root, width = 600, height = 60, bg = '#1d1d1d', bd = 0, highlightthickness = 0, relief = 'ridge')
margem.pack()
#Label no Tkinter exerce a função de apresentar um texto na janela
saudacao = Label(root, bg = "#1d1d1d", fg = '#8A2BE2', font = ("Montserrat", 16))
saudacao.pack()

data = Label(root, bg = "#1d1d1d", fg = '#8A2BE2', font = ("Montserrat", 14))
data.pack(pady = 2)

horas = Label(root, bg = "#1d1d1d", fg = '#8A2BE2', font = ("Montserrat", 64, 'bold'))
horas.pack(pady = 2)


get_saudacao()
get_data()
get_horas()
root.mainloop()