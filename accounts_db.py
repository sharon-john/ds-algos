'''
[{"John", ["sharonjohn@ucla.edu", "sharonjohns.g.ucla.edu"]}, {"John", ["sharonjohn@gmail.com"]}, {"Dinkar", ["dinkarkhattar@gmail.com"]}, {"Dinkar", ["dinkarkhattar@ucla.edu"]}]

'''

class Accounts:
	def __init__(self, fname, emails):
		self.fname = fname 
		self.emails = emails 

def emailChecker(email_list, prev_seen_emails):
	new_unique_emails = []			#list of new emails we will return 
	for email in email_list:		
		if email not in prev_seen_emails: 
			new_unique_emails.append(email)
	return new_unique_emails  

def uniqueEmails(account_list):
	accounts_db = dict() 
	haveSeenBefore = set()
	unique_emails = []
	for account in account_list:
		if account.fname not in accounts_db:
			accounts_db[account.fname] = [ ]
			unique_emails = emailChecker(account.emails, haveSeenBefore)
			for item in unique_emails:
				accounts_db[account.fname].append(item)
				haveSeenBefore.add(item)

		else:
			unique_emails = emailChecker(account.emails, haveSeenBefore)
			for item in unique_emails:
				accounts_db[account.fname].append(item)
				haveSeenBefore.add(item)

	return accounts_db

Account1 = Accounts("John", ["sharonjohn@ucla.edu", "sharonjohn@g.ucla.edu"] )
Account2 = Accounts("John", ["sharonjohn@gmail.com", "sharonjohn@g.ucla.edu"])
Account3 = Accounts("Dinkar", ["dinkarkhattar@gmail.com"] )
Account4 = Accounts("Dinkar", ["dinkarkhattar@ucla.edu","dinkarkhattar@gmail.com"] )
Account5 = Accounts("Sheba", ["sheba@gmail.com", "sheba@stanford.edu", "sheba@mit.edu"])
Account6=  Accounts("Sheba", ["sheba@stanford.edu"])

accounts_list = [Account1, Account2, Account3, Account4, Account5, Account6]

print (uniqueEmails(accounts_list))









