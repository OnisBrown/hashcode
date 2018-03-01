filename = raw_input("type pls: ")
text = open(filename,"r")
lines = sum(1 for line in text)