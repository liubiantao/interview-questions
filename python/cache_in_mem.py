# -*- coding: utf-8 -*-
"""
补全 cache 函数。实现功能：

把计算过的结果，缓存在 `_cache_db` 中.
第二次调用时，读取缓存中的数据，无需重复执行 add 函数。

--------

如何提交代码

1. 在自己的 GitHub 上创建新的仓库。
2. copy 这个文件到自己的仓库。
3. commit 这个原始文件。
4. 开始 coding
5. commit 最终代码，并 push 到 GitHub
6. 仓库的 URL 发给 HR


Tips:

1. 可以重复 commit 多次，以最终的文件为准。
2. 良好的 commit history 也是 coding 能力的体现。

"""
import hashlib

_cache_db = dict()


def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()


def cache(f):
    # reference:
    #  https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
    # https://wiki.python.org/moin/HowTo/Sorting
    def wrapper(*args):
        key = md5(str(sorted(args)))
        if not key in _cache_db:
            # print(args, key)
            _cache_db[key] = f(*args)
        return _cache_db[key]
    return wrapper


@cache
def add(a, b):
    return a + b


if __name__ == '__main__':
    assert add(3, 4) == 7
    assert add(3, 4) == 7
    assert add(8, 4) == 12
    assert add(4, 8) == 12
    assert add(8, 4) == 12
