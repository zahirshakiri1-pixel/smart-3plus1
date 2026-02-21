import streamlit as st
import pandas as pd

st.title("Smart 3+1 System Generator")

st.write("Vendos 4 ndeshje me kuotat përkatëse")

match1 = st.number_input("Kuota Ndeshja 1", min_value=1.00, step=0.01)
match2 = st.number_input("Kuota Ndeshja 2", min_value=1.00, step=0.01)
match3 = st.number_input("Kuota Ndeshja 3", min_value=1.00, step=0.01)
match4 = st.number_input("Kuota Ndeshja 4 (High odd)", min_value=1.00, step=0.01)

if st.button("Gjenero Sistem"):
    total_full = match1 * match2 * match3 * match4
    
    comb1 = match1 * match2 * match3
    comb2 = match1 * match2 * match4
    comb3 = match1 * match3 * match4
    comb4 = match2 * match3 * match4
    
    st.subheader("Rezultatet")
    st.write(f"Kombinimi i plotë: {total_full:.2f}")
    st.write("Sistemi 3 nga 4:")
    st.write(f"Kombinimi 1: {comb1:.2f}")
    st.write(f"Kombinimi 2: {comb2:.2f}")
    st.write(f"Kombinimi 3: {comb3:.2f}")
    st.write(f"Kombinimi 4: {comb4:.2f}")
