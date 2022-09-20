##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Lucas Lima Pinheiro
# RA:263267
##################################################

# Leitura do valor da hora
valor_hora_trabalhada = int(input())

# Leitura do numero de dias trabalhados na semana
dias_trabalhados = int(input())
inicio = 0
final = 0
valor = 0
horas_trabalhadas = 0
periodos_de_trabalho =0

for day in range(dias_trabalhados):
    periodos_de_trabalho = int(input())
    inicio = int(input())
    final = int(input())
    horas_trabalhadas += final - inicio
    valor += (final - inicio) * valor_hora_trabalhada
# Leitora e processamento dos periodos de trabalho de cada dia
# print("horasTrabalhadas", horas_trabalhadas)
# print("valorDia", valorDia)

# Calculo do valor devido ao funcionário


# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
# print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
