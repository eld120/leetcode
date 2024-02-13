import csv


if __name__ == '__main__':
    with open('./top_movies.csv', 'r') as file:
        reader = csv.DictReader(file)
        ratings_distribution = dict()
        for row in reader:
            if row['Rating'] in ratings_distribution.keys():
                ratings_distribution[row['Rating']] += 1
            else:
                ratings_distribution[row['Rating']] = 1
print('Here is the distribution of ratings:')
for rating, count in ratings_distribution.items():
    print(f'{count} movies were rated {rating}')