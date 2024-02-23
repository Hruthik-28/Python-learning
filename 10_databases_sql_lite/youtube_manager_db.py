import sqlite3
con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')

def list_all_videos():
    print('\n')
    print('*' * 50)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print('*' * 50)
    print('\n')

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    print("\nVideo addedd successfully !!!.")

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    con.commit()
    print("\nVideo updated successfully !!!.")


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()
    print("\nVideo deleted successfully !!!.")

def main():
    while True:
        print("\n--- Youtube Manager App with DB ---")
        print("1. List videos")
        print("2. Add video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                add_video(name, time)
            case '3':
                video_id = input('Enter VIDEO ID to update: ')
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                update_video(video_id, name, time)
            case '4':
                video_id = input('Enter VIDEO ID to delete: ')
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice")

    con.close()

if __name__ == "__main__":
    main()