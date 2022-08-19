# from datetime import date
from datetime import datetime

# data_atual = date.today()
# print(data_atual)

# data_em_texto = print("{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year))

# data_em_texto = print(f"{data_atual.day}/{data_atual.month}/{data_atual.year}")

# data_em_texto = data_atual.strftime("%d/%m/%Y")
# print(data_em_texto)


data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y  %H:%M")

print(data_e_hora_em_texto)
