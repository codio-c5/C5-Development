# get user plaintext
plaintext = raw_input("Input: ")

# write user plaintext to file
f = open("userinput.txt", "w") 
f.write("%s" % plaintext)
f.close
