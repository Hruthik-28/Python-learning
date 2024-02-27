from pymongo import MongoClient
from bson import ObjectId

try:
    client = MongoClient("mongodb+srv://<username>:<password>@cluster0.8zlqwnh.mongodb.net/")
    print(client)
except Exception as e:
    print(str(e))

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]}, time: {video["time"]}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {
            "name": name,
            "time": time
        }}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("---YOUTUBE MANAGER---")
        print("1. list all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Quit")
        choice = input("Enter your choice: ")

        match(choice):
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter videoId: ")
                name = input("Enter new video name: ")
                time = input("Enter new video time: ")
                update_video(video_id, name, time)
            case '4':
                pasvideo_id = input("Enter videoId: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                break

if __name__ == "__main__":
    main()