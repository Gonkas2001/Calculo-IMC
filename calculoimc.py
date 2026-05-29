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
    
    total__consultas = 0
    soma_imc = 0

    classificacoes = {
        "Estás abaixo do  peso normal." : 0,
        "Estás abaixo do  peso normal." : 0,
        "Estás acima do peso normal." : 0,
        "Apresentas obesidade." : 0
        }
        
    while True:
            
            escolha = input("\n Olá, queres saber o teu IMC? (s/n): ").lower()

            if escolha not in ["s", "sim"]:
                break
            
            peso = float(input("\n Quanto pesas, em kg?: "))

            altura_cm = int(input("\n Diz-me a tua altura em centímetros: "))

            IMC = calculo_imc(peso, altura_cm)
            
            print(f"\n O teu IMC é de: {IMC: .2f}.")
            
            print(f"\n {classificacao_imc (IMC)}")
        
            total__consultas += 1
            
            soma_imc += IMC
            
            classificacao = classificacao_imc (IMC)
            classificacoes [classificacao] =+ 1
        
            if total__consultas > 0:
                
                media_imc = soma_imc / total__consultas
                
                classificacao_mais_frequente_registada = max(
                    classificacoes,
                    key=classificacoes.get
                )
            
            print(f"\n Númmero total de consultas realizadas: {total__consultas}"),
            print(f"\n Média dos IMC calculados: {media_imc: .2f}"),
            print(f"\n Classificação mais frequentemente registada: {classificacao_mais_frequente_registada}")
            
main_program ()