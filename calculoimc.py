def calculo_imc (peso: float, altura_cm: int) -> float:
    
    altura = altura_cm/100

    IMC = float( peso / (altura*altura))
    
    return IMC  

def classificacao_imc (IMC: float) -> str:
    
        if IMC < 18.5:
            return("\n Estás abaixo do  peso normal.")

        elif IMC >= 18.5 and IMC < 25:
            return("\n Estás com peso normal.")

        elif IMC >= 25 and IMC < 30: 
            return("\n Estás acima do peso normal.")
        
        elif IMC >= 30:
            return("\n Apresentas obesidade.")

def main_program ():
    
    while True:
        
        escolha = input("\n Olá, queres saber o teu IMC? (s/n): ").lower()

        if escolha not in ["s", "sim"]:
            break
        
        peso = float(input("\n Quanto pesas, em kg?: "))

        altura_cm = int(input("\n Diz-me a tua altura em centímetros: "))

        IMC = calculo_imc(peso, altura_cm)
        
        print(f"\n O teu IMC é de: {IMC: .2f}.")
        print(f"\n {classificacao_imc (IMC)}")
        
        
main_program ()