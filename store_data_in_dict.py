user={}

name=input("Enter your name : ")
age=input("Enter your age : ")
fav_movies=input("Enter your fav_movies comma seperated : ").split(',')
fav_songs=input("Enter your fav_songs comma seperated : ").split(',')

user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs

for i,j in user.items():
    print(f"{i}:{j}")