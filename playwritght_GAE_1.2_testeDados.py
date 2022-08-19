# https://www.youtube.com/watch?v=CK6MWehq7vI
# pandas, openpyxl


from tkinter import Frame
from playwright.sync_api import sync_playwright
import pandas as pd
import time
import pyautogui as pagui
import pyperclip
from datetime import datetime

# import pyperclip
# import platform
#

inicio = datetime.today().strftime('%d/%m/%Y %H:%M:%S:%f')
print(f"INICIO:  {inicio}")

################################################ DEFINIÇÕES ################################################

# nome  = "bruno.soares"
nome = "Bruno.soares"
strMail = "@extreme.digital"

tarefa = "https://gae.extremedigital.com.br/portal/"
linkLancamentos = "https://gae.extremedigital.com.br/gae-web/pages/apropriacao-esforco"
linkPagina = "https://login.microsoftonline.com/"

f = '%d/%m/%Y %H:%M:%S:%f'

MODO_DEBUG = True
############################################################################################################

df = pd.read_excel(r"./Lançamento_Horas_Equipe - Junho22.xlsx",
                   engine='openpyxl',
                   date_parser='Data',
                   sheet_name='Monica'
                   )

#print(df.describe())
#print(df.dtypes)


dfGAE = df[["Projeto GAE", "Cliente", "Descrição", "Data", "Horas", "Lancado"]]

#print(dfGAE.count())
#print(dfGAE.describe)
teste = dfGAE.loc[dfGAE["Lancado"] == "Não"]
#teste = dfGAE.query("Lancado == ''")
print(teste.describe)

#df = df[df.Nome == 'Aline']
dfGAE = dfGAE.loc[dfGAE["Lancado"] == "Não"].sort_values(by=['Data'])

for i in dfGAE.index:
    print("->: " +
          str(dfGAE["Projeto GAE"][i]) + "-" +
          str(dfGAE["Cliente"][i]) + "-" +
          str(dfGAE["Data"][i].strftime("%d/%m/%Y"))
          + " -" + str(dfGAE["Horas"][i])
          + " - " + str(str(dfGAE["Horas"][i]).split(".").__len__())
          )

    dataFormatada = str(dfGAE["Data"][i].strftime("%d/%m/%Y"))
    projeto = str(dfGAE["Projeto GAE"][i])
    cliente = str(dfGAE["Cliente"][i])
    descricao = str(dfGAE["Descrição"][i])


    if str(dfGAE["Horas"][i]).split(".").__len__() == 2:
        esforcoHora = ("0"+str(dfGAE["Horas"][i]).split(".")[0])[slice(2)]
        esforcoMinuto = "30" if str(dfGAE["Horas"][i]).split(".")[1] == 5 else "00"
