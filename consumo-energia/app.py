# ==========================================
# Calculadora de Consumo Elétrico Inteligente
# ==========================================

print("=" * 50)
print("     ⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡")
print("=" * 50)

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")

try:
    potencia = float(input("Digite a potência do aparelho em watts (W): "))
    horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

    # Cálculo do consumo mensal
    consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Cálculo opcional do custo
    tarifa_kwh = 0.75
    custo_mensal = consumo_mensal * tarifa_kwh

    # Resultado
    print("\n" + "=" * 50)
    print("             📊 RESULTADO")
    print("=" * 50)

    print(f"Aparelho: {aparelho}")
    print(f"Potência: {potencia:.0f} W")
    print(f"Uso diário: {horas_dia:.1f} horas")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")

    print("=" * 50)
    print("💡  Estimativa baseada em 30 dias de uso.")
    print("⚠️  O valor real pode variar conforme a tarifa")
    print("   de energia e o consumo do aparelho.")
    print("=" * 50)

except ValueError:
    print("\n❌ Erro: digite apenas valores numéricos para")
    print("   potência e horas de uso.")