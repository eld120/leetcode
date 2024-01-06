


if __name__ == '__main__':
    with open('sowpods.txt', 'r') as f:
        counter = {
            'Q': 0,
            'X': 0,
            'Z': 0
        }
        # assuming counting every occurance of Q, X, Z is significant and that's what's being calculated
        # it would be easy to remove the for loop and conditional check to iterate over every letter in 
        # a word that contains our target letter to only count words that have a target letter rather than every target letter
        for val in f.readlines():
            if 'Q' in val:
                for inst in val:
                    if inst == 'Q':
                        counter['Q'] += 1
            elif 'X' in val:
                for inst in val:
                    if inst == 'X':
                        counter['X'] += 1
            elif 'Z' in val:
                for inst in val:
                    if inst == 'Z':
                        counter['Z'] += 1
        reference = 0
        ans = []
        for val in counter:
            if counter[val] == reference:
                ans.append(val)
            elif counter[val] > reference:
                ans = []
                reference = counter[val]
                ans.append(val)
        print(ans)
        
        
                    
                
                    