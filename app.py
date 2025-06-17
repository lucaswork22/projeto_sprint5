import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Painel Megaline", layout="centered")
st.title("Dashboard - Ligações Megaline")

# Leitura dos arquivos
calls = pd.read_csv("notebooks/megaline_calls.csv")
internet = pd.read_csv("notebooks/megaline_internet.csv")
messages = pd.read_csv("notebooks/megaline_messages.csv")
users = pd.read_csv("notebooks/megaline_users.csv")
plans = pd.read_csv("notebooks/megaline_plans.csv")

# ------------------------ Ligações ------------------------
st.subheader("Ligações")

if st.button("Ver Histograma de Duração"):
    fig = px.histogram(calls, x="duration", title="Histograma da Duração das Chamadas")
    st.plotly_chart(fig)

if st.button("Ver Dispersão Duração vs Usuário"):
    fig = px.scatter(calls, x="user_id", y="duration", title="Duração das Chamadas por Usuário")
    st.plotly_chart(fig)

# ------------------------ Internet ------------------------
st.subheader("Internet")

if st.button("Ver Consumo de Internet por Usuário"):
    fig = px.histogram(internet, x="mb_used", title="Uso de Internet (MB)")
    st.plotly_chart(fig)

# ------------------------ Mensagens ------------------------
st.subheader("Mensagens")

if st.button("Ver Quantidade de Mensagens por Usuário"):
    fig = px.histogram(messages, x="user_id", title="Quantidade de Mensagens por Usuário")
    st.plotly_chart(fig)

# ------------------------ Usuários ------------------------
st.subheader("Usuários")

if st.button("Ver Distribuição por Cidade"):
    fig = px.histogram(users, x="city", title="Distribuição de Usuários por Cidade")
    st.plotly_chart(fig)

if st.button("Ver Distribuição por Plano"):
    fig = px.histogram(users, x="plan", title="Distribuição de Usuários por Plano")
    st.plotly_chart(fig)

# ------------------------ Planos ------------------------
st.subheader("Planos")

if st.button("Ver Comparação dos Planos"):
    df_melted = plans.melt(
        id_vars="plan_name",
        value_vars=["usd_monthly_pay", "mb_per_month_included", "minutes_included", "messages_included"],
        var_name="Categoria",
        value_name="Valor"
    )
    fig = px.bar(df_melted, x="plan_name", y="Valor", color="Categoria",
                 title="Comparação dos Planos Megaline", barmode="group")
    st.plotly_chart(fig)