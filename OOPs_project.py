class Movie:
    def __init__(self,title,actor,actress):
        self.title = title
        self.actor = actor
        self.actress = actress
    def info(self):
        print('Movie title :',self.title)
        print('Movie actor :',self.actor)
        print('Movie actress :',self.actress)

list_of_movies = []
while True:
    title = input('enter movie\'s title name:')
    actror = input('enter movie\'s actor name:')
    actress = input('enter movie\'s actress name:')

    movie = Movie(title,actror,actress)
    list_of_movies.append(movie)
    confirm = input('Do you want to another movie\'s details[YES|NO]:')
    if confirm.upper() == 'NO':
        break

# print('list of movies objects are:',list_of_movies)
no = 1
for i in list_of_movies:
    print('Total Numer of movies :',len(list_of_movies))
    print(f"Movie's details {no} are:")
    i.info()
    no = no + 1
        


