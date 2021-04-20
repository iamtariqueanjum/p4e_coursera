text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
str = text[pos+1: ]
value = float(str)
print(value)
