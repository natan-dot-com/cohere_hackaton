import json
import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def diskcache(path, maxsize=None):
    def attr(func):
        nonlocal path
        if not isinstance(path, Path):
            path = Path(path)

        cache = DiskCache(path)
        def _wrapped(*args):
            tup = tuple(args)
            if tup in cache:
                return cache[tup]
            else:
                cache[tup] = func(*args)
                return cache[tup]

        return _wrapped

    return attr

class DiskCache:
    def __init__(self, path: Path, maxsize=None):
        self.path = path
        self.memcache = dict()
        self.maxsize = maxsize

        self.load()
        self.file = open(self.path, "+a")

    def __contains__(self, elem):
        return elem in self.memcache

    def __getitem__(self, elem):
        return self.memcache[elem]

    def __setitem__(self, elem, value):
        self.memcache[elem] = value

        self.file.write(json.dumps({ "key": elem, "value": value }))
        self.file.write("\n")

    def load(self):
        if self.path.exists():
            with open(self.path, "r") as f:
                logger.info(f"loading cache from '{self.path}'")
                for line in f.readlines():
                    entry = json.loads(line)
                    self.memcache[tuple(entry["key"])] = entry["value"]
        else:
            os.makedirs(self.path.parent)
