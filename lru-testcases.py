from lru_cache import lru_cache
def main():
    cache = lru_cache(6)
    cache.put(0,10)
    cache.put(1,15)
    cache.put(2,16)
    # cache.put(3,18)
    assert cache.get_cache() == {0:10,1:15,2:16}
    assert cache.get(1) == 15
    assert cache.get(12) == 0
    cache.put(4,18)
    cache.put(5,19)
    cache.put(7,20)
    assert cache.get_cache() == {0:10,1:15,2:16,4:18,5:19,7:20}
    assert cache.get(5) == 19
    assert cache.get(8) == 0
    print("All Test Cases Passed")

if __name__ == '__main__':
    main()

