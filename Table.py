class Table:
    def __init__(self, columns):
        self.columns = columns
        self.data = {column: [] for column in columns}

    def insert(self, values):
        for column, value in zip(self.columns, values):
            self.data[column].append(value)
    
    def delete(self, condition=None):
        if not any(self.data.values()):
            return
        
        indices_to_delete = []
        for i in range(len(next(iter(self.data.values())))):
            if condition and condition(self.data, i):
                indices_to_delete.append(i)

        for column in self.columns:
            self.data[column] = [val for idx, val in enumerate(self.data[column]) if idx not in indices_to_delete]

    def select(self, selected_columns="*", condition=None):
        if selected_columns == "*":
            selected_columns = self.columns
        
        result = [] 
        if not any(self.data.values()):
            return result
        
        for i in range(len(next(iter(self.data.values())))):
            row = [self.data[col][i] for col in selected_columns if col in self.data]
            if condition and not condition(self.data, i):
                continue
            result.append(tuple(row)) 
        
        return result  

