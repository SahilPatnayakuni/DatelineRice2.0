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

#save_nickname_dict()


def nicknames(name):
    pickle_in = open("nicknames.pkl","rb")
    nickname_dict = pickle.load(pickle_in)
    return nickname_dict[name]

print(nicknames('harry'))
print(nicknames('jim'))
print(nicknames('susan'))
print(nicknames('alan'))
print(nicknames('alex'))
