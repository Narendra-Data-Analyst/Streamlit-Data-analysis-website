import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('DATA ANALYSIS AND VISUALIZATION')
st.info('Note : File should be in csv format')

st.subheader('Import your file here')
file = st.file_uploader("Upload dataset", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    st.write('Total rows & columns:', df.shape)

    if st.button('Preview dataset'):
        st.write(df.head(10))
        st.write('Column names and datatypes')
        st.write(df.dtypes)
    
    cleaned_df=df.copy()

    st.subheader('HANDLING NULL VALUES')

    if st.checkbox('Check null values'):
        st.write(cleaned_df.isnull().sum())

    if st.checkbox('Remove null values'):
        cleaned_df = cleaned_df.dropna()
        st.write(cleaned_df.isnull().sum())

    if st.checkbox('Fill null values'):
        cleaned_df = cleaned_df.fillna("N/A")
        st.write(cleaned_df.isnull().sum())

    st.subheader('HANDLING DUPLICATE VALUES')

    st.write('Total duplicates:',cleaned_df.duplicated().sum())

    if st.checkbox('Drop duplicates'):
        cleaned_df = cleaned_df.drop_duplicates()
        st.write('After removing duplicates:',cleaned_df.shape)
        st.write(cleaned_df.isnull().sum())

    st.subheader('CHANGING COLUMN NAMES')

    old_column_name = st.selectbox('Select column:', cleaned_df.columns)
    new_column_name = st.text_input('Enter new column name')

    if st.button("Preview changes"):
        cleaned_df.rename(columns={old_column_name: new_column_name}, inplace=True)
        st.success("Column replaced successfully")
        st.write(cleaned_df.head(5))

    csv = cleaned_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "DOWNLOAD CLEANED DATASET",
        csv,
        "cleaned_dataset.csv",
        "text/csv"
    )

    st.subheader("DATA VISUALIZATION")

    chart_type = st.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Line Chart", "Histogram"])


    x_axis = st.selectbox("Select X-axis column", cleaned_df.columns)
    y_axis = st.selectbox("Select Y-axis column", cleaned_df.columns)

    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
      ax.bar(df[x_axis], df[y_axis])

    elif chart_type == "Line Chart":
      ax.plot(df[x_axis], df[y_axis])

    elif chart_type == "Histogram":
      ax.hist(df[y_axis])

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(chart_type)

    st.pyplot(fig)
else :
   st.warning("please upload a csv for analysis")