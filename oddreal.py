import streamlit as st

# Título do aplicativo
st.title("Calculadora de Odd Real")

# Entrada de dados
valor_apostado = st.number_input("Valor Apostado (R$)", min_value=0.0, format="%.2f")
odd_back = st.number_input("Odd Back", min_value=0.0, format="%.2f")
comissao_exchange = st.number_input("Comissão da Exchange (%)", min_value=0.0, max_value=100.0, format="%.2f")

# Calcular a odd real
if valor_apostado > 0 and odd_back > 0:
    lucro_bruto = valor_apostado * (odd_back - 1)
    comissao = lucro_bruto * (comissao_exchange / 100)
    lucro_liquido = lucro_bruto - comissao
    odd_real = (lucro_liquido + valor_apostado) / valor_apostado

    # Exibir o resultado
    st.write(f"Lucro Bruto: R$ {lucro_bruto:.2f}")
    st.write(f"Comissão da Exchange: R$ {comissao:.2f}")
    st.write(f"Lucro Líquido: R$ {lucro_liquido:.2f}")
    st.write(f"Odd Real: {odd_real:.4f}")
else:
    st.write("Por favor, insira valores válidos para calcular a odd real.")
