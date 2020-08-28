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
