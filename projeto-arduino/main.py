from ast import arg
from shutil import which

import customtkinter as ctk
from tkinter import ttk, messagebox
from random import choice
from datetime import datetime



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sistema de Gerenciamento de Máquinas Agrícolas")
app.geometry("1200x700")
app.resizable(False,False)

ARQUIVO_FROTAS = "frotas.txt"
ARQUIVO_MONITORAMENTO = "monitoramento.txt"
ARQUIVO_INSUMOS= "insumos.txt"
ARQUIVO_FORNECEDORES = "Fornecedores.txt"


# funções

def mostrar_tela(nome):
    TelaPrincipal_frame.pack_forget()
    frota_frame.pack_forget()
    fornecedores_frame.pack_forget()
    insumos_frame.pack_forget()

    if nome == "Menu":
        TelaPrincipal_frame.pack(fill="both", expand=True, padx=10, pady=10)

    elif nome == "frota":
        frota_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
    
    elif nome == "fornecedores":
        fornecedores_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    elif nome == "insumos":
        insumos_frame.pack(fill="both", expand=True, padx=10, pady=10)

        

def atualizar_menu():
    try:
        with open(ARQUIVO_FROTAS, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()
            total = len(linhas)
    except:
        total = 0

    total_frotas_label.configure(text=f" Total de Máquinas: {total}")


def cadastrar_frota():

    codigo = entry_codigo.get()
    tipo = combo_tipo.get()
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    ano = entry_ano.get()
    status = combo_status.get()

    if codigo == "" or tipo == "":
        messagebox.showerror(
            "Erro",
            "Preencha os campos obrigatórios."
        )
        return

    with open(ARQUIVO_FROTAS, "a", encoding="utf-8") as arq:
        arq.write(
            f"{codigo};{tipo};{marca};{modelo};{ano};{status}\n"
        )

    messagebox.showinfo(
        "Sucesso",
        "Máquina cadastrada!"
    )

    limpar_campos()
    carregar_frotas()
    atualizar_menu()
    
def alterar_frota():

    selected = tabela.focus()

    if not selected:
        messagebox.showerror(
            "Erro",
            "Selecione uma máquina para alterar."
        )
        return

    valores = tabela.item(selected, "values")
    codigo_original = valores[0]

    marca = entry_marca.get()
    modelo = entry_modelo.get()
    ano = entry_ano.get()
    tipo = combo_tipo.get()
    status = combo_status.get()
    codigo = entry_codigo.get()

    frotas = []

    with open(ARQUIVO_FROTAS, "r", encoding="utf-8") as arq:
        for linha in arq:
            dados = linha.strip().split(";")

            if dados[0] == codigo_original:
                frotas.append(
                    f"{codigo};{tipo};{marca};{modelo};{ano};{status}\n"
                )
            else:
                frotas.append(linha)

    with open(ARQUIVO_FROTAS, "w", encoding="utf-8") as arq:
        arq.writelines(frotas)

    carregar_frotas()

    messagebox.showinfo(
        "Sucesso",
        "Máquina alterada!"
    )


def limpar_campos():
    entry_codigo.delete(0, "end")
    entry_marca.delete(0, "end")
    entry_modelo.delete(0, "end")
    entry_ano.delete(0, "end")
    combo_tipo.set("")
    combo_status.set("")

def excluir_frota():
    
    selected = tabela.focus()
    
    if not selected:
        messagebox.showerror(
            "Erro",
            "selecione uma máquina para excluir."
        )
        return
    valores = tabela.item(selected, "values")
    codigo = valores[0]
    frotas = []
    with open(ARQUIVO_FROTAS, "r", encoding="utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split(";")

                if dados[0] != codigo:
                    frotas.append(linha)
    with open(ARQUIVO_FROTAS, "w", encoding="utf-8") as arq:
            arq.writelines(frotas)
    carregar_frotas()
    atualizar_menu()
    
    messagebox.showinfo(
        "Sucesso",
        "Máquina excluída!"
    )
def carregar_frotas():

    tabela.delete(*tabela.get_children())

    try:
        with open(ARQUIVO_FROTAS, "r", encoding="utf-8") as arq:

            for linha in arq:

                dados = linha.strip().split(";")

                tabela.insert(
                    "",
                    "end",
                    values=dados
                )
    except:
        pass
    
    
    #insumos

#insumos

def Cadastrar_Insumos():

    nome = entry_insumo_nome.get()
    quantidade = entry_quantidade.get()
    status = combo_insumo_status.get()
    
    
    if(nome == "" or quantidade == "" ):
        messagebox.showerror(
            "Erro",
            "preencha os campos obrigatórios."
        )
        return
    
    with open(ARQUIVO_INSUMOS, "a", encoding="utf-8") as arq:
        arq.write(f"{nome}; {quantidade}; {status}\n")
        
    carregar_insumos()
    limpar_insumos()
    
    messagebox.showinfo(
        "Sucesso",
        "insumo cadastrado"
        )
  

def alterar_insumos():

    selected = tabela_insumos.focus()

    if not selected:
        messagebox.showerror(
            "Erro",
            "Selecione um insumo."
        )
        return

    valores = tabela_insumos.item(selected, "values")

    nome_original = valores[0]

    nome = entry_insumo_nome.get()
    quantidade = entry_quantidade.get()
    status = combo_insumo_status.get()

    insumos = []

    with open(ARQUIVO_INSUMOS, "r", encoding="utf-8") as arq:

        for linha in arq:

            dados = linha.strip().split(";")

            if dados[0] == nome_original:

                insumos.append(
                    f"{nome};{quantidade};{status}\n"
                )

            else:
                insumos.append(linha)

    with open(ARQUIVO_INSUMOS, "w", encoding="utf-8") as arq:
        arq.writelines(insumos)

    carregar_insumos()

    messagebox.showinfo(
        "Sucesso",
        "Insumo alterado!"
    )
    
def carregar_insumos():
    tabela_insumos.delete(*tabela_insumos.get_children())
    
    try:
        with open(ARQUIVO_INSUMOS, "r", encoding = "utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split(";")
                
                tabela_insumos.insert(
                    "",
                    "end",
                    values=dados
                )
    except:
            
        pass
    
def excluir_insumos():
    selected = tabela_insumos.focus()
    
    if not selected:
        messagebox.showerror(
            "Erro",
            "Selecione um insumo para excluir."
        )
        return
    
    valores = tabela_insumos.item(selected, "values")
    nome = valores[0]
    
    insumos = []

    
    with open(ARQUIVO_INSUMOS, "r", encoding="utf-8") as arq:
        for linha in arq:
            dados = linha.strip().split(";")
            
            if dados[0] != nome:
                insumos.append(linha)
    
    with open(ARQUIVO_INSUMOS, "w", encoding="utf-8") as arq:
        arq.writelines(insumos)
    
    carregar_insumos()
    
    messagebox.showinfo(
        "Sucesso",
        "Insumo excluído!"
    )
    
    
def limpar_insumos():
    entry_insumo_nome.delete(0, "end")
    entry_quantidade.delete(0, "end")
    combo_insumo_status.set("")
    
    

#Funções fornecedores

def carregar_fornecedores():
    tabela_fornecedor.delete(*tabela_fornecedor.get_children())
    try:
        with open(ARQUIVO_FORNECEDORES, "r", encoding="utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split(";")
                if dados:
                    tabela_fornecedor.insert("", "end", values=dados)
    except:
        pass

def cadastrar_fornecedor():

    ID = entry_id.get()
    NOME = entry_nome.get()
    CEP = entry_cep.get()
    TELEFONE = entry_telefone.get()
    EMAIL = entry_email.get()
    
    
    if ID == "" or NOME == "" or CEP == "" or TELEFONE == "" or EMAIL == "":
        messagebox.showerror(
            "Erro",
            "Preencha os campos obrigatórios."
        )
        return

    with open(ARQUIVO_FORNECEDORES, "a", encoding="utf-8") as arq:
        arq.write(f"{ID};{NOME};{CEP};{TELEFONE};{EMAIL}\n")

    carregar_fornecedores()
    messagebox.showinfo(
        "Sucesso",
        "Fornecedor cadastrada!"
    )
    
    entry_id.delete(0, "end")
    entry_nome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")
    entry_cep.delete(0, "end")

def deletar_fornecedor():
     selected = tabela_fornecedor.focus()
     if not selected:
        messagebox.showerror("Erro", "Selecione um fornecedor para excluir!")
        return
    
     if not messagebox.askyesno("Confirmar", "Deseja realmente excluir este fornecedor?"):
        return
    
     valores = tabela_fornecedor.item(selected, "values")
     id_fornecedor = valores[0]
    
     fornecedores = []
     with open(ARQUIVO_FORNECEDORES, "r", encoding="utf-8") as arq:
        for linha in arq:
            if linha.strip():
                dados = linha.strip().split(";")
                if dados[0] != id_fornecedor:
                    fornecedores.append(linha)
    
     with open(ARQUIVO_FORNECEDORES, "w", encoding="utf-8") as arq:
        arq.writelines(fornecedores)
    
     carregar_fornecedores()
    
     messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")

def alterar_fornecedor():
    selected = tabela_fornecedor.focus()
    if not selected:
        messagebox.showerror("Erro", "Selecione um fornecedor para alterar.")
        return
    
    valores = tabela_fornecedor.item(selected, "values")
    id_original = valores[0]   # ID do fornecedor selecionado na tabela

    ID = entry_id.get()
    NOME = entry_nome.get()
    CEP = entry_cep.get()
    TELEFONE = entry_telefone.get()
    EMAIL = entry_email.get()

    if ID == "" or NOME == "" or CEP == "" or TELEFONE == "" or EMAIL == "":
        messagebox.showerror("Erro", "Preencha os campos obrigatórios.")
        return

    fornecedores = []

    with open(ARQUIVO_FORNECEDORES, "r", encoding="utf-8") as arq:
        for linha in arq:
            if not linha.strip():
                continue
            dados = linha.strip().split(";")

            if dados[0] == id_original:
                fornecedores.append(f"{ID};{NOME};{CEP};{TELEFONE};{EMAIL}\n")
            else:
                fornecedores.append(linha)

    with open(ARQUIVO_FORNECEDORES, "w", encoding="utf-8") as arq:
        arq.writelines(fornecedores)

    carregar_fornecedores()
   
    entry_id.delete(0, "end")
    entry_nome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")
    entry_cep.delete(0, "end")

    messagebox.showinfo("Sucesso", "Fornecedor alterado!")
    
def limpar_fornecedor():
    entry_id.delete(0, "end")
    entry_nome.delete(0, "end")
    entry_cep.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")



#monitoramento 

temperaturas = list(range(18, 41))
umidades = list(range(30, 91))


def monitorar():

    temp = choice(temperaturas)
    umi = choice(umidades)

    luz = choice([
        "Adequada",
        "Baixa"
    ])

    temperatura_label.configure(
        text=f"🌡 Temperatura: {temp}°C"
    )

    umidade_label.configure(
        text=f"💧 Umidade: {umi}%"
    )

    iluminacao_label.configure(
        text=f"💡 Iluminação: {luz}"
    )


    hora = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    horario_label.configure(
        text=f"⏰ Atualizado: {hora}"
    )

    with open(
        ARQUIVO_MONITORAMENTO,
        "a",
        encoding="utf-8"
    ) as arq:

        arq.write(
            f"{hora};"
            f"{temp};"
            f"{umi};"
            f"{luz};"
        
        )

    app.after(
        5000,
        monitorar
    )


#menu lateral

menu = ctk.CTkFrame(
    app,
    width=220
)

menu.pack(
    side="left",
    fill="y"
)

titulo_menu = ctk.CTkLabel(
    menu,
    text="FAZENDA",
    font=("Arial", 22, "bold")
)

titulo_menu.pack(
    pady=20
)

btn_dashboard = ctk.CTkButton(
    menu,
    text=" Monitoramento",
    command=lambda: mostrar_tela("Menu")
)

btn_dashboard.pack(
    padx=10,
    pady=10,
    fill="x"
)

btn_frota = ctk.CTkButton(
    menu,
    text=" Cadastro de Frotas",
    command=lambda: mostrar_tela("frota")
)

btn_frota.pack(
    padx=10,
    pady=10,
    fill="x"
)
btn_insumos = ctk.CTkButton(
    menu,
    text=" Insumos",
    command=lambda: mostrar_tela("insumos")
)

btn_insumos.pack(
    padx=10,
    pady=10,
    fill="x"

)

btn_fornecedores = ctk.CTkButton(
    menu,
    text= "Fornecedores",
    command=lambda:mostrar_tela("fornecedores")
)

btn_fornecedores.pack(
    padx=10,
    pady=10,
    fill="x"
)

principal = ctk.CTkFrame(app)
principal.pack(
    side="right",
    fill="both",
    expand=True
)



#tela

TelaPrincipal_frame = ctk.CTkFrame(principal)

titulo_dash = ctk.CTkLabel(
    TelaPrincipal_frame,
    text="Monitoramento",
    font=("Arial", 28, "bold")
)

titulo_dash.pack(
    pady=20
)

total_frotas_label = ctk.CTkLabel(
    TelaPrincipal_frame,
    text=" Total de Máquinas: 0",
    font=("Arial", 20)
)

total_frotas_label.pack(
    pady=10
)

temperatura_label = ctk.CTkLabel(
    TelaPrincipal_frame,
    text="🌡 Temperatura: --",
    font=("Arial", 20)
)

temperatura_label.pack(
    pady=5
)

umidade_label = ctk.CTkLabel(
    TelaPrincipal_frame,
    text="💧 Umidade: --",
    font=("Arial", 20)
)

umidade_label.pack(
    pady=5
)

iluminacao_label = ctk.CTkLabel(
    TelaPrincipal_frame,
    text="💡 Iluminação: --",
    font=("Arial", 20)
)

iluminacao_label.pack(
    pady=5
)


horario_label = ctk.CTkLabel(
    TelaPrincipal_frame,
    text="",
    font=("Arial", 16)
)

horario_label.pack(
    pady=10
)

#Cadastro de Frota 

frota_frame = ctk.CTkFrame(principal)

titulo_frota = ctk.CTkLabel(
    frota_frame,
    text="Cadastro de Máquinas",
    font=("Arial", 26, "bold")
)

titulo_frota.pack(
    pady=15
)

form = ctk.CTkFrame(frota_frame)
form.pack(
    padx=10,
    pady=10,
    fill="x"
)

ctk.CTkLabel(
    form,
    text="Código"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

entry_codigo = ctk.CTkEntry(form)
entry_codigo.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form,
    text="Tipo"
).grid(
    row=1,
    column=0
)

combo_tipo = ctk.CTkComboBox(
    form,
    values=[
        "Trator",
        "Colheitadeira",
        "Caminhonete",
        "Pulverizador"
    ]
   
)

combo_tipo.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form,
    text="Marca"
).grid(
    row=2,
    column=0
)

entry_marca = ctk.CTkEntry(form)
entry_marca.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form,
    text="Modelo"
).grid(
    row=3,
    column=0
)

entry_modelo = ctk.CTkEntry(form)
entry_modelo.grid(
    row=3,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form,
    text="Ano"
).grid(
    row=4,
    column=0
)

entry_ano = ctk.CTkEntry(form)
entry_ano.grid(
    row=4,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form,
    text="Status"
).grid(
    row=5,
    column=0
)

combo_status = ctk.CTkComboBox(
    form,
    values=[
        "Disponível",
        "Operando",
        "Manutenção"
    ]
)

combo_status.grid(
    row=5,
    column=1,
    padx=5,
    pady=5
)


#botões de ação frota 

btn_cadastrar = ctk.CTkButton(
    form,
    text="Cadastrar",
    command=cadastrar_frota
)

btn_cadastrar.grid(
    row=2,
    column=2,
    columnspan=1,
    pady=10,
    padx=5
   
)
btn_alterar = ctk.CTkButton(
    form,
    text="Alterar",
    command=alterar_frota
)

btn_alterar.grid(
    row=3,
    column=2,
    columnspan=1,
    pady=10,
    padx=10
    
)

btn_limpar = ctk.CTkButton(
    form,   
    text="Limpar Campos",
    command=limpar_campos
)

btn_limpar.grid(
    row=2,
    column=2,
    columnspan=3,
    pady=10,
    padx=150
)
btn_excluir = ctk.CTkButton(
    form,
    text="Excluir",
    command=excluir_frota
)
btn_excluir.grid(
    row=3, 
    column=2,
    columnspan=3,
    pady=10,
    padx=250
)


#Tabela de frota

style = ttk.Style()

style.theme_use("default")

style.configure(
    "Treeview",
    background="#1E1E1E",
    foreground="white",
    fieldbackground="#0B1738",
    rowheight=25
)

frame_tabela = ctk.CTkFrame(
    frota_frame
)

frame_tabela.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

colunas = (
    "Código",
    "Tipo",
    "Marca",
    "Modelo",
    "Ano",
    "Status"
)

tabela = ttk.Treeview(
    frame_tabela,
    columns=colunas,
    show="headings"
)

for col in colunas:
    tabela.heading(
        col,
        text=col
    )
    tabela.column(
        col,
        width=120
    )

tabela.pack(
    fill="both",
    expand=True
)


# Tela fornecedores
fornecedores_frame = ctk.CTkFrame(principal)

titulo_fornecedores = ctk.CTkLabel(
    fornecedores_frame,
    text= "Cadastro de fornecedores",
    font=("Arial",26,"bold")
)

titulo_fornecedores.pack(
    pady = 15
)

form = ctk.CTkFrame(fornecedores_frame)
form.pack(
    padx = 10,
    pady = 10,
    fill ="x"
)

ctk.CTkLabel(
    form,
    text= "ID fornecedor"
).grid(row =1, column = 0)

entry_id = ctk.CTkEntry(form)
entry_id.grid(
    row =1,
    column = 1,
    padx = 5,
    pady= 5
)

ctk.CTkLabel(
    form,
    text= "Nome do fornecedor",
).grid(row = 2, column=0)

entry_nome = ctk.CTkEntry(form)
entry_nome.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form,
    text= "CEP do fornecedor",
).grid(
    row = 3,
    column = 0
)

entry_cep = ctk.CTkEntry(form)
entry_cep.grid(
    row = 3,
    column = 1,
    padx = 5,
    pady = 5
)

ctk.CTkLabel(
    form,
    text= "Telefone do fornecedor",
).grid(row = 4, column = 0)

entry_telefone = ctk.CTkEntry(form)
entry_telefone.grid(
    row = 4,
    column = 1,
    padx = 5,
    pady = 5
)

ctk.CTkLabel(
    form,
    text= "Email do fornecedor"
).grid(row =5, column = 0)

entry_email =ctk.CTkEntry(form)
entry_email.grid(
    row = 5,
    column = 1,
    padx = 5,
    pady =5
)



#Cadastro fornecedores 

btn_cadastrar = ctk.CTkButton(
    form,
    text="Cadastrar",
    command=cadastrar_fornecedor
)
btn_cadastrar.grid(
    row=2,
    column=2,
    columnspan=1,
    pady=10,
    padx=5
)

btn_deletar = ctk.CTkButton(
    form,
    text= "deletar",
    command= deletar_fornecedor
)

btn_deletar.grid(
    row =3,
    column = 2,
    columnspan=1,
    pady=10,
    padx=5
)

btn_alterar = ctk.CTkButton(
    form,
    text= "Alterar",
    command= alterar_fornecedor
)

btn_alterar.grid(
    row =4,
    column = 2,
    columnspan=1,
    pady=10,
    padx=5
)

btn_Limpar = ctk.CTkButton(
    form,
    text="Limpar Campos",
    command=limpar_fornecedor
)
btn_Limpar.grid(
    row=5,
    column=2,
    columnspan=1,
    pady=10,
    padx=5)




#tabela fornecedor

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview",
    background="#1E1E1E",
    foreground="white",
    fieldbackground="#0B1738",
    rowheight=25
)

# 2. FRAME PARA A TABELA
frame_tabela_fornecedor = ctk.CTkFrame(
    fornecedores_frame  # ← DENTRO DO FRAME DE FORNECEDORES
)

frame_tabela_fornecedor.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# 3. COLUNAS DA TABELA
colunas_fornecedor = (
    "ID",
    "Nome",
    "CEP",
    "Telefone",
    "Email"
)

# 4. CRIAÇÃO DA TABELA
tabela_fornecedor = ttk.Treeview(
    frame_tabela_fornecedor,
    columns=colunas_fornecedor,
    show="headings"
)

# 5. CONFIGURAÇÃO DOS CABEÇALHOS
for col in colunas_fornecedor:
    tabela_fornecedor.heading(
        col,
        text=col
    )
    tabela_fornecedor.column(
        col,
        width=120
    )

# 6. EXIBIÇÃO DA TABELA
tabela_fornecedor.pack(
    fill="both",
    expand=True
)


# TELA INSUMOS


insumos_frame = ctk.CTkFrame(principal)

titulo_insumos = ctk.CTkLabel(
    insumos_frame,
    text="Cadastro de Insumos",
    font=("Arial", 26, "bold")
)

titulo_insumos.pack(pady=15)

form_insumos = ctk.CTkFrame(insumos_frame)

form_insumos.pack(
    padx=10,
    pady=10,
    fill="x"
)

ctk.CTkLabel(
    form_insumos,
    text="Nome"
).grid(row=0, column=0, padx=5, pady=5)

entry_insumo_nome = ctk.CTkEntry(form_insumos)

entry_insumo_nome.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form_insumos,
    text="Quantidade"
).grid(row=1, column=0)

entry_quantidade = ctk.CTkEntry(form_insumos)

entry_quantidade.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)

ctk.CTkLabel(
    form_insumos,
    text="Status"
).grid(row=2, column=0)

combo_insumo_status = ctk.CTkComboBox(
    form_insumos,
    values=[
        "Disponível",
        "Baixo",
        "Em falta"
    ]
)

combo_insumo_status.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)

# BOTÕES

ctk.CTkButton(
    form_insumos,
    text="Cadastrar",
    command=Cadastrar_Insumos
).grid(row=0, column=2, padx=10)

ctk.CTkButton(
    form_insumos,
    text="Alterar",
    command=alterar_insumos
).grid(row=1, column=2, padx=10)

ctk.CTkButton(
    form_insumos,
    text="Excluir",
    command=excluir_insumos
).grid(row=2, column=2, padx=10)

ctk.CTkButton(
    form_insumos,
    text="Limpar",
    command=limpar_insumos
).grid(row=3, column=2, padx=10)

# TABELA

frame_tabela_insumos = ctk.CTkFrame(insumos_frame)

frame_tabela_insumos.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

colunas_insumos = (
    "Nome",
    "Quantidade",
    "Status"
)

tabela_insumos = ttk.Treeview(
    frame_tabela_insumos,
    columns=colunas_insumos,
    show="headings"
)

for col in colunas_insumos:

    tabela_insumos.heading(
        col,
        text=col
    )

    tabela_insumos.column(
        col,
        width=180
    )

tabela_insumos.pack(
    fill="both",
    expand=True
)


mostrar_tela("Menu")

carregar_frotas()
atualizar_menu()
monitorar()
carregar_fornecedores()
carregar_insumos()

app.mainloop()
