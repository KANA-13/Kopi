import streamlit as st
import time

st.title('Simulasi Proses Pemanggangan Biji Kopi ☕')

st.write("""
Simulasi ini menggambarkan perubahan suhu dan waktu dalam proses pemanggangan biji kopi.
Gunakan slider untuk mengatur durasi pemanggangan!
""")

# Input dari user
durasi = st.slider('Durasi Pemanggangan (menit)', 1, 10, 5)

# Tombol mulai simulasi
if st.button('Mulai Pemanggangan'):
    st.write('Memulai proses pemanggangan...')
    progress_bar = st.progress(0)
    
    for menit in range(durasi):
        suhu = 100 + 10 * menit  # simulasi suhu naik
        st.write(f"Menit ke-{menit+1}: Suhu {suhu}°C")
        progress_bar.progress((menit+1) / durasi)
        time.sleep(1)  # simulasi waktu berjalan
        
    st.success('Pemanggangan Selesai! ☕')
