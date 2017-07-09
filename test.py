"""
To run tests you need to install pytest
"""
from glob import glob
import os
import re
import json
from jsonschema import validate

TEMPLATE_KEYS = json.load(open('coin_schema.json'))['required']

def test_coin_names():
    re_coin_fname = re.compile(r'^[a-z0-9][a-z0-9_]+[a-z0-9]\.json$', re.I)
    for fname in os.listdir('coin'):
        if not re_coin_fname.match(fname):
            assert False, '%s is invalid coin filename' % fname


def test_coin_template_keys():
    tpl = json.load(open('coin_template.json'))
    assert set(tpl.keys()) == set(TEMPLATE_KEYS)


def test_coins_keys():
    for fname in glob('coin/*.json'):
        coin = json.load(open(fname))
        assert set(coin.keys()) == set(TEMPLATE_KEYS)


def test_coins_readme_link():
    for fname in glob('coin/*.json'):
        name = fname.split('/')[1].split('.')[0]
        content = open('README.rst').read()
        assert '<coin/%s.json>' % name in content


def test_validate_with_schema():
    schema = json.load(open('coin_schema.json'))
    for fname in glob('coin/*.json'):
        coin = json.load(open(fname))
        validate(coin, schema)
