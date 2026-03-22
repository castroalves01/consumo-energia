aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência (W): "))
horas = float(input("Horas por dia: "))

consumo = (potencia * horas * 30) / 1000
custo = consumo * 0.75

print("\nResultado:")
print("Aparelho:", aparelho)
print("Consumo:", round(consumo, 2), "kWh/mês")
print("Custo: R$", round(custo, 2))