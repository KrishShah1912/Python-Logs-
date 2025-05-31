letter = '''Hello Mr <|Name|>
 You are selcected Congratulation!!!
 <|DATE|>'''
print (letter. replace ("<|Name|>" , "KRISH") . replace ("<|DATE|>" , "24th December"))
# here we have chained the .replace like we have 1st replace name with krish , then we have again made change in that krish string like date with 24th dec
