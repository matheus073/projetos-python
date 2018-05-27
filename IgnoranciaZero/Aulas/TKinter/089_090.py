from tkinter import *
from Aulas.TKinter.app_canvas_linhas import Linhas
from Aulas.TKinter.app_canvas_SPFC import SPFC
from Aulas.TKinter.app_canvas_fatia import Fatia
from Aulas.TKinter.app_canvas_carinha import Carinha
from Aulas.TKinter.app_canvas_carinha_2 import *
from Aulas.TKinter.app_canvas_mario import Mario
import shelve

AZUL="#4814c1"

class Login(object):
    def __init__(self, i):
        self.mestre=i

        self.font=("Verdana","36","bold")

        self.selecionado=False
        self.entrou=False

        self.frame0=Frame(i)
        self.frame1 = Frame(i,bg=AZUL)
        self.frame2 = Frame(i, bg=AZUL)
        self.frame3 = Frame(i, bg=AZUL)
        self.frame4 = Frame(i, bg=AZUL)

        self.TelaPrincipal()

    def TelaPrincipal(self):
        self.img_criar = PhotoImage(file="Imagens/b_criar.ppm")
        self.img_entrar = PhotoImage(file="Imagens/b_entrar.ppm")
        self.img_novo = PhotoImage(file='Imagens/b_novo.ppm')
        self.img_python = PhotoImage(file='Imagens/bg_python.gif')
        self.logo = Label(self.frame0, image=self.img_python)
        self.UsuarioESenha()
        self.checkbutoon_lembrar = Checkbutton(self.frame2, text="Lembrar-me", font=self.font, bg=AZUL,command=self.CheckbuttonLembrar)
        self.button_entrar = Button(self.frame3, text="Entrar", command=self.Entrar)
        self.button_entrar["image"] = self.img_entrar
        self.button_novo = Button(self.frame3, text="Novo", command=self.Novo)
        self.button_novo["image"] = self.img_novo
        self.resposta_label = Label(self.frame4)
        self.resposta_label.pack()
        self.EmpacotarElementos()
        self.Preenxer()

    def EmpacotarUsuarioESenha(self):
        self.ususario_label.pack()
        self.usuario_entrada.pack()
        self.senha_label.pack()
        self.senha_entry.pack()

    def EmpacotarElementos(self):
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        self.logo.pack()
        self.EmpacotarUsuarioESenha()
        self.checkbutoon_lembrar.pack()
        self.button_entrar.pack(side=LEFT)
        self.button_novo.pack(side=RIGHT)
        self.resposta_label.pack()

    def DestoyTela(self):
        self.frame0.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()

        self.logo.destroy()
        self.checkbutoon_lembrar.destroy()
        self.button_entrar.destroy()
        self.button_novo.destroy()
        self.resposta_label.destroy()

    def Entrar(self):

        usuario=self.usuario_entrada.get()
        senha=self.senha_entry.get()

        if usuario in db:
            if db[usuario]["Senha"] == senha:
                self.resposta_label['text'] = "Bem vindo " + str(db[usuario]["Nome"])
                self.resposta_label["fg"] = "blue"
                self.DestoyTela()
                self.TelaSecundaria()

                if self.selecionado:
                    db['Lembrar_Usuário'] =usuario
                    db["Lembrar_Senha"]=senha


            else:
                self.resposta_label["text"] = "Senha invalida"
                self.resposta_label["fg"] = "red"

        else:
            self.resposta_label["text"] = "Login não existe"
            self.resposta_label["fg"] = "red"

    def CheckbuttonLembrar(self):
        self.selecionado= not self.selecionado

    def TelaSecundaria(self):
        self.mestre.resizable(False,False)

        self.button_linhas=Button(i, text="App Canvas: Linhas", command=self.AtivarCanvasLinhas)
        self.button_linhas.pack(fill=BOTH)

        self.button_SPFC=Button(i,text="App Canvas: SPFC",command=self.AtivarCanvasSPFC)
        self.button_SPFC.pack(fill=BOTH)

        self.button_fatia=Button(i,text="App Canvas: Fatiar",command=self.AtivarCanvasFatia)
        self.button_fatia.pack(fill=BOTH)

        self.button_carinha=Button(i,text="App Canvas: Carinha soridente",command=self.AtivarCanvasCarinha)
        self.button_carinha.pack(fill=BOTH)

        self.button_carinha_2=Button(i,text="App Canvas: Carinha Feliz 2",command=self.AtivarCanvasCarinha2)
        self.button_carinha_2.pack(fill=BOTH)

        self.button_mario=Button(i,text="App Canvas: Mario",command=self.AtivarCanvasMario)
        self.button_mario.pack(fill=BOTH)

    def AtivarCanvasLinhas(self):

        Linhas(self.mestre)
        self.DestroyCanvas()

    def AtivarCanvasCarinha2(self):
        Carinha2(self.mestre)
        self.DestroyCanvas()

    def AtivarCanvasMario(self):
        Mario(self.mestre)
        self.DestroyCanvas()

    def DestroyCanvas(self):
        self.button_linhas.destroy()
        self.button_SPFC.destroy()
        self.button_fatia.pack_forget()
        self.button_carinha.forget()
        self.button_carinha_2.forget()
        self.button_mario.forget()

    def AtivarCanvasCarinha(self):
        Carinha(self.mestre)
        self.DestroyCanvas()

    def AtivarCanvasSPFC(self):
        SPFC(self.mestre)
        self.DestroyCanvas()

    def AtivarCanvasFatia(self):
        Fatia(self.mestre)
        self.DestroyCanvas()

    def DesempacotarFrames0234(self):
        self.frame0.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()

    def DesempacotarElementos(self):

        self.logo.pack_forget()
        self.ususario_label.pack_forget()
        self.usuario_entrada.pack_forget()
        self.senha_label.pack_forget()
        self.senha_entry.pack_forget()
        self.checkbutoon_lembrar.pack_forget()
        self.button_entrar.pack_forget()
        self.button_novo.pack_forget()
        self.resposta_label.pack_forget()

    def EmpacotarCriar(self):
        self.l_nome.pack()
        self.e_nome.pack()
        self.l_email.pack()
        self.e_email.pack()
        self.b_criar.pack()

    def DestroyCriar(self):
        self.b_criar.destroy()
        self.l_nome.destroy()
        self.e_nome.destroy()
        self.l_email.destroy()
        self.e_email.destroy()

    def UsuarioESenha(self):
        self.ususario_label = Label(self.frame1, text="Usuario", font=self.font, bg=AZUL)
        self.usuario_entrada = Entry(self.frame1, font=self.font)
        self.senha_label = Label(self.frame1, text="Senha", font=self.font, bg=AZUL)
        self.senha_entry = Entry(self.frame1, show="*", font=self.font)
        self.EmpacotarUsuarioESenha()

    def Preenxer(self):
        if "Lembrar_Usuário" in db:
            self.usuario_entrada.insert(0,db["Lembrar_Usuário"])
            self.senha_entry.insert(0,db["Lembrar_Senha"])

    def Novo(self):
            self.DesempacotarElementos()
            self.DesempacotarFrames0234()

            self.l_nome = Label(self.frame1, text='Nome', font=self.font, bg=AZUL)
            self.e_nome = Entry(self.frame1, font=self.font)
            self.l_email = Label(self.frame1, text='Email', font=self.font, bg=AZUL)
            self.e_email = Entry(self.frame1, font=self.font)
            self.b_criar = Button(self.frame1, image=self.img_criar, command=self.Criar)
            self.UsuarioESenha()
            self.EmpacotarCriar()
            self.frame4.pack()
            self.resposta_label.pack()

    def Criar(self):

        usuario=self.usuario_entrada.get()
        senha=self.senha_entry.get()
        nome=self.e_nome.get()
        email=self.e_email.get()
        if usuario == '' or senha == '' or nome=='' or email=='':
            self.MSG("Nenhum dos campos pode estar vazio")
        elif usuario in db:
            self.MSG("Esse usuario já está em uso")

        else:
            db[usuario] = {'Nome': nome, 'Email': email, 'Senha': senha}
            self.MSG("Usuario cadastrado com sucesso", "blue")
            self.button_novo["image"]=self.img_novo
            self.ususario_label["fg"]="black"
            self.senha_label["fg"]="black"
            self.ususario_label["text"]="Usuario"

            self.resposta_label.pack_forget()
            self.frame4.pack_forget()
            self.frame1.pack_forget()

            self.DestroyCriar()


            self.EmpacotarElementos()

    def MSG(self, texto, cor="red"):
        self.resposta_label["text"] = texto
        self.resposta_label["fg"] = cor




db = shelve.open("Arquivos/Login.db", "c")

i = Tk()

i["bg"]=AZUL

Login(i)

i.title("Login")

i.mainloop()