CoinDataBase
============

About project
-------------
Coindatabase is a database of crypto currencies basic properties like market
symbol, website, privacy/scalability/governor features, etc.

Data of each currency are stored in a separate YAML file. Feel free to send
pull requests to change existing coins or add new coins.


How to add new coin
-------------------

Copy `coin_template.yml <coin_template.yml>`_ to coin/ directory and name it
with coin name. Use common coin name, do not lowercase all letters, use
underscore instead of space.

Good names:

* Etherium_Classic.yml
* NEM.yml
* iDice.yml

Bad names:

* Etherium Classic.yml
* etherium_classic.yml
* Nem.yml
* nem.yml
* idice.yml

Edit the new file and fill all coin propertes you know. If you do knot know or
do not understand some properties just put "?" string there. Do not delete
keys, just put "?" string e.g.:

    tx_per_second: "?"

There could be multiple values for keys `website`, `explorer` and
`message_board`. In such case use key with numeric suffix e.g.
`website2`, `website3`, etc. Do not use suffix 1 for first item.
The key `website` is correct, `website1` is incorrect.

The required minimum set of non-blank properties to add new coin is:

* name
* symbol 
* website

Add link to new coin file to README.rst. List of coins are sorted in alphabetic
order.

Conventions
-----------

Numbers could be specified in short form using suffixes K (thousands),
M (millions) and B (billions) e.g. 21M equals to 21000000

For `block_key` property the suffixes are KB (kilobytes) and
MB (megabytes).

For boolean properties like `anonymous` the "yes" and "no" values must be used.

If the property could not be applied to the coin e.g. `masternode_supply` for
Etherium, set the value to "NA".

If the value is unlimited use `Inf` literal e.g.:

    max_supply: Inf


Coins
-----

* `Bitcoin <coin/Bitcoin.yml>`_
* `Ethereum <coin/Ethereum.yml>`_
* `Ripple <coin/Ripple.yml>`_
