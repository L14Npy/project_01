import json

MAX = 2**63 - 1

class Dataframe():
    data: dict
    def __init__(self, data: list| dict | None = None):
        self.data = self._construct_data(data)
        
    
    def _construct_data(self, data: list| dict | None = None) -> dict:
        _data = {}
        if isinstance(data, (tuple,list)):
            for i,d in enumerate(data):
                if isinstance(d, dict):
                    for k,v in d.items():
                        if _data.get(k) is None:
                            _data[k] = []
                        _data[k].append(v)
                else:
                    _data.setdefault("data", []).append(d)

        elif isinstance(data, dict):
            for k,v in data.items():
                _data[k] = v if isinstance(v, list) else [v]
        elif data is not None:
            _data = dict(data)
        return _data

    def __str__(self) -> str:
        return self.get_table()
    
    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]

    def get_table(self, *, column_limit:int | None = None, max_row:int | None = None) -> str:
        if not len(self.data): return type(self)
        if not column_limit: column_limit = MAX
        if not max_row: max_row = MAX
        spcs = {
            k: min(max(max(len(str(x)) for x in v), len(k)), column_limit)
            for k, v in self.data.items()
        }

        index_w = len(str(max(len(v) for v in self.data.values())))
        header = f"{'':<{index_w}} | " + " | ".join(
            f"{str(k)[:column_limit]:<{spcs[k]}}" for k in self.data.keys()
        )

        max_rows = min(max(len(v) for v in self.data.values()), max_row)

        rows = []
        for row_idx in range(max_rows):
            row = [f"{row_idx:<{index_w}}"]
            for col_idx, k in enumerate(self.data.keys()):
                values = self.data[k]
                if row_idx < len(values):
                    val = values[row_idx]
                    if isinstance(val, (int, str, float)):
                        row.append(f"{str(val)[:column_limit]:<{spcs[k]}}")
                    else:
                        row.append(f"{str(type(val))[:column_limit]:<{spcs[k]}}")
                else:
                    row.append("None".ljust(spcs[k]))
            rows.append(" | ".join(row))

        return header + "\n" + "\n".join(rows)

    def to_json(self, path: str, func:callable, **kwargs):
        data = func(self.data) if func else self.data
        with open(path, "w", encoding='utf-8') as f:
            json.dump(data, f, **kwargs)

    @classmethod
    def from_json(cls, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls(data)

    def max(self, key: str) -> int:
        return max(self.data[key])
    
    def add(self, df):
        if not isinstance(df, Dataframe):
            df = Dataframe(df)
        for k,v in df.data.items():
            if self.data.get(k) is None:
                self.data[k] = []
            self.data[k].extend(v)
    
    def len(self):
        return len(self.data) + 1
    
    def counts(self, key):
        result = {}
        for v in self.data[key]:
            result[v] = result.get(v, 0) + 1
        return result

    def sort(self, key: str, reverse: bool = False):
        sorted_idx = sorted(range(len(self.data[key])), key=lambda i: self.data[key][i], reverse=reverse)

        for k in self.data.keys():
            self.data[k] = [self.data[k][i] for i in sorted_idx]

        return self

    def group_by(self, key: str, value: str, as_new_row: str | None = None) -> dict:
        result = {}
        for k, v in zip(self.data[key], self.data[value]):
            result.setdefault(k, []).append(v)

        if as_new_row:
            return Dataframe({
                key: list(result.keys()),
                as_new_row: list(result.values())
            })
        return result
    
    def mean(self, key: str) -> float:
        values = self.data[key]
        return sum(values) / len(values) if values else 0

    def flatify(self, key: str, columns: list[str]):
        res = {col: [] for col in columns}

        for row in self.data[key]:
            for elem in row:
                for col in columns:
                    res[col].append(elem.get(col))

        return Dataframe(res)

    def apply(self, func:callable):
        self.data = func(self.data)
        return self

    def group_apply(self, key: str, value: str, func: callable, as_new_row: str | None = None) -> dict:
        grouped = {}
        for k, v in zip(self.data[key], self.data[value]):
            grouped.setdefault(k, []).append(v)

        result = {k: func(vals) for k, vals in grouped.items()}

        if as_new_row:
            return Dataframe({
                key: list(result.keys()),
                as_new_row: list(result.values())
            })
        return result

    
    def explode(self, key: str, parent_keys: list[str] = None, columns: list[str] = None):
        parent_keys = parent_keys or []
        columns = columns or []

        res = {k: [] for k in parent_keys + columns}

        for idx in range(len(self.data[key])):
            nested_list = self.data[key][idx]
            parent_vals = {k: self.data[k][idx] for k in parent_keys}
            for elem in nested_list:
                for k in parent_keys:
                    res[k].append(parent_vals[k])
                for col in columns:
                    res[col].append(elem.get(col))

        return Dataframe(res)

    def filter(self, predicate: callable):
        rows = [
            {col: self.data[col][i] for col in self.data}
            for i in range(len(next(iter(self.data.values()))))
        ]

        filtered_rows = [row for row in rows if predicate(row)]

        res = {col: [row[col] for row in filtered_rows] for col in self.data}
        return Dataframe(res)


    def add_col(self, **kwargs):
        for k,v in kwargs.items():
            self.data[k] = list(v)
        return self
    
    def del_col(self, *args):
        for k in args:
            del self.data[k]
        return self
       
if __name__ == "__main__":
    #df = Dataframe([{"todo": 1, "ASCO": 20}, {"todo": 2, "ASCO": 30}, {"todo": 5, "ASCO": 2000}])
    #df1 = Dataframe([[1,2], [2,3], [3,4], [4,5]])
    #print(df1)
    data = Dataframe.from_json("data/mipymes.json")
    dat = []
    for d in data["products"]:
        for v in d:
            dat.append(v["category"])
    daf = Dataframe(dat)
    daf = daf.new_col("cantidad", [daf.counts("data")[v] for v in daf["data"]])
    print(daf, sep="\n")