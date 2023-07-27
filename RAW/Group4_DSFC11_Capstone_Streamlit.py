import streamlit as st
import pandas as pd
import pickle

data = pd.read_csv('df_final_withproba_noskip.csv')
with open("model_rh.pkl", "rb") as f:
    model = pickle.load(f)
# Set the page title and icon
st.set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")


# Define a dictionary with page names and content
PAGES = {
    "Introduction": {
        "picture": "streamlit/first.jpg",
        "games_intro": "streamlit/games_intro.png",
        "movies": "streamlit/movies.png",
        "activities": "streamlit/activities.png",
        "description": "The Philippine Gaming Industry earned 78 Trillion PHP in 2020 and is expected to grow to 121 Trillion PHP by 2027. The PH Gaming Industry is highly valued but local game developers struggle to succeed as stakeholders within the ecosystem.",
        "success": "Among games released by Filipino Developers from 2015 to 2018, only one is successful.",
        "problem":"The PH Gaming Industry is highly valued but local game developers struggle to succeed as stakeholders within the ecosystem.",

    },
"Player Retention": {
        
    "eda_1_title": "Player Behavior Flowchart",
    "retention": "streamlit/retention.png",
    "retention_text": "This flowchart shows the stages players go through when playing the game. This is important\
    to understand to give developers an idea on player behavior.\n\n\
    - To Play - players have bought the game but are yet to play it\n\
    - Owned - after gaining interest, players would buy the game upon release\n\
    - Playing - currently playing the game\n\
    - Dropped - stopped playing the game without finishing it\n\
    - Finished - completed all stages of the game",


    "eda_2_title": "How to Achieve High Retention",
    "retention_1": "streamlit/retention_1.png",
    "retention_1_text": "A key to keeping players engaged with the game is by looking into player retention.\
        In particular, retention rate could be the key to the success of a game since having high retention implies high level player engagement, more chances of higher revenues, long-term success by having a loyal fan base, etc."
    },
    "Methodology": {
        "objectives": "<h1 style='font-weight:bold; font-size: 36px;'>Methodology and Dataset</b></li></ul>",
        "objectives_pic" : "streamlit/methodology.png",
        "dataset" : "streamlit/dataset.png",
        "corr_plot" : "streamlit/corr_plot.png",
        "dataset_desc" : "Gathering and Processing of Data",
        "overview_desc" : "Overview of Methodology",
        "corr_desc":"Correlation Plot",
    },

    "Machine Learning Model": {
        "pipeline_title" : "Choosing the Model",
        "model_exp_desc" : "Model Explainability",
        "conf_matrix" : "streamlit/confusion_matrix.png",
        "model_exp" : "streamlit/model_exp.png",
        "model_exp_1" : "streamlit/model_exp_1.png",
    },

    "Conclusions": {

        "conc_1": "streamlit/conc_1.png",
        "conc_2": "streamlit/conc_2.png",
        "conc_3": "streamlit/conc_3.png",
        "conc_4": "streamlit/conc_4.png",
    },

    "Model Deployment": {
        "predict": "Predict the School Type"
    },

}

# Add a title for the sidebar
st.sidebar.title("JAHtGPt")

# Create a radio button in the sidebar to select the page
page = st.sidebar.radio("Go to", list(PAGES.keys()))

if page == "Introduction":
    st.write(f"# {page}")
    st.image(PAGES[page]["picture"], width=1000)
    st.write(PAGES[page]["description"])
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["success"])), unsafe_allow_html=True)
    st.image(PAGES[page]["games_intro"], width=1000)
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["problem"])), unsafe_allow_html=True)
elif page == "Player Retention":
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["eda_1_title"])), unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image(PAGES[page]["retention"], width=400)
    with col2:
        st.write(PAGES[page]["retention_text"])

    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["eda_2_title"])), unsafe_allow_html=True)

    col3, col4 = st.columns([2, 3])
    with col3:
        st.image(PAGES[page]["retention_1"], width=400)
    with col4:
        st.write(PAGES[page]["retention_1_text"])


elif page == "Methodology":
    st.write(PAGES[page]["objectives"], unsafe_allow_html=True)
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["overview_desc"])), unsafe_allow_html=True)
    st.image(PAGES[page]["objectives_pic"], width=1000)
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["dataset_desc"])), unsafe_allow_html=True)
    st.image(PAGES[page]["dataset"], width=1000)
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["corr_desc"])), unsafe_allow_html=True)
    st.image(PAGES[page]["corr_plot"], width=1000)
    st.write("Beaten or finished has a high correlation with reviews_count or the number of reviews. As this metric is used to compute for the target feature retention, it was still included in the data.\n\
    Meh has a high correlation with dropped. Since other features related to customer rating (such as exceptional and recommended) are not available in the data, it was decided to exclude meh and retain dropped.\n\
    After data cleaning and preprocessing, the feature ratings_count was removed. Further investigation showed that its perfect correlation with review_count is because they are referring to the same metric which is the number of reviews.", unsafe_allow_html=True)

    
elif page == "Machine Learning Model":
    
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["pipeline_title"])), unsafe_allow_html=True)
    st.write("After training the data on 8 different models and various under- and oversampling methods, Gradient Boosting Classification emerged as the best model.")
    st.image(PAGES[page]["conf_matrix"], width=1000)

    st.write("To understand the behavior of the model, feature importance plots based on SHAPley values were generated.")
    
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["model_exp_desc"])), unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image(PAGES[page]["model_exp"], width=400)
    with col2:
        st.write("The top features contributing to the prediction of the model are toplay, number of reviews, dropped, and playtime.")
    
    col3, col4 = st.columns([2, 3])
    with col3:
        st.image(PAGES[page]["model_exp_1"], width=400)
    with col4:
        st.write("""This beeswarm plot shows how high or low values of the features affect the model prediction. It can be observed that the higher values (shown as pink streaks in the plot), of the features toplay, review_count, and playtime all contribute to the positive prediction of the model.Meanwhile, the third most important feature dropped has a negative impact since its higher values result in a negative prediction.""")



elif page == "Conclusions":
    st.markdown("<h2 style='font-weight: lighter; font-size: 30px;'>After analyzing the model and its feature importance plots, the following conclusions and recommendations were drawn for each identified key feature.</h2>", unsafe_allow_html=True)
    st.image(PAGES[page]["conc_1"], width=1000)
    st.image(PAGES[page]["conc_2"], width=1000)
    st.image(PAGES[page]["conc_3"], width=1000)
    st.image(PAGES[page]["conc_4"], width=1000)

elif page == "Model Deployment":
    st.title("Game Retention Rate Prediction Model")

    with st.form("New Input"):
        input_data = {}

        
        input_data["reviews_count"] = st.number_input("Number of Reviews", min_value=0, value=0)
        input_data["playtime"] = st.number_input("Playtime", min_value=0, value=0)
        input_data["yet"] = st.number_input("Number of Planning to Play", min_value=0,value=0)
        input_data["toplay"] = st.number_input("Number of Wishlist", min_value=0, value=0)
        
        input_data["dropped"] = st.number_input("Number of Dropped", min_value=0, value=0)
        input_data["OriginalCost"] = st.number_input("Original Cost", min_value=0.0,value=0.0)
    
        genres = ['Indie', 'action_tag', 'adventure_tag', 'casual_tag', 'sports_tag', 'strategy_tag']
        genre_selection = st.multiselect("Game Genre", genres)
        for genre in genres:
            input_data[genre] = genre in genre_selection

        # Console
        consoles = ['PS Vita', 'Xbox Series S/X', 'Android', 'macOS', 'PlayStation', 'Nintendo DSi', 'iOS', 'GameCube', 'Nintendo DS', 'Dreamcast', 'PSP', 'Linux', 'PC',
                    'Game Boy Advance', 'PlayStation 3', 'Nintendo 3DS', 'Nintendo Switch', 'Wii U', 'Xbox 360', 'PlayStation 4', 'Wii', 'Xbox', 'PlayStation 5', 'Xbox One', 'PlayStation 2']
        console_selection = st.multiselect("Console", consoles)
        for console in consoles:
            input_data[console] = console in console_selection

        # Marketplaces
        marketplaces = ['GOG', 'Xbox Store', 'PlayStation Store', 'Epic Games', 'Xbox 360 Store', 'itch.io', 'Nintendo Store', 'Google Play', 'Steam', 'App Store']
        marketplace_selection = st.multiselect("Marketplace", marketplaces)
        for marketplace in marketplaces:
            input_data[marketplace] = marketplace in marketplace_selection

        # Developers
        developers = ['franchise_tag', 'top_developer', 'top_publisher']
        developer_selection = st.multiselect("Developer", developers)
        for developer in developers:
            input_data[developer] = developer in developer_selection

        # Player Types
        player_types = ['coop', 'multiplayer', 'online coop', 'pvp', 'singleplayer']
        player_type_selection = st.multiselect("Player Type", player_types)
        for player_type in player_types:
            input_data[player_type] = player_type in player_type_selection

        submit = st.form_submit_button("SUBMIT")

        if submit:
            df = pd.DataFrame([input_data])  # Wrapping the dictionary in a list to treat it as a single record   
            # Generate predictions
            try:
                result = model.predict(df)
                if result[0] == 1:
                    st.write('Result: High Retention')  # For High Retention
                else:
                    st.write('Result: Low Retention')  # For Low Retention
            except Exception as e:
                st.write(f'Prediction failed with error: {e}')

