import csv


def no_one_for_the_longest():
    '''
    What song was the #1 song for the most weeks of 2000, who was the artist, and how many weeks was it at #1?
    proposed - song, artist, weeks @ no1

    '''
    with open('./billboard100_2000.csv', 'r') as file:
        reader = csv.DictReader(file)
        most_weeks_at_no_one = ('', 0, '')
        billboard_no_one_songs = dict()
        for row in reader:
            if row['rank'] == '1' and row['song'] in billboard_no_one_songs.keys():
                billboard_no_one_songs[row['song']]['weeks_at_1'] += 1
                
                if billboard_no_one_songs[row['song']]['weeks_at_1'] > most_weeks_at_no_one[1]:
                    #breakpoint()
                    most_weeks_at_no_one = (row['song'], billboard_no_one_songs[row['song']]['weeks_at_1'], row['artist'])
                elif billboard_no_one_songs[row['song']]['weeks_at_1'] == most_weeks_at_no_one[1]:
                    most_weeks_at_no_one += (row['song'], billboard_no_one_songs[row['song']]['weeks_at_1'], row['artist'])
            elif row['rank'] == '1':
                billboard_no_one_songs[row['song']] = {'weeks_at_1': 0,'artist': row['artist']}
        
            
    print(f'Song that held the most weeks at no 1: {most_weeks_at_no_one[0]} by {most_weeks_at_no_one[2]} - held no 1 for {most_weeks_at_no_one[1]} weeks')





if __name__ == '__main__':
    no_one_for_the_longest()