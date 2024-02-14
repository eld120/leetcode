import csv




def find_artist_with_most_top_songs():
    '''
    What artist had the most songs chart in 2000, and what were those songs?
    '''
    with open('./billboard100_2000.csv', 'r') as file:
        reader = csv.DictReader(file)
        top_artists_dict = dict()
        top_hitmaker = ('artist',[], 0 )
        for row in reader:
            if row['artist'] not in top_artists_dict.keys():
                top_artists_dict[row['artist']] = {'total_songs': 1, 'all_songs':[row['song']]}
            elif row['song'] not in top_artists_dict[row['artist']]['all_songs']:
                top_artists_dict[row['artist']]['total_songs'] += 1
                top_artists_dict[row['artist']]['all_songs'] += [row['song']]
                if top_artists_dict[row['artist']]['total_songs'] > top_hitmaker[2]:
                    top_hitmaker = (row['artist'], top_artists_dict[row['artist']]['all_songs'], top_artists_dict[row['artist']]['total_songs'])

    print(f'{top_hitmaker[0]} was the top artist with {top_hitmaker[2]} songs:')
    for song in top_hitmaker[1]:
        print(f'\t{song}')


if __name__ == '__main__':
    find_artist_with_most_top_songs()