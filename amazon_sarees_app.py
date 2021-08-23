import pandas as pd
import streamlit as st

st.set_page_config('Amazon Recommendation System')

odf = pd.read_csv('cleaned_dataset_of_sarees_recomendation.csv')
sdf = pd.read_csv('final_sililarities_of_all_values.csv')


def get_recommendation(id):
    rec_df = odf.iloc[sdf.iloc[id][1:]]
    return rec_df

st.header('Amazon Recommendation System')


product_list = odf['desc'].values


selected_product = st.selectbox(
    "Type or select a product from the dropdown",
    range(len(product_list)),
    format_func=lambda x: product_list[x]
)

col1, col2 = st.columns((1,2))

with col1:
    st.markdown(
    f"""
    <div class="container" style="float:right;">
        <img class="logo-img" src="{odf['image_url'].values[selected_product]}">
    </div>
    """,
    unsafe_allow_html=True
)
with col2:
    st.markdown('<p style="font-weight: bold;">{}</p>'.format(odf['brand'].values[selected_product]), unsafe_allow_html=True)
    st.markdown('<p>{}</p>'.format(odf['desc'].values[selected_product]), unsafe_allow_html=True)
    st.markdown('<p><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color: #565959;">₹{}</span></p>'.format(odf['disc_price'].values[selected_product], odf['actual_price'].values[selected_product]), unsafe_allow_html=True)


st.markdown('<p style="font-size: 1.2rem;">Products related to this item:</p>', unsafe_allow_html=True)

st.write()

rec_df = get_recommendation(selected_product)

count = 0

for i in range(4):
    for j in st.columns(3):
        
        if count == 10:
            break
        with j:
            st.image(rec_df['image_url'].values[count])
            st.markdown('<p style="text-align: center; font-weight: bold;">{}</p>'.format(rec_df['brand'].values[count]), unsafe_allow_html=True)
            st.markdown('<p style="text-align: center;">{}</p>'.format(rec_df['desc'].values[count]), unsafe_allow_html=True)
            st.markdown('<p style="text-align: center;"><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color: #565959;">₹{}</span></p>'.format(rec_df['disc_price'].values[count], rec_df['actual_price'].values[count]), unsafe_allow_html=True)
        count += 1
