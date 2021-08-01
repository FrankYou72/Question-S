from .Q_data import Packs
from .questionS import Question

questions_list = []

for p in Packs.keys():
    for e in Packs[p][1].keys():
        q = Question(p, e)
        questions_list.append(q)

print(questions_list)