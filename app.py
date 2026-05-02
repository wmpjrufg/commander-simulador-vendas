import streamlit as st

# Configuração da página
st.set_page_config(page_title="Simulador de Incremento de Vendas", layout="centered")

st.title("📊 Simulador de Incremento de Vendas (IoT)")
st.write("Simule o impacto do sistema nas vendas por comanda do seu cliente no mês, além de projetar o Retorno sobre o Investimento (ROI).")

st.divider()

# --- SEÇÃO 1: DADOS DO ESTABELECIMENTO (AGORA EM COLUNA ÚNICA) ---
st.header("1. Dados do Estabelecimento")

num_comandas = st.number_input("Nº de Comandas por Mês", min_value=0, step=1)

st.subheader("Cerveja (Garrafa)")
perc_cerveja = st.number_input("% de Venda Cerveja", min_value=0.0, max_value=500.0, step=0.1, help="Qual a porcentagem das comandas totais que consomem cerveja?")
valor_cerveja = st.number_input("Preço de Venda Cerveja (R$)", min_value=0.0, step=0.01)

st.subheader("Chopp")
perc_chopp = st.number_input("% de Venda Chopp", min_value=0.0, max_value=500.0, step=0.1, help="Qual a porcentagem das comandas totais que consomem chopp?")
valor_chopp = st.number_input("Preço de Venda Chopp (R$)", min_value=0.0, step=0.01)

st.divider()

st.header("2. Projeção de Incremento (IoT)")

perc_inc_cerveja = st.number_input("% de comandas que venderão Cerveja a mais", min_value=0.0, max_value=100.0, step=1.0)
n_mais_cerveja = st.number_input("N+ Cervejas por Comanda", min_value=0, value=1, step=1)

perc_inc_chopp = st.number_input("% de comandas que venderão Chopp a mais", min_value=0.0, max_value=100.0, step=1.0)
n_mais_chopp = st.number_input("N+ Chopp por Comanda", min_value=0, value=1, step=1)

st.divider()

st.header("3. Custos do Sistema")
investimento = st.number_input("Valor do Investimento na Ferramenta IoT (R$)", min_value=0.0, value=5000.00, step=100.0)

st.divider()

# --- CÁLCULOS (Igual à planilha) ---
# Quantidade base de comandas por produto
qtd_comandas_cerveja = num_comandas * (perc_cerveja / 100)
qtd_comandas_chopp = num_comandas * (perc_chopp / 100)

# Quantidade de comandas que terão incremento
comandas_inc_cerveja = qtd_comandas_cerveja * (perc_inc_cerveja / 100)
comandas_inc_chopp = qtd_comandas_chopp * (perc_inc_chopp / 100)

# Receita gerada pelo incremento
receita_inc_cerveja = comandas_inc_cerveja * n_mais_cerveja * valor_cerveja
receita_inc_chopp = comandas_inc_chopp * n_mais_chopp * valor_chopp

# Total de incremento financeiro
total_incremento = receita_inc_cerveja + receita_inc_chopp

# Cálculo do ROI: (Retorno - Custo) / Custo
if investimento > 0:
    roi_percentual = ((total_incremento - investimento) / investimento) * 100
else:
    roi_percentual = 0.0

# --- SEÇÃO DE RESULTADOS ---
st.header("📈 Resultados da Simulação")

# Exibindo os resultados em cards bonitos (métricas)
col_res1, col_res2, col_res3 = st.columns(3)

col_res1.metric(label="Incremento Cerveja", value=f"R$ {receita_inc_cerveja:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
col_res2.metric(label="Incremento Chopp", value=f"R$ {receita_inc_chopp:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
col_res3.metric(label="Aumento Bruto Total", value=f"R$ {total_incremento:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

st.write("") # Espaço

# Destaque para o ROI e Lucro Líquido
lucro_liquido = total_incremento - investimento
st.success(f"**Lucro Líquido Estimado (Total - Investimento):** R$ {lucro_liquido:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

if investimento > 0:
    if roi_percentual >= 0:
        st.info(f"🚀 **ROI (Retorno sobre Investimento):** {roi_percentual:.2f}%")
    else:
        st.error(f"⚠️ **ROI (Retorno sobre Investimento):** {roi_percentual:.2f}% (Prejuízo)")

# # Tabela de apoio para conferência de números (opcional, para ver as bases)
# with st.expander("Ver detalhes dos cálculos (Oculto)"):
#     st.write(f"- Comandas Cerveja Mês: {qtd_comandas_cerveja:,.0f}")
#     st.write(f"- Comandas Chopp Mês: {qtd_comandas_chopp:,.0f}")
#     st.write(f"- Comandas Cerveja c/ Incremento ({perc_inc_cerveja}%): {comandas_inc_cerveja:,.0f}")
#     st.write(f"- Comandas Chopp c/ Incremento ({perc_inc_chopp}%): {comandas_inc_chopp:,.0f}")