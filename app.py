import streamlit as st
import json
import os

FILE_PATH = "saldo.json"

# Fungsi load saldo
def load_saldo():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return data.get("saldo", 0)
    return 0

# Fungsi save saldo
def save_saldo(saldo):
    with open(FILE_PATH, "w") as f:
        json.dump({"saldo": saldo}, f)

# Load saldo awal
if "saldo" not in st.session_state:
    st.session_state.saldo = load_saldo()

st.title("💰 Aplikasi Tabungan Sederhana")

uang = st.number_input("Masukkan jumlah uang (Rp)", min_value=1000, step=1000)

if st.button("Tabung"):
    st.session_state.saldo += uang
    save_saldo(st.session_state.saldo)  # Simpan langsung ke file
    st.success(f"✅ Berhasil menabung Rp {uang:,}")

# Tampilkan total tabungan
st.subheader(f"Total Tabungan: Rp {st.session_state.saldo:,}")

# Visual bola 🔵 (1 bola = 1 juta)
jumlah_bola = st.session_state.saldo // 1_000_000
if jumlah_bola > 0:
    st.write("Isi Tabungan (🔵 = Rp 1.000.000):")
    st.write("".join(["🔵" for _ in range(jumlah_bola)]))
