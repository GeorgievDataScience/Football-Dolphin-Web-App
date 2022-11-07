import streamlit as st

import data_from_football_dolphin_api

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


all_teams = ["Arsenal", "Aston Villa", "Barnsley", "Birmingham", "Blackburn", "Blackpool", "Bolton", "Bournemouth", "Bradford", "Brighton",
             "Burnley", "Cardiff", "Charlton", "Chelsea", "Coventry", "Crystal Palace", "Derby", "Everton", "Fulham", "Huddersfield", "Hull",
             "Ipswich", "Leeds", "Leicester", "Liverpool", "Man City", "Man United", "Middlesbrough", "Newcastle", "Norwich", "Nott'm Forest",
             "Portsmouth", "QPR", "Reading", "Sheffield United", "Sheffield Weds", "Southampton", "Stoke", "Sunderland", "Swansea", "Tottenham",
             "Watford", "West Brom", "West Ham", "Wigan", "Wimbledon", "Wolves"]


all_seasons = ["2021/22", "2020/21", "2019/20", "2018/19", "2017/18", "2016/17", "2015/16", "2014/15", "2013/14",
               "2012/13", "2011/12", "2010/11", "2009/10", "2008/09", "2007/08", "2006/07", "2005/06",
               "2004/05", "2003/04", "2002/03", "2001/02", "2000/01", "1999/00", "1998/99", "1997/98",
               "1996/97", "1995/96"]

st.title('Home')

st.write('This web application analyzes English Premier League data from 1995/96 season to 2021/22 season. The web application provides three types of analytics:')

st.write('1. The first analysis is for the games played in one season. This is on the left sidebar page with name "Football season statistics". On this page user can select one season from all and the web app will show six statistical bar chart for slected season.')
st.write('2. The second analysis includes the head-to-head matches. This is on the left sidebar page with name "Head to head statistics". On this page user can select two teams from all and the web app will show six statistical bar chart for head to head matches.')
st.write('3. The third analysis is about the matches played by a team. This is on the left sidebar page with name "Team statistics". On this page user can select one team from all and the web app will show six statistical bar chart for slected team.')

st.write('If you read this, you are on the home page. From here user can see the three types of analyzed data in tables without charts.')

selected_type_of_analysis = st.radio(
     "Select type of analysis",
     ("Head to head statistics", "Team statistics", "Football season statistics"))


if selected_type_of_analysis == "Head to head statistics":
     st.header('Statistic for head to head matches in data tables')
     
     selected_hth_first_team = st.selectbox('Select first team', (all_teams), 26)
     selected_hth_second_team = st.selectbox('Select second team', (all_teams), 24)
     
     if selected_hth_first_team == selected_hth_second_team:
        st.error(
            'Please select two different teams. The first team and the second team are the same. The first team is. ' 
            + selected_hth_first_team + ' and the second team is ' 
            + selected_hth_second_team, icon="🚨")
     else:
         if "message" in data_from_football_dolphin_api.head_to_head_statistics(
                 "full time result", selected_hth_first_team, selected_hth_second_team):
             st.error(data_from_football_dolphin_api.head_to_head_statistics(
                 "full time result", selected_hth_first_team, selected_hth_second_team)["message"].to_string(index=False))
         else:
             st.header('1. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team + '- full time result')
             st.table(data_from_football_dolphin_api.head_to_head_statistics(
                 "full time result", selected_hth_first_team, selected_hth_second_team).T)
             
             st.header('2. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team + '- result first half and the match')
             st.table(data_from_football_dolphin_api.head_to_head_statistics(
                 "result first half and the match", selected_hth_first_team, selected_hth_second_team).T)
             
             st.header('3. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team + '- home vs away full time result')
             st.table(data_from_football_dolphin_api.head_to_head_statistics(
                 "home vs away full time result", selected_hth_first_team, selected_hth_second_team).T)
             
             st.header('4. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team + '- total number of matches with goals over / under')
             col1, col2 = st.columns(2)
             col1.table(data_from_football_dolphin_api.head_to_head_statistics(
                 "goals over", selected_hth_first_team, selected_hth_second_team).T)
             col2.table(data_from_football_dolphin_api.head_to_head_statistics(
                 "goals under", selected_hth_first_team, selected_hth_second_team).T)
             
             st.header('5. ' + selected_hth_first_team + ' vs ' + selected_hth_second_team + '- total number of matches with exact number of goals in the match')
             st.table(data_from_football_dolphin_api.head_to_head_statistics(
                 "exact number of goals in the match", selected_hth_first_team, selected_hth_second_team).T)
             
            
if selected_type_of_analysis == "Team statistics":
     st.header('Statistic for matches for selected team in data tables')

     selected_team = st.selectbox('Select team', all_teams)
     
     
     st.header('1. ' + selected_team + '- full time result')
     st.table(data_from_football_dolphin_api.team_statistics("full time result", selected_team).T)
     
     st.header('2. ' + selected_team + '- result first half and the mach')
     st.table(data_from_football_dolphin_api.team_statistics(
         "result first half and the match", selected_team).T)
     
     st.header('3. ' + selected_team + '- home vs away full time result')
     st.table(data_from_football_dolphin_api.team_statistics(
         "home vs away full time result", selected_team).T)
     
     st.header('4. ' + selected_team + '- total number of matches with goals over / under')
     col1, col2 = st.columns(2)
     col1.table(data_from_football_dolphin_api.team_statistics(
         "goals over", selected_team).T)
     col2.table(data_from_football_dolphin_api.team_statistics(
         "goals under", selected_team).T)
     
     st.header('5. ' + selected_team + '- total number of matches with exact number of goals in the match')
     st.table(data_from_football_dolphin_api.team_statistics(
         "exact number of goals in the match", selected_team).T)
     
    


if selected_type_of_analysis == "Football season statistics":
     st.header('Statistic for matches for selected season in data tables')
     
     selected_season = st.selectbox('Select season', all_seasons)
     
     st.header('1. All scores in season ' + selected_season + ' English Premier League')
     st.table(data_from_football_dolphin_api.football_season_statistics(
         "all scores", 
         selected_season)
         .T)
     
     st.header('2. Home vs away- full time result in season ' + selected_season + ' English Premier League')
     st.table(data_from_football_dolphin_api.football_season_statistics(
         "home vs away full time result", 
         selected_season)
         .T)
     
     st.header('3. Home vs away- result first half and the match in season ' + selected_season + ' English Premier League')
     st.table(data_from_football_dolphin_api.football_season_statistics(
         "home vs away result first half and the match", 
         selected_season)
         .T)
     
     st.header('4. Total number of matches with goals over / under in season ' + selected_season + ' English Premier League')
     col1, col2 = st.columns(2)
     
     col1.table(
         data_from_football_dolphin_api.football_season_statistics(
         "goals over", 
         selected_season)
         .T)
     col2.table(
         data_from_football_dolphin_api.football_season_statistics(
         "goals under", 
         selected_season)
         .T)
     
     st.header('5. Total number of matches with exact number of goals in the match in season ' + selected_season + ' English Premier League')
     st.table(
         data_from_football_dolphin_api.football_season_statistics(
         "exact number of goals in the match", 
         selected_season)
         .T)
     



