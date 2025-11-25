import streamlit as st

st.title("Perguntas especiais ❤️")

# Entrada — Entrar ou Sair
entrada = st.text_input("Digite [E] para Entrar ou [S] para Sair:")

if entrada:
    if entrada.upper() == "E":
        st.success("Você entrou, parabéns.")
    else:
        st.warning("Você saiu.")

# Data
conhecer = "29/09/2023"
data = st.text_input("Digite a data que nos conhecemos (dd/mm/aaaa):")

if data:
    if data == conhecer:
        st.success("Boa, acertou!")
    else:
        st.error("Errado!!!")

# Bar
local = "Manga Rosa"
bar = st.text_input("Digite o nome do bar que nos conhecemos:")

if bar:
    if bar.lower() == local.lower():
        st.success("Parabéns!")
    else:
        st.error(":(")
