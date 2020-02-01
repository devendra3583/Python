#Q. WAP to take a big string as input and extract all emails and ph. no.s from it inside 2 separate lists

def email_phone(s):
	email = []
	phone = []
	return email,phone

if __name__ == "__main__":
	s = "Hello, my email is abc@gmail.com and abc-@gmail.com and abc-def@gmail.com and my phone no is 011-40404040404000000000 and 080-70707070700000000000 and 11-435435435 my my"
	email,phone = email_phone(s) 
	print "Email: {}".format(email)
	print "Phone: {}".format(phone)

