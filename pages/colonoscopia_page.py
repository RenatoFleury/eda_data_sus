import streamlit as st
from components.navbar import NavBar
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.functions import mes_para_numero, categorize_period

def coloscopia_first_graph():
    df = pd.read_csv("csv_files/colonoscopia.csv", sep=';')
    df["Ano/mês processamento"] = df["Ano/mês processamento"].apply(lambda x: x.split("/")[1]+'/'+str(mes_para_numero(x.split("/")[0])))
    df["Ano"] = df["Ano/mês processamento"].apply(lambda x: int(x.split("/")[0]))
    df["Mês"] = df["Ano/mês processamento"].apply(lambda x: int(x.split("/")[1]))
    df["Período"] = df["Ano"].apply(categorize_period)
    df['Data'] = pd.to_datetime(df['Ano/mês processamento'], format='%Y/%m')
    df = df[['Data', 'Ano', 'Mês', 'Período', '1 Região Norte', '2 Região Nordeste', '3 Região Sudeste', '4 Região Sul', '5 Região Centro-Oeste', '0 Ignorado/Exterior', 'Total',]]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Data"], y=df["0 Ignorado/Exterior"], mode='lines', name='0 Ignorado/Exterior'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["1 Região Norte"], mode='lines', name='1 Região Norte'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["2 Região Nordeste"], mode='lines', name='2 Região Nordeste'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["3 Região Sudeste"], mode='lines', name='3 Região Sudeste'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["4 Região Sul"], mode='lines', name='4 Região Sul'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["5 Região Centro-Oeste"], mode='lines', name='5 Região Centro-Oeste'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["Total"], mode='lines', name='Total'))
    fig.update_layout(
        title=dict(text="COLONOSCOPIA"),
        plot_bgcolor='white',
        xaxis_title='Data',
        yaxis_title='Quantidade',
    )

    st.plotly_chart(fig)

def main():
    NavBar()

    df = pd.read_csv("csv_files/colonoscopia.csv", sep=';')
    df["Ano/mês processamento"] = df["Ano/mês processamento"].apply(lambda x: x.split("/")[1]+'/'+str(mes_para_numero(x.split("/")[0])))
    df["Ano"] = df["Ano/mês processamento"].apply(lambda x: int(x.split("/")[0]))
    df["Mês"] = df["Ano/mês processamento"].apply(lambda x: int(x.split("/")[1]))
    df["Período"] = df["Ano"].apply(categorize_period)
    df['Data'] = pd.to_datetime(df['Ano/mês processamento'], format='%Y/%m')
    df = df[['Data', 'Ano', 'Mês', 'Período', '1 Região Norte', '2 Região Nordeste', '3 Região Sudeste', '4 Região Sul', '5 Região Centro-Oeste', '0 Ignorado/Exterior', 'Total',]]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Data"], y=df["0 Ignorado/Exterior"], mode='lines', name='0 Ignorado/Exterior'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["1 Região Norte"], mode='lines', name='1 Região Norte'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["2 Região Nordeste"], mode='lines', name='2 Região Nordeste'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["3 Região Sudeste"], mode='lines', name='3 Região Sudeste'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["4 Região Sul"], mode='lines', name='4 Região Sul'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["5 Região Centro-Oeste"], mode='lines', name='5 Região Centro-Oeste'))
    fig.add_trace(go.Scatter(x=df["Data"], y=df["Total"], mode='lines', name='Total'))
    fig.update_layout(
        title=dict(text="Colonoscopia"),
        plot_bgcolor='white',
        xaxis_title='Data',
        yaxis_title='Quantidade',
    )

    st.plotly_chart(fig)
    
    df_pre_pand = df[df["Ano"] < 2020]
    df_pand = df[(df["Ano"] >= 2020) & (df["Ano"] < 2022)]
    df_pos_pand = df[df["Ano"] >= 2022]
    
    fig = px.line(df, x='Data', y='Total', color='Período', markers=True, title="Colonoscopias Totais")
    fig.update_layout(plot_bgcolor='white')
    st.plotly_chart(fig)
    
    regioes = list(df.columns[4:10])
    for regiao in regioes:
        fig = px.line(df, x='Data', y=regiao, color='Período', markers=True, title=f"Colonoscopias {regiao}")
        fig.update_layout(plot_bgcolor='white')
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()