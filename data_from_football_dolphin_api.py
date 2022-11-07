import http.client
import pandas as pd

def head_to_head_statistics(type_of_statistics, first_team, second_team):
    
    type_of_statistics = type_of_statistics.replace(" ", "%20")
    first_team = first_team.replace(" ", "%20")
    second_team = second_team.replace(" ", "%20")
    
    conn = http.client.HTTPSConnection("football-dolphin.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "******************************************",
        'X-RapidAPI-Host': "******************************************"
        }

    conn.request("GET", "/headtoheadstatistics/?type_of_statistics=" + type_of_statistics + "&first_team=" + first_team + "&second_team=" + second_team , headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = pd.read_json(data)    
    
    return data



def team_statistics(type_of_statistics, team):
    
    type_of_statistics = type_of_statistics.replace(" ", "%20")
    team = team.replace(" ", "%20")
    
    conn = http.client.HTTPSConnection("football-dolphin.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "******************************************",
        'X-RapidAPI-Host': "******************************************"
        }

    conn.request("GET", "/teamstatistics/" + type_of_statistics + "/" + team, headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = pd.read_json(data) 
    
    return data





def football_season_statistics(type_of_statistics, season):
    
    type_of_statistics = type_of_statistics.replace(" ", "%20")
    
    conn = http.client.HTTPSConnection("football-dolphin.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "******************************************",
        'X-RapidAPI-Host': "******************************************"
        }

    conn.request("GET", "/footballseasonstatistics/" + type_of_statistics + "/" + season, headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = pd.read_json(data)
    
    return data
    

    



