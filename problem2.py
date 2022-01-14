game_scores = [92,89,104,102,96,100,88,110,107,94,96,102,114]


def check_score(num):
    if num >= 100:
        return True
    else: 
        return False

def quarter_avg(num):
    return num / 4



game_results = filter(check_score, game_scores)
avg_points = map(quarter_avg, game_scores)

avg_points2 = map(lambda score: score / 4, game_scores)
game_results2 = filter(lambda score: score >= 100, game_scores)

print ('OVER 100 LIST',list(game_results))
print('OVER 100 LIST 2', list(game_results2))
print('QUARTER AVG.', list(avg_points))
print('QUARTER AVG. 2', list(avg_points2))


