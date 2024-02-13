import csv

if __name__ == '__main__':
    with open('./top_movies.csv', 'r') as file:
        reader = csv.DictReader(file)
        movies_by_distributor = dict()
        for row in reader:
            if row['Distributor'] in movies_by_distributor.keys():
                movies_by_distributor[row['Distributor']].append(row['Title'])
            else:
                movies_by_distributor[row['Distributor']] = [row['Title']]
                                                             
        most_movies = 0
        leading_distributor = ''
        for distributor, movies in movies_by_distributor.items():
            if len(movies) > most_movies:
                most_movies = len(movies)
                leading_distributor = distributor
            elif len(movies) == most_movies:
                leading_distributor += f',{distributor}'
        print(f'{leading_distributor} has the most movies ({most_movies}) in the top 1000 grossing movies list')