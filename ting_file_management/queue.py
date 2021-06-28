class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        file = self._data[0]
        self._data.pop(0)
        return file

    def search(self, index):
        if(self._data[index] and index >= 0):
            return self._data[index]
        else:
            raise IndexError
