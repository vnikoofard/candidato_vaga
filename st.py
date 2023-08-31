import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('data.csv')

st.title("Relação candidato vaga das unidades da UFF")

bar = st.sidebar

cidades = bar.multiselect("Selecione o(s) campos", df.Cidade.unique())
cursos = bar.multiselect("Selecione o(s) cursos", df[df['Cidade'].isin(cidades)].Curso.unique())
graus = bar.multiselect("Selecione o(s) grau", df[df['Cidade'].isin(cidades) & df['Curso'].isin(cursos)].Grau.unique())
turnos = bar.multiselect("Selecione o(s) turno", df[df['Cidade'].isin(cidades) & df['Curso'].isin(cursos) & df['Grau'].isin(graus)].Turno.unique())

for cidade in cidades:
    for curso in cursos:
        for grau in graus:
            for turno in turnos:
                ddf = df[(df.Cidade == cidade) & (df.Curso == curso) & (df.Grau==grau) & (df.Turno==turno)]
                if ddf.empty:
                    continue
                fig=px.line(ddf, x='year', y='Inscritos/Vagas', title=f'{cidade} - {curso} - {grau}s')
                fig.update_xaxes(tickvals=df.year.unique())
                st.plotly_chart(fig)
        