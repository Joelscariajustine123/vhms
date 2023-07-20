from web3 import Web3, HTTPProvider
from web3.contract import Contract


def connect_to_ethereum():
    infura_url = 'https://linea-goerli.infura.io/v3/7a114a387c914ca2a47357118f63e4fb'
    web3 = Web3(HTTPProvider(infura_url))
    return web3
