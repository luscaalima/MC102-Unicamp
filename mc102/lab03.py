###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Lucas Lima Pinheiro
# RA: 263267
###################################################


dayWeek = int(input())
startTime = int(input())
startMinutes = int(input())
studentOrNot = str(input())
payment = str(input())

# NOTURNO ->TRUE
# VESPERTINO ->FALSE

def vespertinoOuNoturno(hora, minutos):
    if hora < 18:
        return False
    elif hora == 18:
        if minutos >= 30:
            return True
        else:
            return False
    elif hora > 18:
        return True

def valorStudentVespertino(diaSemana: int):

    if diaSemana ==1 or diaSemana == 7:
        return 15
    elif diaSemana ==2 or diaSemana == 3:
        return 7.5
    elif diaSemana ==4 or diaSemana == 5 or diaSemana == 6:
        return 10
 
def valorStudentNoturno(diaSemana: int):

    if diaSemana ==1:
        return 15
    elif diaSemana ==2 or diaSemana == 3 :
        return 10
    elif diaSemana ==4 or diaSemana == 5 :
        return 15
    elif diaSemana ==6 or diaSemana == 7 :
        return 20
   
def  valorIngressoParaEstudante(flag:bool,diaSemana:int):
    #NOTURNO
 if flag:
     return valorStudentNoturno(diaSemana)
 else:
  return valorStudentVespertino(diaSemana)

def getValorIngressoNoturno(diaSemana:int):

    if diaSemana ==1 or diaSemana ==4 or diaSemana == 5:
        return 30
    elif diaSemana ==2 or diaSemana == 3:
        return 20
    elif diaSemana==6 or  diaSemana ==7:
        return 40

def getDescontoNoturno(diaSemana:int):

    if diaSemana ==1 or diaSemana ==6:
        return 30
    elif diaSemana ==2 or diaSemana == 3 or diaSemana==4 or diaSemana==5:
        return 50
    elif diaSemana ==7:
        return 20
    
def getDescontoVespertino(diaSemana:int):

    if diaSemana ==1:
        return 30
    elif diaSemana ==2 or diaSemana == 3 or diaSemana==4 or diaSemana==5 or diaSemana==6:
        return 50
    elif diaSemana ==7:
        return 20    
    
def getValorIngressoVespertino(diaSemana:int):

    if diaSemana ==1 or diaSemana ==7:
        return 30
    elif diaSemana ==2 or diaSemana == 3 or diaSemana==4:
        return 15
    elif diaSemana ==5 or diaSemana == 6:
        return 20

ingresso = 0

# ESTUDANTE
if studentOrNot.upper() == "S":
    ingresso = valorIngressoParaEstudante(vespertinoOuNoturno(startTime,startMinutes),dayWeek)
    
#NÃO ESTUDANTE 
else:
#NOTURNO   E (DOMINGO OU QUARTA OU QUINTA) INGRESSO MESMO VALOR
    if vespertinoOuNoturno(startTime,startMinutes) and ( dayWeek == 1  or dayWeek == 4 or dayWeek ==5):
        ingresso = getValorIngressoNoturno(dayWeek)
        if payment.upper() == "C":
            desconto = getDescontoNoturno(dayWeek)
            ingresso =  ingresso - (ingresso*(desconto/100))
#NOTURNO   E (SEGUNDA OU TERÇA) INGRESSO MESMO VALOR            
    elif vespertinoOuNoturno(startTime,startMinutes) and ( dayWeek == 2  or dayWeek == 3):
        ingresso = getValorIngressoNoturno(dayWeek)
        if payment.upper() == "C":
            desconto = getDescontoNoturno(dayWeek)
            ingresso =  ingresso - (ingresso*(desconto/100))  
#NOTURNO   E (SEXTA OU SABADO) INGRESSO MESMO VALOR            
    elif vespertinoOuNoturno(startTime,startMinutes) and ( dayWeek == 6  or dayWeek == 7):
        ingresso = getValorIngressoNoturno(dayWeek)
        if payment.upper() == "C":
            desconto = getDescontoNoturno(dayWeek)
            ingresso =  ingresso - (ingresso*(desconto/100))          
#VESPERTINO   E (DOMINGO OU SABADO) INGRESSO MESMO VALOR               
    elif vespertinoOuNoturno(startTime,startMinutes)== False and ( dayWeek == 1  or dayWeek == 7):
      ingresso = getValorIngressoVespertino(dayWeek)
      if payment.upper() == "C":
            desconto = getDescontoVespertino(dayWeek)
            ingresso =  ingresso - (ingresso*(desconto/100))
#VESPERTINO   E (SEGUNDA OU TERCA OU QUARTA) INGRESSO MESMO VALOR               
    elif vespertinoOuNoturno(startTime,startMinutes)== False and ( dayWeek == 2  or dayWeek == 3 or dayWeek == 4):
      ingresso = getValorIngressoVespertino(dayWeek)
      if payment.upper() == "C":
            desconto = getDescontoVespertino(dayWeek)
            ingresso =  ingresso - (ingresso*(desconto/100))
#VESPERTINO   E (QUINTA OU SEXTA) INGRESSO MESMO VALOR               
    elif vespertinoOuNoturno(startTime,startMinutes)== False and ( dayWeek ==5  or dayWeek == 6):
      ingresso = getValorIngressoVespertino(dayWeek)
      if payment.upper() == "C":
            desconto = getDescontoVespertino(dayWeek)
            ingresso =  ingresso - (ingresso*(desconto/100))        
            
print("Valor do ingresso: R$", format(ingresso, ".2f").replace(".", ","))
