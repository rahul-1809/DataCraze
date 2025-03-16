import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load dataset
def load_data():
    file_path = "final_preprocessed.csv"  # Update path if needed
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    numeric_columns = ["retweetCount", "likeCount", "viewCount", "author_followers", "author_following"]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["date"] + numeric_columns)
    return df

df = load_data()

st.set_page_config(layout="wide", page_title="Twitter Data Dashboard")
st.title("📊 Twitter Data Dashboard 🐦")

# Sidebar Filters
st.sidebar.header("🎛️ Filters")
languages = ["All"] + sorted(df["lang"].astype(str).unique().tolist())
selected_langs = st.sidebar.multiselect("🌎 Select Language(s)", languages, default=["All"])
start_date = st.sidebar.date_input("📅 Start Date", df["date"].min())
end_date = st.sidebar.date_input("📅 End Date", df["date"].max())

# Apply filters
filtered_df = df.copy()
if "All" not in selected_langs:
    filtered_df = filtered_df[filtered_df["lang"].isin(selected_langs)]
filtered_df = filtered_df[(filtered_df["date"] >= pd.to_datetime(start_date)) & (filtered_df["date"] <= pd.to_datetime(end_date))]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("📝 Total Tweets", filtered_df.shape[0])
col2.metric("❤️ Total Likes", filtered_df["likeCount"].sum())
col3.metric("🔄 Total Retweets", filtered_df["retweetCount"].sum())

col4, col5, col6 = st.columns(3)
col4.metric("👥 Total Followers", filtered_df["author_followers"].sum())
col5.metric("👍 Avg Likes per Tweet", round(filtered_df["likeCount"].mean(), 2))
col6.metric("🔁 Avg Retweets per Tweet", round(filtered_df["retweetCount"].mean(), 2))

# Grid Layout for Graphs
col1, col2 = st.columns(2)

# Engagement Trends Over Time
fig_time = px.line(filtered_df.groupby("date")[['retweetCount', 'likeCount', 'viewCount']].sum().reset_index(),
                   x="date", y=["retweetCount", "likeCount", "viewCount"],
                   title="📈 Daily Engagement Trends")
col1.plotly_chart(fig_time, use_container_width=True)

# Language Distribution
fig_lang = px.pie(filtered_df, names="lang", title="🌍 Tweets by Language")
col2.plotly_chart(fig_lang, use_container_width=True)

# Second Row Layout
col3, col4 = st.columns(2)

# Engagement Distribution by Verification Status
fig_box = px.box(filtered_df, x="author_isVerified", y="retweetCount", title="✅ Engagement by Verification Status")
col3.plotly_chart(fig_box, use_container_width=True)

# New Graph: Retweets vs Likes Scatter Plot
fig_scatter = px.scatter(filtered_df, x="likeCount", y="retweetCount", color="lang", title="🔍 Retweets vs Likes")
col4.plotly_chart(fig_scatter, use_container_width=True)

# Third Row Layout
col5, col6 = st.columns(2)

# Distribution of Author Followers
fig_hist = px.histogram(filtered_df, x="author_followers", title="📊 Distribution of Author Followers", nbins=50)
col5.plotly_chart(fig_hist, use_container_width=True)

# Correlation Matrix
fig_corr = px.imshow(filtered_df[["retweetCount", "likeCount", "viewCount", "author_followers"]].corr(),
                      title="📌 Correlation Matrix of Engagement Features", text_auto=True)
col6.plotly_chart(fig_corr, use_container_width=True)

# New Bar Plot: Average Retweets Per Day
retweets_per_day = filtered_df.groupby("date")["retweetCount"].mean().reset_index()
fig_avg_retweets = px.bar(retweets_per_day, x="date", y="retweetCount", title="📊 Average Retweets Per Day")
st.plotly_chart(fig_avg_retweets, use_container_width=True)

