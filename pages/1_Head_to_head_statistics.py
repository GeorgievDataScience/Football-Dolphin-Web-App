import streamlit as st

import data_from_football_dolphin_api as fd
import charts



st.title('Head to head statistics in English Premier League')
st.write('This web page presents six statistical bar charts for H2H matches in the English Premier League. If the user wants to change the teams, he can do it from the selection boxes below.')


all_teams = ["Arsenal", "Aston Villa", "Barnsley", "Birmingham", "Blackburn", "Blackpool", "Bolton", "Bournemouth", "Bradford", "Brighton",
             "Burnley", "Cardiff", "Charlton", "Chelsea", "Coventry", "Crystal Palace", "Derby", "Everton", "Fulham", "Huddersfield", "Hull",
             "Ipswich", "Leeds", "Leicester", "Liverpool", "Man City", "Man United", "Middlesbrough", "Newcastle", "Norwich", "Nott'm Forest",
             "Portsmouth", "QPR", "Reading", "Sheffield United", "Sheffield Weds", "Southampton", "Stoke", "Sunderland", "Swansea", "Tottenham",
             "Watford", "West Brom", "West Ham", "Wigan", "Wimbledon", "Wolves"]

selected_hth_first_team = st.selectbox(
     'Select first team',
     (all_teams), 26)

selected_hth_second_team = st.selectbox(
     'Select second team',
     (all_teams), 24)


if selected_hth_first_team == selected_hth_second_team:
   st.error('Please select two different teams. The first team and the second team are the same. The first team is. ' + selected_hth_first_team + ' and the second team is ' + selected_hth_second_team, icon="🚨")
else:
    if "message" in fd.head_to_head_statistics(
            "full time result", selected_hth_first_team, selected_hth_second_team):
        st.error(fd.head_to_head_statistics(
            "full time result", selected_hth_first_team, selected_hth_second_team)["message"].to_string(index=False))
    else:
        # Chart 1
        st.header('1. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team +' in English Premier League- full time result')

        st.pyplot(charts.horizontal_bar_chart(fd.head_to_head_statistics("full time result", selected_hth_first_team, selected_hth_second_team)))
 
        # Chart 2
        st.header('2. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team +' in English Premier League- result first half and the match')

        st.pyplot(charts.horizontal_bar_chart(fd.head_to_head_statistics("result first half and the match", selected_hth_first_team, selected_hth_second_team)))
 
  
        # Chart 3
        st.header('3. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team +' in English Premier League- home vs away full time result')

        st.pyplot(charts.horizontal_bar_chart(fd.head_to_head_statistics("home vs away full time result", selected_hth_first_team, selected_hth_second_team)))
 
        # Chart 4
        st.header('4. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team +' in English Premier League- total number of matches woth goals under')

        st.pyplot(charts.horizontal_bar_chart(fd.head_to_head_statistics("goals under", selected_hth_first_team, selected_hth_second_team)))
 
        # Chart 5
        st.header('5. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team +' in English Premier League- total number of matches woth goals over')

        st.pyplot(charts.horizontal_bar_chart(fd.head_to_head_statistics("goals over", selected_hth_first_team, selected_hth_second_team)))
 
 
        # Chart 6
        st.header('6. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team +' in English Premier League- total number of matches with exact number of goals in the match')

        st.pyplot(charts.horizontal_bar_chart(fd.head_to_head_statistics("exact number of goals in the match", selected_hth_first_team, selected_hth_second_team)))
 
 