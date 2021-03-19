import pickle
data = [[99999, "admin", 100], [99998, "tester", 99]]


with open("quiz_data.txt", "wb") as fp:
    pickle.dump(data, fp)