from web3 import Web3

def get_web3_provider():
    provider_url = 'http://localhost:8545'  # Replace with your Ethereum node URL
    return Web3(Web3.HTTPProvider(provider_url))

web3 = get_web3_provider()
