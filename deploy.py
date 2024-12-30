import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
import sys

# testnet URL and private key
bsc_testnet_url = 'https://data-seed-prebsc-1-s1.binance.org:8545/'

private_key=sys.argv[2]

# Initialize web3
web3 = Web3(Web3.HTTPProvider(bsc_testnet_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Ensure the connection is successful
if not web3.is_connected():
    print("Connection failed")
    exit()

# Account from private key
account = web3.eth.account.from_key(private_key)
print(f"Deploying contracts with the account: {account.address}")

# Contract ABI and bytecode

try:
    with open(sys.argv[1] + '.abi', 'r') as file:
        abi = json.load(file)

    with open(sys.argv[1] + '.bin', 'r') as file:
        data = file.readlines()
        bytecode = data[0]

    # Contract deployment
    Contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = web3.eth.get_transaction_count(account.address)
    transaction = {
        'chainId': 97,
        'gasPrice': web3.eth.gas_price,
        'from': account.address,
        'nonce': nonce,
        'gas': 100000
    }

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Transaction hash: {tx_hash.hex()}")

    # Wait for the transaction receipt
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Contract deployed at address: {tx_receipt.contractAddress}")

except FileNotFoundError:
    print(f"Error: The file at file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
