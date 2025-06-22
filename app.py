import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# Load route lists from CSVs
def load_routes(file_path):
    return pd.read_csv(file_path)['RouteName'].unique().tolist()

list_k = load_routes('data/bus_details/bus_details_kl.csv')
list_ap = load_routes('data/bus_details/bus_details_ap.csv')
list_tl = load_routes('data/bus_details/bus_details_tl.csv')
list_kb = load_routes('data/bus_details/bus_details_kb.csv')
list_rs = load_routes('data/bus_details/bus_details_rs.csv')
list_sb = load_routes('data/bus_details/bus_details_sb.csv')
list_hr = load_routes('data/bus_details/bus_details_hp.csv')
list_as = load_routes('data/bus_details/bus_details_as.csv')
list_up = load_routes('data/bus_details/bus_details_up.csv')
list_wb = load_routes('data/bus_details/bus_details_wb.csv')

# Page setup
slt.set_page_config(layout='wide')

web = option_menu(menu_title='Red Bus',
                  options=['Home', 'States and Routes'],
                  icons=['house', 'info-circle'],
                  orientation='horizontal')

# Home Page
if web == "Home":
    #slt.image("data\image\redBus-Logo-Vector.svg", width=200)

    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:] Transportation")
    slt.subheader(":blue[Objective:]")
    slt.markdown(""" The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution.""")
    slt.subheader(":blue[Overview:]")
    slt.markdown("""
    Selenium: A tool used for automating web browsers, often for web scraping.
    Pandas: Used to transform and preprocess data for analysis.
    MySQL: Stores the processed data in a SQL database.
    Streamlit: For interactive data visualization and filtering.
    """)
    slt.subheader(":blue[Skill take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL, mysql-connector-python, Streamlit.")
    slt.subheader(":blue[Developed by:] R Keerthi")

# State-Route-Fare Filter Logic
def render_bus_data(route_list):
    k = slt.selectbox('List of routes', route_list)
    select_fare = slt.radio("Choose bus fare range", ["50-1000", "1000-2000", "2000 and above"])

    if select_fare == "50-1000":
        fare_filter = "price BETWEEN 50 AND 1000"
    elif select_fare == "1000-2000":
        fare_filter = "price BETWEEN 1000 AND 2000"
    else:
        fare_filter = "price > 2000"

    try:
        conn = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='1234', database='redbus')
        cursor = conn.cursor()
        query = f"""
            SELECT * FROM bus_details
            WHERE {fare_filter} AND Route_name = '{k}'
            ORDER BY price DESC
        """
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=['ID', 'Bus_Name','Bus_Type' ,'Start_Time', 'End_Time', 'Time_duration', 'Price',
                                           'Seats_available', 'Rating', 'Route_link', 'Route_name'])
        df["Route_link"] = df["Route_link"].apply(lambda x: f'<a href="{x}" target="_blank">Link</a>')

# Optional: rename column for display
        df.rename(columns={"Route_link": "Booking Link"}, inplace=True)

        slt.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

    except Exception as e:
        slt.error(f"Database error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

# States and Routes Page
if web == "States and Routes":
    S = slt.selectbox("Lists of States", [
        "Kerala", "Andhra Pradesh", "Telugana", "Kadambam", "Rajasthan",
        "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"])

    if S == 'Kerala':
        render_bus_data(list_k)
    elif S == 'Andhra Pradesh':
        render_bus_data(list_ap)
    elif S == 'Telugana':
        render_bus_data(list_tl)
    elif S == 'Kadambam':
        render_bus_data(list_kb)
    elif S == 'Rajasthan':
        render_bus_data(list_rs)
    elif S == 'South Bengal':
        render_bus_data(list_sb)
    elif S == 'Haryana':
        render_bus_data(list_hr)
    elif S == 'Assam':
        render_bus_data(list_as)
    elif S == 'Uttar Pradesh':
        render_bus_data(list_up)
    elif S == 'West Bengal':
        render_bus_data(list_wb)
