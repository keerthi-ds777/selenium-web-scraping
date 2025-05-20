import pandas as pd 
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

#kerala bus
list_k=[]
df_k=pd.read_csv('df_kl.csv')
for i,r in df_k.iterrows():
    list_k.append(r['route_names'])
    
#andhara pradesh bus

list_ap=[]
df_ap=pd.read_csv('df_ap.csv')
for i,r in df_ap.iterrows():
    list_ap.append(r['route_names'])

#telungana bus

list_tl=[]
df_tl=pd.read_csv('df_tl.csv')
for i,r in df_tl.iterrows():
    list_tl.append(r['route_names'])

#kadamba bus

list_kb=[]
df_kb=pd.read_csv('df_kb.csv')
for i,r in df_kb.iterrows():
    list_kb.append(r['route_names'])

#rajasthan bus

list_rs=[]
df_rs=pd.read_csv('df_rs.csv')
for i,r in df_rs.iterrows():
    list_rs.append(r['route_names'])
    
#south bengal

list_sb=[]
df_sb=pd.read_csv('df_sb.csv')
for i,r in df_sb.iterrows():
    list_sb.append(r['route_names'])
    
#himachal pradesh

list_hr=[]
df_hr=pd.read_csv('df_hr.csv')
for i,r in df_hr.iterrows():
    list_hr.append(r['route_names'])
    
#assam

list_as=[]
df_as=pd.read_csv('df_as.csv')
for i,r in df_as.iterrows():
    list_as.append(r['route_names'])

#uttar pradesh

list_up=[]
df_up= pd.read_csv('df_up.csv')
for i,r in df_up.iterrows():
    list_up.append(r['route_names'])

#west bengal

list_wb=[]
df_wb=pd.read_csv('df_up.csv')
for i,r in df_wb.iterrows():
    list_wb.append(r['route_names'])
    

#setting page configuration
slt.set_page_config(layout='wide')

web= option_menu(menu_title='Red Bus',
                 options=['Home','states and routes'],
                 icons=['house','info circle'],
                 orientation='Horizontal')

#setting home page 
if web=='Home':
    slt.title('Red Bus Information System')
    slt.subheader(":[Domain:] Transportation")
    slt.subheader(":[Objective:]")  
    slt.image('redbus.jpg', caption='Red Bus',use_column_width=True)
    slt.markdown('Welcome to Red Bus Information System, an interactive platform that provides real-time updates on Kerala, Andhra Pradesh, Telangana, Kadamba, Rajasthan, South Bengal, Himachal Pradesh, Assam, Uttar Pradesh, and West Bengal Red Bus services.')
    slt.markdown('Please select the state and route you are interested in.')
    
# states and route page settings
if web=='states and routes':
   S= slt.selectbox("Lists of states",['Kerala','Andhara pradesh','Telungana','Kadambam','Rajasthan','Assam','South bengal','Uttar pradesh','Himachal pradesh'])
   select_fare=slt.radio('choose bus fare range',['50-1000','1000-2000','2000 above'])
 
   if S=='Kerala':
       k= slt.selectbox('list of routes',list_k)
       
       if select_fare=="50-1000":
            conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='redbus')
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
                conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='redbus')
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
            
  

# routes fpr andhra pradesh

   
   if S=='Andhra pradesh':
       k= slt.selectbox('list of routes',list_ap)
       
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
            
        
# routes for telangana
    
   if S=='Telungana':
       k= slt.selectbox('list of routes',list_tl)
       
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
            

# routes for kadambam
   if S=='Kadambam':
       k= slt.selectbox('list of routes',list_kb)
       
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
            

# Rajasthan
   if S=='Rajastahan':
       k= slt.selectbox('list of routes',list_rs)
       
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
            
# South bengal 
    
   if S=='South bengal':
       k= slt.selectbox('list of routes',list_tl)
       
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
                

# assam 
   if S=='Assam':
       k= slt.selectbox('list of routes',list_as)
       
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