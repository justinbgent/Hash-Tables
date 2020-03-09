# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        #hash(key) % self.capacity
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        else:
            linkedPair = self.storage[index]
            # code isn't fully dry, if statement appears twice. Statement enables overriding past LinkedPairs
            if linkedPair.key == key:
                linkedPair.value = value
                return
            # goes to the last link to prepare to add next value
            while linkedPair.next:
                linkedPair = linkedPair.next
                if linkedPair.key == key:
                    linkedPair.value = value
                    return
            linkedPair.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        linkedPair = self.storage[index]
        if linkedPair:
            previous = None
            while True:
                if linkedPair.key == key:
                    # Now I found the value that needs to be removed
                    if previous:
                        previous.next = linkedPair.next
                        linkedPair = None # linkedPair not the first item in list
                        break
                    elif self.storage[index].next:
                        self.storage[index] = self.storage[index].next # linkedPair first item in list
                        break
                    else:
                        self.storage[index] = None # linkedPair has no next or previous (only item stored in index)
                        break
                else:
                    if linkedPair.next == None:
                        print("Warning: Key Not Found")
                        break
                    previous = linkedPair
                    linkedPair = linkedPair.next
        else:
            print("Warning: Key Not Found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        linkedPair = self.storage[index]
        if linkedPair:
            while True:
                if linkedPair.key == key:
                    return linkedPair.value
                else:
                    if linkedPair.next:
                        linkedPair = linkedPair.next
                    else:
                        return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        newStorage = [None] * self.capacity
        oldStorage = self.storage
        self.storage = newStorage

        for i in oldStorage:
            if i:
                self.insert(i.key, i.value)
                linkedPair = i
                while linkedPair.next:
                    linkedPair = linkedPair.next
                    self.insert(linkedPair.key, linkedPair.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
