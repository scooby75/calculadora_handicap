import streamlit as st

def calcular_odd_justa(vitorias_casa, empates, derrotas):
    total_partidas = vitorias_casa + empates + derrotas

    # Calcula as probabilidades
    prob_vitoria_casa = vitorias_casa / total_partidas
    prob_empate = empates / total_partidas
    prob_vitoria_visitante = derrotas / total_partidas

    # Calcula as odds justas para Match Odds
    odd_vitoria_casa = 1 / prob_vitoria_casa
    odd_empate = 1 / prob_empate
    odd_vitoria_visitante = 1 / prob_vitoria_visitante

    # Calcula a linha de handicap (por exemplo, linha 0.5)
    linha_handicap = 0.5 * (vitorias_casa - derrotas) / total_partidas

    # Calcula as odds justas para Handicap Asiático
    odd_vitoria_casa_handicap = 1 / (prob_vitoria_casa + linha_handicap)
    odd_empate_handicap = 1 / (prob_empate + linha_handicap)
    odd_vitoria_visitante_handicap = 1 / (prob_vitoria_visitante + linha_handicap)

    return {
        "Match Odds": {
            "Odd Vitória da Casa": odd_vitoria_casa,
            "Odd Empate": odd_empate,
            "Odd Vitória Visitante": odd_vitoria_visitante,
        },
        "Handicap Asiático": {
            "Linha de Handicap": linha_handicap,
            "Odd Vitória da Casa (Handicap)": odd_vitoria_casa_handicap,
            "Odd Empate (Handicap)": odd_empate_handicap,
            "Odd Vitória Visitante (Handicap)": odd_vitoria_visitante_handicap,
        },
    }

# Interface do Streamlit
st.title("Calculadora de Odds")

# Entradas do usuário
vitorias_casa = st.slider("Número de Vitórias da Casa:", min_value=0, max_value=10, value=5)
empates = st.slider("Número de Empates:", min_value=0, max_value=10, value=3)
derrotas = st.slider("Número de Derrotas:", min_value=0, max_value=10, value=2)

# Calcula as odds justas
odds_justas = calcular_odd_justa(vitorias_casa, empates, derrotas)

# Exibe as odds decimais
st.write("### Match Odds:")
st.write("Odd Vitória da Casa:", round(odds_justas["Match Odds"]["Odd Vitória da Casa"], 2))
st.write("Odd Empate:", round(odds_justas["Match Odds"]["Odd Empate"], 2))
st.write("Odd Vitória Visitante:", round(odds_justas["Match Odds"]["Odd Vitória Visitante"], 2))

st.write("### Handicap Asiático:")
st.write("Linha de Handicap:", round(odds_justas["Handicap Asiático"]["Linha de Handicap"], 2))
st.write("Odd Vitória da Casa (Handicap):", round(odds_justas["Handicap Asiático"]["Odd Vitória da Casa (Handicap)"], 2))
st.write("Odd Empate (Handicap):", round(odds_justas["Handicap Asiático"]["Odd Empate (Handicap)"], 2))
st.write("Odd Vitória Visitante (Handicap):", round(odds_justas["Handicap Asiático"]["Odd Vitória Visitante (Handicap)"], 2))
