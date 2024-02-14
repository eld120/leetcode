import csv


def longest_lived_songs():
    '''
    What song(s) were on the charts (anywhere on the charts) for the most weeks of 2000?
    '''
    with open('./billboard100_2000.csv', 'r') as file:
        reader = csv.DictReader(file)
        songs_with_tenure = (0, [])
        billboard_song_data = dict()
        for row in reader:
            if row['song'] in billboard_song_data.keys():
                billboard_song_data[row['song']] += 1
                if billboard_song_data[row['song']] > songs_with_tenure[0]:
                    songs_with_tenure = (billboard_song_data[row['song']], [row['song']])
                elif billboard_song_data[row['song']] == songs_with_tenure[0]:
                    songs_with_tenure[1].append(row['song'])
            else:
                billboard_song_data[row['song']] = 1
            
    print(f'the following songs appeared on the billboard {songs_with_tenure[0]} times:')
    for song in songs_with_tenure[1]:
        print(f'\t{song}')

if __name__ == '__main__':
    longest_lived_songs()