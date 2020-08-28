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
  
