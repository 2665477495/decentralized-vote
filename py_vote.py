from web3 import Web3

# 连接到以太坊网络（使用Infura节点）
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# 智能合约地址和ABI
contract_address = '0xContractAddress'  # 替换为您的智能合约地址
contract_abi = [{'constant': True, 'inputs': [], 'name': 'candidatesCount', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {'constant': False, 'inputs': [{'name': '_name', 'type': 'string'}], 'na...

# 加载智能合约
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# 注册选民
def register_voter(voter_address):
    # 设置默认账户
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # 调用智能合约方法
    tx_hash = contract.functions.registerVoter(voter_address).transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt.status:
        print('Voter registered successfully!')
    else:
        print('Failed to register voter.')

# 投票
def vote(candidate_index):
    # 设置默认账户
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # 调用智能合约方法
    tx_hash = contract.functions.vote(candidate_index).transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt.status:
        print('Vote submitted successfully!')
    else:
        print('Failed to submit vote.')

# 获取候选人数和得票数
def get_results():
    candidates_count = contract.functions.candidatesCount().call()
    for i in range(candidates_count):
        vote_count = contract.functions.getCandidateVoteCount(i).call()
        print('Candidate', i, 'Votes:', vote_count)

# 使用示例
voter_address = '0xVoterAddress'  # 替换为选民地址
candidate_index = 0  # 替换为候选人索引

register_voter(voter_address)
vote(candidate_index)
get_results()
