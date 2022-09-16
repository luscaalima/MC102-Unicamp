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
# # 1 a 60
startMinutes = int(input())
studentOrNot = str(input())
payment = str(input())

#  18h30m -> Noturno
#  18h29m -> Vespertino

# s -> ESTUDANTE
# n -> NÃO ESTUDANTE

# D -> DINHEIRO
# C -> CARTÃO


def vespertinoOuNoturno(hora, minutos):
    if hora < 18:
        # VESPERTINO
        return False
    elif hora == 18:
        if minutos >= 30:
            # NOTURNO
            return True
        else:
            # VESPERTINO
            return False
    elif hora > 18:
        # NOTURNO
        return True


#  match diaSemana:
#             case 1:
#                 return 'DOMINGO'
#             case 2:
#              return 'SEGUNDA'
#             case 3:
#                 return 'TERÇA'
#             case 4:
#                 return 'QUARTA'
#             case 5:
#                  return 'QUINTA'
#             case 6:
#                 return 'SEXTA'
#             case 7:
#               return "SABADO"
#             case _:
#               return -1

# função retorna o valor do ingresso a depender do dia da semana para estudante
def valorStudent(diaSemana: int):

    if diaSemana ==1:
        return 15
    elif diaSemana ==2:
        return 10
    elif diaSemana ==3:
        return 10
    elif diaSemana ==4:
        return 15
    elif diaSemana ==5:
        return 15
    elif diaSemana ==6:
        return 10
    elif diaSemana ==7:
        return 20
    

# leitura de dados
ingresso = 0

# ESTUDANTE
if studentOrNot.upper() == "S":
    ingresso = valorStudent(dayWeek)
else:
    # DOMINGO
    if dayWeek == 1:
        # DOMINGO NÃO TEM VERIFICAÇÕES

        if payment.upper() == "C":
            ingresso = 30 - (30 * (30 / 100))
        else:
            ingresso = 30
            # if vespertinoOuNoturno(startTime,startMinutes) :
            #     print("DOMINGO NOTURNO")
            # else :
            #  print("DOMINGO VESPERTINO")
        # SEGUNDA
    elif dayWeek == 2:
        if vespertinoOuNoturno(startTime, startMinutes):
            ingresso = 20 - (20 * (50 / 100))
        else:
            ingresso = 15 - (15 * (50 / 100))
    # TERÇA
    elif dayWeek == 3:
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                ingresso = 20 - (20 * (50 / 100))
            else:
                ingresso = 20
        else:
            if payment.upper() == "C":
                ingresso = 15 - (15 * (50 / 100))
            else:
                ingresso = 15
    # QUARTA
    elif dayWeek == 4:
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                ingresso = 30 * (50 / 100)
            else:
                ingresso = 30
        else:
            if payment.upper() == "C":
                ingresso = 15 - (15 * (50 / 100))
            else:
                ingresso = 15
    # QUINTA
    elif dayWeek == 5:
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                ingresso = 30 - (30 * (50 / 100))
            else:
                ingresso = 30
        else:
            if payment.upper() == "C":
                ingresso = 20 - (20 * (50 / 100))
            else:
                ingresso = 20
    # SEXTA
    elif dayWeek == 6:
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                # DESCONTO
                ingresso = 40 - (40 * 30 / 100)
            else:
                ingresso = 40
        else:
            if payment.upper() == "C":
                ingresso = 20 - (20 * (50 / 100))
            else:
                ingresso = 20
    # SABADO
    elif dayWeek == 7:
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                ingresso = 40 - (40 * (20 / 100))
            else:
                ingresso = 40
        else:
            if payment.upper() == "C":
                ingresso = 30 - (30 * (20 / 100))
            else:
                ingresso = 30

# saída do valor do ingresso
print("Valor do ingresso: R$", format(ingresso, ".2f").replace(".", ","))
