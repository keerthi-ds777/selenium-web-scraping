import pandas as pd 
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

#kerala bus
list_k=[]
df_k=pd.read_csv(r'data\bus_details\bus_details_kl.csv')
for i,r in df_k.iterrows():
    list_k.append(r['RouteName'])
    
#andhara pradesh bus

list_ap=[]
df_ap=pd.read_csv(r'data\bus_details\bus_details_ap.csv')
for i,r in df_ap.iterrows():
    list_ap.append(r['RouteName'])

#telungana bus

list_tl=[]
df_tl=pd.read_csv(r'data\bus_details\bus_details_tl.csv')
for i,r in df_tl.iterrows():
    list_tl.append(r['RouteName'])

#kadamba bus

list_kb=[]
df_kb=pd.read_csv(r'data\bus_details\bus_details_kb.csv')
for i,r in df_kb.iterrows():
    list_kb.append(r['RouteName'])

#rajasthan bus

list_rs=[]
df_rs=pd.read_csv(r'data\bus_details\bus_details_rs.csv')
for i,r in df_rs.iterrows():
    list_rs.append(r['RouteName'])
    
#south bengal

list_sb=[]
df_sb=pd.read_csv(r'data\bus_details\bus_details_sb.csv')
for i,r in df_sb.iterrows():
    list_sb.append(r['RouteName'])
    
#himachal pradesh

list_hr=[]
df_hr=pd.read_csv(r'data\bus_details\bus_details_hp.csv')
for i,r in df_hr.iterrows():
    list_hr.append(r['RouteName'])
    
#assam

list_as=[]
df_as=pd.read_csv(r'data\bus_details\bus_details_as.csv')
for i,r in df_as.iterrows():
    list_as.append(r['RouteName'])

#uttar pradesh

list_up=[]
df_up= pd.read_csv(r'data\bus_details\bus_details_up.csv')
for i,r in df_up.iterrows():
    list_up.append(r['RouteName'])

#west bengal

list_wb=[]
df_wb=pd.read_csv(r'data\bus_details\bus_details_wb.csv')
for i,r in df_wb.iterrows():
    list_wb.append(r['RouteName'])
    

#setting page configuration
slt.set_page_config(layout='wide')

web= option_menu(menu_title='Red Bus',
                 options=['Home','states and routes'],
                 icons=['house','info circle'],
                 orientation='Horizontal')

#setting home page 
# Home page setting
if web=="Home":
    #slt.image("redBus-Logo-Vector.svg", width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:] Transportation")
    slt.subheader(":blue[Objective:]")
    slt.markdown(""" The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solut...""")
    slt.subheader(":blue[Overview:]")
    slt.markdown("""Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. 
    Pandas: use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis."""
    )
    slt.markdown("""MySQL with help of sql to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
    and the data was efficiently inserted into relevant tables for storage and retrieval""")
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user friendly framework for data visualization and analysis.")
    slt.subheader(":blue[Skill take:]")
    slt.markdown("Selenium, Python, Pandas, Mysql, mysql-connector-python, Streamlit.")
    slt.subheader(":blue[Developed by:] Kavitha Thangavel")

# States and Routes page setting
if web=="🌐 States and Routes":
   slt.title("States and Routes")
   slt.write("Select a state to view available routes.")
   S = slt.selectbox("Lists of States",["Kerala","Andhra Pradesh","Telugana","Goa",
        "Rajasthan","South Bengal","Haryana","Assam","Uttra Pradesh","West Bengal"])

   select_fare = slt.radio("choose bus fare range",["50-1000","1000-2000","2000 and above"])


 
   if S=='Kerala':
       slt.title("States and Routes")
       slt.write("Select a state to view available routes.")
    # Add more widgets or data display here
       k= slt.selectbox('list of routes',list_k)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='redbus')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Bus_type','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,password='1234',database='redbus')
                cursor=conn.cursor()
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price < 2000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            
  

# routes fpr andhra pradesh

   
   if S=='Andhra pradesh':
       k= slt.selectbox('list of routes',list_ap)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price < 2000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            
        
# routes for telangana
    
   if S=='Telungana':
       k= slt.selectbox('list of routes',list_tl)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price < 2000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

# routes for kadambam
   if S=='Kadambam':
       k= slt.selectbox('list of routes',list_kb)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price < 2000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

# Rajasthan
   if S=='Rajastahan':
       k= slt.selectbox('list of routes',list_rs)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price < 2000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            
# South bengal 
    
   if S=='South bengal':
       k= slt.selectbox('list of routes',list_tl)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price < 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                

# assam 
   if S=='Assam':
       k= slt.selectbox('list of routes',list_as)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='127.0.0.1',port=3306,username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
            conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price < 2000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            
# Himachal pradesh
    
   if S=='Himachal pradesh':
       k= slt.selectbox('list of routes',list_hr)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price < 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)

# uttar pradesh
    
   if S=='Uttar pradesh':
       k= slt.selectbox('list of routes',list_up)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price < 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)


# west bengal

    
   if S=='Himachal pradesh':
       k= slt.selectbox('list of routes',list_hr)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
            cursor=conn.cursor()
            
            query=f'''select * from bus_details where
            price between  50 and 1000 and Route_name = {k}
            order by price desc'''

            cursor.execute(query)
            result=cursor.fetchall()
            df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                             'Seats_available','Rating','Route_link','Route_name'])
            slt.dataframe(df)
            

       elif select_fare=="1000-2000":
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price between  1000 and 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)
                
       elif select_fare=="2000 and above":
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='practice connection')
                cursor=conn.cursor()
                
                query=f'''select * from bus_details where
                price < 2000 and Route_name = {k}
                order by price desc'''

                cursor.execute(query)
                result=cursor.fetchall()
                df=pd.DataFrame(result, columns=['ID','Bus_Name','Start_Time','End_Time','Time_duration','Price',
                                                'Seats_available','Rating','Route_link','Route_name'])
                slt.dataframe(df)