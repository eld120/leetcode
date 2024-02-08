

# if __name__ == '__main__':
#     with open('./countries.txt', 'r') as f:
#         countries_containing_united = []
#         for word in f.readlines():
            
#             if "united" in word.lower():
#                 countries_containing_united.append(word.rstrip('\n'))

#         print(countries_containing_united)


if __name__ == '__main__':
    with open('./countries.txt', 'r') as file:
        countries_containing_united = []
        for word in file:
            
            if "united" in word.lower():
                countries_containing_united.append(word.rstrip('\n'))

        print(countries_containing_united)