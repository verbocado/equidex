from flask import Flask, jsonify
from uuid import uuid4

from blockchain import Blockchain


# setup
app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return 'TODO'


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return 'TODO'


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
