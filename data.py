import pandas as pd



def sort_tuple(tup: tuple) -> tuple:
    """
    Sorts the given tuple so that the elements are in alphabetical order.
    """
    tup = sorted(tup, key=str.lower)
    return tup



def read_csv():
    df = pd.read_csv('latest.csv')
    return df



def to_map_name(zoneId: int) -> str:
    if zoneId == 559: return "Nagrand Arena"
    elif zoneId == 562: return "Blade's Edge Arena"
    elif zoneId == 572: return "Ruins of Lordaeron"
    elif zoneId == 617: return "Dalaran Sewers"



def is_2v2(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['is2v2'] = (df['teamPlayerName1'].notnull()  & df['teamPlayerName2'].notnull()  & df['teamPlayerName3'].isnull()  & df['teamPlayerName4'].isnull()  & df['teamPlayerName5'].isnull()
                &  df['enemyPlayerName1'].notnull() & df['enemyPlayerName2'].notnull() & df['enemyPlayerName3'].isnull() & df['enemyPlayerName4'].isnull() & df['enemyPlayerName5'].isnull())
    return df



def is_3v3(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['is3v3'] = (df['teamPlayerName1'].notnull()  & df['teamPlayerName2'].notnull()  & df['teamPlayerName3'].notnull()  & df['teamPlayerName4'].isnull()  & df['teamPlayerName5'].isnull()
                &  df['enemyPlayerName1'].notnull() & df['enemyPlayerName2'].notnull() & df['enemyPlayerName3'].notnull() & df['enemyPlayerName4'].isnull() & df['enemyPlayerName5'].isnull())
    return df



def is_5v5(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['is5v5'] = (df['teamPlayerName1'].notnull()  & df['teamPlayerName2'].notnull()  & df['teamPlayerName3'].notnull()  & df['teamPlayerName4'].notnull()  & df['teamPlayerName5'].notnull()
                &  df['enemyPlayerName1'].notnull() & df['enemyPlayerName2'].notnull() & df['enemyPlayerName3'].notnull() & df['enemyPlayerName4'].notnull() & df['enemyPlayerName5'].notnull())
    return df



def is_win(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['isWin'] = (df['teamColor'] == df['winnerColor'])
    return df



def is_loss(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['isLoss'] = (df['teamColor'] != df['winnerColor'])
    return df



def cleanup_data(df: pd.DataFrame) -> pd.DataFrame:
    data = df.shift(periods=1, axis=1)
    data['startTime'] = pd.to_datetime(data['startTime'], unit='s')
    data['endTime'] = pd.to_datetime(data['endTime'], unit='s')
    data['startTime'] = data['startTime'].dt.tz_localize('UTC').dt.tz_convert('US/Central').dt.strftime('%Y-%m-%d %H:%M')
    data['endTime'] = data['endTime'].dt.tz_localize('UTC').dt.tz_convert('US/Central').dt.strftime('%Y-%m-%d %H:%M')
    data = is_2v2(data)
    data = is_3v3(data)
    data = is_5v5(data)
    data = is_win(data)
    data = is_loss(data)
    data['mapName'] = data['zoneId'].apply(to_map_name)
    return data



def get_2v2_data() -> pd.DataFrame:
    data = read_csv()
    data = cleanup_data(data)
    data = data[data['is2v2'] == True]
    data_2v2 = pd.DataFrame(columns=['win', 'date', 'map', 'duration', 'teamComp', 'enemyComp',
                                'oldTeamRating',      'newTeamRating',      'diffRating',      'mmr',
                                'enemyOldTeamRating', 'enemyNewTeamRating', 'enemyDiffRating', 'enemyMmr'
                                ])
    teamPlayerClass1s,  teamPlayerClass2s  = [], []
    enemyPlayerClass1s, enemyPlayerClass2s = [], []
    for index,row in data.iterrows():
        teamPlayerClass1s.append(row['teamPlayerClass1'].title())
        teamPlayerClass2s.append(row['teamPlayerClass2'].title())
        enemyPlayerClass1s.append(row['enemyPlayerClass1'].title())
        enemyPlayerClass2s.append(row['enemyPlayerClass2'].title())
    teamComps = []
    enemyComps = []
    for i in range(len(teamPlayerClass1s)):
        teamClasses = sort_tuple((teamPlayerClass1s[i], teamPlayerClass2s[i]))
        enemyClasses = sort_tuple((enemyPlayerClass1s[i], enemyPlayerClass2s[i]))
        teamComps.append(teamClasses[0] + ' - ' + teamClasses[1])
        enemyComps.append(enemyClasses[0] + ' - ' + enemyClasses[1])
    data_2v2['win'] = data['isWin']
    data_2v2['date'] = data['startTime']
    data_2v2['map'] = data['mapName']
    data_2v2['duration'] = data['duration']
    data_2v2['teamComp'] = teamComps
    data_2v2['enemyComp'] = enemyComps
    data_2v2['oldTeamRating'] = data['oldTeamRating']
    data_2v2['newTeamRating'] = data['newTeamRating']
    data_2v2['diffRating'] = data['diffRating']
    data_2v2['mmr'] = data['mmr']
    data_2v2['enemyOldTeamRating'] = data['enemyOldTeamRating']
    data_2v2['enemyNewTeamRating'] = data['enemyNewTeamRating']
    data_2v2['enemyDiffRating'] = data['enemyDiffRating']
    data_2v2['enemyMmr'] = data['enemyMmr']
    return data_2v2



def get_3v3_data() -> pd.DataFrame:
    data = read_csv()
    data = cleanup_data(data)
    data = data[data['is3v3'] == True]
    data_3v3 = pd.DataFrame(columns=['win', 'date', 'map', 'duration', 'teamComp', 'enemyComp',
                                'oldTeamRating',      'newTeamRating',      'diffRating',      'mmr',
                                'enemyOldTeamRating', 'enemyNewTeamRating', 'enemyDiffRating', 'enemyMmr'
                                ])
    teamPlayerClass1s,  teamPlayerClass2s,  teamPlayerClass3s  = [], [], []
    enemyPlayerClass1s, enemyPlayerClass2s, enemyPlayerClass3s = [], [], []
    for index,row in data.iterrows():
        teamPlayerClass1s.append(row['teamPlayerClass1'].title())
        teamPlayerClass2s.append(row['teamPlayerClass2'].title())
        teamPlayerClass3s.append(row['teamPlayerClass3'].title())
        enemyPlayerClass1s.append(row['enemyPlayerClass1'].title())
        enemyPlayerClass2s.append(row['enemyPlayerClass2'].title())
        enemyPlayerClass3s.append(row['enemyPlayerClass3'].title())
    teamComps  = []
    enemyComps = []
    for i in range(len(teamPlayerClass1s)):
        teamClasses = sort_tuple((teamPlayerClass1s[i], teamPlayerClass2s[i], teamPlayerClass3s[i]))
        enemyClasses = sort_tuple((enemyPlayerClass1s[i], enemyPlayerClass2s[i], enemyPlayerClass3s[i]))
        teamComps.append(teamClasses[0] + ' - ' + teamClasses[1] + ' - ' + teamClasses[2])
        enemyComps.append(enemyClasses[0] + ' - ' + enemyClasses[1] + ' - ' + enemyClasses[2])
    data_3v3['win']  = data['isWin']
    data_3v3['date'] = data['startTime']
    data_3v3['map']  = data['mapName']
    data_3v3['duration']  = data['duration']
    data_3v3['teamComp']  = teamComps
    data_3v3['enemyComp'] = enemyComps
    data_3v3['oldTeamRating'] = data['oldTeamRating']
    data_3v3['newTeamRating'] = data['newTeamRating']
    data_3v3['diffRating'] = data['diffRating']
    data_3v3['mmr'] = data['mmr']
    data_3v3['enemyOldTeamRating'] = data['enemyOldTeamRating']
    data_3v3['enemyNewTeamRating'] = data['enemyNewTeamRating']
    data_3v3['enemyDiffRating'] = data['enemyDiffRating']
    data_3v3['enemyMmr'] = data['enemyMmr']
    return data_3v3



def get_5v5_data() -> pd.DataFrame:
    data = read_csv()
    data = cleanup_data(data)
    data = data[data['is5v5'] == True]
    data_5v5 = pd.DataFrame(columns=['win', 'date', 'map', 'duration', 'teamComp', 'enemyComp',
                                'oldTeamRating',      'newTeamRating',      'diffRating',      'mmr',
                                'enemyOldTeamRating', 'enemyNewTeamRating', 'enemyDiffRating', 'enemyMmr'
                                ])
    teamPlayerClass1s,  teamPlayerClass2s,  teamPlayerClass3s,  teamPlayerClass4s,  teamPlayerClass5s  = [], [], [], [], []
    enemyPlayerClass1s, enemyPlayerClass2s, enemyPlayerClass3s, enemyPlayerClass4s, enemyPlayerClass5s = [], [], [], [], []
    for index,row in data.iterrows():
        teamPlayerClass1s.append(row['teamPlayerClass1'])
        teamPlayerClass2s.append(row['teamPlayerClass2'])
        teamPlayerClass3s.append(row['teamPlayerClass3'])
        teamPlayerClass4s.append(row['teamPlayerClass4'])
        teamPlayerClass5s.append(row['teamPlayerClass5'])
        enemyPlayerClass1s.append(row['enemyPlayerClass1'])
        enemyPlayerClass2s.append(row['enemyPlayerClass2'])
        enemyPlayerClass3s.append(row['enemyPlayerClass3'])
        enemyPlayerClass4s.append(row['enemyPlayerClass4'])
        enemyPlayerClass5s.append(row['enemyPlayerClass5'])
    teamComps  = []
    enemyComps = []
    for i in range(len(teamPlayerClass1s)):
        teamClasses = sort_tuple((teamPlayerClass1s[i], teamPlayerClass2s[i], teamPlayerClass3s[i], teamPlayerClass4s[i], teamPlayerClass5s[i]))
        enemyClasses = sort_tuple((enemyPlayerClass1s[i], enemyPlayerClass2s[i], enemyPlayerClass3s[i], enemyPlayerClass4s[i], enemyPlayerClass5s[i]))
        teamComps.append(teamClasses[0] + ' ' + teamClasses[1] + ' ' + teamClasses[2] + ' ' + teamClasses[3] + ' ' + teamClasses[4])
        enemyComps.append(enemyClasses[0] + ' ' + enemyClasses[1] + ' ' + enemyClasses[2] + ' ' + enemyClasses[3] + ' ' + enemyClasses[4])
    data_5v5['win']  = data['isWin']
    data_5v5['date'] = data['startTime']
    data_5v5['map']  = data['mapName']
    data_5v5['duration']  = data['duration']
    data_5v5['teamComp']  = teamComps
    data_5v5['enemyComp'] = enemyComps
    data_5v5['oldTeamRating'] = data['oldTeamRating']
    data_5v5['newTeamRating'] = data['newTeamRating']
    data_5v5['diffRating'] = data['diffRating']
    data_5v5['mmr'] = data['mmr']
    data_5v5['enemyOldTeamRating'] = data['enemyOldTeamRating']
    data_5v5['enemyNewTeamRating'] = data['enemyNewTeamRating']
    data_5v5['enemyDiffRating'] = data['enemyDiffRating']
    data_5v5['enemyMmr'] = data['enemyMmr']
    return data_5v5
    

    
def get_2v2_winrates(data_2v2: pd.DataFrame) -> pd.DataFrame:
    data_2v2['wins'] = data_2v2['win'].astype(int)
    data_2v2['games'] = 1
    data_2v2 = data_2v2.groupby(['enemyComp']).agg({'wins': 'sum', 'games': 'sum'})
    data_2v2['winrate'] = data_2v2['wins'] / data_2v2['games']
    data_2v2 = data_2v2.sort_values(by=['winrate'], ascending=False)
    data_2v2['winrate'] = data_2v2['winrate'].apply(lambda x: "{:.1%}".format(x))
    data_2v2 = data_2v2.reset_index()
    return data_2v2



def get_3v3_winrates(data_3v3: pd.DataFrame) -> pd.DataFrame:
    data_3v3['wins'] = data_3v3['win'].astype(int)
    data_3v3['games'] = 1
    data_3v3 = data_3v3.groupby(['enemyComp']).agg({'wins': 'sum', 'games': 'sum'})
    data_3v3['winrate'] = data_3v3['wins'] / data_3v3['games']
    data_3v3 = data_3v3.sort_values(by=['winrate'], ascending=False)
    data_3v3['winrate'] = data_3v3['winrate'].apply(lambda x: "{:.1%}".format(x))
    data_3v3 = data_3v3.reset_index()
    return data_3v3



def get_5v5_winrates(data_5v5: pd.DataFrame) -> pd.DataFrame:
    data_5v5['wins'] = data_5v5['win'].astype(int)
    data_5v5['games'] = 1
    data_5v5 = data_5v5.groupby(['enemyComp']).agg({'wins': 'sum', 'games': 'sum'})
    data_5v5['winrate'] = data_5v5['wins'] / data_5v5['games']
    data_5v5 = data_5v5.sort_values(by=['winrate'], ascending=False)
    data_5v5['winrate'] = data_5v5['winrate'].apply(lambda x: "{:.1%}".format(x))
    data_5v5 = data_5v5.reset_index()
    return data_5v5



def get_2v2_winrates_per_map(data_2v2: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the winrates for each unique map in the data.
    """
    data_2v2['wins'] = data_2v2['win'].astype(int)
    data_2v2['games'] = 1
    data_2v2 = data_2v2.groupby(['map']).agg({'wins': 'sum', 'games': 'sum'})
    data_2v2['winrate'] = data_2v2['wins'] / data_2v2['games']
    data_2v2 = data_2v2.sort_values(by=['winrate'], ascending=False)
    data_2v2['winrate'] = data_2v2['winrate'].apply(lambda x: "{:.1%}".format(x))
    data_2v2 = data_2v2.reset_index()
    return data_2v2
