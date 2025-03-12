salário= float(input("informe o salário do funcionario"))
if salário<2.000:
    aumento= salário*0.10
else:
    aumento= salário*0.05
    novo_salario= salário+ aumento
    print("o novo salario é:", novo_salario)    