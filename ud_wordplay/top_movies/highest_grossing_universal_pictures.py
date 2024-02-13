import csv


if __name__ == '__main__':
    with open('./top_movies.csv', 'r') as file:
        reader = csv.DictReader(file)
        top_grossing_dollars = 0
        top_grossing_movie = ''
        for row in reader:
            if row['Distributor'] == 'Universal Pictures' and int(row['US Sales']) > top_grossing_dollars:
                top_grossing_dollars = int(row['US Sales']) 
                top_grossing_movie = row['Title']               
            
    print(f'Top Grossing US Movie from Univeral Pictures:\n\t{top_grossing_movie} with ${top_grossing_dollars:.2f} in US ticket sales')