#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        It will have to traverse each node at least 1 to append all the keys"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        it will have to traverse at least one to append all the values"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        It will have to traverse at least one to append all the items"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n^2) Why and under what conditions?
        It's quadratic because first it has to traverse all the buckets and
        then traverse all the nodes"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        self.size = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                self.size += 1
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(1) Why and under what conditions?
        In this case it's just assigning and returning so it is constant time"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # TODO: Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None
        # if entry is None:
        #     return False
        # else:
        #     return True

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(1) Why and under what conditions?
        this is also constant because it's assigning and returning"""
        # TODO: Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # TODO: Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # TODO: If found, return value associated with given key
        if entry is not None:
            return entry[1]
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        else: 
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(n) Why and under what conditions?
        this is linear because if there's an entry it has to traverse at least
        one time"""
        #Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # TODO: Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        # entry = (key, value)
        # bucket.append(entry)
        if entry:
            current_node = bucket.head
            while current_node is not None:
                if current_node.data[0] == key:
                    current_node.data = (key, value)
                    break
                current_node = current_node.next
        else:
            bucket.append((key, value))
            self.size += 1
        

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(n) Why and under what conditions?
        this is also constant time because it has to traverse at least one time"""
        # TODO: Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # TODO: Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        current_node = bucket.head
        previous_node = None
        found = False

        while current_node is not None:
            # If the head is the target node
            if bucket.head.data[0] == key: 
                # If the head points to a node 
                if bucket.head.next is not None:
                    # Reassign the head  
                    bucket.head = bucket.head.next  
                    found = True
                    self.size -= 1
                    break
                else:
                    # The list only have one node
                    bucket.head = None  
                    bucket.tail = None
                    found = True
                    self.size = 0
                    break
            # found the target node and the node is not the head
            elif current_node.data[0] == key:
                # Is the tail the targeted node?  
                if current_node == bucket.tail: 
                    previous_node.next = None
                    bucket.tail = previous_node
                    found = True
                    self.size -= 1
                    break

                else:  # The targeted node points to something
                    previous_node.next = current_node.next
                    found = True
                    self.size -= 1
                    break
            else:  # Not the target node
                previous_node = current_node
                current_node = current_node.next

        if not found:
            raise KeyError('Key not found: {}'.format(key))
        


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
