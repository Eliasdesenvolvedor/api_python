
# baseado no canal "Hashtag Programação": https://www.youtube.com/watch?v=eel1OVIdfUw
# https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL
# https://docs.awesomeapi.com.br/api-de-moedas
#/last/:moedas
from cProfile import label
from cgitb import text
from cProfile import label
from tkinter.tix import COLUMN, ROW
from matplotlib.pyplot import text
import requests # permite o consumo de dados do api
from  tkinter import * # permite a utilização de janelas  
import json # para ler json 

cotacoes=requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes= cotacoes.json()
#bid é o valor da cotação

#dolar=cotacoes ['USDBRL'] ['bid']

print(cotacoes)
#Tk(); mainloop() # também é possivel, os metodos podem ser facilmente
#  acessados devido a essa forma de importação  from  tkinter import *
# ---------------------------- 
saida_cotacao="valor"
def dolar_cotacao(x):
   if (x==1):
      ativos=cotacoes ['USDBRL'] ['bid']
   if (x==2):
      ativos=cotacoes ['EURBRL'] ['bid']
   if (x==3):
      ativos=cotacoes ['BTCBRL'] ['bid']
   
   #texto["text"]=dolar
   texto["text"]=ativos

    

janela = Tk() # ele chama essa função só dela estar na variavel 
janela.title("cotação") # coloca o título 
janela.geometry("400x400+1+1")
print(janela.geometry())
texto = Label(janela,text="cotação do dólar "+ saida_cotacao)
texto.grid (column=0,row=0,padx=10,pady=10) # padx=50,pady=50 são uma forma de criar espaço
#botao=Button(janela,text="saber cotação do dólar ?",command=dolar_cotacao)
botao=Button(janela,text="saber cotação do USDBRL ?",command=lambda: dolar_cotacao(1))
# chama a função sem  () no buttum , pois é um parâmetro
botao.grid (column=1,row=0,padx=10,pady=10)
#---
botao1=Button(janela,text="saber cotação do EURBRL ?",command=lambda: dolar_cotacao(2))
botao1.grid (column=1,row=2,padx=10,pady=10)
#---
#---
botao1=Button(janela,text="saber cotação do BTCBRL ?",command=lambda: dolar_cotacao(3))
botao1.grid (column=1,row=3,padx=10,pady=10)
#---
janela.mainloop() # sem isso a janela fecha na hora, ele sempre fica em baixo de tudo