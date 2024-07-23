import streamlit as st
import pandas as pd
import numpy as np 
import pickle
from sklearn.tree import DecisionTreeRegressor

# Carregar o modelo

with open('arvore_final_model.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Titulo do aplicativo

st.title('Cadastro de informações para previsão de renda')


# Caixas de seleção

sexo = st.selectbox('Sexo:', ['Masculino', 'Feminino'])
posse_veiculo = st.selectbox('Posse de veículo:', ['Sim', 'Não'])
posse_imovel = st.selectbox('Posse de imóvel:', ['Sim', 'Não'])
tipo_renda = st.selectbox('Tipo de renda:', ['Empresário', 'Pensionista',
                                             'Servidor Publico', 'Bolsita'])
educacao = st.selectbox('Nivel de escolaridade:', ['Secundário', 'Superior completo', 'Superior incompleto',
                                              'Pós graduação'])
estado_civil = st.selectbox('Estado Civil:', ['Casado', 'Solteiro', 'União',
                                             'Separado', 'Viúvo'])
tipo_residencia = st.selectbox('Tipo de residencia:', ['Casa', 'Com os pais', 'Comunitário', 
                                                       'Estúdio', 'Governamental'])

# Campo de entrada de numeros reais

qtd_filhos = st.number_input('Quantidade de Filhos', min_value=0, max_value=20, step=1)
idade = st.number_input('Idade', min_value=0, max_value=120, step=1)
tempo_emprego = st.number_input('Tempo de Emprego(em anos)', min_value=0, max_value=60, step=1)
qt_pessoas_residencia = st.number_input('Pessoas na residencia', min_value=0, max_value=20, step=1)


# Carregando CSV projeto 

df_streamlit = pd.read_csv('df_limpo_R01.csv')
df_streamlit = df_streamlit.astype(float)

# Botão para salvar os dados

if st.button('Salvar dados e prever renda'):

    # If dos CRIA

    if tipo_residencia == 'Casa':
        df_streamlit['tipo_residencia_Casa'] = 1
    elif tipo_residencia == 'Com os pais':
        df_streamlit['tipo_residencia_Com os pais'] = 1
    elif tipo_residencia == 'Comunitário':
        df_streamlit['tipo_residencia_Comunitário'] = 1
    elif tipo_residencia == 'Estúdio':
        df_streamlit['tipo_residencia_Estúdio'] = 1
    elif tipo_residencia == 'Governamental':
        df_streamlit['tipo_residencia_Governamental'] = 1


    if estado_civil == 'Separado':
        df_streamlit['estado_civil_Separado'] = 1
    elif estado_civil == 'Solteiro':
        df_streamlit['estado_civil_Solteiro'] = 1
    elif estado_civil == 'União':
        df_streamlit['estado_civil_União'] = 1
    elif estado_civil == 'Viúvo':
        df_streamlit['estado_civil_Viúvo'] = 1

    if tipo_renda == 'Bolsista':
        df_streamlit['tipo_renda_Bolsista'] = 1
    elif tipo_renda == 'Empresário':
        df_streamlit['tipo_renda_Empresário'] = 1
    elif tipo_renda == 'Pensionista':
        df_streamlit['tipo_renda_Pensionista'] = 1
    elif tipo_renda == 'Servidor Publico':
        df_streamlit['tipo_renda_Servidor público'] = 1

    if educacao == 'Pós graduação':
        df_streamlit['educacao_Pós graduação'] = 1
    elif educacao == 'Secundário':
        df_streamlit['educacao_Secundário'] = 1
    elif educacao == 'Superior completo':
        df_streamlit['educacao_Superior_completo'] = 1
    elif educacao == 'Superior incompleto':
        df_streamlit['educacao_Superior incompleto'] = 1

    # Salvando dados de sexo, posse_veiculo e posse_imovel

    if sexo == 'Masculino':
        df_streamlit['sexo_M'] = 1

    if posse_veiculo == 'Sim':
        df_streamlit['posse_de_veiculo'] = 1

    if posse_imovel == 'Sim':
        df_streamlit['posse_de_imovel'] = 1

    # Salvando dados float

    df_streamlit['qtd_filhos'] = qtd_filhos
    df_streamlit['idade'] = idade
    df_streamlit['tempo_emprego'] = tempo_emprego
    df_streamlit['qt_pessoas_residencia'] = qt_pessoas_residencia
    
    

    # Exibir o DataFrame

    st.write('Dados Coletados')
    st.dataframe(df_streamlit)

    # Salvando o DataFrame em CSV

    df_streamlit.to_csv('dados_usuario_streamlit.csv', index=False)
    st.write("Os dados foram salvos com sucesso!")

    # Prevendo a renda 

    vasco = modelo.predict(df_streamlit)
    st.write("Resultados das Previsões:")
    st.write(vasco[0])
