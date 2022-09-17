
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro=""
x= org.split(" ")
#z = x- stopwords
for b in x:
    if b in stopwords:
        acro= acro +("")
    else:
        acro= acro + b[0]
acro= acro.upper()        
print(acro)