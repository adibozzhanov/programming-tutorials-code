"""
This file describes the code for a single Node in the network.

Assumption is that each node has a copy of the whole blockchain.
"""

import json

from flask import Flask

from blockchain import BlockChain

app = Flask(__name__)
bc = BlockChain()


@app.route('/chain', methods=['GET'])
def get_chain():
    return json.dumps(bc.chain)


app.run(debug=True, port=5000)
