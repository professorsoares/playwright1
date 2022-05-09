# https://www.youtube.com/watch?v=CK6MWehq7vI
# pandas, openpyxl


from playwright.sync_api import sync_playwright
import pandas as pd
import time
import pyautogui as pagui
import pandas as pd

#dado = pd.read_excel("DadosRH.xlsx", engine='xlrd')

# df = pd.read_csv("DadosRH.csv", sep=";")
df = pd.read_excel(r"dadosValeSocial.xlsx", engine='openpyxl')
#, sheet_name=0, engine='openpyxl', index_col=0
print(len(df))
print((df.dtypes))
nome = "Bruno.soares"

df = df[df.Nome == nome.split(".")[0]]
print(df.head(5))

# Caso a data não venha como DateTime,
# precisa forçar cnversão na importação ou converter com pd.to_datetime(df['Nome_Campo']) .

df = df[df.Nome == nome.split(".")[0]]
df = df[df.Lancado != "s"]
for i in df.index:
    #print("Nome: {df["Nome"][i]} Data " + str(df["Data"][i]).replace("/", ""))
    print(f'ID: {df["ID"][i]} - Nome: {df["Nome"][i]} - Data:' + str((df["Data"]).dt.strftime('%d%m%Y')[i]))
    #pagui.write(str(df["Data"][i]).replace("/", ""), interval=0.30)
    # pagui.1ait_for_timeout(2000)
