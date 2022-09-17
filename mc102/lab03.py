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

dayWeek = int(input())
startTime = int(input())
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


# função retorna o valor do ingresso a depender do dia da semana para estudante
def valorStudentVespertino(diaSemana: int):

    if diaSemana ==1:
        return 15
    elif diaSemana ==2:
        return 7.5
    elif diaSemana ==3:
        return 7.5
    elif diaSemana ==4:
        return 10
    elif diaSemana ==5:
        return 10
    elif diaSemana ==6:
        return 10
    elif diaSemana ==7:
        return 15
 
def valorStudentNoturno(diaSemana: int):

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
        return 20
    elif diaSemana ==7:
        return 20
    

# leitura de dados
ingresso = 0

# ESTUDANTE
if studentOrNot.upper() == "S":
   if vespertinoOuNoturno(startTime, startMinutes):
    ingresso = valorStudentNoturno(dayWeek)
   else:
      ingresso = valorStudentVespertino(dayWeek)
else:
    # DOMINGO
    if dayWeek == 1:
        # DOMINGO NÃO TEM VERIFICAÇÕES
        if payment.upper() == "C":
            ingresso = 30 - (30 * (30 / 100))
        else:
            ingresso = 30
    # SEGUNDA OU TERÇA
    elif dayWeek == 2 or dayWeek ==3:
          # SEGUNDA OU TERÇA NOTURNO
        if vespertinoOuNoturno(startTime, startMinutes):
             if payment.upper() == "C":
              ingresso = 20 - (20 * (50 / 100))
             else:
              ingresso=20    
         # SEGUNDA OU TERÇA VESPERTINO      
        else:
          if payment.upper() == "C":  
            ingresso = 15 - (15 * (50 / 100))
          else:
              ingresso=15    
    # QUARTA
    elif dayWeek == 4:
        # QUARTA NOTURNO
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                ingresso = 30 * (50 / 100)
            else:
                ingresso = 30
         # QUARTA VESPERTINO       
        else:
            if payment.upper() == "C":
                ingresso = 15 - (15 * (50 / 100))
            else:
                ingresso = 15
    # QUINTA
    elif dayWeek == 5:
            # QUINTA NOTURNO
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                ingresso = 30 - (30 * (50 / 100))
            else:
                ingresso = 30
          # QUINTA VESPERTINO        
        else:
            if payment.upper() == "C":
                ingresso = 20 - (20 * (50 / 100))
            else:
                ingresso = 20
    # SEXTA
    elif dayWeek == 6:
        #SEXTA NOTURNO
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                # DESCONTO
                ingresso = 40 - (40 * 30 / 100)
            else:
                ingresso = 40
         #SEXTA VESPERTINO        
        else:
            if payment.upper() == "C":
                ingresso = 20 - (20 * (50 / 100))
            else:
                ingresso = 20
    # SABADO
    elif dayWeek == 7:
          # SABADO NOTURNO
        if vespertinoOuNoturno(startTime, startMinutes):
            if payment.upper() == "C":
                ingresso = 40 - (40 * (20 / 100))
            else:
                ingresso = 40
           # SABADO VESPERTINO       
        else:
            if payment.upper() == "C":
                ingresso = 30 - (30 * (20 / 100))
            else:
                ingresso = 30
                
print("Valor do ingresso: R$", format(ingresso, ".2f").replace(".", ","))
