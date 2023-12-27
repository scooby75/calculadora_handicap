import streamlit as st

def calcular_probabilidades(vitorias, empates, derrotas):
    total_partidas = vitorias + empates + derrotas
    total_partidas = max(total_partidas, 1)  # Evita divisão por zero
    prob_vitoria = vitorias / total_partidas
    prob_empate = empates / total_partidas
    prob_derrota = derrotas / total_partidas
    return prob_vitoria, prob_empate, prob_derrota

def calcular_odds(prob_vitoria, prob_empate, prob_derrota):
    odd_vitoria = 1 / prob_vitoria if prob_vitoria > 0 else float('inf')
    odd_empate = 1 / prob_empate if prob_empate > 0 else float('inf')
    odd_derrota = 1 / prob_derrota if prob_derrota > 0 else float('inf')
    return odd_vitoria, odd_empate, odd_derrota

def calcular_handicap(prob_vitoria, prob_empate, prob_derrota):
    linha_handicap = (prob_vitoria + prob_empate - prob_derrota) / 2
    linha_handicap = max(linha_handicap, 0)  # Garante que a linha de handicap seja no mínimo 0
    odd_vitoria_handicap = 1 / (prob_vitoria + linha_handicap) if prob_vitoria + linha_handicap > 0 else float('inf')
    odd_empate_handicap = 1 / (prob_empate + linha_handicap) if prob_empate + linha_handicap > 0 else float('inf')
    odd_derrota_handicap = 1 / (prob_derrota + linha_handicap) if prob_derrota + linha_handicap > 0 else float('inf')
    return linha_handicap, odd_vitoria_handicap, odd_empate_handicap, odd_derrota_handicap

# Interface do Streamlit
st.title("Calculadora de Odds")

# Informações Últimos 5 Jogos
st.header("Últimos 5 Jogos")
vitorias = st.slider("Número de Vitórias:", min_value=0, max_value=5, value=2)
empates = st.slider("Número de Empates:", min_value=0, max_value=5, value=1)
derrotas = st.slider("Número de Derrotas:", min_value=0, max_value=5, value=2)

# Cálculos
prob_vitoria, prob_empate, prob_derrota = calcular_probabilidades(vitorias, empates, derrotas)
odd_vitoria, odd_empate, odd_derrota = calcular_odds(prob_vitoria, prob_empate, prob_derrota)
linha_handicap, odd_vitoria_handicap, odd_empate_handicap, odd_derrota_handicap = calcular_handicap(prob_vitoria, prob_empate, prob_derrota)

# Exibição dos Resultados
st.write("### Probabilidades:")
st.write(f"Probabilidade de Vitória: {prob_vitoria:.2%}")
st.write(f"Probabilidade de Empate: {prob_empate:.2%}")
st.write(f"Probabilidade de Derrota: {prob_derrota:.2%}")

st.write("### Odds:")
st.write(f"Odd Vitória: {odd_vitoria:.2f}")
st.write(f"Odd Empate: {odd_empate:.2f}")
st.write(f"Odd Derrota: {odd_derrota:.2f}")

st.write("### Handicap Asiático:")
st.write(f"Linha de Handicap: {linha_handicap:.2f}")
st.write(f"Odd Vitória (Handicap): {odd_vitoria_handicap:.2f}")
st.write(f"Odd Empate (Handicap): {odd_empate_handicap:.2f}")
st.write(f"Odd Derrota (Handicap): {odd_derrota_handicap:.2f}")
