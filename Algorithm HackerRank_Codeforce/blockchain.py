from flask import json, jsonify
from flask.app import Flask
from uuid import uuid4
import hashlib
from time import time
from requests.api import request

class blockchain():
    def __init__(self):
        super().__init__()
        self.chain = []
        self.current_transactions = []

        #create a genesis block
        self.new_block(previous_hash = 1, proof = 100)


    def new_block(self, proof, previous_hash= None):
        #Create new blocks and then adds to the existing chain
        """This method will contain two para proof and previous hash"""
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "proof": proof,
            previous_hash: previous_hash or self.hash(self.chain[-1]),
        }

        #Set the current transaction list to empty
        self.current_transactions = []
        self.chain.append(block)
        return(block)


    def new_transaction(self):
        #Adds new transaction to already existing transactions

        """This will create a new transaction which will be sent to  the next block. It will contain three variables including sender, recipient and amount """
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount,
            }
        )
        return (self.last_block["index"]+1)

    @staticmethod
    def hash(block):
        #used for hasing a block
        """The follow code will create a SHA-256 block has and also ensure that the dictionary is ordered"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        #Call the last block in the chain
        return (self.chain[-1])
        

    def register_node(self):
        #Register a new node and add it to the network
        pass

    @staticmethod
    def valid_proof(self,last_proof,proof):
        #Ensure wheather a submitted block to the chain solves the problem
        guess = f'{last_proof}{proof}'.endcode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4]=="0000"

    def valid_chain(self):
        #check if the subsequent blocks in the chain are valid or not
        pass

    def proof_of_work(self, last_proof):
        """This method is where you the consensus algorithm is implemented""" 
        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof


app = Flask(__name__)
node_identifier = str(uuid4()).replace("-","")

blockchain = blockchain()

@app.route("/mine", methods=["GET"])

def mine():
    return("Mining a new Block")

@app.route('/chain', methods=["GET"])

def full_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route('/transactions/new', methods=["POST"])

def new_transaction():
    values = request.get_json()

    required = ["sender","recipient","amount"]

    if not all(k in values for k in required):
        return("Missing values", 400)

        index = blockchain.new_transaction(values["sender"], values["recipient", values["amount"]])
        response = {"message": f'Transaction is scheduled to be added to Block No.{index}'}

        return jsonify(response),201