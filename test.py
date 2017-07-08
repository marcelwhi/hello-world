"""
To run tests you need to install pytest
"""
from glob import glob
import os
import re
import json

TEMPLATE_KEYS = [
    'name',
    'symbol',
    'website',
    'explorer',
    'message_board',
    'max_supply',
    'twitter',
    'reddit',
    'repo',
    'genesis_block_date',
    'proof_type',
    'hash_algo',
    'block_time',
    'block_size',
    'block_reward',
    'anonymous',
    'whitepaper',
    'tx_per_second',
    'core_lang',
    'masternode',
    'masternode_supply',
    'smart_contracts',
    'lightning_network',
]

def test_coin_names():
    re_coin_fname = re.compile(r'^[a-z0-9][a-z0-9_]+[a-z0-9]\.json$', re.I)
    for fname in os.listdir('coin'):
        if not re_coin_fname.match(fname):
            assert False, '%s is invalid coin filename' % fname


def test_coin_template_keys():
    tpl = json.load(open('coin_template.json'))
    assert set(tpl.keys()) == set(TEMPLATE_KEYS)


def test_coins_keys():
    re_extra_key = re.compile(
        '^(website|explorer|message_board)([2-9]|\d{2,})$'
    )
    for fname in glob('coin/*.json'):
        coin = json.load(open(fname))
        keys = [x for x in coin.keys() if not re_extra_key.match(x)]
        assert set(keys) == set(TEMPLATE_KEYS)


def test_coins_readme_link():
    for fname in glob('coin/*.json'):
        name = fname.split('/')[1].split('.')[0]
        content = open('README.rst').read()
        assert '<coin/%s.json>' % name in content
