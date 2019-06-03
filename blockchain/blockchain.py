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
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            init_string = str(new_proof**2 - previous_proof**2).encode()
            hash_result = hashlib.sha256(init_string).hexdigest()
            if hash_result[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
                
        
        




