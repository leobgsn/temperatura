import requests

from tkinter import *


def mostar_temperaturas():

    APY_KEY = "950420dbffaf78cbac873d0103025aff"
    cidade = "rio de janeiro"
    Link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={APY_KEY}&lang=pt_br"

    requisicao = requests.get(Link)
    requisicao_disc = requisicao.json()
    descricao = requisicao_disc['weather'][0]['description']
    temperatura = requisicao_disc['main']['temp'] -273.15

    texto = f'''
    tempo: {descricao}
    temperatura: {temperatura}ΒΊc'''

    texto_temperatura["text"] = texto 







janela = Tk()
janela.title("temperatura")
janela.geometry("400x300")


texto_orientacao = Label(janela, text="ππππππ ππππ πππ π πππππππππππ ππ πΉππ ππ πππππππ")
texto_orientacao.grid(column=0, row=0, padx=20, pady=20)

botao = Button(janela, text="πππππππ πππππππππππ", command=mostar_temperaturas)
botao.grid(column=0, row=1, padx=50, pady=50)

texto_temperatura = Label(janela, text="ππππππ ππ πππππ πππ πππ π πππππππππππ ππ πππππ ππππ")
texto_temperatura.grid(column=0, row=2, padx=50, pady=50)



janela.mainloop()