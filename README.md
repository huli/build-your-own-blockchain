### Tutorials and Notes to 'Blockchain A-Z - Learn how to build your first blockchain' (Udemy)
---

*These are just my personal comments for later refreshing. I can highly recommend taking the course if you are interested in the topic.*

### Blockchain Intuition

#### What is a Blockchain?
*A blockchain is a continuously growing list of records, called blocks, which are linked and secured using cryptography. \
(Wikipedia)*

* Origin: Paper 'How to Time-Stamp a Digital Document (1991)'
* Block
    * Data: "Hello World!"
    * Prev. Hash: 034DFA357
    * Hash:       4D56E1F05
* Genesis Block (First block)
* Blocks are linked like linked lists (Prev. Hash is pointer to previous block)

![alt text](images/blockchain.png "the concept of a blockchain")
*© SuperDataScience*

#### Understanding SHA256-Hash

* Comes from the NSA
* One of the core principle of the blockchain
* 64 characters
* 64 chars * 4 bits = 256 bits
* https://tools.superdatascience.com/blockchain/hash
* The 5 requirements for hash algorithms:
    * One-Way
    * Deterministic
    * Fast computation
    * The Avalanche Effect
        * Input changes slightly -> output changes significantly
    * Must withstand collision
        * Pigeonhole principle

#### Immutable Ledger

* Traditional ledgers where written
* Immutable ledger -> blockchain
* If you could hack one block, every following block is invalid and would have to be hacked as well because of the cryptographic link -> not possible

Interesting reading: https://medium.com/cryptoeconomics-australia/the-blockchain-economy-a-beginners-guide-to-institutional-cryptoeconomics-64bf2f2beec4

#### Distributed P2P Network

![alt text](images/p2p_networks.png "tampering a single blockchain")
*© SuperDataScience*

* The consensus determines whoose chain is valid
* If your local chain is considered invalid by the consensus it gets replaced

How to hack into a blockchain:
* Exchange data block
* Recompute current hash
* Recompute all following hash
* Deploy this change on the majority of peers at the same time


#### How Mining Works: The Nonce

* Its (mining) all about the nonce
* One block can contain multiple transactions

![alt text](images/the_nonce.png "the nonce")
*© SuperDataScience*


#### How Mining Works: The Cryptographic Puzzle

SHA256-Hash: 6ac3c336e4094835293a3fed8a4b5fedde1b5e2626d9838fed50693bba00af0e\
As decimal number: 48291044447847787216835688875138221669503123235521482818857727304311439929102

* Finding the hash (the Golden Nonce) is called the cryptographic puzzle
* How it works:
    * Keep iterating the nonce until you get below the target
    * Add the block
    * Whole things starts over

![alt text](images/the_puzzle.png "Finding the golden nonce")
*© SuperDataScience*

#### Byzantine Fault Tolerance

![alt text](images/byzantine_fault_tolerance.png "The byzantine fault tolerance")
*© SuperDataScience*

* No more than 1/3 of the participants must be traitors
* The byzantine general problem: https://people.eecs.berkeley.edu/~luca/cs174/byzantine.pdf


#### Consensus Protocol

* Cryptographic puzzle: hard to solve - easy to verify
* *The longest chain is king*
* In a blockchain you only need > 50% for consensus

![alt text](images/consensus.png "The consensus protocol")
*© SuperDataScience*

*A short guide for the consensus protocols:* 
*https://www.coindesk.com/short-guide-blockchain-consensus-protocols*  
*Try it out:*
*https://tools.superdatascience.com/blockchain/coinbase*

