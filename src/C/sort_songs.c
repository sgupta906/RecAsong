// sort_songs.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a struct for songs
typedef struct {
    char title[100];
    char artist[100];
    int popularity;
} Song;

// Function to compare songs by popularity
int compare(const void *a, const void *b) {
    Song *songA = (Song *)a;
    Song *songB = (Song *)b;
    return songB->popularity - songA->popularity; // Descending order
}

// Function to sort songs
void sort_songs(Song *songs, int n) {
    qsort(songs, n, sizeof(Song), compare);
}

// Function to read songs from stdin
void read_songs(Song *songs, int n) {
    for (int i = 0; i < n; i++) {
        scanf("%s %s %d", songs[i].title, songs[i].artist, &songs[i].popularity);
    }
}

// Function to print sorted songs to stdout
void print_songs(Song *songs, int n) {
    for (int i = 0; i < n; i++) {
        printf("%s by %s (Popularity: %d)\n", songs[i].title, songs[i].artist, songs[i].popularity);
    }
}

// Main function
int main() {
    int n;
    scanf("%d", &n); // Read the number of songs
    Song songs[n];

    read_songs(songs, n);
    sort_songs(songs, n);
    print_songs(songs, n);

    return 0;
}
