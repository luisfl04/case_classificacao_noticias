# Decisões tomadas na implementação do projeto:

## Escolha da abordagem de classificação usando regras:
A escolha se deu principalmente por ser a mais simples e funcional(Tendo em vista o contexto) e por basicamente não haver a necessidade, e viabilidade, de implementar um modelo de machine learn para classificar as notícias. Usar a abordagem de classificação a partir de uma lista de palavras já classificadas fornece uma mínima segurança e confiabilidade no resultado, ainda mais pela robustez da base de palavras que foi usada no projeto em relação a quantidade e qualidade. É importante frisar que a classificação usada não tem uma acurácia confiável, devido a estar sensísel a possíveis contextos externos que não estão mapeados. Portanto, a partir das premissas citadas, se deu a escolha por uma classificação baseada em regras.


## Manipulação de dados em relação a posíveis erros ou falta de resultados na pesquisa de noticias:
No decorrer da implementação, ficou quase claro que o resultado das noticias iriam ser obtidas, digamos que em 95% dos casos, com isso, não foi um problema a falta de dados obtidos das pesquisas de noticias, contudo, em ocorrência de algum erro na busca, a aplicação consegue mapear e informar ao usuário. Toda a manipulação de dados realizada nas funções implementadas foram feitas tendo em vista o mapeamento de possíveis exceções que podiam vir a ocorrer ou possíveis casos de dados nulos(Como na obtenção do tema da pesquisa a partir da escolha do usuário no input inicial). Portanto, a captura de possíveis erros e manipulação dos mesmos está implementada de forma básica, muito possivelmente podendo ser refinada.

