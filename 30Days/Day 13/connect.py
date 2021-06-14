import pprint

import pandas as pd
import requests

api_key = "a6742b0b8327a2a50221e778f8881f07"

"""
Endpoint
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=a6742b0b8327a2a50221e778f8881f07
"""
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&page=1"
print(endpoint)
#r = requests.get(endpoint) #json={"api_key": api_key})
#print(r.status_code)
#print(r.text)

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
#print(endpoint)
r = requests.get(endpoint)
#pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        #print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
           # print(result['title'], _id)
            movie_ids.add(_id)
        #print(list(movie_ids))
output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
print(df.head)
df.to_csv(output, index=False)