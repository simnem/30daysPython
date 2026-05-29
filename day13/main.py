numbers = [-4, -3, -2, -1, 0, 2, 4, 6]


new_list = [ n for n in numbers if n <= 0]

#print(new_list)


list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list_of_lists = [list_of_list for l in list_of_lists for list_of_list in l]

#print(new_list_of_lists)

list_of_tuples = [(0, 1, 0, 0, 0, 0, 0),
                    (1, 1, 1, 1, 1, 1, 1),
                    (2, 1, 2, 4, 8, 16, 32),
                    (3, 1, 3, 9, 27, 81, 243),
                    (4, 1, 4, 16, 64, 256, 1024),
                    (5, 1, 5, 25, 125, 625, 3125),
                    (6, 1, 6, 36, 216, 1296, 7776),
                    (7, 1, 7, 49, 343, 2401, 16807),
                    (8, 1, 8, 64, 512, 4096, 32768),
                    (9, 1, 9, 81, 729, 6561, 59049),
                    (10, 1, 10, 100, 1000, 10000, 100000)]

new_list_of_tuples = [ (i, 1, i, i*1, i**2, i**3, i**4, i**5) for i in range(11)]
# print(new_list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [ [country[0][0].upper(),country[0][0][:3].upper(),country[0][1].upper()] for country in countries ]

#print(new_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries_dic = [{'country':country[0][0].upper(), 'city':country[0][1].upper()} for country in countries]

#print(new_countries_dic)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [ f'{name[0][0]} {name[0][1]}' for name in names]

#print(new_names)

x = lambda x1, y1, x2, y2: (y2-y1) / (x2 - x1)
print(x(1,2,3,4))