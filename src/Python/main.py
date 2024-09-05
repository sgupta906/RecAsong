# main.py
import subprocess
import requests

def get_user_preferences():
    print("Welcome to RecASong!")
    
    mood = input("How are you feeling today? (happy, sad, energetic, relaxed): ").strip().lower()
    genre = input("What's your favorite music genre? (pop, rock, jazz, classical): ").strip().lower()
    artist = input("Who's your favorite artist? (e.g., The Beatles, Drake): ").strip()

    return mood, genre, artist


def call_java_utility(mood):
    try:
        # Call the Java program with the correct classpath
        result = subprocess.run(['java', '-cp', 'src', 'Java.Utility', mood], capture_output=True, text=True)
        print("Java Program Output:")
        print(result.stdout)
    except Exception as e:
        print(f"Error calling Java utility: {e}")

# Rest of your Python script...

def fetch_song_recommendations(mood, genre, artist):
    # Mock API call (replace with actual API code)
    print(f"Fetching songs for mood: {mood}, genre: {genre}, artist: {artist}")
    
    songs = [
        {"title": "Song1", "artist": "ArtistA", "popularity": 50},
        {"title": "Song2", "artist": "ArtistB", "popularity": 70},
        {"title": "Song3", "artist": "ArtistC", "popularity": 30},
    ]
    
    return songs

def sort_songs_with_c(songs):
    # Convert song list to input format for C program
    input_data = f"{len(songs)}\n" + "\n".join(f"{song['title']} {song['artist']} {song['popularity']}" for song in songs)

    # Call the C program using subprocess
    result = subprocess.run(['./src/C/sort_songs'], input=input_data, text=True, capture_output=True)

    if result.returncode == 0:
        print("Sorted Songs:\n", result.stdout)
    else:
        print("Error sorting songs:", result.stderr)

def main():
    mood, genre, artist = get_user_preferences()
    songs = fetch_song_recommendations(mood, genre, artist)
    sort_songs_with_c(songs)

if __name__ == "__main__":
    main()
