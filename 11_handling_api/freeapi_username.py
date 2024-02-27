import requests

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")

def fetch_random_joke():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes/joke/random'
    res = requests.get(url)
    data = res.json()

    if data["success"] and "data" in data:
        joke = data["data"]["content"]
        return joke
    else:
        Exception("Failed to fetch joke")

def fetch_youtube_video(videoId):
    if not videoId:
        Exception("VideoId is required")
    res = requests.get(f"https://api.freeapi.app/api/v1/public/youtube/videos/{videoId}")
    data = res.json()

    if data["success"] and "data" in data:
        return data
    else:
        Exception("Failed to fetch video")

# def main():
#     try:
#         username, country = fetch_random_user()
#         print(f"username:{username} \n Country:{country}")
#     except Exception as e:
#         print(str(e))
        
# def main():
#     try:
#         joke = fetch_random_joke()
#         print(f"Randome Joke: \n \t {joke}")
#     except Exception as e:
#         print(str(e))

def main():
    try:
        video = fetch_youtube_video("EQwmQLU1S6I")
        channel_stats = video["data"]["channel"]["statistics"]
        video_details = video["data"]["video"]["items"]
        print("Channel stats: ")
        print(f"viewCount: {channel_stats["viewCount"]}")
        print(f"subscriberCount: {channel_stats["subscriberCount"]}")
        print(f"videoCount: {channel_stats["videoCount"]}")
        print("\n")
        print(f"video title: {video_details["snippet"]["title"]}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()