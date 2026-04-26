import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import base64

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
BASE_DIR = os.path.dirname(__file__)

orders = pd.read_csv(os.path.join(BASE_DIR, "main_data_orders.csv"))
payments = pd.read_csv(os.path.join(BASE_DIR, "main_data_payment.csv"))

orders['order_month'] = pd.to_datetime(orders['order_month'])

# =========================
# LOAD LOGO
# =========================
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image(os.path.join(BASE_DIR, "logo.png"))

# =========================
# SIDEBAR
# =========================
st.sidebar.header("🔍 Filter Data")

year_filter = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(orders['order_month'].dt.year.unique())
)

month_range = st.sidebar.slider(
    "Rentang Bulan",
    1, 12, (1, 12)
)

# =========================
# FILTER DATA
# =========================
orders_filtered = orders[
    (orders['order_month'].dt.year == year_filter) &
    (orders['order_month'].dt.month >= month_range[0]) &
    (orders['order_month'].dt.month <= month_range[1])
]

# =========================
# HEADER
# =========================
st.markdown(f"""
<div style="display: flex; align-items: center;">
    <img src="data:image/png;base64,{logo_base64}" 
         style="width:70px; margin-right:15px; animation: zoom 2s ease-in-out infinite alternate;">
    <h1>E-Commerce Dashboard</h1>
</div>

<style>
@keyframes zoom {{
    from {{ transform: scale(1); opacity: 0.8; }}
    to {{ transform: scale(1.1); opacity: 1; }}
}}
</style>
""", unsafe_allow_html=True)

st.caption("Analisis tren pesanan dan metode pembayaran pelanggan")

st.markdown("---")

# =========================
# KPI
# =========================
col1, col2, col3 = st.columns(3)

total_orders = orders_filtered['order_id'].sum()
avg_orders = int(orders_filtered['order_id'].mean()) if len(orders_filtered) > 0 else 0

orders_year = orders[orders['order_month'].dt.year == year_filter]
baseline = orders_year['order_id'].sum()

delta = total_orders - baseline

payment_dist_kpi = payments.set_index('payment_type').iloc[:, 0]
top_payment = payment_dist_kpi.idxmax()

col1.metric("📦 Total Orders", f"{total_orders:,}", delta=f"{delta:+}")
col2.metric("📊 Avg Order", avg_orders)
col3.metric("💳 Top Payment", top_payment)

st.markdown("---")

# =========================
# LAYOUT
# =========================
left, right = st.columns(2)

# =========================
# CHART 1 - TREND
# =========================
with left:
    st.subheader("📈 Tren Pesanan Bulanan")

    monthly_orders = orders_filtered.groupby(
        orders_filtered['order_month'].dt.to_period("M")
    )['order_id'].sum()

    monthly_orders.index = monthly_orders.index.to_timestamp()

    fig, ax = plt.subplots()

    ax.plot(
        monthly_orders.index,
        monthly_orders.values,
        marker='o'
    )

    if len(monthly_orders) > 0:
        max_val = monthly_orders.max()
        max_idx = monthly_orders.idxmax()
        ax.scatter(max_idx, max_val)
        ax.annotate("Peak", (max_idx, max_val))

    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Order")
    plt.xticks(rotation=45)

    st.pyplot(fig)
    plt.close(fig)

    st.success("📌 Titik tertinggi (peak) ditandai pada grafik.")

# =========================
# CHART 2 - PAYMENT
# =========================
with right:
    st.subheader("💳 Distribusi Pembayaran")

    chart_type = st.selectbox(
        "Pilih jenis chart",
        ["Bar", "Pie"]
    )

    payment_dist = payments.set_index('payment_type').iloc[:, 0]
    payment_dist = payment_dist.sort_values(ascending=False)

    fig2, ax2 = plt.subplots()

    if chart_type == "Bar":
        payment_dist.plot(kind='bar', ax=ax2)
        ax2.set_ylabel("Jumlah Transaksi")
    else:
        payment_dist.plot(kind='pie', autopct='%1.1f%%', ax=ax2)

    ax2.set_xlabel("")

    st.pyplot(fig2)
    plt.close(fig2)

# =========================
# DATA TABLE + DOWNLOAD
# =========================
st.markdown("---")
st.subheader("📊 Data Detail")

show_data = st.checkbox("Tampilkan Data")

if show_data:
    st.dataframe(orders_filtered)

    csv = orders_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Data",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv'
    )

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("© 2026 - E-Commerce Data Analysis Dashboard")