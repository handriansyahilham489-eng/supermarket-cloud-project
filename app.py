import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('model_penjualan.pkl', 'rb'))

st.title("Prediksi Pendapatan Supermarket")

unit_price = st.number_input("Unit Price", min_value=0.0)
quantity = st.number_input("Quantity", min_value=1)

tax = st.number_input("Tax 5%", min_value=0.0)

branch = st.selectbox("Branch", [0,1,2])
city = st.selectbox("City", [0,1,2])

product_line = st.selectbox(
    "Product Line",
    [0,1,2,3,4,5]
)

if st.button("Prediksi"):

    data = pd.DataFrame([[
        unit_price,
        quantity,
        tax,
        branch,
        city,
        product_line
    ]], columns=[
        'Unit price',
        'Quantity',
        'Tax 5%',
        'Branch',
        'City',
        'Product line'
    ])

    hasil = model.predict(data)

    st.success(
        f"Prediksi Pendapatan : {hasil[0]:,.2f}"
    )
