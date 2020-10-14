import pandas as pd
import copy
from progress.bar import Bar

class Apriori:
    def __init__(self, _file, _support=0.02, _confidence=0.3):
        groceries = pd.read_csv(_file)
        groceries_array = groceries.values

        self.support = _support
        self.confidence = _confidence
        self.record_num = groceries_array.shape[0]
        self.data = []
        self.frequence = []
        self.frequence.append({})

        for i in range(groceries_array.shape[0]):
            now_data = []
            for j in range(groceries_array[i][0]):
                t = groceries_array[i][j + 1]
                now_data.append(t)
                t = tuple([t, ])
                if t in self.frequence[0]:
                    self.frequence[0][t] += 1
                else:
                    self.frequence[0][t] = 1
            now_data.sort()
            self.data.append(now_data)
        
        for key in list(self.frequence[0].keys()):
            if self.frequence[0][key] / self.record_num < self.support:
                self.frequence[0].pop(key)

    def dfs_record(self, record, depth):
        def dfs(record, now, depth, temp, ret):
            if depth == 0:
                ret.append(tuple(copy.deepcopy(temp)))
            else:
                for i in range(now, len(record)):
                    temp.append(record[i])
                    dfs(record, i + 1, depth - 1, temp, ret)
                    temp.pop()
        ret = []
        dfs(record, 0, depth, [], ret)
        return ret

    def get_all_subset(self, record):
        res = []
        for i in range(1, len(record)):
            res.extend(self.dfs_record(record, i))
        return res

    def expand_one_step(self, last_dic):
        res = {}
        keys = list(last_dic.keys())
        next_key_len = len(keys[0]) + 1
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                flag = True
                for k in range(0, len(keys[i]) - 1):
                    if keys[i][k] != keys[j][k]:
                        flag = False
                if keys[i][-1] == keys[j][-1]:
                    flag = False
                if flag:
                    t = list(keys[i])
                    t.append(keys[j][-1])
                    t.sort()
                    res[tuple(t)] = 0

        progress_bar = Bar('Processing', max=100, fill='#', suffix='now: %(percent)d / 100 %%')
        for i, record in enumerate(self.data):
            if i % int(self.record_num / 100) == 0:
                progress_bar.next()
            for item in self.dfs_record(record, next_key_len):
                if item in res:
                    res[item] += 1

        for key in list(res.keys()):
            if res[key] / self.record_num < self.support:
                res.pop(key)
        progress_bar.finish()
        return res

    def expand(self):
        i = 0
        while True:
            print("Scanning %d time..." % (i + 1))
            dic = self.expand_one_step(self.frequence[i])
            if dic:
                self.frequence.append(dic)
                i += 1
            else:
                break
    
    def get_res(self):
        res = []
        for i in range(1, len(self.frequence)):
            for key in list(self.frequence[i].keys()):
                t = list(key)
                for posterior in self.dfs_record(t, 1):
                    posterior = list(posterior)
                    prior = list(set(t) - set(posterior))
                    prior.sort()
                    posterior.sort()
                    prior = tuple(prior)
                    posterior = tuple(posterior)
                    now_support = self.frequence[i][tuple(t)] / self.record_num
                    now_confidence = self.frequence[i][tuple(t)] / self.frequence[i - 1][prior]
                    # print(prior, "->" , posterior, ":  ", now_confidence)
                    if now_confidence > self.confidence:
                        res.append([prior, posterior, now_support, now_confidence])
        return res

    def print_res(self, res):
        for item in res:
            # print(item[0], "->", item[1], "  support: ", item[2], " confidence: ", item[3])
            print("%-40s -> %-30s Support: %4f,   Confidence: %4f" % \
                (str(item[0]), str(item[1]), item[2], item[3]))

if __name__ == "__main__":
    apriori = Apriori("groceries.csv")
    apriori.expand()
    items = apriori.get_res()
    apriori.print_res(items)
    