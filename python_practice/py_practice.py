import pandas as pd
import csv
import os

#  class StreamingWriter():
#         header = ["unique_users", "mean_session", "total_duration"]
#         def __init__(self, file_path, file_name, file_type):
#             self.file_path = file_path
#             self.file_name = file_name
#             self.file_type = file_type
#             self.full_file_path = os.path.join(file_path, file_name + "." + file_type)
        
#         def write_summary(self, rows):
#             with open(self.full_file_path, "w", newline="") as csv_file:
#                 #create the csv file
#                 csvwriter = csv.writer(csv_file)
#                 #csv write header
#                 csvwriter.writerow(StreamingWriter.header)
#                 for row in rows:
#                     csvwriter.writerow(row)

# class StreamingData(StreamingWriter):
#     def __init__(self, file_path, file_name, file_type):
#         super().__init__(file_path, file_name, file_type):
#         self.data_source = self.full_file_path
#         self.df = None

#     def load(self):
#         try:
#             self.df = pd.read_csv(self.data_source)
#         except Exception as e:

    
#     def summary(self):
#        if self.df is not None:
#            unique_users = self.df['user_id'].nunique()
#            mean_session = round(self.df['mean_session'].mean(), 2)
#            total_duration = round(self.df['session_duration'].sum(),2)



class MovieLog():
    tup = tuple()
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
    
    def add_movie(self):
        a, b = (self.title, self.rating)
        convert_tup = list(MovieLog.tup)
        convert_tup.append(a)
        convert_tup.append(b)
        MovieLog.tup = tuple(convert_tup)
        return MovieLog.tup
    
    def __str__():
        return f"Movies in tuple are {MovieLog.tup}"

    def high_threshold(self):
        lst = []
        highest = list(filter(lambda x: x[1] > 6, MovieLog.tup))

add_it = MovieLog("a", 7.6)


# highest_ranked = add_it.high_threshold()
# print(highest_ranked)


# tup = (("Barbie", 4.6), ("Oppenheimer", 2.5), ("Never Been Kiss", 7.6))

# a, b =  ("Oppen", 2.2,)

