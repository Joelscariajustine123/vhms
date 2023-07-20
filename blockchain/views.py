# from django.http import JsonResponse
# from .utils import create_block, get_latest_block, is_chain_valid


# from vhmsapp.models import Animal

# def add_medical_record(request):
#     # Retrieve and validate data from the request
#     index = request.POST.get('index')
#     timestamp = request.POST.get('timestamp')
#     data = request.POST.get('data')
#     previous_hash = request.POST.get('previous_hash')
#     animal_id = request.POST.get('animal_id')

#     # Retrieve the animal object
#     animal = Animal.objects.get(id=animal_id)

#     # Create a new block and link it to the animal
#     block = create_block(index, timestamp, data, previous_hash, animal)
#     return JsonResponse({'block_created': True})

# def validate_chain(request):
#     is_valid = is_chain_valid()
#     return JsonResponse({'is_valid': is_valid})

# from vhmsapp.models import Animal

# def get_blockchain(request):
#     blockchain = list(Block.objects.order_by('index').values())
#     blockchain_with_animal_data = []

#     for block in blockchain:
#         animal_id = block['animal_id']
#         if animal_id:
#             animal = Animal.objects.get(id=animal_id)
#             block['animal_data'] = {
#                 'id': animal.id,
#                 'name': animal.name,
#                 # Add more animal fields as needed
#             }
#         else:
#             block['animal_data'] = None

#         blockchain_with_animal_data.append(block)

#     return JsonResponse({'blockchain': blockchain_with_animal_data})







from django.shortcuts import render
import datetime
import hashlib
import json
from django.http import JsonResponse


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0')

    def create_block(self, nonce, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True


# Creating our Blockchain
blockchain = Blockchain()

# Mining a new block
def mine_block(request):
    if request.method == 'GET':
        previous_block = blockchain.get_previous_block()
        previous_nonce = previous_block['nonce']
        nonce = blockchain.proof_of_work(previous_nonce)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(nonce, previous_hash)
        response = {'message': 'Congratulations, you just mined a block!',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'nonce': block['nonce'],
                    'previous_hash': block['previous_hash']}
    return JsonResponse(response)

# Getting the full Blockchain
def get_chain(request):
    if request.method == 'GET':
        response = {'chain': blockchain.chain,
                    'length': len(blockchain.chain)}
    return JsonResponse(response)

# Checking if the Blockchain is valid
def is_valid(request):
    if request.method == 'GET':
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response = {'message': 'All good. The Blockchain is valid.'}
        else:
            response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return JsonResponse(response)





