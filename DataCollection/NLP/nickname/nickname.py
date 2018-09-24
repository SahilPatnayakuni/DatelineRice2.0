import csv
from collections import defaultdict
import pickle

def save_nickname_dict():
    nicknames = defaultdict(set)
    with open('names.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for name in row:
                for name2 in row:
                    nicknames[name].add(name2)
    f = open("nicknames.pkl","wb")
    pickle.dump(nicknames,f)
    f.close()

save_nickname_dict()
