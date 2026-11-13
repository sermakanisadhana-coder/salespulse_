
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="DIT Sales Report Automation",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 DIT Sales Report Automation")
st.subheader("Sales Performance Dashboard")

st.markdown("""
Welcome to the Sales Report Automation System.
Upload your sales dataset to view and validate your records.
""")

st.divider()

# File upload
st.header("Upload Sales Dataset")

uploaded_file = st.file_uploader(
    "Choose your Excel or CSV file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    try:
        # Read uploaded file
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")

        # Required columns
        required_columns = [
            "Employee Name",
            "Sales Target",
            "Sales Achieved"
        ]

        missing_columns = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_columns:
            st.error(
                "Missing required columns: "
                + ", ".join(missing_columns)
            )

        else:
            st.success("Dataset validation successful!")

            # Dashboard metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Employees", len(df))

            with col2:
                st.metric(
                    "Total Sales Target",
                    f"{df['Sales Target'].sum():,.2f}"
                )

            with col3:
                st.metric(
                    "Total Sales Achieved",
                    f"{df['Sales Achieved'].sum():,.2f}"
                )

            # Data preview
            st.header("Sales Data Preview")
            st.dataframe(df, use_container_width=True)

            # Download uploaded data
            csv_data = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "Download Dataset",
                data=csv_data,
                file_name="Sales_Data.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"Unable to process file: {e}")

else:
    st.info("Please upload a CSV or Excel sales dataset.")

st.divider()

st.caption("DIT-P05 | Team T05 | Sales Report Automation")
