import pandas as pd
from twilio.rest import Client


# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACc4f092c727d97f0a18c2971f39b35380"
auth_token  = "06820ba881a50a99f536ff3c17acbbfc"
client = Client(account_sid, auth_token)

#instalar as bibliotecas
#pandas
#openpyxl
#twillio manda sms


# Passo a passo e solução 

#Abrir os 6 arquivos em excel 
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    
    if (tabela_vendas['Vendas'] > 55000).any():
        vendendor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f' No mes {mes} alguém bateu a beta. Vendedor: {vendendor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5583988761221",
            from_="+14784107527",
            body=f' No mes {mes} alguém bateu a beta. Vendedor: {vendendor}, Vendas: {vendas}')

        print(message.sid)





#para a cada arquivo : 

#verificar se algum valor na coluna vendas é maior que 55 mil .

#se for maior que 55 mil -> enviar sms com o nome e mês e as dele. 

#caso não seja maior que 55 mil não quero fazer nada. 