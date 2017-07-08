#!/usr/bin/env python
from glob import glob
import json


def main(**kwargs):
    for fname in glob('coin/*.json'):
        coin = json.load(open(fname))
        missing = []
        for key, val in coin.items():
            if val == "?" or val == []:
                missing.append((key, val))
        if missing:
            print('File: %s' % fname)
            for key, val in missing:
                print(' * %s: %s' % (key, val))


if __name__ == '__main__':
    main()
