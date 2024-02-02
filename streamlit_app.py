import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Welcome message
st.write("# Welcome to Streamlit!")



# Create columns for each token
num_tokens = 5  # Adjust based on the number of tokens you have
cols = st.columns(num_tokens)

# Placeholder URLs for the logos
logos_urls = {
    "PPAY": "https://s2.coinmarketcap.com/static/img/coins/64x64/7870.png",
    "DAI": "https://cryptologos.cc/logos/multi-collateral-dai-dai-logo.png",
    "USDT": "https://assets.coingecko.com/coins/images/30168/large/USDT_.png?1696529088",
    "ETH": "https://assets.coingecko.com/coins/images/279/large/ethereum.png?1696501628",
    "WBTC": "https://cryptologos.cc/logos/wrapped-bitcoin-wbtc-logo.png"
}
# Function to display a single cryptocurrency token
def display_crypto_token(token_name, token_price, price_change, logo_url):
    # Image and metric are now side by side in one column
    st.image(logo_url, width=50)  # Adjust width as necessary
    st.metric(label=token_name, value=f"${token_price}", delta=f"{price_change}%")

# Placeholder data for each token
tokens_data = {
    "PPAY": {"token_price": "0.33", "price_change": "+15.7%"},
    "DAI": {"token_price": "0.98", "price_change": "+15.7%"},
    "USDT": {"token_price": "1.01", "price_change": "+15.7%"},
    "ETH": {"token_price": "398.33", "price_change": "+15.7%"},
    "WBTC": {"token_price": "14324.33", "price_change": "+15.7%"}
}

# Display each token in its own column
for i, (token_name, token_info) in enumerate(tokens_data.items()):
    with cols[i]:
        display_crypto_token(token_name, **token_info, logo_url=logos_urls[token_name])

# Add a placeholder for the "View All" option in the last available column
with cols[-1]:  # Use -1 to refer to the last item of the list
    st.button("View All")

# Use the DataFrame with the extracted data points
df_response_times = pd.DataFrame({
    "Date_Index": [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0],
    "Response_Time": [330, 320, 310, 340, 320, 320, 330, 310, 320, 310, 300, 310, 320]
})

# Convert Date_Index to actual dates for visualization
date_range = pd.date_range(start="2022-11-22", periods=len(df_response_times), freq='W-TUE')
df_response_times['Date'] = date_range

# Create a line chart
st.altair_chart(alt.Chart(df_response_times).mark_line().encode(
    x='Date:T',  # T specifies that the field is temporal (time)
    y='Response_Time:Q'  # Q specifies that the field is a quantitative measure
).properties(width=700, height=400), use_container_width=True)

# Use the DataFrame with the extracted data points
df_volumes = pd.DataFrame({
    "Month_Index": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0],
    "Volume": [50, 225, 200, 150, 100, 75, 100, 80, 75, 70, 75, 70]
})

# Convert Month_Index to actual months for visualization
df_volumes['Month'] = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Create an area chart
st.altair_chart(alt.Chart(df_volumes).mark_area().encode(
    x='Month',
    y='Volume:Q'
).properties(width=700, height=400), use_container_width=True)
