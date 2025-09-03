# Decisões tomadas na implementação do projeto:

## Escolha da abordagem de classificação usando regras:
A escolha se deu principalmente por ser a mais simples e funcional(Tendo em vista o contexto) e por basicamente não haver a necessidade, e viabilidade, de implementar um modelo de machine learn para classificar as notícias. Usar a abordagem de classificação a partir de uma lista de palavras já classificadas fornece uma mínima segurança e confiabilidade no resultado, ainda mais pela robustez da base de palavras que foi usada no projeto em relação a quantidade e qualidade. É importante frisar que a classificação usada não tem uma acurácia confiável, devido a estar sensísel a possíveis contextos externos que não estão mapeados. Portanto, a partir das premissas citadas, se deu a escolha por uma classificação baseada em regras.


## 