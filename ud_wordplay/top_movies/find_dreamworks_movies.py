import csv

if __name__ == '__main__':
    with open('./top_movies.csv', 'r') as file:
        reader = csv.DictReader(file)
        print('Distributed by DreamWorks:')
        for line in reader:
            if line['Distributor'] == 'DreamWorks':
                print(f'\t{line["Title"]}')