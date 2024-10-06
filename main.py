import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np



st.set_page_config(page_title="Amine's Portfolio", page_icon="👋", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  # Utiliser la méthode json() pour obtenir les données JSON

# Charger l'animation Lottie
lottie_coder = load_lottie("https://lottie.host/a8fc6282-bbec-4d5f-84e4-e4bdde86b853/V3QK5jczlI.json")
lottie_contact = load_lottie("https://lottie.host/347d0c3f-587b-43c9-8815-21028beb1d4a/mtw0z0XqIX.json")
image_zelda = Image.open("project.png")
image_pokeshop = Image.open("pokeshop.png")
image_automate = Image.open("automate.png")
image_wordle = Image.open("wordle.png")

# Sidebar Section
with st.sidebar:
    category = option_menu(
        menu_title="Main Menu",
        options=['Portfolio', 'Analyse Uber', 'Analyse Tips', 'Joint Analysis'],
        icons=['briefcase', 'bar-chart', 'currency-dollar', 'layers'],
        orientation='vertical'
    )

    if category == 'Portfolio':
        selected = option_menu(
            menu_title="Portfolio",
            options=['About', 'Education', 'Experience', 'Projects', 'Contact'],
            icons=['person', 'book', 'briefcase', 'code-slash', 'chat-left-text-fill'],
            orientation='vertical'
        )
    elif category == 'Analyse Uber':
        selected = option_menu(
            menu_title="Analyse Uber",
            options=['Temporal Analysis', 'Spatial Analysis', 'Base Analysis', 'Trip Duration Analysis', 'Heatmap Analysis'],
            icons=['clock', 'geo-alt', 'building', 'speedometer', 'thermometer-half'],
            orientation='vertical'
        )
    elif category == 'Analyse Tips':
        selected = option_menu(
            menu_title="Analyse Tips",
            options=['Tipping Behavior Analysis', 'Gender and Smoking Analysis', 'Day and Time Analysis'],
            icons=['wallet', 'gender-ambiguous', 'calendar'],
            orientation='vertical'
        )
    elif category == 'Joint Analysis':
        selected = option_menu(
            menu_title="Joint Analysis",
            options=['Temporal vs Tips Analysis', 'Spatial vs Tips Analysis'],
            icons=['clock-history', 'geo'],
            orientation='vertical'
        )

# Header Section
with st.container():
    st.subheader("Welcome to my Portfolio! :wave:")
    st.title("I am Amine M'ZALI")
    st.write("Aspiring Data Scientist with a passion for Big Data and Machine Learning")
    st.write("##")

# About Section
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.write("##")
            st.header("About Me")
            st.write("I am currently a student at Efrei Paris and an intern at RATP, working on autonomous vehicle projects.")
            st.write("With a solid background in engineering, data science, and machine learning, I am enthusiastic about using technology to solve real-world challenges.")
            st.write("I am passionate about video games and aeronautics, and I am always looking for new challenges and enriching experiences!")
        with col2:
            if lottie_coder:
                st_lottie(lottie_coder, height=300, key="about_lottie")  # Afficher l'animation si elle est bien chargée
            else:
                st.write("Lottie animation failed to load.")

    st.write("---")

# Education Section
if selected == 'Education':
    with st.container():
        st.header("Education")
        st.write("##")
        st.write("Below is a summary of my educational background, including the courses I have taken and my specializations:")
        st.write("---")
        st.subheader("Efrei Paris : Master in Big Data & Machine Learning")
        st.write("2024-2026")
        st.write("""
        - **Program:** Grande École, Computer Engineering in apprenticeship
        - **Courses:**
            - Machine Learning, Deep Learning, Reinforcement Learning
            - Large Language Models (LLM)
            - Databases SQL/NoSQL, Data Lakes & Data Integration
            - Data Engineering, Functional Programming (Scala)
            - API & Webservices, DevOps & MLOps
            - Data Visualization, Cloud Certification for Big Data
            - Generative AI (Vision), Data Management & Ethics
        """)
        st.write("---")
        st.subheader("CY Cergy : Engineering in Computer Science")
        st.write("2023-2024")
        st.write("""
        - **Program:** Grande École, Computer Engineering in apprenticeship
        - **Courses:**
            - Advanced Algorithms and Programming, Web Programming
            - Python, Java, C
            - Operating Systems (Linux, Windows), Computer Architecture
            - Linear Optimization, Theory of Languages
            - Probability and Simulation, Databases
        """)
        st.write("---")
        st.subheader("Insa Rouen - Preparatory Engineering Cycle")
        st.write("2021-2023")
        st.write("""
        - **Program:** Sciences and Techniques for Engineering (First cycle)
        - **Courses:**
            - Structured Algorithmics, Imperative Programming
            - Introduction to AI, Data and Data Management
            - Mathematics (Algebra, Geometry, Probability, Statistics, Differential Equations)
            - Physics (Classical Mechanics, Thermodynamics, Optics, Electromagnetism)
        """)

# Experience Section
if selected == 'Experience':
    with st.container():
        st.header("Professional Experience")
        st.write("##")
        st.write("Here are some of the roles I have held, along with my responsibilities:")
        st.write("---")
        st.subheader("Data Scientist - Autonomous Vehicle Project")
        st.write("RATP | Apprenticeship | 2024-2026")
        st.write("""
        - **Description:** Responsible for processing and analyzing operational data from the RATP Autonomous Vehicle project.
        - **Tasks:**
            - Analyze data from vehicles, sensors, and other systems
            - Develop automated dashboards and reports
            - Create web apps and pages to present analysis results
            - Implement algorithms for automatic event detection
        """)
        st.write("---")
        st.subheader("Data Analyst & AI Scientist - HR Department")
        st.write("RATP | Apprenticeship | 2023-2024")
        st.write("""
        - **Description:** Data Analyst in the Human Resources department of RATP.
        - **Tasks:**
            - Analyze HR data, develop dashboards, and automated reports
            - Implement AI in HR processes, automate Excel files, and create custom dashboards
            - Provide expertise in data analysis and advisory services
        """)
        st.write("---")
        st.subheader("Logistician - Ambroise Paré Clinic")
        st.write("CDD | 2022")
        st.write("""
        - **Description:** Logistician in a pharmaceutical warehouse for a clinic.
        - **Tasks:**
            - Receive medical supplies, distribute them to clinics
            - Maintain computerized inventory of products, store items in automated shelving systems
            - Create stock allocations for various medical departments
        """)

# Projects Section
if selected == 'Projects':
    with st.container():
        st.header("My Projects")
        st.write('##')
        st.write("Below are some of the projects I've worked on, highlighting their features, technologies used, and links to the source code:")

        st.write("---")
        # Zelda Project
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.image(image_zelda, caption="Zelda Recreation Project", width=200)
        with col2:
            st.subheader("Recreating Zelda with Java")
            st.write("Recreate the foundation of Zelda: A Link To The Past in Java.")
            st.write("The player can:")
            st.write("""
            - Move around
            - Attack and lose health
            - Interact with objects and use them
            - Enter houses
            - Earn money
            - Teleport
            - Trade with NPCs
            - Access an inventory
            """)
            st.subheader("Technologies Used")
            st.write("- Java, JavaFX")
            st.markdown("[View GitHub Project](https://github.com/Simiamine/Zelda)")

        st.write("---")
        # Pokeshop Project
        col3, col4 = st.columns(2, gap="large")
        with col3:
            st.image(image_pokeshop, caption="Online Shop Project", width=200)
        with col4:
            st.subheader("Online Pokémon Store")
            st.write("Mock-up of an online store for selling Pokémon.")
            st.write("Features:")
            st.write("""
            - Home Page, Catalog, Cart
            - Customer and Vendor Accounts
            - Purchase History
            - Add/Modify Items and Stocks
            """)
            st.subheader("Technologies Used")
            st.write("- HTML, CSS, JavaScript, PHP, MySQL")
            st.markdown("[View GitHub Project](https://github.com/Simiamine/Pokeshop)")

        st.write("---")
        # Automate Editor Project
        col5, col6 = st.columns(2, gap="large")
        with col5:
            st.image(image_automate, caption="Automate Editor Project", width=200)
        with col6:
            st.subheader("Automate State Editor in C")
            st.write("Project to manage finite state automata (AEF) in C.")
            st.write("The program allows:")
            st.write("""
            - Manipulate automata: Create, Modify, Delete
            - Import/export automata from/to a file
            - Check if a word is recognized
            - Verify and complete automata
            - Multiply and concatenate automata
            """)
            st.subheader("Technologies Used")
            st.write("- C")
            st.markdown("[View GitHub Project](https://github.com/Simiamine/ProjetCAutomate)")

        st.write("---")
        # Bouche Cousue Project
        col7, col8 = st.columns(2, gap="large")
        with col7:
            st.image(image_wordle, caption="Bouche Cousue Game", width=200)
        with col8:
            st.subheader("Bouche Cousue - Wordle-like Game")
            st.write("Word guessing game developed in FreePascal, inspired by the French game Motus and the popular Wordle game.")
            st.write("Game Rules:")
            st.write("""
            - Guess the mystery word in 6 tries.
            - Only common nouns in the dictionary are allowed.
            - Letters surrounded by a red box are correctly placed.
            - Letters surrounded by a yellow box are present but misplaced.
            - Letters with a blue background are not in the word.
            """)
            st.subheader("Technologies Used")
            st.write("- FreePascal")
            st.markdown("[View GitHub Project](https://github.com/Simiamine/BoucheCousue)")

# Contact Section
if selected == 'Contact':
    with st.container():
        st.header("Get in touch!")
        st.write("##")
        st.write("Feel free to reach out for collaborations, questions, or just to say hi!")
        st.write('##')

        contact_form = """
        <style>
            form {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
        <form action="https://formsubmit.co/mzaliamine@gmail.com" method="POST">
            <input type = "hidden" name ="_captcha" value = "false">
            <input type="text" name="name" placeholder = "Your name" required>
            <input type="email" name="email" placeholder = "Your email" required>
            <textarea name = "message" placeholder = "Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_col, right_col = st.columns((2, 1), gap="large")
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            if lottie_contact:
                st_lottie(lottie_contact, height=300, key="contact_lottie")  # Afficher l'animation si elle est bien chargée
            else:
                st.write("Lottie animation failed to load.")

# Uber Analysis Section
if 'Analyse Uber' in category:
    with st.container():
        st.header("Analyse Uber")
        st.write("##")
        st.write("This section includes an analysis related to Uber's data, helping to understand customer patterns and opportunities for growth.")
        
        # Load Dataset
        df = pd.read_csv("uber-raw-data-apr14.csv")
        df['Date/Time'] = pd.to_datetime(df['Date/Time'])
        df['Hour'] = df['Date/Time'].dt.hour
        df['Day'] = df['Date/Time'].dt.day
        df['DayOfWeek'] = df['Date/Time'].dt.dayofweek
        df['Month'] = df['Date/Time'].dt.month
        df['Weekday'] = df['Date/Time'].dt.day_name()

        if selected == 'Temporal Analysis':
            # Temporal Analysis Section
            st.subheader("Temporal Analysis")
            # Number of Trips by Hour
            st.write("### Number of Trips by Hour")
            fig_hour = px.histogram(df, x='Hour', nbins=24, title='Number of Uber Trips by Hour', labels={'Hour': 'Hour of Day', 'count': 'Number of Trips'})
            st.plotly_chart(fig_hour)
            
            # Number of Trips by Day of Week
            st.write("### Number of Trips by Day of the Week")
            fig_dayofweek = px.histogram(df, x='DayOfWeek', nbins=7, title='Number of Uber Trips by Day of the Week', labels={'DayOfWeek': 'Day of Week', 'count': 'Number of Trips'})
            fig_dayofweek.update_xaxes(tickvals=[0, 1, 2, 3, 4, 5, 6], ticktext=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
            st.plotly_chart(fig_dayofweek)
            
            # Number of Trips by Day of Month
            st.write("### Number of Trips by Day of the Month")
            fig_day = px.histogram(df, x='Day', nbins=30, title='Number of Uber Trips by Day of the Month', labels={'Day': 'Day of Month', 'count': 'Number of Trips'})
            st.plotly_chart(fig_day)

            # Average Number of Trips per Hour
            st.write("### Average Number of Trips per Hour")
            avg_trips_hour = df.groupby('Hour').size().mean()
            st.write(f"The average number of trips per hour is: {avg_trips_hour:.2f}")
            
            # Average Trips by Weekday
            st.write("### Average Number of Trips by Weekday")
            avg_trips_weekday = df.groupby('Weekday').size().reset_index(name='Average Trips').sort_values(by='Average Trips', ascending=False)
            fig_avg_weekday = px.bar(avg_trips_weekday, x='Weekday', y='Average Trips', title='Average Number of Trips by Weekday', labels={'Weekday': 'Day of Week', 'Average Trips': 'Number of Trips'})
            st.plotly_chart(fig_avg_weekday)

        elif selected == 'Spatial Analysis':
            # Spatial Analysis Section
            st.subheader("Spatial Analysis")
            # Map of Pickups
            st.write("### Map of Uber Pickups")
            fig_map = px.scatter_mapbox(df, lat='Lat', lon='Lon', hover_name='Base', hover_data=['Date/Time'],
                                        title='Uber Pickups in New York City', zoom=10, height=500)
            fig_map.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig_map)
            
            # Scatter Plot of Lat vs Lon
            st.write("### Scatter Plot of Latitude vs Longitude")
            fig_scatter = px.scatter(df, x='Lon', y='Lat', title='Scatter Plot of Uber Pickups (Latitude vs Longitude)', labels={'Lon': 'Longitude', 'Lat': 'Latitude'})
            st.plotly_chart(fig_scatter)
            
            # Top 10 Busiest Pickup Locations
            st.write("### Top 10 Busiest Pickup Locations")
            top_locations = df['Lat'].round(3).astype(str) + ', ' + df['Lon'].round(3).astype(str)
            top_locations_count = top_locations.value_counts().head(10)
            st.write(top_locations_count)

            # Correlation between Latitude and Longitude
            st.write("### Correlation between Latitude and Longitude")
            correlation = df['Lat'].corr(df['Lon'])
            st.write(f"The correlation between Latitude and Longitude is: {correlation:.2f}")

        elif selected == 'Base Analysis':
            # Base Analysis Section
            st.subheader("Base Analysis")
            # Number of Trips by Base
            st.write("### Number of Trips by Base")
            fig_base = px.histogram(df, x='Base', title='Number of Uber Trips by Base', labels={'Base': 'Base Code', 'count': 'Number of Trips'})
            st.plotly_chart(fig_base)
            
            # Analysis of Bases during Peak Hour
            st.write("### Analysis of Bases during Peak Hour")
            peak_hour = df['Hour'].value_counts().idxmax()
            peak_hour_data = df[df['Hour'] == peak_hour]
            fig_peak_base = px.histogram(peak_hour_data, x='Base', title=f'Number of Trips by Base during Peak Hour ({peak_hour}:00)', labels={'Base': 'Base Code', 'count': 'Number of Trips'})
            st.plotly_chart(fig_peak_base)

        elif selected == 'Trip Duration Analysis':
            # Trip Duration Analysis Section
            st.subheader("Trip Duration Analysis")
            # Estimated Trip Duration Analysis
            st.write("### Estimated Trip Duration Analysis")
            # Adding random trip durations for analysis (in minutes)
            import numpy as np
            np.random.seed(42)
            df['Trip_Duration'] = np.random.randint(5, 30, df.shape[0])
            fig_duration = px.histogram(df, x='Trip_Duration', nbins=25, title='Estimated Trip Duration Distribution', labels={'Trip_Duration': 'Duration (minutes)', 'count': 'Number of Trips'})
            st.plotly_chart(fig_duration)
            
            # Trip Duration by Hour of Day
            st.write("### Trip Duration by Hour of Day")
            fig_duration_hour = px.box(df, x='Hour', y='Trip_Duration', title='Trip Duration by Hour of Day', labels={'Hour': 'Hour of Day', 'Trip_Duration': 'Duration (minutes)'})
            st.plotly_chart(fig_duration_hour)

        elif selected == 'Heatmap Analysis':
            # Heatmap Analysis Section
            st.subheader("Heatmap Analysis")
            # Heatmap of Pickups by Hour and Day of Week
            st.write("### Heatmap of Pickups by Hour and Day of Week")
            heatmap_data = df.groupby(['DayOfWeek', 'Hour']).size().reset_index(name='Counts')
            fig_heatmap = px.density_heatmap(heatmap_data, x='Hour', y='DayOfWeek', z='Counts', color_continuous_scale='Viridis',
                                             title='Heatmap of Uber Pickups by Hour and Day of Week', labels={'Hour': 'Hour of Day', 'DayOfWeek': 'Day of Week'})
            fig_heatmap.update_yaxes(tickvals=[0, 1, 2, 3, 4, 5, 6], ticktext=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
            st.plotly_chart(fig_heatmap)

            # Analysis of Trips by Day and Hour
            st.write("### Number of Trips by Day and Hour")
            fig_day_hour = px.bar(df, x='Day', y='Hour', color='Hour', title='Number of Trips by Day and Hour', labels={'Day': 'Day of Month', 'Hour': 'Hour of Day'})
            st.plotly_chart(fig_day_hour)

# Tips Analysis Section
with st.container():
    st.header("Analyse Tips")
    st.write("##")
    st.write("This section includes an analysis of the tips dataset, exploring tipping behaviors based on various factors.")
    
    # Load Tips Dataset
    df_tips = pd.read_csv("tips.csv")
    df_tips['tip_percentage'] = (df_tips['tip'] / df_tips['total_bill']) * 100

    if selected == 'Tipping Behavior Analysis':
        # Tipping Behavior Analysis Section
        st.subheader("Tipping Behavior Analysis")
        # Distribution of Total Bill
        st.write("### Distribution of Total Bill")
        fig_total_bill = px.histogram(df_tips, x='total_bill', title='Distribution of Total Bill', labels={'total_bill': 'Total Bill ($)', 'count': 'Count'})
        st.plotly_chart(fig_total_bill)
        
        # Distribution of Tips
        st.write("### Distribution of Tips")
        fig_tips = px.histogram(df_tips, x='tip', title='Distribution of Tips', labels={'tip': 'Tip ($)', 'count': 'Count'})
        st.plotly_chart(fig_tips)

        # Tip Percentage by Total Bill
        st.write("### Tip Percentage by Total Bill")
        fig_tip_percentage = px.scatter(df_tips, x='total_bill', y='tip_percentage', title='Tip Percentage by Total Bill', labels={'total_bill': 'Total Bill ($)', 'tip_percentage': 'Tip Percentage (%)'})
        st.plotly_chart(fig_tip_percentage)

        # Average Tip by Gender
        st.write("### Average Tip by Gender")
        avg_tip_gender = df_tips.groupby('sex')['tip'].mean().reset_index()
        fig_avg_tip_gender = px.bar(avg_tip_gender, x='sex', y='tip', title='Average Tip by Gender', labels={'sex': 'Gender', 'tip': 'Average Tip ($)'})
        st.plotly_chart(fig_avg_tip_gender)

        # Average Tip by Smoking Status
        st.write("### Average Tip by Smoking Status")
        avg_tip_smoker = df_tips.groupby('smoker')['tip'].mean().reset_index()
        fig_avg_tip_smoker = px.bar(avg_tip_smoker, x='smoker', y='tip', title='Average Tip by Smoking Status', labels={'smoker': 'Smoking Status', 'tip': 'Average Tip ($)'})
        st.plotly_chart(fig_avg_tip_smoker)

    elif selected == 'Gender and Smoking Analysis':
        # Gender and Smoking Analysis Section
        st.subheader("Gender and Smoking Analysis")
        # Average Tip by Gender and Smoking Status
        st.write("### Average Tip by Gender and Smoking Status")
        avg_tip_gender_smoker = df_tips.groupby(['sex', 'smoker'])['tip'].mean().reset_index()
        fig_avg_tip_gender_smoker = px.bar(avg_tip_gender_smoker, x='sex', y='tip', color='smoker', barmode='group', title='Average Tip by Gender and Smoking Status', labels={'sex': 'Gender', 'tip': 'Average Tip ($)', 'smoker': 'Smoking Status'})
        st.plotly_chart(fig_avg_tip_gender_smoker)

        # Tip Percentage by Gender and Smoking Status
        st.write("### Tip Percentage by Gender and Smoking Status")
        if 'tip_percentage' in df_tips.columns:
            fig_tip_percentage_gender_smoker = px.box(df_tips, x='sex', y='tip_percentage', color='smoker', title='Tip Percentage by Gender and Smoking Status', labels={'sex': 'Gender', 'tip_percentage': 'Tip Percentage (%)', 'smoker': 'Smoking Status'})
            st.plotly_chart(fig_tip_percentage_gender_smoker)
        else:
            st.write("The 'tip_percentage' column is missing from the dataset.")

    elif selected == 'Day and Time Analysis':
        # Day and Time Analysis Section
        st.subheader("Day and Time Analysis")
        # Average Tip by Day of the Week
        st.write("### Average Tip by Day of the Week")
        avg_tip_day = df_tips.groupby('day')['tip'].mean().reset_index()
        fig_avg_tip_day = px.bar(avg_tip_day, x='day', y='tip', title='Average Tip by Day of the Week', labels={'day': 'Day of the Week', 'tip': 'Average Tip ($)'})
        st.plotly_chart(fig_avg_tip_day)

        # Average Tip by Time (Lunch/Dinner)
        st.write("### Average Tip by Time (Lunch/Dinner)")
        avg_tip_time = df_tips.groupby('time')['tip'].mean().reset_index()
        fig_avg_tip_time = px.bar(avg_tip_time, x='time', y='tip', title='Average Tip by Time (Lunch/Dinner)', labels={'time': 'Time of Day', 'tip': 'Average Tip ($)'})
        st.plotly_chart(fig_avg_tip_time)

        # Tip Percentage by Day of the Week
        st.write("### Tip Percentage by Day of the Week")
        if 'tip_percentage' in df_tips.columns:
            fig_tip_percentage_day = px.box(df_tips, x='day', y='tip_percentage', title='Tip Percentage by Day of the Week', labels={'day': 'Day of the Week', 'tip_percentage': 'Tip Percentage (%)'})
            st.plotly_chart(fig_tip_percentage_day)
        else:
            st.write("The 'tip_percentage' column is missing from the dataset.")

# Joint Analysis Section
if 'Joint Analysis' in category:
    with st.container():
        st.header("Joint Analysis: Uber and Tips Data")
        st.write("##")
        st.write("This section includes a joint analysis of the Uber dataset and the Tips dataset to explore potential relationships between different behaviors.")
        
        # Load Uber Dataset
        df_uber = pd.read_csv("uber-raw-data-apr14.csv")
        df_uber['Date/Time'] = pd.to_datetime(df_uber['Date/Time'])
        df_uber['Hour'] = df_uber['Date/Time'].dt.hour
        df_uber['DayOfWeek'] = df_uber['Date/Time'].dt.dayofweek
        df_uber['Weekday'] = df_uber['Date/Time'].dt.day_name()

        # Load Tips Dataset
        df_tips = pd.read_csv("tips.csv")
        df_tips['tip_percentage'] = (df_tips['tip'] / df_tips['total_bill']) * 100

        if selected == 'Temporal vs Tips Analysis':
            # Temporal vs Tips Analysis Section
            st.subheader("Temporal vs Tips Analysis")
            st.write("### Average Tip Percentage vs Uber Trips by Hour")
            
            # Calculate Average Tips per Hour for the Tips dataset
            df_tips['Hour'] = np.random.choice(df_uber['Hour'].unique(), size=len(df_tips))
            avg_tip_hour = df_tips.groupby('Hour')['tip_percentage'].mean().reset_index()
            avg_trips_hour = df_uber.groupby('Hour').size().reset_index(name='Number of Trips')
            
            # Normalize the number of Uber trips for comparison
            avg_trips_hour['Normalized Trips'] = avg_trips_hour['Number of Trips'] / avg_trips_hour['Number of Trips'].max() * 100
            
            # Merge both datasets on Hour
            joint_hour_analysis = pd.merge(avg_tip_hour, avg_trips_hour, on='Hour')
            
            # Plot Average Tip Percentage vs Normalized Number of Uber Trips by Hour
            fig_joint_hour = px.line(joint_hour_analysis, x='Hour', y=['tip_percentage', 'Normalized Trips'],
                                     title='Average Tip Percentage vs Normalized Number of Uber Trips by Hour',
                                     labels={'value': 'Percentage / Normalized Trips', 'variable': 'Metric'})
            st.plotly_chart(fig_joint_hour)

        elif selected == 'Spatial vs Tips Analysis':
            # Spatial vs Tips Analysis Section
            st.subheader("Spatial vs Tips Analysis")
            st.write("### Comparison of Tips Based on Uber Pickup Locations")
            
            # Randomly assign Uber pickup locations to Tips data for analysis
            df_tips['Lat'] = np.random.choice(df_uber['Lat'].unique(), size=len(df_tips))
            df_tips['Lon'] = np.random.choice(df_uber['Lon'].unique(), size=len(df_tips))
            
            # Normalize tip percentage for better comparison
            df_tips['Normalized Tip Percentage'] = df_tips['tip_percentage'] / df_tips['tip_percentage'].max() * 100
            
            # Plot Normalized Tip Percentage by Uber Pickup Location
            fig_spatial_tips = px.scatter_mapbox(df_tips, lat='Lat', lon='Lon', color='Normalized Tip Percentage',
                                                 title='Normalized Tip Percentage by Uber Pickup Location',
                                                 labels={'Normalized Tip Percentage': 'Normalized Tip Percentage (%)'},
                                                 zoom=10, height=500)
            fig_spatial_tips.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig_spatial_tips)