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

# print('->',type(dayWeek))


# def qualDiaE(diaSemana:int):
    
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
def valorStudent(diaSemana:int):
    
 match diaSemana:
            case 1:
                return 15
            case 2 : 
            #  case 3:
             return 10
            case 3:
                return 10    
            case 4:
                return 15
            case 5:
                 return 15
            case 6:
                return 20 
            case 7:
              return 20
            case _:
              return -1  
      
      

                    
   

# leitura de dados
priceTicket = 0

#ESTUDANTE
if studentOrNot =='s':
   print('estudante')
   priceTicket=valorStudent(dayWeek)
else:   
 print('não estudante') 
    #DOMINGO
 if dayWeek == 1 :
     #DOMINGO NÃO TEM VERIFICAÇÕES
     print('DOMINGO')
     priceTicket=30*(30/100)
            # if vespertinoOuNoturno(startTime,startMinutes) :
            #     print("DOMINGO NOTURNO") 
            # else :
            #  print("DOMINGO VESPERTINO") 
     #SEGUNDA
 elif dayWeek == 2  :
        if vespertinoOuNoturno(startTime,startMinutes) :
                print("SEGUNDA NOTURNO") 
                priceTicket=20*(50/100)
        else :
         print("SEGUNDA VESPERTINO") 
         priceTicket=15*(50/100)
    #TERÇA 
 elif dayWeek == 3 :
        if vespertinoOuNoturno(startTime,startMinutes) :
                    print("TERÇA NOTURNO") 
                    if payment =='c':
                     priceTicket=20*(50/100)
                    else:
                        priceTicket=20 
        else :
                  print("TERÇA VESPERTINO") 
                  if payment =='c':
                     priceTicket=15*(50/100)
                  else:
                       priceTicket=15
    #QUARTA
 elif dayWeek == 4  :
        if vespertinoOuNoturno(startTime,startMinutes) :
                print("QUARTA NOTURNO") 
                if payment =='c': 
                  priceTicket=30*(50/100)
                else:
                    priceTicket=30
        else :
                print("QUARTA VESPERTINO") 
                if payment =='c':   
                 priceTicket=15*(50/100)
                else:
                  priceTicket=15  
    #QUINTA
 elif dayWeek == 5 :
        if vespertinoOuNoturno(startTime,startMinutes) :
            print("QUINTA NOTURNO") 
            if payment =='c':  
             priceTicket=30*(50/100)
            else:
                priceTicket=30
        else :
            print("QUINTA VESPERTINO") 
            if payment =='c': 
             priceTicket=20*(50/100)
            else:
                priceTicket=20
    #SEXTA 
 elif dayWeek == 6 :
        if vespertinoOuNoturno(startTime,startMinutes) :
            print("SEXTA NOTURNO")
            if payment =='c':
                #DESCONTO
              print("passasasa")
              priceTicket= 40 *(30/100)
            else :
                priceTicket=40
        else :
            print("SEXTA VESPERTINO")
            if payment =='c':
             priceTicket=20*(50/100)
            else :
                priceTicket=20
    #SABADO
 elif dayWeek == 7  :   
        if vespertinoOuNoturno(startTime,startMinutes) :
                print("SABADO NOTURNO")
                if payment =='s':
                  priceTicket=40*(20/100)
                else:
                    priceTicket=40
        else :
                print("SABADO VESPERTINO")
                if payment =='c':
                 priceTicket=30*(20/100)
                else:
                   priceTicket=30  
                
print('Valor do ingresso: R$', format(priceTicket, '.2f').replace('.', ','))