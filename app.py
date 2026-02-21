import streamlit as st
import pandas as pd
import itertools

st.title("Smart 3+1 Auto Generator (Mozzart CSV)")

uploaded_file = st.file_uploader("Ngarko CSV nga Mozzart", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("Preview i të dhënave:")
    st.dataframe(df)

    # Supozojmë që CSV ka kolonë 'Match' dhe 'Odd'
    low_odds = df[df['Odd'] <= 1.30]
    high_odds = df[df['Odd'] >= 2.80]

    if len(low_odds) >= 3 and len(high_odds) >= 1:
        selected_low = low_odds.head(3)
        selected_high = high_odds.head(1)

        final_matches = pd.concat([selected_low, selected_high])

        st.subheader("4 Ndeshjet e Zgjedhura:")
        st.dataframe(final_matches)

        odds_list = final_matches['Odd'].tolist()

        st.subheader("Sistemi 3/4:")
        for combo in itertools.combinations(odds_list, 3):
            total = 1
            for odd in combo:
                total *= odd
            st.write(combo, "=", round(total, 2))

        st.subheader("Sistemi 4/4:")
        total_4 = 1
        for odd in odds_list:
            total_4 *= odd
        st.write("4/4 =", round(total_4, 2))

    else:
        st.warning("Nuk ka mjaftueshëm ndeshje sipas kriterit.")
