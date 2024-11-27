

import statistics as st

empresas = {
"empresa1": [900,6000,1200,8000,1400],
"empresa2": [5000,4000,3000,2000,7000],
"empresa3": [1200,1300,8000,3000,15000],
"empresa4": [1400,1200,1600,4500,5900],
"empresa5":[1400,1750,2000,4500,1000]
}

for empresa, valores in empresas.items():
    print(f"Empresa: {empresa}")
    print(f"Media: {st.mean(valores)}")
    print(f"Mediana: {st.median(valores)}")
    print(f"Diferença entre a média e a mediana: {st.mean(valores) - st.median(valores)}")
    print(f"Desvio Padrão: {st.stdev(valores)}")
    print("Amplitude: ", max(valores) - min(valores))
    print(f"----------------------------------------")

Resposta = """

1) Qual empresa escolheria?

Dentro das opções avaliadas, temos 2 empresas que merecem destaque:

Empresa2: Segunda média mais alta, a menor diferença entre a média e mediana e o segundo menos desvio padrão. É uma opção que apresenta um a melhor relação entre consistência na distribuição dos salários com rendimentos atrativos. Seria uma opção conservadora. Por um lado teria uma garantia de um salário bom ao longo do tempo porém seria uma escolhada que limitaria ganhos potenciais ao longo prazo.

Empresa 3: Maior salário registrado, maior média porém maior desvio padrão, demonstrando uma alta discrepância entre os salários. Seria a opção mais "arrojada".
Provavelmente começaria com salários mais baixos porém, é a opção que tem um potencial de ganhos maior ao longo prazo.

2) Pelo meu perfil, escolheria a empresa 3, mesmo correndo mais riscos.

 O que você entendeu do desvio padrão, média, moda, mediana, amplitude, variância dessa empresa?

O desvio padrão da empresa 3 (5888.123640006212) é o maior mensurado, significa que há a maior variação entre cada um dos salários em relação a média, ou seja, não há uma consistência nos salários pagos.

A média significa que, caso a empresa iguale os salários, todos receberiam o salário médio registrado (5700).

A moda seria o salário com a maior quantidade observada.

A mediana é uma medida de análise central.

Amplitude é a diferença entre o menor salário e o maior salário.

A variância é assim como o desfio padrão, é uma medida de dispersão, em outras palavras, a variância verifica o quão próximo os salários está da média. Quanto menor a variância, maior a igualdade salarial.

"""

print(Resposta)