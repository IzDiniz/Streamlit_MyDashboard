import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo


# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")
st.sidebar.markdown("")


# Adicionando o logo no body
# st.image("logo.png", width=150)

st.title("Iago Diniz Fontes", )
st.markdown("### Estagiar na área de Tecnologia da Informação")
st.markdown("###### iago.diniz@gmail.com")
st.markdown("###### (11) 96987-0219")
st.markdown("###### Rua Bernador dos Santos, 10, Beta 263")
st.markdown("###### São Paulo, SP - Zona Oeste")
st.markdown("###### nascimento 01/08/2004")
st.subheader("", divider="gray")


# Resumo pessoal e profissional
st.markdown("### Resumo")
st.write(" Estudande de Engenharia de software motivado e disciplinado, buscando oportunidade de desenvolvimkento profissional em uma organização respeitável. Estou em busca da minha primeira oportunidade de estagiar na área de tecnologia da informação, onde poderei evoluir tanto profissionalmente quanto pessoalmente. Desenvolvi projetos como freelancer na criação de  web landing pages e web stores na utilização de Html, Css e JavaScript.")
st.subheader("", divider="gray")


st.markdown("### Formação Acadêmica")
st.markdown("""
    <style>
    .bullet-list {
        list-style-type: disc;
        padding-left: 20px;
    }
    """, unsafe_allow_html=True)

st.markdown("""
##### Bacharelado - FIAP
<ul class="bullet-list">
    <li>Cursando - Engenharia de Software, agosto 2023 - junho 2027</li>
</ul>

##### Ensino Médio Técnico - Senac Tito
<ul class="bullet-list">
    <li class="bullet-list-list">  Concluído - Técnico em Informática, Janeiro 2020 - Dezembro 2022</li>
</ul>

##### Curso Técnico - Saga Lapa
<ul class="bullet-list">
    <li class="bullet-list-list"> Concluído - Técnico em Modelagem de Games 2D e 3D, outubro 2021 - Outubro 2022</li>
</ul>

""", unsafe_allow_html=True)




st.subheader("", divider="gray")
st.markdown("### Idiomas")
st.markdown("""
    <style>
    .text {
        font-size: 30px;  /* Ajuste o tamanho da fonte conforme necessário */
        line-height: 1.5;  /* Ajuste a altura da linha conforme necessário */
    }
    </style>
    """, unsafe_allow_html=True)

# Conteúdo com quebras de linha
st.markdown("""
<p class="text">
Português - Nativo<br>
Inglês - Intermediário/Avançado<br>
Espanhol - Básico <br><br>

Wizard (Inglês) - 1 ano, Módulo: infántil<br>
IW Taboão (Inglês) - 3 anos, Módulos: Getting by, Survival, Socialize and High Conversation<br> 
Colégio Dom Henrique (Inglês e Espanhol) - Idiomas aprendidos durante o curso do ensino fundamental
</p>
""", unsafe_allow_html=True)


st.subheader("", divider="gray")
st.markdown("### Conhecimentos / Skills")

# Criar duas colunas
col1, col2 = st.columns(2)

# Definir as listas para cada coluna
skills_col1 = ["Lógica de Programação", "Python", "Java POO", "Data Science", "Cisco Packet Tracer", "Pacote Office (Excel, Power Point, Word)", ] 
skills_col2 = ["C#", "C++", "REACT", "JavaScript", "HTML", "CSS", "Machine Learning", "Power BI", "SQL"]

# Adicionar os itens na primeira coluna
with col1:
    st.subheader("")
    for skill in skills_col1:
        st.write(f"- {skill}")

# Adicionar os itens na segunda coluna
with col2:
    st.subheader("")
    for skill in skills_col2:
        st.write(f"- {skill}")




