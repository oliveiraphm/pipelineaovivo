import streamlit as st
from datetime import datetime, time
from contrato import Vendas
from pydantic import ValidationError
from database import salvar_no_postgres


def main():

    st.title("Sistema de CRM e VEndas da ZapFlow - Frontenn Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Campo para selecionar a data em que a venda foi realizada")
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada")
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda realizada")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos vendidos")
    produto = st.selectbox("Campo de seleção para escolher o produto vendido", ["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])


    if st.button("Salvar"):
        try:

            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email, 
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            salvar_no_postgres(venda)
            
        except ValidationError as e:
            st.error(f"Deu erro: {e}")

        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data e Hora da Venda: {data_hora}")
        st.write(f"Valor da Venda: R${valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")

if __name__ == "__main__":
    main()