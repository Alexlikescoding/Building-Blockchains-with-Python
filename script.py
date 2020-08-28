######################################## script.py ##############################################
transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# add your code below
my_transaction = {
  'amount': '12',
  'sender': 'Lifu',
  'receiver': 'Beina'
}

mempool.append(my_transaction)

block_transactions=[mempool[2],mempool[2],mempool[2]]

########################## import sha256 #####################
from hashlib import sha256
text = 'I am excited to learn about blockchain!'
hash_result = sha256(text.encode())
#print(hash_result)
print(hash_result.hexdigest())

######################################
from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
#my_blockchain.print_blocks()

my_blockchain.chain[1].transactions = 'fake_transactions'

my_blockchain.validate_chain()

############# import sha256 #########
from hashlib import sha256
###### sets the amount of leading zeros that must be found in the hash produced by the nonce #####
difficulty = 2
nonce = 0

############### creating the proof ############## 
string = str(nonce) + str(new_transactions)
proof = sha256(string.encode()).hexdigest()
# printing proof
#print(proof)
  
# finding a proof that has 2 leading zeros
while proof[:2] != '0'*difficulty:
  nonce += 1
  string = str(nonce) + str(new_transactions)
  proof = sha256(string.encode()).hexdigest()
  #print(proof)
final_proof=proof
# printing final proof that was found
print(final_proof)

########################### Blockchain Summary #########################
from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()

