import streamlit as st

import data_from_football_dolphin_api as fd
import charts


st.title('Football season statistics in English Premier League')
st.write('This web page presents six statistical bar charts for selected season in the English Premier League. If the user wants to change the season, he can do it from the selection boxes below.')

all_seasons = ["2021/22", "2020/21", "2019/20", "2018/19", "2017/18", "2016/17", "2015/16", "2014/15", "2013/14",
               "2012/13", "2011/12", "2010/11", "2009/10", "2008/09", "2007/08", "2006/07", "2005/06",
               "2004/05", "2003/04", "2002/03", "2001/02", "2000/01", "1999/00", "1998/99", "1997/98",
               "1996/97", "1995/96"]

# Chart 1
st.header('1. Home team vs away team in English Premier League- full time result')

selected_season = st.selectbox('Select season', all_seasons, key= "Chart 1")

st.pyplot(charts.vertical_bar_chart(fd.football_season_statistics(
    "home vs away full time result", 
    selected_season)))


# Chart 2
st.header('2. All Scores in English Premier League- total number of matches ')

selected_season = st.selectbox('Select season', all_seasons,key= "Chart 2")

st.pyplot(charts.horizontal_bar_chart(fd.football_season_statistics(
    "all scores", 
    selected_season)))

# Chart 3
st.header('3. Home team vs away team in English Premier League- result first half time and the match')

selected_season = st.selectbox('Select season', all_seasons, key= "Chart 3")

st.pyplot(charts.horizontal_bar_chart(fd.football_season_statistics(
    "home vs away result first half and the match", 
    selected_season)))

# Chart 4
st.header('4. Total number of matches with Goals Over 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5 and 9.5 in English Premier League')

selected_season = st.selectbox('Select season', all_seasons, key= "Chart 4")

st.pyplot(charts.horizontal_bar_chart(fd.football_season_statistics(
    "goals over", 
    selected_season)))

# Chart 5
st.header('5. Total number of matches with Goals Under 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5 and 9.5 in English Premier League')

selected_season = st.selectbox('Select season', all_seasons, key= "Chart 5")

st.pyplot(charts.horizontal_bar_chart(fd.football_season_statistics(
    "goals under", 
    selected_season)))

# Chart 6 
st.header('6. Total number of matches with exact number of goals in the match- English Premier League')

selected_season = st.selectbox('Select season', all_seasons, key= "Chart 6")

st.pyplot(charts.horizontal_bar_chart(fd.football_season_statistics(
    "exact number of goals in the match", 
    selected_season)))

