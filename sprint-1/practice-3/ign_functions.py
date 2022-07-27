
def get_platform(games_df, target_platform):
    """
    | Help on user-defined function get_platform:
    |
    | This function works on the ign dataframe & takes inputs: 
    | - games_df - dataframe of ign games 
    | - target_platform - a string naming the gaming platform the games were released on 
    |
    | This function returns:
    | - platform_only - a dataframe containing only games released on the input target_platform
    """
    platform_only = games_df[games_df['platform'] == target_platform]
    return platform_only

def bar_plot_genres(games_df, target_platform):
    """
    | Help on user-defined function bar_plot_genres:
    |
    | This function creates a bar plot of primary genres for games of a certain platform. 
    |
    | Takes the following inputs: 
    | - games_df - dataframe of ign games 
    | - target_platform - a string naming the gaming platform the games were released on
    |
    | This function returns:
    | - bar plot showing count of each primary genre for that gaming platform 
    """
    # get games from this platform 
    this_platform = get_platform(games_df, target_platform)
    # plot primary genre
    this_platform.primary_genre.value_counts().plot.bar(title = 'Genres of all ' + target_platform + ' games')