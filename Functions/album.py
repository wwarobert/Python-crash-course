def make_album(artist_name, album_title, number_of_songs=None):
    """Return dictionary of albums"""
    album = {'artist_name': artist_name, 'album_title': album_title}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album


print(make_album("Arcade Fire", "Funeral"))
print(make_album("The Stooges", "The Stooges"))
print(make_album("Sparks", "Kimono my house"))
print(make_album("Juvenile", "400 Degreez", 18))

while True:
    album_name = input("Please enter artist name: ")
    album_title = input("Please enter album title: ")

    print(make_album(album_name, album_title))

    quit = input("Enter 'q' if you want to quit ")
    if (quit == 'q'):
        break
