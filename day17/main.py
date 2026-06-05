fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

names = ['Finland', 'Norway','Denmark','Iceland', 'Estonia','Russia', 'Sweden']
*nordic_countries, es, ru = names

print(nordic_countries, es, ru)


