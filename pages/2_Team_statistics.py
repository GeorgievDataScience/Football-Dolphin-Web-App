import streamlit as st

import data_from_football_dolphin_api as fd
import charts

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title('Team statistics in English Premier League')
st.write('This web page presents six statistical bar charts for selected team in the English Premier League. If the user wants to change the team, he can do it from the selection box below.')


selected_team = st.selectbox(
     'Select on team',
     ("Arsenal", "Aston Villa", "Barnsley", "Birmingham", "Blackburn", "Blackpool", "Bolton", "Bournemouth", "Bradford", "Brighton",
     "Burnley", "Cardiff", "Charlton", "Chelsea", "Coventry", "Crystal Palace", "Derby", "Everton", "Fulham", "Huddersfield", "Hull",
     "Ipswich", "Leeds", "Leicester", "Liverpool", "Man City", "Man United", "Middlesbrough", "Newcastle", "Norwich", "Nott'm Forest",
     "Portsmouth", "QPR", "Reading", "Sheffield United", "Sheffield Weds", "Southampton", "Stoke", "Sunderland", "Swansea", "Tottenham",
     "Watford", "West Brom", "West Ham", "Wigan", "Wimbledon", "Wolves"))

# Chart 1
st.header('1. ' + selected_team + ' in the English Premier League- full time result')

st.pyplot(charts.horizontal_bar_chart(fd.team_statistics("full time result", selected_team)))


# Chart 2

st.header('2. ' + selected_team + ' in English Premier League- result first half and the match')

st.pyplot(charts.horizontal_bar_chart(fd.team_statistics("result first half and the match", selected_team)))


# Chart 3
st.header('3. ' + selected_team +' in English Premier League- home vs away full time result')

st.pyplot(charts.horizontal_bar_chart(fd.team_statistics("home vs away full time result", selected_team)))


# Chart 4
st.header('4. ' + selected_team +'  in English Premier League- total number of matches with goals over')

st.pyplot(charts.horizontal_bar_chart(fd.team_statistics("goals over", selected_team)))


# Chart 5
st.header('5. ' + selected_team +' in English Premier League- total number of matches woth goals under')

st.pyplot(charts.horizontal_bar_chart(fd.team_statistics("goals under", selected_team)))


# Chart 6
st.header('6. ' + selected_team +' in English Premier League-total number of matches with exact number of goals in the match')

st.pyplot(charts.horizontal_bar_chart(fd.team_statistics("exact number of goals in the match", selected_team)))


