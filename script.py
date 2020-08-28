############################################ test2.py ##########################################
load_file_in_context('script.py')

try:
  my_transaction
except NameError:
  fail_tests("Did you remember to define `my_transaction`?")

if len(mempool) != 7:
  fail_tests("Did you add `my_transaction` to `mempool`?")

if type(mempool[6]) is not dict:
  fail_tests("Looks like the item you added to `mempool` is not of type `dictionary`")

pass_tests()

########################################### test3.py ##########################################
load_file_in_context("block.py")

transaction1 = {
	'test': '30',
  'test2': '35'
}

previous_hash = '0'

current_block = Block(transaction1, previous_hash)

if ('transactions') not in current_block.__dict__:
  fail_tests("An instance of `chain` is not defined inside the `Block` class.")

if ('previous_hash') not in current_block.__dict__:
  fail_tests("An instance of `previous_hash` is not defined inside the `Block` class.")
  
if ('nonce') not in current_block.__dict__:
  fail_tests("An instance of `nonce` is not defined inside the `Block` class.")

if current_block.nonce != 0:
  fail_tests("Please set the `nonce` value to `0` before proceeding.")
  
pass_tests()

########################################### test4.py ##########################################
load_file_in_context("block.py")

transaction = {
  'data': 30,
  'sender': 'alice'
}

curr = Block(transaction, "0")

string = curr.generate_hash()

if str(curr.hash) not in string:
  fail_tests("Oops! It looks like you forgot to uncomment the line that generates the `Block` hash in `__init__()`.")
  
############################################# block.py #########################################
import datetime
from hashlib import sha256

#changed data to transactions

class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash) 
        
############################################ blockchain.py #######################################
#imports the Block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    self.chain.append(new_block)

  def validate_chain(self):
    for i in range(1,len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if current.hash != current.generate_hash():
        return False
      elif previous.hash != previous.generate_hash():
        return False
      else:
        return True
   
  def proof_of_work(self, block, difficulty=2):
    proof = block.generate_hash()
    while proof[:2] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof
      
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

