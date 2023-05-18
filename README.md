# VotingSystem Smart Contract: decentralized-vote 🗳️

This is a smart contract written in Solidity for a simple voting system. It allows users to register as voters, vote for candidates, and retrieve voting results. The contract is designed to ensure transparency and security in the voting process.

## Features ✨

- Registration: Voters can register their addresses to participate in the voting. 📝
- Voting: Registered voters can cast their votes for a specific candidate. 🗳️
- Results: The contract provides functions to retrieve the vote count for each candidate. 📊

## Requirements 📋

- Solidity ^0.8.0
- OpenZeppelin SafeMath library

## Getting Started 🚀

Follow the steps below to deploy and interact with the smart contract:

1. Install Solidity compiler and OpenZeppelin library.
2. Deploy the `VotingSystem` contract to an Ethereum network of your choice, providing an array of candidate names and the duration of the voting period.
3. Register voters using the `registerVoter` function.
4. Allow registered voters to cast their votes using the `vote` function, providing the index of the candidate they want to vote for.
5. Retrieve the vote count for each candidate using the `getCandidateVoteCount` function.

## Interacting with the Smart Contract using Python and Web3 🐍

The following example demonstrates how to interact with the smart contract using Python and the Web3 library:

```python
from web3 import Web3

# Connect to the Ethereum network (using Infura node)
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Smart contract address and ABI
contract_address = '0xContractAddress'  # Replace with your smart contract address
contract_abi = [{'constant': True, 'inputs': [], 'name': 'candidatesCount', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_name', 'type': 'string'}], 'na...

# Load the smart contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Register a voter
def register_voter(voter_address):
    # Set the default account
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # Call the smart contract method
    tx_hash = contract.functions.registerVoter(voter_address).transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt.status:
        print('Voter registered successfully!')
    else:
        print('Failed to register voter.')

# Vote
def vote(candidate_index):
    # Set the default account
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # Call the smart contract method
    tx_hash = contract.functions.vote(candidate_index).transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt.status:
        print('Vote submitted successfully!')
    else:
        print('Failed to submit vote.')

# Get candidate count and vote count
def get_results():
    candidates_count = contract.functions.candidatesCount().call()
    for i in range(candidates_count):
        vote_count = contract.functions.getCandidateVoteCount(i).call()
        print('Candidate', i, 'Votes:', vote_count)

# Example usage
voter_address = '0xVoterAddress'  # Replace with the voter's address
candidate_index = 0  # Replace with the candidate index

register_voter(voter_address)


vote(candidate_index)
get_results()
```

## Contract Details 📝

Refer to the main section for detailed information about the smart contract's structs, storage, functions, and modifiers.

## License 📄

This smart contract is released under the MIT License. 📜
