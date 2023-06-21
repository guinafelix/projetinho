# Projeto realizado na disciplina de análise de algoritmos

### Equipe:
  ##### Diego Sindeaux
  ##### Guilherme Félix

### Questão proposta:
  ##### 2. Considere uma modificacao do problema do corte de barras na qual, além do preço Pi de cada barra, cada corte incide um custo fixo c. O rendimento da empresa associado com uma solução agora é a soma dos preços dos pedaços menos os custos dos cortes realizados. Implemente um algoritmo recursivo com memoização e um algoritmo iterativo com programação dinâmica para resolver esse problema. Suas implementações devem poder mostrar o custo da solução ótima e também mostrar a solução ótima. Em seguida, compare esses dois algoritmos experimentalmente.


**Considerações**
    
  #### A questão pede que a implementação seja capaz de retornar o custo da solução ótima e mostrar a solução. Nossas funções são capazes de retornar esses valores, mas optamos por não os mostrar durante a execução dos testes pois iria poluir o console e seria inviável analisar as informações. No entanto, implementamos a função <code>printSolutions</code> que é capaz de informar o custo e a soluções encontradas. Desse modo, pudemos comparar a diferença entre os valores produzidos pelas abordagens dinâmica e gulosa.

**Conclusões** 

  #### Durante os testes, conseguimos observar que o algoritmo que utiliza a estratégia gulosa possui um tempo de execução menor se comparado ao algoritmo de programação dinâmica. Isso se deve ao fato de ele considerar apenas o custo ótimo local enquanto realiza as iterações. Em relação ao custo das soluções encontradas, a diferença é bem mais expressiva. Entre os testes, conseguimos obter resultados que diferiam dezenas de unidades. Também observamos que o caminho encontrado pela solução gulosa raramente era o mesmo encontrado pela abordagem dinâmica. Podemos relacionar esse ponto com as discussões vistas no decorrer da disciplina sobre o fato de a solução gulosa naõ poder garantir que a solução ótima será encontrada.

