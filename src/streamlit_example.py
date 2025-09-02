import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Hello, Streamlit')
st.write('Este é o meu primerio aplicativo com Streamlit')

st.header('Este é um header')
st.subheader('Este é um subheader')
st.text('Este é um texto seimples')
st.markdown('E esté é um **Texto em Negrito** e *italico*')

data = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 45],
    'Salário': [5000, 7000, 9000]
}

df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salário'])
st.pyplot(fig)

if st.button('Clique Aqui'):
    st.write('Botão clicado vez!')

idade = st.slider('Selecione sua idade', 0, 100, 25)
st.write(f'Idade selecionada: {idade}')

opcao = st.selectbox(
    'Escolha um departamento:',
    ['Recursos Humanos', 'TI', 'Vendas']
)
st.write(f'Departamento Selecionado: {opcao}')