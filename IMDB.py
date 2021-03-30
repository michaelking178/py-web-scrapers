import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

headers = {
    'x-rapidapi-key': "7de8ef5e02mshb36ace0cf793ad5p116d01jsn4e9e59bd2993",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

search = input("Search a movie or TV show title: ")
querystring = {"s":search, "page":"1", "r":"json"}

response = requests.request("GET", url, headers=headers, params=querystring)
jsonResponse = response.json()

print(jsonResponse['Search'][0]['Title'])
print(jsonResponse['Search'][0]['Year'])
print(jsonResponse['Search'][0]['Poster'])
