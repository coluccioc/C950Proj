# Self resizing Chaining Hash Table
# Stores Key - Value pairs
class ChainHashTable:
    # Constructor with optional capacity
    # Initiates all buckets with an empty list
    def __init__(self, capacity=10):
        self.size = 0
        self.capacity = capacity
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Built-in Hash function, hashes a key
    def hashed(self, key):
        return hash(key) % self.capacity

    # Insert function to add new Key Value pairs
    # Resizes if size/capacity is .8 or greater
    def insert(self, key, item):
        bucket = self.hashed(key)
        bucket_list = self.table[bucket]

        # If key already in table, update item
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # Add new item
        key_value = [key, item]
        bucket_list.append(key_value)
        self.size += 1

        # If Load Factor > .8, we resize to double capacity
        if self.size > self.capacity / 0.8:
            self.resize()
        return True

    # Search function takes a Key as an argument and returns the Value
    def search(self, key):
        bucket = self.hashed(key)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Looks up a key and removes the KV pair if found
    def remove(self, key):
        bucket = self.hashed(key)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
                self.size -= 1

    # Resize function. Called when Load Factor > .8
    # Creates a new empty table, moves all KVs from current table, assigns new table to current
    def resize(self):
        self.capacity *= 2
        newTable = []
        for i in range(self.capacity):
            newTable.append([])
        for bucket in self.table:
            for key, value in bucket:
                bucket = self.hashed(key)
                newTable[bucket].append((key, value))
        self.table = newTable
