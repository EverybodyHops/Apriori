import pandas as pd
import copy

class Apriori:
    def __init__(self, _file, _support=0.05, _confidence=0.5):
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
                if t in self.frequence[0]:
                    self.frequence[0][t] += 1
                else:
                    self.frequence[0][t] = 1
            now_data.sort()
            self.data.append(now_data)
        
        for key in list(self.frequence[0].keys()):
            if self.frequence[0][key] / self.record_num < self.support:
                self.frequence[0].pop(key)

    def dfs_record(self, record_index, depth):
        def dfs(record, now, depth, temp, ret):
            if depth == 0:
                ret.append(tuple(copy.deepcopy(temp)))
                # print(ret)
            else:
                for i in range(now, len(record)):
                    temp.append(record[i])
                    dfs(record, i + 1, depth - 1, temp, ret)
                    temp.pop()
        ret = []
        # print(len(self.data[record_index]), self.data[record_index])
        dfs(self.data[record_index], 0, depth, [], ret)
        return ret



if __name__ == "__main__":
    apriori = Apriori("groceries.csv")
    # print(apriori.frequence)
    print(len(list(set(apriori.dfs_record(11, 2)))))
