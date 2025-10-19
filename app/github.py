import httpx

GITHUB_API_URL = "https://api.github.com/users/{username}/gists"

def get_gists(username: str):
    url = GITHUB_API_URL.format(username=username)
    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        return [
            {
                "id": gist["id"],
                "description": gist["description"],
                "url": gist["html_url"]
            }
            for gist in response.json()
        ]
    except httpx.HTTPStatusError:
        return None
