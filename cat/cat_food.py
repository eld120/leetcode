import json

'''
Seeking to seek out which ingredients might agree with my 14 year old cat
who was sick recently. Using python to identify distinct ingredients in 

'''
# data of all unique indgredients
with open('./ingredients.json') as json_file:
    data = json.load(json_file)
    

def all_data(data: json)-> tuple:
    '''
    returns a set of unique ingredients, a tuple flavors, and a brand data dict
    '''
    ingredients = []
    flavors = tuple()
    brand_data = {}
    for brand in data:
        brand_data |= data[brand]
        for flavor in data[brand]:
            flavors += (flavor,)
            for ingredient in data[brand][flavor]:
                ingredients.append(ingredient.lower())
    unique_ingredients = set(ingredients)
    
    return (unique_ingredients, flavors, brand_data)


def favorable_ingredients(data: tuple[set,tuple,dict])-> tuple[tuple,tuple]:
    '''
    returns a tuple of (favorable ingredients, unfavorable ingredients)
    '''
    # favorable_flavors = ("Digest Sensitive Loaf in Sauce Canned Cat Food", 
    #                  "Prescription Diet Gastrointestinal Biome with Chicken Dry Cat Food",)
    favorable_flavors = ("Prescription Diet Gastrointestinal Biome with Chicken Dry Cat Food",)
    favorable_ingredients = tuple()
    unfavorable_ingredients = tuple()
    for ingredient in data[2]:
        
        for ingrendient in data[2][ingredient]:
            if ingredient in favorable_flavors:

                favorable_ingredients += (ingrendient.lower(),)
            else:
                unfavorable_ingredients += (ingrendient.lower(),)
    # print(f'--------------------------FAVORABLE--------------------------\
    #         -------------------------------------------------------------\
    #         {favorable_ingredients}\
    #         -------------------------------------------------------------\
    #         -------------------------------------------------------------\
    #         --------------------------UNFAVORABLE--------------------------\
    #         {unfavorable_ingredients}')
    return (favorable_ingredients, unfavorable_ingredients)

def slice_dice(data):
    favorable = set(data[0])
    unfavorable = set(data[1])
    shared_ingredients = favorable & unfavorable
    beneficial = favorable - unfavorable
    print(f'--------------------------FAVORABLE--------------------------\
            -------------------------------------------------------------\
          {beneficial}-------------------------------------------------------------\
            -------------------------------------------------------------\
            --------------------------SHARED--------------------------\
            {shared_ingredients}')





if __name__ == '__main__':
    
    slice_dice(favorable_ingredients(all_data(data)))
    
        