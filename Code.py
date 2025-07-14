import requests

def isMoroccan(user_id):
    end_point = f"https://fantasy.premierleague.com/api/entry/{user_id}"
    r = requests.get(end_point)

    if r.status_code != 200:
        return False
    
    data = r.json()
    return data.get("player_region_name", "").lower() == "morocco"

def AverageRank(user_id):
    end_point = f"https://fantasy.premierleague.com/api/entry/{user_id}/history"
    r = requests.get(end_point)

    if status_code != 200:
        return False
    
    data = r.json()
    ranks = [s['rank'] for s in data['past'] if s['rank']]

    if not ranks:
        return False
    
    return sum(ranks) / len(ranks)

results = []

for i in range(1,5000000,1000):
    if isMoroccan(i):
        avg = AverageRank(i)
        if avg:
            results.append((i,avg))

top5 = sorted(results,key=lambda x: x[1])[:5]

print("Top 5 Moroccan FPL Managers by Average Rank:")
for i, avg in top5:
    print(f"User ID: {i}, Avg Rank: {int(avg):,}")