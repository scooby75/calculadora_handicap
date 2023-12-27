import streamlit as st

def calcular_odd_match_handicap(vitorias_casa, empates, derrotas, info_type="H2H"):
    total_partidas = vitorias_casa + empates + derrotas

    # Adiciona uma pequena margem para evitar divisão por zero
    epsilon = 1e-9
    prob_vitoria_casa = vitorias_casa / (total_partidas + epsilon)
    prob_empate = empates / (total_partidas + epsilon)
    prob_vitoria_visitante = derrotas / (total_partidas + epsilon)

    odd_vitoria_casa = 1 / prob_vitoria_casa
    odd_empate = 1 / prob_empate
    odd_vitoria_visitante = 1 / prob_vitoria_visitante

    if info_type == "H2H":
        linha_handicap = 0.0
    elif info_type == "Casa":
        linha_handicap = (vitorias_casa - derrotas) / total_partidas
    elif info_type == "Visitante":
        linha_handicap = (vitorias_casa - derrotas) / total_partidas

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

# Informações H2H
st.header("H2H (Head-to-Head)")
vitorias_casa_h2h = st.slider("Número de Vitórias da Casa H2H:", min_value=0, max_value=10, value=5, key="vc_h2h")
empates_h2h = st.slider("Número de Empates H2H:", min_value=0, max_value=10, value=3, key="e_h2h")
derrotas_h2h = st.slider("Número de Derrotas H2H:", min_value=0, max_value=10, value=2, key="d_h2h")

odds_h2h = calcular_odd_match_handicap(vitorias_casa_h2h, empates_h2h, derrotas_h2h, "H2H")
st.write("### Odds para H2H:")
st.write("Odd Vitória da Casa:", round(odds_h2h["Match Odds"]["Odd Vitória da Casa"], 2))
st.write("Odd Empate:", round(odds_h2h["Match Odds"]["Odd Empate"], 2))
st.write("Odd Vitória Visitante:", round(odds_h2h["Match Odds"]["Odd Vitória Visitante"], 2))

# Informações Últimos 5 Jogos Time da Casa
st.header("Últimos 5 Jogos - Time da Casa")
vitorias_casa_casa = st.slider("Número de Vitórias da Casa Últimos 5 Jogos:", min_value=0, max_value=5, value=2, key="vc_casa")
empates_casa = st.slider("Número de Empates Últimos 5 Jogos:", min_value=0, max_value=5, value=2, key="e_casa")
derrotas_casa = st.slider("Número de Derrotas Últimos 5 Jogos:", min_value=0, max_value=5, value=1, key="d_casa")

odds_casa = calcular_odd_match_handicap(vitorias_casa_casa, empates_casa, derrotas_casa, "Casa")
st.write("### Odds para Últimos 5 Jogos - Time da Casa:")
st.write("Odd Vitória da Casa:", round(odds_casa["Match Odds"]["Odd Vitória da Casa"], 2))
st.write("Odd Empate:", round(odds_casa["Match Odds"]["Odd Empate"], 2))
st.write("Odd Vitória Visitante:", round(odds_casa["Match Odds"]["Odd Vitória Visitante"], 2))

# Informações Últimos 5 Jogos Time Visitante
st.header("Últimos 5 Jogos - Time Visitante")
vitorias_casa_visitante = st.slider("Número de Vitórias da Casa Últimos 5 Jogos:", min_value=0, max_value=5, value=3, key="vc_visitante")
empates_visitante = st.slider("Número de Empates Últimos 5 Jogos:", min_value=0, max_value=5, value=1, key="e_visitante")
derrotas_visitante = st.slider("Número de Derrotas Últimos 5 Jogos:", min_value=0, max_value=5, value=1, key="d_visitante")

odds_visitante = calcular_odd_match_handicap(vitorias_casa_visitante, empates_visitante, derrotas_visitante, "Visitante")
st.write("### Odds para Últimos 5 Jogos - Time Visitante:")
st.write("Odd Vitória da Casa:", round(odds_visitante["Match Odds"]["Odd Vitória da Casa"], 2))
st.write("Odd Empate:", round(odds_visitante["Match Odds"]["Odd Empate"], 2))
st.write("Odd Vitória Visitante:", round(odds_visitante["Match Odds"]["Odd Vitória Visitante"], 2))
