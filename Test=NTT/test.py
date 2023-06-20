import pickle

from ntt_func import ntt    

with open("sample.pickle", mode="rb") as f:
    r = pickle.load(f)

print(r)

r_out = ntt(r)

print(r_out)