import customtkinter as ctk 
import time
# O "customtkinter é o mesmo tkinter,só que tem padrões mais bonitos, ELE PERMITER DARKMODE, ELE PERMITE PERSONALIZAÇÕA MAIS NONITAS NATURALMENTE ""

#vAMOS DEFINE OS PADRÕES DE CORES DO CUSTOMTKINTER 
ctk.set_appearance_mode("Dark")# Dark, System(padrão do sistema ), light
ctk.set_default_color_theme("green")# blue, green, dark-blue
                        
class Aplicativo(ctk.CTk):# ESSA É UMA SUB CLASS DO TKINTER, 2 PASSO CRIA SUA CLASS E PASSA COM O PAREMETRO DA CLASS PRA CRIA SUA JANELA, E USAR O __init__
    def __init__(self):# fução __init__ tem que rodar o  super().__init__()
        super().__init__()
        # executa os meus comandos persnalizados 
        self.title =("Sistema de Cadastro")
        

        # cria  a divisão da tela 
        #grid_systems : sistema de grid de linhas e colunas
        self.grid_columnconfigure(1, weight=1) # weight é o peso de cada uma das colunas,
        # colinas com peso 1 elas se expande com a tela, colunas com o peso 0 elas não se espamdem com a tela 
        self.grid_rowconfigure(0, weight=1)    #para configurar linhas e colunas 
        
        #parte lateral
        # Frame - é usado para criar una ubica aba 
        self.barra_lateral = ctk.CTkFrame(self, width=200) # width  ele vai defini a largura da aba dentro da janela 
        self.barra_lateral.grid(row=0, column=0, sticky="nswe", pady=10) # Nesse comando é pra defini em qual lado vai fica a  coluna lateral Row = é pra definir qual a linha da aba - columns = é pra definir qual a coluna da aba 
                                                  # sticky = é um paramentor que define a direção "norte , sul etc..." e onde voçe quer que as bordas fiquem presas/ expandi as bordas
    

        #parte principal 
        # TabView   é  usado quando é pra cria mais de uma aba 
        self.janelas_abas = ctk.CTkTabview(self, width=400) # width  ele vai defini a largura da aba dentro da janela
        self.janelas_abas.grid(row=0, column=1, sticky="nsew", padx=10) # sticky = é um paramentor que define a direção "norte , sul etc..." e onde voçe quer que as bordas fiquem presas/ expandi as bordas

        self.janelas_abas.add("Perfil")
        self.janelas_abas.add("Preferencias")
        self.janelas_abas.add("Dashboard")

        # PRa colocar elementos na tela do 'tkinter' voçe tem duas formas  ou coloca em linha e colunas que normalmente e usado para estrutura as telas  
        # OU usa o '.pack' que ele vai alocando um elemento em baixo do outro
        # O '.grid' da mais flexbilidade que ele permite voce escolhe onde coloca os elementos em qual 'row = linha' e 'column = coluna', voçe cola d lado , cima , baixo e na diagonal -  como se tivesse criando uma tabela  virtual 


        # preencher as partes / abas
        #preencher aba lateral
        self.construir_abalateral() 
        #preencher aba perfil 
        self.construir_abaperfil()
        #preencher aba preferencias 
        self.construir_abapreferencias()
        #preencher aba sistemas 
        self.construir_abasistemas()


    def construir_abalateral(self):
        self.titulo = ctk.CTkLabel(self.barra_lateral,
                                    text="Lucas Dev",
                                    font=ctk.CTkFont(size=18,weight="bold", family="Courier"))

        self.titulo.pack(pady=(30, 5), padx=(22,22))
        self.sub_titulo = ctk.CTkLabel(self.barra_lateral,
                                    text="")

        self.sub_titulo.pack(pady=(0, 10), )

        self.botão_principal = ctk.CTkButton(self.barra_lateral,
                                             text="Dashboard Principal",
                                             fg_color="green",
                                             hover_color="Darkgreen",
                                             command=self.ir_para_Dashboard)
        self.botão_principal.pack(pady=(40,50), padx=(10, 10))

        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral,
                                             text="Modo Escuro",
                                             command= self.mudar_modo_dark)
        self.switch_mododark.pack(side="bottom") # para alocar direto o botão no final é usado o parametro de "side = bottom" caso fosse no topo era "side=top"
        self.switch_mododark.select()
        
    def construir_abaperfil(self): 
        self.aba_perfil = self.janelas_abas.tab("Perfil")
        #campo de nome
        self.campo_nome = ctk.CTkEntry(self.aba_perfil,
                                  placeholder_text="Digite seu nome",# É um parametro onde vai cria um espço reservado pra alocar o texto solicitado 
                                  width=400)
        self.campo_nome.pack(pady=(20, 20))
        
        #radio button do nivel do usuario - "Radio Button é o botão no qual voçe so pode marca uma unica opção
        self.nivel_usuario = ctk.IntVar(value=0)
        self.radio_Label = ctk.CTkLabel(self.aba_perfil, text="Nivel do Usuário")
        self.radio_basico = ctk.CTkRadioButton(self.aba_perfil,
                                               text="Básico",
                                               variable=self.nivel_usuario,
                                               value=1) 
        # Dois "Radio Button" que compatilham  a mesma variavel estão conectados, quando vc seleciona 1, automaticamente ele tira a selção do outro assim que funciona no Tkinter
        self.radio_admin = ctk.CTkRadioButton(self.aba_perfil,
                                               text="Administrado",
                                               variable=self.nivel_usuario,
                                               value=2) 
        self.radio_Label.pack()
        self.radio_basico.pack(pady=(10,5))
        self.radio_admin.pack(pady=(10, 5), padx=(45, 40))

        #checkbox de notificações - Esse checkbox é usado para criar aquela caixa de site onde vc marca para receber notificações 
        self.checkbox_notificacoes = ctk.CTkCheckBox(self.aba_perfil,
                                                     text = "Receber Notificações")
        self.checkbox_notificacoes.pack(pady =(40, 30))

        
        #botão salvar perfil 
        self.botao_salvarperfil = ctk.CTkButton(self.aba_perfil,
                                             text="Salvar Perfil",
                                             fg_color="green",# comando 'fg_color' é usado par amudar a cor do botão
                                             hover_color="Darkgreen",
                                             command=self.salvarperfil) # esse comando 'hover' é usado quando vc passa o ponteiro do mouse em cimna do botao 
       
        self.botao_salvarperfil.pack(pady=(40,50))

    def construir_abapreferencias(self):
       
        self.abapreferencias = self.janelas_abas.tab("Preferencias")
        
        # Label - Seleciona o Idioma:
        self.label_idiomas = ctk.CTkLabel(self.abapreferencias, 
                        text="Selecione um Idioma:")
        self.label_idiomas.pack(pady=(20, 5))

        #Menu opções de Idiomas :
        self.menu_idiomas = ctk.CTkOptionMenu(self.abapreferencias,
                                              values=["Portugues", "Ingles", "Espanhol", "Italiano"],
                                              fg_color="green",
                                              button_hover_color="Darkgreen")
        self.menu_idiomas.pack()

        #Label - Volume do Sistema: 
        self.label_volume = ctk.CTkLabel(self.abapreferencias,
                                         text = "Volume do Sistema:")
        #slide - Volume do Sistema:
        self.slider_volume = ctk.CTkSlider(self.abapreferencias,
                                           from_=0, to=100, # A palavra " From" é restrita do pythom  - para não da conflito se usar o " _ ",que fica "from_"
                                           fg_color="green",                 
                                            button_hover_color="Darkgreen",
                                            command=self.atualizar_volume) 
        self.label_volume.pack(pady=(30, 5))                                 
        self.slider_volume.pack()
        self.slider_volume.set(50)

        self.label_valor_volume = ctk.CTkLabel(self.abapreferencias,
                                         text="50%")
        self.label_valor_volume.pack()     
        

    def construir_abasistemas(self):
        self.abasistemas = self.janelas_abas.tab("Dashboard")
        self.label_carregamento = ctk.CTkLabel(self.abasistemas,
                                               text="Testar Carregamento do Sistema",
                                               font=ctk.CTkFont(size=16, family="Courier"))
        self.label_carregamento.pack(pady=(30,30))

        self.barra_progresso = ctk.CTkProgressBar(self.abasistemas,
                                                  width = 400)
        self.barra_progresso.pack(pady=(10, 10))
        self.barra_progresso.set(0)

        self.botao_progresso = ctk.CTkButton(self.abasistemas,
                                             text = "Iniciar Carregamento",
                                             fg_color="green",
                                             hover_color="Darkgreen",
                                             command =self.carregar_progresso)
        
        self.botao_progresso.pack(pady=(10, 10))

    def ir_para_Dashboard(self):
       self.janelas_abas.set("Dashboard")

    def mudar_modo_dark(self):
        if self.switch_mododark.get() == 1 :
            ctk.set_appearance_mode("Dark")
        else:
             ctk.set_appearance_mode("light")
    
    def salvarperfil(self):
        nome = self.campo_nome.get()
        if self.nivel_usuario.get() == 2:
            nivel = "Admin"
        else:
            nivel = "Básico"
        receber_notificações = self.checkbox_notificacoes.get()
        print("Nome", nome)
        print("Nivel do Usuário", nivel)
        print("Notificação", receber_notificações)
        self.titulo.configure(text = f"{nome} App") # A função ".configure" voçe pode editar configurações dentro de um elemento 
        self.sub_titulo.configure(text = nivel)

    def atualizar_volume(self, novo_valor_volume):
        self.label_valor_volume.configure(text = f"{int(novo_valor_volume)}%")
    
    def carregar_progresso(self):
        for i in range(100):
            # executar uma tarefa que demora 
            time.sleep(0.1) # A biblioteca time, foi usada pra cada vez que houve uma interação do "for" rodar, por tras dos panos ela ta atualizando  
            self.barra_progresso.set((i + 1) / 100)
            self.update() # usado para atualizar a interface da janela 


janela = Aplicativo()
janela.mainloop()


