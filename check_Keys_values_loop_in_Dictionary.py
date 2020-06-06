user_info={
    'Name':'Monish',
    'age':22,
    'fav_movies':['Iron-Man','Avengers','Batman'],
    'fav_heros':['Robert Downey Junior','Nawazuddin Siddiqui','Shah Rukh Khan']
}

# Check if key exist in Dictionary
# if 'Name' in user_info:
#     print('present')
# else:
#     print('Not Present')

# Check if value exist in Dictionary
# if 'Monish' in user_info.values():
#     print('Present')
# else:
#     print('Not Present')

# Loop in Dictionary

# for i in user_info:
#     print(i)    # print keys of dictionary
#     print(user_info[i]) # print values of dictionary

# values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))