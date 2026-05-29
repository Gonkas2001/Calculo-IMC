def calculo_imc (num1: float, num2: int, operador: str ) -> float:

escolha = input("\n Olá, queres saber o teu IMC? (s/n): ")

if escolha not in ["s", "sim"]:
    break

num1 = float(input("\n Quanto pesas, em kg?: "))

num2 = int(input("\n Diz-me a tua altura em centímetros: "))

altura == num2/100

IMC == .2float( num1 / (altura*altura))

if IMC < 18.5 
    print("\n Estás fora do peso normal.")

elif IMC >= 18.5 & IMC < 25 
    print("\n Estás com peso normal.")

elif IMC >= 25
    print("\n Estás acima do peso normal")