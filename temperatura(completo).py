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
    temperatura: {temperatura}ºc'''

    texto_temperatura["text"] = texto 







janela = Tk()
janela.title("temperatura")
janela.geometry("400x300")


texto_orientacao = Label(janela, text="𝒄𝒍𝒊𝒒𝒖𝒆 𝒑𝒂𝒓𝒂 𝒗𝒆𝒓 𝒂 𝒕𝒆𝒎𝒑𝒆𝒓𝒂𝒕𝒖𝒓𝒂 𝒆𝒎 𝑹𝒊𝒐 𝒅𝒆 𝒋𝒂𝒏𝒆𝒊𝒓𝒐")
texto_orientacao.grid(column=0, row=0, padx=20, pady=20)

botao = Button(janela, text="𝒎𝒐𝒔𝒕𝒓𝒂𝒓 𝒕𝒆𝒎𝒑𝒆𝒓𝒂𝒕𝒖𝒓𝒂", command=mostar_temperaturas)
botao.grid(column=0, row=1, padx=50, pady=50)

texto_temperatura = Label(janela, text="𝒂𝒑𝒆𝒏𝒂𝒔 𝒖𝒎 𝒄𝒍𝒊𝒄𝒌 𝒑𝒓𝒂 𝒗𝒆𝒓 𝒂 𝒕𝒆𝒎𝒑𝒆𝒓𝒂𝒕𝒖𝒓𝒂 𝒆𝒎 𝒕𝒆𝒎𝒑𝒐 𝒓𝒆𝒂𝒍")
texto_temperatura.grid(column=0, row=2, padx=50, pady=50)



janela.mainloop()