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

# --- SEÇÃO 3: INVESTIMENTO ---
st.header("3. Custos do Sistema")

col_custo1, col_custo2 = st.columns(2)
with col_custo1:
    custo_implantacao = st.number_input("Valor da Implantação (R$ - Pagamento Único)", min_value=0.0, value=2000.00, step=100.0)
with col_custo2:
    custo_mensal = st.number_input("Valor da Mensalidade (R$ / Mês)", min_value=0.0, value=500.00, step=50.0)

st.divider()

# --- LÓGICA DE CÁLCULO ---
# Quantidade base
qtd_comandas_cerveja = num_comandas * (perc_cerveja / 100)
qtd_comandas_chopp = num_comandas * (perc_chopp / 100)

# Impacto do IoT (Comandas atingidas)
comandas_inc_cerveja = qtd_comandas_cerveja * (perc_inc_cerveja / 100)
comandas_inc_chopp = qtd_comandas_chopp * (perc_inc_chopp / 100)

# Financeiro Mensal
receita_inc_cerveja_mensal = comandas_inc_cerveja * n_mais_cerveja * valor_cerveja
receita_inc_chopp_mensal = comandas_inc_chopp * n_mais_chopp * valor_chopp
total_bruto_mensal = receita_inc_cerveja_mensal + receita_inc_chopp_mensal

# Financeiro Anual
receita_inc_cerveja_anual = receita_inc_cerveja_mensal * 12
receita_inc_chopp_anual = receita_inc_chopp_mensal * 12
total_bruto_anual = total_bruto_mensal * 12

# Custos e ROI Anual
custo_total_anual = custo_implantacao + (custo_mensal * 12)
lucro_liquido_anual = total_bruto_anual - custo_total_anual

if custo_total_anual > 0:
    roi_anual = (lucro_liquido_anual / custo_total_anual) * 100
else:
    roi_anual = 0.0

# --- EXIBIÇÃO DOS RESULTADOS ---
st.header("📈 Resultados da Simulação")

# Função para formatação de Moeda Brasileira
def format_real(valor):
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# VISÃO MENSAL
st.subheader("📅 Visão Mensal")
c1, c2, c3 = st.columns(3)
c1.metric("Aumento Cerveja (Mês)", format_real(receita_inc_cerveja_mensal))
c2.metric("Aumento Chopp (Mês)", format_real(receita_inc_chopp_mensal))
c3.metric("Total Bruto (Mês)", format_real(total_bruto_mensal))

st.write("") # Espaço em branco

# VISÃO ANUAL
st.subheader("🗓️ Visão Anual (12 Meses)")
c4, c5, c6 = st.columns(3)
c4.metric("Aumento Cerveja (Ano)", format_real(receita_inc_cerveja_anual))
c5.metric("Aumento Chopp (Ano)", format_real(receita_inc_chopp_anual))
c6.metric("Total Bruto (Ano)", format_real(total_bruto_anual))

st.divider()

# ROI ANUAL
st.header("💰 Análise de Retorno (1º Ano)")
st.write(f"Custo total estimado no primeiro ano (Implantação + 12x Mensalidades): **{format_real(custo_total_anual)}**")

if lucro_liquido_anual > 0:
    st.success(f"**Ganho Líquido Estimado no Ano (Receita Total - Custos):** {format_real(lucro_liquido_anual)}")
    st.balloons()
else:
    st.error(f"**Resultado Líquido Anual:** {format_real(lucro_liquido_anual)}")

st.info(f"🚀 **ROI Anual (Retorno sobre Investimento):** {roi_anual:.2f}%")