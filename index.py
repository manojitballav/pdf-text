import pdftotext

# Load your PDF
with open("test.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
    
# get the number of pages
# print(len(pdf))

# creating a text file
file = open("test.txt", "w")
for page in pdf:
    file.write(page)
file.close()
