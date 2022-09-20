##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Lucas Lima Pinheiro
# RA:263267
##################################################

# Leitura do valor da hora
from distutils.log import debug


valor_hora_trabalhada = int(input())

# Leitura do numero de dias trabalhados na semana
dias_trabalhados = int(input())
inicio = 0
final = 0
valor = 0
horas_trabalhadas = 0
periodos_de_trabalho = 0
hora_extra = 0
hora_trabalhada_periodo = 0

for dia in range(dias_trabalhados):
    # for day in range(7):
    periodos_de_trabalho = int(input())
    if periodos_de_trabalho > 0:
        hora_trabalhada_periodo =0
        for i in range(periodos_de_trabalho):
            inicio = int(input())
            final = int(input())
            hora_trabalhada_periodo += final - inicio
            horas_trabalhadas += final - inicio
            valor += (final - inicio) * valor_hora_trabalhada

        if hora_trabalhada_periodo > 8:
          hora_extra += hora_trabalhada_periodo - 8
    else:
        inicio = int(input())
        final = int(input())
        horas_trabalhadas += final - inicio
        valor += (final - inicio) * valor_hora_trabalhada
        if (final - inicio) > 8:
            print("passou 0")
            hora_extra += (final - inicio) - 8


if horas_trabalhadas > 44 and hora_extra < 0:
    hora_extra = horas_trabalhadas - 44
    valor = valor + ((valor_hora_trabalhada * 50 / 100) * hora_extra)


# Calculo do valor devido ao funcionário
if hora_extra > 0 and horas_trabalhadas < 44:
    valor = valor + ((valor_hora_trabalhada * 50 / 100) * hora_extra)


# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", hora_extra)
print("Valor devido: R$ {:0.2f}".format(valor))
