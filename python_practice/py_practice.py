# import pandas as pd
# import csv
# import os

# #  class StreamingWriter():
# #         header = ["unique_users", "mean_session", "total_duration"]
# #         def __init__(self, file_path, file_name, file_type):
# #             self.file_path = file_path
# #             self.file_name = file_name
# #             self.file_type = file_type
# #             self.full_file_path = os.path.join(file_path, file_name + "." + file_type)
        
# #         def write_summary(self, rows):
# #             with open(self.full_file_path, "w", newline="") as csv_file:
# #                 #create the csv file
# #                 csvwriter = csv.writer(csv_file)
# #                 #csv write header
# #                 csvwriter.writerow(StreamingWriter.header)
# #                 for row in rows:
# #                     csvwriter.writerow(row)

# # class StreamingData(StreamingWriter):
# #     def __init__(self, file_path, file_name, file_type):
# #         super().__init__(file_path, file_name, file_type):
# #         self.data_source = self.full_file_path
# #         self.df = None

# #     def load(self):
# #         try:
# #             self.df = pd.read_csv(self.data_source)
# #         except Exception as e:

    
# #     def summary(self):
# #        if self.df is not None:
# #            unique_users = self.df['user_id'].nunique()
# #            mean_session = round(self.df['mean_session'].mean(), 2)
# #            total_duration = round(self.df['session_duration'].sum(),2)



# class MovieLog():
#     tup = tuple()
#     def __init__(self, title, rating):
#         self.title = title
#         self.rating = rating
    
#     def add_movie(self):
#         a, b = (self.title, self.rating)
#         convert_tup = list(MovieLog.tup)
#         convert_tup.append(a)
#         convert_tup.append(b)
#         MovieLog.tup = tuple(convert_tup)
#         return MovieLog.tup
    
#     def __str__():
#         return f"Movies in tuple are {MovieLog.tup}"

#     def high_threshold(self):
#         lst = []
#         highest = list(filter(lambda x: x[1] > 6, MovieLog.tup))

# add_it = MovieLog("a", 7.6)


# # highest_ranked = add_it.high_threshold()
# # print(highest_ranked)


# # tup = (("Barbie", 4.6), ("Oppenheimer", 2.5), ("Never Been Kiss", 7.6))

# # a, b =  ("Oppen", 2.2,)

# ratings = (("The Batman", 8.1), ("Morbius", 4.8), ("Everything Everywhere All At Once", 8.6), ("Cats", 2.3))

# def rr():
#     above = [title for title, rating in ratings if rating > 7.5]
#     return above

# # #list comprehension
# # lstit = [title for title, rating in ratings if rating > 7.5 ]

# movie_scores = {"Barbie": 7.6, "Oppenheimer": 8.5}

# movie_scores["Dune"] = 8.2

# print(movie_scores)

# titles = ["Dune", "Arrival", "Blade Runner"]
# scores = [8.2, 7.9, 8.0]

# zipit = zip(titles, scores)
# dictZip = dict(zipit)
# print(dictZip)

# tgs = [("The Batman", "action", 8.1), ("Morbius", "drama", 4.8), ("Everything Everywhere All At Once", "drama", 8.6), ("Cats", "musical", 2.3)]

# def breakout(args):
#     for title, genre, score in args:
#         print(f"Title: {title}\n Genre: {genre}\n Score: {score}")

# # SELECT AVG(age)
# # FROM users_table
# # WHERE age > 26

# there = breakout(tgs)
# print(there)

# raw_movies = [" Dune ", " Oppenheimer", "Barbie ", "  Tenet  "]

# def cleanList(dirtyList):
#     cleaned = [x.lower().strip() for x in raw_movies]
#     return cleaned

# activate = cleanList(raw_movies)
# print(activate)

runtimes = [95, 110, 87, 130, 100, 145, 98]
above = [ x for x in runtimes if x > 100]
print(above)

subs = {'Netflix': 232, 'Disney+': 157, 'Hulu': 50, 'Apple TV+': 25}
new_sub = {key: sub for key, sub in subs.items() if sub > 100}

print(new_sub)

platforms = ['Netflix', 'Hulu', 'Disney+']
ratings = [4.8, 3.9, 4.5]

zipit = zip(platforms, ratings)
lz = list(zipit)
print(lz)

for key, value in lz:
    print(f"{key}: {value}\n")

def show_genres(**kwargs):
    for show, genre in kwargs.items():
        print(f"{show}: {genre}")

test = {"Mulan": 8.5, "Little Mermaid": 5.5, "Zeus": 10}
#or show_genres(Mulan="action", Mermaid="Fantasy")

printIT = show_genres(**test)
print(printIT)

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
    
    def is_hit(self):
        if self.rating > 7.5:
            return True
        else:
            return False
