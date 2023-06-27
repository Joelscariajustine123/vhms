import hashlib
import json
from .models import Block

def calculate_hash(index, timestamp, data, previous_hash):
    value = str(index) + str(timestamp) + str(data) + str(previous_hash)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()






from vhmsapp.models import Animal

def create_block(index, timestamp, data, previous_hash, animal):
    block = Block.objects.create(
        index=index,
        timestamp=timestamp,
        data=data,
        previous_hash=previous_hash,
        current_hash=calculate_hash(index, timestamp, data, previous_hash)
    )
    animal.blockchain_block = block
    animal.save()
    return block





def get_latest_block():
    try:
        return Block.objects.latest('index')
    except Block.DoesNotExist:
        return None

def is_chain_valid():
    blocks = Block.objects.order_by('index')
    previous_hash = '0'

    for block in blocks:
        if block.current_hash != calculate_hash(block.index, block.timestamp, block.data, previous_hash):
            return False
        previous_hash = block.current_hash

    return True
