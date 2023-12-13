from tkinter import*
from tkinter import ttk
import tkinter as tk
albuns_cadastrados = []
filtragem = []
def dados():

    arquivo = open('dados.txt', 'a', encoding='UTF-8')
    arquivo.write(nomeAlbum.get() + "|" + anoLancamento.get()+"|" + nomeArtista.get() + "|" + str(debutAlbum.get())+'|')
    arquivo.write('\n')
    arquivo.close()

def filtrar_albuns():
    global texto_filtro
    window1 =Tk()
    window1.title('Filtragem de Álbuns')
    window1.geometry('500x500')
    texto_filtro = Entry(window1)
    botao_filtro = Button(window1, text='Filtrar', command=busca_nome)
    texto_filtro.place(x=40,y=40)
    botao_filtro.place(x=180,y=40)
    text = Label (window1, text=filtragem[n])
    with open('dados.txt', 'r', encoding='UTF-8') as arquivo:
        filtro = arquivo.read().split('\n')
        albuns_cadastrados = filtro
        for n in range(0, len(albuns_cadastrados)):
            filtragem.append(albuns_cadastrados[n].split('|'))
    
    window1.mainloop()

def busca_nome():

    texto = texto_filtro.get()
    for n in range(0, len(filtragem)):
        if filtragem[n][0] in texto:
            print(filtragem[n])
        else:
            print('Álbum não encontrado')


def listar_albuns():
    with open('dados.txt','r', encoding='UTF-8') as arquivo:
        texto = arquivo.read().split('\n'+'|')
        for linha in texto:
            continue

    window = Tk()
    window.title('Lista de álbuns cadastrados')
    window.geometry('800x600')
    texto = Label(window,text=linha)
    texto.place(x=30,y=30)
    texto1 = Label(window, text='Nome do álbum|Ano|Artista|Debut')
    texto1.place(x=110, y=10)
    window.mainloop()


window = Tk()
window.title('Cadastro de Álbuns')
window.geometry('500x400')

lbl1 = Label(window, text='Nome do Álbum: ')
lbl2 = Label(window, text='Ano de Lançamento: ')
lbl3 = Label(window, text='Nome do Artista/Banda: ')
lbl4 = Label(window, text='Album de estréia do artista: ')


nomeAlbum = Entry()
anoLancamento = Entry()
nomeArtista = Entry()
debutAlbum = StringVar()
debutAlbum1 = Radiobutton(window, text="Sim", variable=debutAlbum, value='Sim')
debutAlbum2 = Radiobutton(window, text="Não", variable=debutAlbum, value='Não')
cadastrar = Button(window, text='Cadastrar Album', command=dados)
mostrar_lista = Button(window, text='Listar Álbuns', command=listar_albuns)
filtrar = Button(window, text='Filtrar Albuns', command=filtrar_albuns)

nomeAlbum.place(x=190,y=50)
anoLancamento.place(x=190,y=100)
nomeArtista.place(x=190,y=150)
lbl1.place(x=50, y=50)
lbl2.place(x=50, y=100)
lbl3.place(x=50, y=150)
lbl4.place(x=50, y=200)
debutAlbum1.place(x=200,y=200)
debutAlbum2.place(x=250,y=200)
cadastrar.place(x=50,y=250)
mostrar_lista.place(x=160,y=250)
filtrar.place(x=250,y=250)
window.mainloop()