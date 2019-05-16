#!/usr/bin/env python

'''

Approach: X, x@gmail.com, x@yahoo.com; X, x@yahoo.com, x@ucla.edu, 

[{x,[x@gmail.com, x@yahoo.com, x@ucla.edu]}, ...... }] 

store fname: [ list of email ] key-value pairs. 
We want a list of previously seen emails. We would wanna do O(1) lookup here. We could use a set() in Python 

iterate through the accounts list, when we see a new name, create an entry in our 
accounts database if it doesn't already exist. 

If it does exist, check if the email is already present in the PreviouslySeenEmails data store 
If it's there, we don't add this to our account database, if it isn't there, we append it to the 
fname -> list of vals. 

All entries come with fname, emails. Some emails might be empty. 

Not optimizing for space complexity. 

'''

class Accounts:
	def __init__(self, fname, emails):
		self.fname = fname 
		self.emails = emails 

def accountProcessing(accounts_list):
	accounts_db = dict()
	allEmails = set()

	for account in accounts_list:				#O(N) assuming accounts_list has N elements  
		if account.fname not in accounts_db:	
			accounts_db[account.fname] = [ ]	

		for email in account.emails:			#O(m) to iterate through the total emails for a given account 
			if email not in allEmails:
				allEmails.add(email)
				accounts_db[account.fname].append(email)   #O(1) amortized 

	return accounts_db

''' 
N >>> m. i.e total number of accounts always much greater than number of emails associated with any one account 

time complexity: O(N*m)

'''

Account1 = Accounts("John", ["sharonjohn@ucla.edu", "sharonjohn@g.ucla.edu"] )
Account2 = Accounts("John", ["sharonjohn@gmail.com", "sharonjohn@g.ucla.edu"])
Account3 = Accounts("Dinkar", ["dinkarkhattar@gmail.com"] )
Account4 = Accounts("Dinkar", ["dinkarkhattar@ucla.edu","dinkarkhattar@gmail.com"] )
Account5 = Accounts("Sheba", ["sheba@gmail.com", "sheba@stanford.edu", "sheba@mit.edu"])
Account6=  Accounts("Sheba", ["sheba@stanford.edu"])

accounts_list = [Account1, Account2, Account3, Account4, Account5, Account6]

print (accountProcessing(accounts_list))





