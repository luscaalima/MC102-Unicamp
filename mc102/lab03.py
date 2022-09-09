###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Lucas Lima Pinheiro
# RA: 263267
###################################################

# <Dia da semana>
# <Hora de início da sessão>
# <Minuto de início da sessão>
# <Estudante>
# <Método de pagamento>

# 1 a 07
dayWeek = int(input())
# 0 a 24
startTime = int(input())
# 1 a 60
startMinutes = int(input())

studentOrNot = str(input())

payment = str(input())


def vespertinoOuNoturno(hora, minutos):
    if (hora >= 18 and minutos > 30) or (hora > 18):
        return True
    else:
        return False


# leitura de dados
priceTicket = 0
# DOMINGO E NÃO ESTUDANTE
# if dayWeek == 1 and studentOrNot == "n":
#     priceTicket = 30.00 * (3/10)

# SEGUNDA-FEIRA
# elif dayWeek == 2 and  vespertinoOuNoturno(startTime,startMinutes) :
#     print("")

# valor do ingresso inteiro

# print("Valor do ingresso", priceTicket)


print('olhar aqui', vespertinoOuNoturno(startTime, startMinutes))
# valor a pagar


# saída do valor do ingresso
# print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))
