def calculo_imc (peso: float, altura: int, altura_cm: int, IMC: float) -> float:
    
    altura == altura_cm/100

    IMC == float( peso / (altura*altura))
    
    return IMC  

while True:
        
        escolha = input("\n Olá, queres saber o teu IMC? (s/n): ").lower()

        if escolha not in ["s", "sim"]:
            break

        peso = float(input("\n Quanto pesas, em kg?: "))

        altura_cm = int(input("\n Diz-me a tua altura em centímetros: "))

        IMC = calculo_imc(peso, altura_cm)
        
        print(f"\n O teu IMC é de: {IMC: .f}")

        if IMC < 18.5:
            print("\n Estás fora do peso normal.")

        elif IMC >= 18.5 & IMC < 25:
            print("\n Estás com peso normal.")

        elif IMC >= 25:
            print("\n Estás acima do peso normal")