import streamlit as st
from components.navbar import NavBar
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.functions import mes_para_numero, categorize_period


def main():
    NavBar()
    csv_file = 'csv_files/internações.csv'
    origin_df = pd.read_csv(csv_file, sep=';')
    columns = list(origin_df.columns)

    formated_df = pd.DataFrame()
    formated_df["Data"] = origin_df[columns[0]].apply(lambda x: x.split("/")[1]+'/'+str(mes_para_numero(x.split("/")[0])))
    formated_df["Data"] = pd.to_datetime(formated_df["Data"], format='%Y/%m')
    formated_df["Ano"] = formated_df["Data"].apply(lambda x: x.year)
    formated_df["Mês"] = formated_df["Data"].apply(lambda x: x.month)
    formated_df["Período"] = formated_df["Ano"].apply(categorize_period)
    for column in columns[1:]:
        formated_df[column] = origin_df[column]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=formated_df["Data"], y=formated_df["1 Região Norte"], mode='lines', name='1 Região Norte'))
    fig.add_trace(go.Scatter(x=formated_df["Data"], y=formated_df["2 Região Nordeste"], mode='lines', name='2 Região Nordeste'))
    fig.add_trace(go.Scatter(x=formated_df["Data"], y=formated_df["3 Região Sudeste"], mode='lines', name='3 Região Sudeste'))
    fig.add_trace(go.Scatter(x=formated_df["Data"], y=formated_df["4 Região Sul"], mode='lines', name='4 Região Sul'))
    fig.add_trace(go.Scatter(x=formated_df["Data"], y=formated_df["5 Região Centro-Oeste"], mode='lines', name='5 Região Centro-Oeste'))
    fig.add_trace(go.Scatter(x=formated_df["Data"], y=formated_df["Total"], mode='lines', name='Total'))
    fig.update_layout(
        title=dict(text="Internações (cid: Câncer Colorretal)"),
        xaxis_title='Data',
        yaxis_title='Quantidade',
        plot_bgcolor='white',
    )
    st.plotly_chart(fig)
    
    for column in columns[1:]:
        fig = px.line(formated_df, x='Data', y=column, color='Período', markers=True, title=f"Internações (cid: Câncer Colorretal) por período <br>{column}")
        fig.update_layout(
            plot_bgcolor='white',
            xaxis_title='Data',
            yaxis_title='Quantidade',
        )
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()