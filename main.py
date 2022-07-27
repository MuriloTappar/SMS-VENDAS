# pip install Twilio
#pip install openpyxl
#pip install pandas
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC23ce6e20d1b0ed82a2dea64286a615fb"
# Your Auth Token from twilio.com/console
auth_token  = "adadc3c96b65a54ea52124d2c76d0330"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5551996814901",
            from_="+12184034867",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
