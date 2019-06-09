#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {
                 'index': len(self.chain)+1, 
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash
                 }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]

    def mine_block(self):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        block = self.create_block(proof, previous_hash)
        return block

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_result = self.create_hash_from_proofs(new_proof, previous_proof)
            if hash_result[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def create_hash_from_proofs(self, actual_proof, previous_proof):
        init_string = str(actual_proof**2 - previous_proof**2).encode()
        hash_result = hashlib.sha256(init_string).hexdigest()
        return hash_result
        
    def is_chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_result = self.create_hash_from_proofs(proof, previous_proof)
            if hash_result[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
            
app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block')
def mine_block():
    block = blockchain.mine_block()
    response = {'message': 'Congratulations, you just found the nonce!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200
    

@app.route('/get_chain')
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/is_valid')
def is_valid():
    is_valid = blockchain.is_chain_valid()
    response = {'is_valid': is_valid}
    return jsonify(response), 200

# run the app
app.run(host= '0.0.0.0', port=5000)
            
            
            
            
            
            
            
            
        
        




