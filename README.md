![badge](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=F7DF1E)
![badge](https://img.shields.io/badge/Anaconda-323330?style=for-the-badge&logo=anaconda&logoColor=green)
![badge](https://img.shields.io/badge/Jupyter-white?style=for-the-badge&logo=jupyter&logoColor=orange)

# Previsão de Renda
Modelo de previsão de renda do projeto 2 do curso de Cientista de Dados da EBAC

## Entendimento do negócio

* Objetivo do projeto

    Prever a renda de indivíduos com base em variáveis socioeconômicas.

* Perguntas de Negócio

    Quais fatores mais influenciam a renda?

* Critérios de sucesso

    Um modelo com R² igual ou acima de 0.30 será considerado bem-sucedido

## Entendimento dos dados

Foram fornecidas 13 variáveis mais a variável resposta (Renda).

### Dicionário de dados


| Variável                | Descrição                                           | Tipo         |
| ----------------------- |:---------------------------------------------------:| ------------:|
| data_ref                |  Data de referência de coleta das variáveis                                      | Data|
| id_cliente              |  Código de identificação do cliente                                      | Inteiro|
| sexo                    |  Sexo do cliente                                      | Categórica|
| posse_de_veiculo        |  Indica se o cliente possui veículo                                      | Booleana|
| posse_de_imovel         |  Indica se o cliente possui imóvel                                      | Booleana|
| qtd_filhos              |  Quantidade de filhos do cliente                                      | Inteiro|
| tipo_renda              |  Tipo de renda do cliente                                      | Categórica|
| educacao                |  Grau de instrução do cliente                                      | Categórica|
| estado_civil            |  Estado civil do cliente                                      | Categórica|
| tipo_residencia         |  Tipo de residência do cliente (própria, alugada etc)                                      | Categórica|
| idade                   |  Idade do cliente                                      | Inteiro|
| tempo_emprego           |  Tempo no emprego atual                                      | Float |
| qt_pessoas_residencia   |  Quantidade de pessoas que moram na residência                                      | Inteiro |
| renda                   |  Renda em reais                                      | Float|


## Bibliotecas Utilizadas

* pandas
* numpy
* seaborn
* sklearn
* pickle

## Modelagem

Será utilizado árvores de regressão para prever valores contínuos. Diferentemente das árvores de decisão, que são usadas para classificação, as árvores de regressão são projetadas para prever valores numéricos.

## Avaliação dos resultados 

* Treinamento R²: 0.5722091057726075
* Treinamento MSE: 36995479.1727673
* Teste R²: 0.34664533622626315
* Teste MSE: 36996641.10373707

## Implantação 

Minha integração com o Streamlit envolve carregar o modelo de previsão de renda desenvolvido no Jupyter Notebook e coletar dados de um usuário hipotético para prever sua renda

https://github.com/user-attachments/assets/2c11a4c7-7dd1-4f14-89c2-24b329ddb5c3

