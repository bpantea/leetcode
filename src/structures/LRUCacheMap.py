from unittest import TestCase


class CacheNode:

    def __init__(self, key, value):
        self.next: CacheNode = None
        self.prev: CacheNode = None
        self.key = key
        self.value = value

    def __str__(self) -> str:
        left_key = self.prev.key if self.prev is not None else None
        right_key = self.next.key if self.next is not None else None
        return "{prev: " + str(left_key) + ", next: " + str(right_key) + ", key: " + str(self.key) + "}"


class LRUCacheMap:

    def __init__(self, key_size, fetch_value):
        assert key_size > 0
        self.key_maximum_size = key_size
        self.root: CacheNode = None
        self.last: CacheNode = None
        self.__map = {}
        self.current_size = 0
        self.fetch_value = fetch_value

    def get(self, key):
        if key not in self.__map:
            self.__fetch(key)
            return self.__map[key].value
        else:
            cached = self.__map[key]
            self.__update_hit_for_existing_node(cached)
            return cached.key

    def __fetch(self, key):
        value = self.fetch_value(key)
        new_node = CacheNode(key=key, value=value)
        self.__add_node_to_map(new_node)

    def __evict_root(self):
        evicted = self.root
        self.root = self.root.next
        del self.__map[evicted.key]

    def __update_hit_for_existing_node(self, node: CacheNode):
        if self.last == node:
            return
        self.__remove_node_from_hits(node)
        self.__hit_node(node)

    def __remove_node_from_hits(self, node: CacheNode):
        if node == self.last:
            raise Exception('Last element cannot be removed')
        if self.root == node:
            self.root = node.next
            self.root.prev = None
        else:
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev

    def __add_node_to_map(self, node: CacheNode):
        if self.current_size >= self.key_maximum_size:
            self.__evict_root()
        self.__hit_node(node)
        self.__map[node.key] = node
        self.current_size += 1

    def __hit_node(self, node: CacheNode):
        if self.root is None:
            self.root = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.last.next = None


def fetch_value_for_key(key):
    print('Fetching value for ', key)
    return "value for " + str(key)


class LRUCacheTest(TestCase):
    def test_foo(self):
        cache_map = LRUCacheMap(4, fetch_value_for_key)
        # for i in range(10):
        #     cache_map.get(i)
        cache_map.get(0)
        cache_map.get(1)
        cache_map.get(2)
        cache_map.get(3)
        cache_map.get(0)
        cache_map.get(1)

        print('Here it comes')
        cache_map.get(5)
        cache_map.get(2)
        cache_map.get(0)
        cache_map.get(1)
        cache_map.get(6)


