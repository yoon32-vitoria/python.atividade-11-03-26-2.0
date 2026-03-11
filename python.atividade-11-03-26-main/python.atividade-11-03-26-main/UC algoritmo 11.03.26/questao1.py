salario_por_hora = float(input("Digite o salário por hora: "))
horas_por_semana = float(input("Digite o número de horas trabalhadas por semana: "))
desconto_percentual = float(input("Digite o percentual de descontos (impostos e contribuições): "))

Cálculos
horas_mensais = horas_por_semana * 4.33
salario_bruto_mensal = salario_por_hora * horas_mensais
valor_total_descontos = salario_bruto_mensal * (desconto_percentual / 100)
salario_liquido_mensal = salario_bruto_mensal - valor_total_descontos

Resultado
print(f"Salário bruto mensal: Rsalario 
bruto")
 ensal:.2f")print(f"Totaldedescontos:R {valor_total_descontos:.2f}")
print(f"Salário líquido mensal: R$ {salario_liquido_mensal:.2f}")