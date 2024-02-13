import csv

with open('./top_movies.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    earliest_release_date = 2025
    
    for row in reader:
        if int(row['Release Date']) < earliest_release_date:
            earliest_release_date = int(row['Release Date']) 
            oldest_top_grossing_movies = [row['Title']]
        elif int(row['Release Date']) == earliest_release_date:
            oldest_top_grossing_movies.append(row['Title'])

print(f'The earliest year on the top movies list is {earliest_release_date}\nHere are the movies from {earliest_release_date}:')
for movie in oldest_top_grossing_movies:
    print(f'\t{movie}')