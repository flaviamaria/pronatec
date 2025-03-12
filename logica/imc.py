peso= float(input("digite seu peso"))
altura= float(input("digite sua altura"))
imc= peso/(altura*altura)
if(imc <18.5):
    print("Desnutrido", imc)
elif(imc <=24.5):
    print("Normal", )