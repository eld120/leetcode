import csv

def all_no_one_songs_and_artists():
    '''
    
    Print out all of the #1 songs and the artists who made them. If a song was #1 for more than one week, only print it once. Example output:
    These were the number one songs of 2000:
    "Try Again" - Aaliyah
    "Say My Name" - Destiny's Child
    "What A Girl Wants" - Christina Aguilera
    "Maria Maria" - Santana Featuring The Product G&B
    "Smooth" - Santana Featuring Rob Thomas
    "Independent Women Part I" - Destiny's Child
    '''
    with open('./billboard100_2000.csv', 'r') as file:
        reader = csv.DictReader(file)
        all_no_one_songs = dict()
        for row in reader:
            if row['rank'] == '1' and row['song'] in all_no_one_songs.keys():
                continue
            elif row['rank'] == '1':
                all_no_one_songs[row['song']] = row['artist']
    print('These were the number one songs of 2000:')
    for song, artist in all_no_one_songs.items():
        print(f'\t"{song}"- {artist}')

            

if __name__ == '__main__':
    all_no_one_songs_and_artists()