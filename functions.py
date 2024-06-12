# Main function for finding player type

def main():
    
    player_type = input('Is the player a hitter or a pitcher? ').strip().lower()

    # Based on what the user inputs here a code wil run gathering hitting / pitching statistics 
    
    if player_type == 'hitter':
        get_hitter_stats()
    elif player_type == 'pitcher':
        get_pitcher_stats()
    else:
        print('Invalid player type. Please try again.')

# Function that will run if player is a hitter
        
def get_hitter_stats():
    hits = int(input('Please enter the player\'s number of hits: '))
    walks = int(input('Please enter the player\'s number of walks: '))
    hit_by_pitch = int(input('Please enter how many times they have been hit by a pitch: '))
    at_bats = int(input('Please enter the player\'s at bats: '))
    sacrifice_flies = int(input('Please enter the player\'s number of sacrifice flies: '))
    singles = int(input('Please enter the number of singles the player has: '))
    doubles = int(input('Please enter the number of doubles the player has: '))
    triples = int(input('Please enter the number of triples the player has: '))
    home_runs = int(input('Please enter the number of home runs the player has: '))

    # Holds the statistics 
    
    hitter_stats = {
        'hits': hits,
        'walks': walks,
        'hit_by_pitch': hit_by_pitch,
        'at_bats': at_bats,
        'sacrifice_flies': sacrifice_flies,
        'singles': singles,
        'doubles': doubles,
        'triples': triples,
        'home_runs': home_runs
    }
    
    # Prints the calculated statistics
    print(f"Batting Average: {batting_average(hits, at_bats):.3f}") # returns batting average
    print(f"On-Base Percentage: {on_base_percentage(hits, walks, hit_by_pitch, at_bats, sacrifice_flies):.3f}") # returns obp
    print(f"Slugging Percentage: {slugging(singles, doubles, triples, home_runs, at_bats):.3f}") # returns slugging
    print(f"Closest Player: {padres(hits, at_bats)}") # returning the closest padres player
    

# The 3 functions below are calculating the batting statistics of the player 

def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    
    batting_average = hits / at_bats 
    return batting_average

def on_base_percentage(hits, walks, hit_by_pitch, at_bats, sacrifice_flies):
    denominator = at_bats + walks + hit_by_pitch + sacrifice_flies
    if denominator == 0:
        return 0
    return (hits + walks + hit_by_pitch) / denominator

def slugging(singles, doubles, triples, home_runs, at_bats):
    total_bases = singles + (2 * doubles) + (3 * triples) + (4 * home_runs)
    if at_bats == 0:
        return 0
    return total_bases / at_bats

# The function below compares the users player to a Padres player using Batting Average  
    
def padres(hits, at_bats):
    
    batting_avg = hits / at_bats if at_bats != 0 else 0
        
    if 0.0 <= batting_avg < 0.200:
        return 'Your hitter is closest to Padres player Kyle Higashioka' #BA is .180 
    elif 0.200 <= batting_avg < 0.227:
        return 'Your hitter is closest to Padres player Ha Seong Kim' #BA is .220
    elif 0.227 <= batting_avg < 0.241:
        return 'Your hitter is closest to Padres player Luis Campusano' #BA is .234
    elif 0.241 <= batting_avg < 0.248:
        return 'Your hitter is closest to Padres player Manny Machado' #BA is .248
    elif 0.248 <= batting_avg < 0.267:
        return 'Your hitter is closest to Padres player Jake Cronenworth' #BA is .262
    elif 0.267 <= batting_avg < 0.277:
        return 'Your hitter is closest to Padres player Jackson Merrill' #BA is .272
    elif 0.277 <= batting_avg < 0.300:
        return 'Your hitter is closest to Padres player Fernando Tatis Jr' #BA is .281
    elif 0.300 <= batting_avg < 0.326:
        return 'Your hitter is closest to Padres player Jurickson Profar' #BA is .325
    elif 0.326 <= batting_avg < 0.350:
        return 'Your hitter is closest to Padres player Luis Arraez' #BA is .326
    
    else:
        return 'No close Padres player comparison available'

# This function will run if the player is a pitcher

def get_pitcher_stats():
    walks = int(input('Please enter the player\'s number of walks: '))
    innings_pitched = float(input('Please enter the number of innings pitched: '))
    hits_allowed = int(input('Please enter the number of hits allowed: '))
    hit_by_pitch = int(input('Please enter the number of times the pitcher has hit a player with a pitch: '))
    strikeouts = int(input('Please enter the number of strikeouts they have: '))
    earned_runs = int(input('Please enter the number of earned runs they have: '))
    
    era = calculate_era(innings_pitched, earned_runs)  # Calculate ERA

# Holds Pitching Statistics
    
    pitcher_stats = {
        'walks': walks,
        'innings_pitched': innings_pitched,
        'hits_allowed': hits_allowed,
        'hit_by_pitch': hit_by_pitch,
        'strikeouts': strikeouts,
        'earned_runs': earned_runs
      
    }
    
    print(f"ERA: {calculate_era(innings_pitched, earned_runs):.2f}")
    print(f"WHIP: {calculate_whip(innings_pitched, hits_allowed, walks):.3f}")
    print(f"Strikeouts per 9 innings: {calculate_k_per_9(innings_pitched, strikeouts):.2f}")
    print(f"Walk Percentage: {calculate_walk_percentage(innings_pitched, hits_allowed, walks, hit_by_pitch):.2f}%")
    print(f"Closest Player: {padres_pitcher(era)}")

#The 4 functions below are calculating the pitching statistics of the pitcher    
    
def calculate_era(innings_pitched, earned_runs):
    if innings_pitched == 0:
        return 0
    
    era = (earned_runs * 9) / innings_pitched 
    return era

def calculate_whip(innings_pitched, hits_allowed, walks):
    if innings_pitched == 0:
        return 0
    return (walks + hits_allowed) / innings_pitched

def calculate_k_per_9(innings_pitched, strikeouts):
    if innings_pitched == 0:
        return 0
    return (strikeouts * 9) / innings_pitched

def calculate_walk_percentage(innings_pitched, hits_allowed, walks, hit_by_pitch):
    batters_faced = (innings_pitched * 3) + hits_allowed + walks + hit_by_pitch
    if batters_faced == 0:
        return 0
    return (walks / batters_faced) * 100

# The function below compares the user player to a Padres pitcher based on their earned run average

def padres_pitcher(era):
    
    if 0.0 <= era < 3.08:
        return 'Your pitcher is closest to Padres player Enyel De Los Santos'  # ERA is 2.96
    elif 3.08 <= era < 3.28:
        return 'Your pitcher is closest to Padres player Yu Darvish'  # ERA is 3.20
    elif 3.28 <= era < 3.39:
        return 'Your pitcher is closest to Padres player Dylan Cease'  # ERA is 3.36
    elif 3.39 <= era < 3.67:
        return 'Your pitcher is closest to Padres player Michael King'  # ERA is 3.58
    elif 3.67 <= era < 4.71:
        return 'Your pitcher is closest to Padres player Matt Waldron'  # ERA is 3.76
    elif 4.71 <= era < 5.66:
        return 'Your pitcher is closest to Padres player Joe Musgrove'  # ERA is 5.66
    else:
        return 'No close Padres player comparison available'

main()






    

