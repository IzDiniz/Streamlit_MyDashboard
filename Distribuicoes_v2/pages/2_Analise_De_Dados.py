import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from scipy.stats import norm


# Função para carregar os dados do Excel
@st.cache_data
def load_data(path: str):
   data = pd.read_excel(path)
   return data

# Carregando dados do Excel
df = load_data("CANCER_FORMATADO.xlsx")
st.dataframe(df, width=1000,height=400)

st.markdown(" ")
st.markdown("<h2 style='text-align: center;'>Analisando os Dados</h2>", unsafe_allow_html=True)
st.markdown("""
<ul>    
   <h6>Colunas Disponíveis:</h6>
      <li>Pessoas: Nome dos pacientes.</li>
      <li>Idade: Idade dos pacientes.</li>
      <li>Gênero: Masculino ou Feminino.</li>
      <li>Tipo Sanguíneo: Tipo sanguíneo dos pacientes.</li>
      <li>Condição Médica: Todos os pacientes têm câncer.</li>
      <li>Data de Admissão: Data em que o paciente foi admitido.</li>
      <li>Tipo Urgência: Classificação da urgência (Urgente, Opcional, Emergência).</li>
</ul>

<br><br>

<ul> 
   <h6>Objetivo da Análise:</h6>
   <li>Calcular a porcentagem de homens e mulheres que adquiriram câncer antes dos 30 anos, entre 30 e 40 anos, e após os 40 anos.</li>
   <li>Verificar se há correlação entre o tipo sanguíneo e a incidência de câncer.</li>
   <li>Analisar a relação entre o tipo de urgência e a idade/gênero.</li>
   <li>Criar gráficos de barras ou pizza para visualizar a taxa de urgência em relação à idade, separando por gênero.</li> 
</ul> 

<br><br>
            
<ul>
   <h6>Perguntas a serem respondidas durante o processo:</h6>
      <li>Qual gênero possuí a maior probabilidade de adquirir cancer?</li>
      <li>Qual a faixa etária mais comum para adquirir cancer?</li>
      <li>Qual a urgência mais comum entre os pacientes com cancer?</li>
      <li>Há alguma relação do tipo sanguineo e do tipo de urgência?</li>
</ul>
            
            
            
            
""", unsafe_allow_html=True)



st.markdown("<h2 style='text-align: center;'>Quantidade por Genero</h2>", unsafe_allow_html=True)
genero = df.groupby("Genero")["Pessoas"].count().reset_index()
colors = {"Masculino": "Cyan", "Feminino": "Red"}
fig = px.bar(genero, x="Genero", y="Pessoas", color="Genero", color_discrete_map=colors)
st.plotly_chart(fig)

# Filtros interativos
st.sidebar.header("Filtros")
idade_min = int(df['Idade'].min())
idade_max = int(df['Idade'].max())
selected_age_range = st.sidebar.slider(
   "Selecione a faixa etária:",
   min_value=idade_min,
   max_value=idade_max,
   value=(idade_min, idade_max)
)

# Filtrar os dados com base na faixa etária selecionada
filtered_df = df[(df['Idade'] >= selected_age_range[0]) & (df['Idade'] <= selected_age_range[1])]

# Gráfico de Barras: Taxa de Urgência por Gênero
urgency_counts = filtered_df.groupby(['Genero', 'Tipo Urgência']).size().unstack()
urgency_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel("Gênero")
plt.ylabel("Contagem")
plt.title("Taxa de Urgência por Gênero")
st.pyplot(plt)

st.markdown("""
   <div>  
      <h3 style='text-align: center;'>Qual gênero possuí a maior probabilidade de adquirir cancer?</h3>
      <p>Para responder a essa pergunta, vamos analisar a quantidade de homens e mulheres que adquiriram câncer em diferentes faixas etárias.
      Com base nos dados, podemos observar que a quantidade de mulheres que adquiriram câncer é maior do que a quantidade de homens. 
      <br> <br>
      Embora a quantidade de mulheres seja maior, a porcentagem de mulheres que adquiriram câncer antes dos 30 anos é menor do que a porcentagem de homens percebemos isso ao selecionar a faixa etária no filtro ao lado.
      Por outro lado, a porcentagem de mulheres que adquiriram câncer após os 40 anos é maior do que a porcentagem de homens. <br>
      Portanto, podemos concluir que os homens têm uma maior probabilidade de adquirir câncer antes do período de 30 a 40 anos, enquanto as mulheres têm uma maior probabilidade de adquirir câncer após o período de 30 a 40 anos.</p>
      
      <br>
      <h3 style='text-align: center;'>Qual a faixa etária mais comum para adquirir cancer?</h3>
      <p>Com base nos dados, a faixa etária mais comum para adquirir câncer é entre 30 e 40 anos.
      Podemos ver que a idade mais propicia para adquirir cancer é 34 anos em diante, onde a quantidade de pessoas que adquiriram cancer é maior.
      </p>
         
   </div> 
""",unsafe_allow_html=True)

# Exibir estatísticas descritivas
st.markdown("""<h3 style='text-align: center;'> Estatísticas Descritivas </h3>""", unsafe_allow_html=True)
st.write(filtered_df[['Idade', 'Genero', 'Tipo Urgência']].describe())






# Gráfico de Gaussiana/Normal: Variação de Casos ao Longo dos Anos
st.markdown("""<h3 style='text-align: center;'>Variação de Casos de Câncer pela densidade</h3>""", unsafe_allow_html=True)

# Extrair o ano da coluna "Data de Admissão"
df['Ano'] = pd.to_datetime(df['Data de Admissão']).dt.year

# Filtrar os dados para o período de 2019 a 2024
df_filtered = df[(df['Ano'] >= 2019) & (df['Ano'] <= 2024)]

# Contagem de casos por ano
yearly_counts = df_filtered['Ano'].value_counts().sort_index()

# Criar o gráfico de Gaussiana/Normal
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Gerar dados para a curva de Gaussiana
mu = yearly_counts.mean()  # Média
sigma = yearly_counts.std()  # Desvio padrão
x = np.linspace(yearly_counts.min(), yearly_counts.max(), 100)
y = norm.pdf(x, mu, sigma)

# Plotar a curva de Gaussiana
ax2.plot(x, y, 'r-', label='Distribuição Normal')

# Plotar os dados reais
ax2.hist(yearly_counts, bins=6, density=True, alpha=0.6, color='g', label='Dados Reais')

# Configurações do gráfico
ax2.set_xlabel("Número de Casos")
ax2.set_ylabel("Densidade")
ax2.set_title("Distribuição de Casos de Câncer (2019-2024)")
ax2.legend()
st.pyplot(fig2)

# Tabela de Densidade por Ano
st.markdown("""<h3 style='text-align: center;'>Tabela da densidade de Casos de Câncer por Ano (2019-2024)</h3>""", unsafe_allow_html=True)

# Calcular a densidade de casos por ano
total_cases = yearly_counts.sum()
yearly_density = yearly_counts / total_cases

# Criar um DataFrame para a tabela
density_table = pd.DataFrame({
   'Ano': yearly_density.index,
   'Número de Casos': yearly_counts,
   'Densidade': yearly_density.values
})

# Exibir a tabela
st.dataframe(density_table)








@st.cache_data
def load_data(path: str):
   data = pd.read_excel(path)
   return data

# Carregar os dados
df = load_data("./CANCER_FORMATADO.xlsx")
st.subheader(" ", divider=True)

# Título do aplicativo
st.markdown("""<h2 style='text-align: center;'>Relação entre Tipo Sanguíneo e Urgência nos Exames</h2>""", unsafe_allow_html=True)

# Agrupar os dados por tipo sanguíneo e tipo de urgência
grouped_data = df.groupby(['Tipo Sanguineo', 'Tipo Urgência']).size().unstack()

# Calcular a porcentagem de cada tipo de urgência para cada tipo sanguíneo
percentage_data = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100

# Exibir a tabela de porcentagem
st.markdown("""<h3 style='text-align: center;'>Porcentagem de Tipos de Urgência por Tipo Sanguíneo</h3>""", unsafe_allow_html=True)
st.dataframe(percentage_data)

# Gráfico de Barras: Porcentagem de Tipos de Urgência por Tipo Sanguíneo
st.markdown("""<h3 style='text-align: center;'>Gráfico de Barras: Porcentagem de Tipos de Urgência por Tipo Sanguíneo</h3>""", unsafe_allow_html=True)

# Configurar o gráfico
fig, ax = plt.subplots(figsize=(12, 6))
percentage_data.plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel("Tipo Sanguíneo")
ax.set_ylabel("Porcentagem")
ax.set_title("Distribuição de Tipos de Urgência por Tipo Sanguíneo")
plt.xticks(rotation=45)
st.pyplot(fig)

# Análise textual
st.write("A tabela e o gráfico acima mostram a distribuição dos tipos de urgência (Urgente, Opcional, Emergência) para cada tipo sanguíneo.")

st.markdown("""<div> 
                  <h3 style='text-align: center;'>Qual a urgência mais comum entre os pacientes com cancer?</h3>
               </div>""", unsafe_allow_html=True)
            
st.markdown("""<p>
                  Com base nos dados, a urgência mais comum entre os pacientes com câncer é a urgência opcional, seguida pela urgente e emergência.
                  Ou seja, a maioria dos pacientes com câncer tem uma urgência opcional, o que significa que a situação não é crítica e pode ser tratada em um momento oportuno.
               </p>""", unsafe_allow_html=True)
               
st.markdown("""<p>
                  Podemos observar também que a distribuição dos tipos de urgência varia entre os diferentes tipos sanguíneos, 
                  indicando que certos tipos sanguíneos podem ter uma maior ou menor incidência de determinados tipos de urgência.
               </p>""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Há alguma relação do tipo sanguineo e do tipo de urgência?</h3>", unsafe_allow_html=True)
st.markdown("""<p>Para responder se há alguma correlação entre o tipo sanguíneo e o tipo de urgência, vamos observar a distribuição das cores nas barras para cada tipo sanguíneo:

<h6>Distribuição Variada:</h6> As proporções de cada tipo de urgência (Emergência, Urgente, Opcional) variam entre os diferentes tipos sanguíneos. Isso significa que certos tipos sanguíneos podem ter uma maior ou menor incidência de determinados tipos de urgência. <br> <br>

<h6>Padrões Específicos:</h6> Por exemplo, tipos sanguíneos como A+, O+, e O- apresentam diferentes proporções de urgências relacionado a categoria urgente, indicando que a distribuição não é uniforme. <br> <br>

<h4>Conclusão</h4>
Sim, parece haver uma correlação entre o tipo sanguíneo e o tipo de urgência, pois a distribuição dos tipos de urgência varia conforme o tipo sanguíneo. Portanto, é possível que certos tipos sanguíneos sejam mais propensos a determinados tipos de urgências médicas, como por exemplo
tipos sanguíneos que possuem o sangue B+, tendem a ter emergêcias em casos de adquirir cancer, diferente de quem possue o tipo sanguíneo -AB, onde a emergência tende a ser opicional ou de baixo risco. <p>""", unsafe_allow_html=True)




