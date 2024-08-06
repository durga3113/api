import requests

def get_spotify_tracks(query):
    search_url = f'https://api.maher-zubair.tech/search/spotify?q={query}'

    try:
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        result = data.get('result', [])
        formatted_result = []
        for track in result:
            formatted_result.append({
                "artist": track['artist'],
                "duration": track['duration'],
                "popularity": track['popularity'],
                "preview": track['preview'],
                "title": track['title'],
                "url": track['url']
            })
        return {
            "developer": "Eypz God",
            "result": formatted_result,
            "status": 200
        }
    except Exception as e:
        return {
            "developer": "Eypz God",
            "error": str(e),
            "status": response.status_code if response else 500
        }
