# pdf-text
Simple script to read a pdf and output to a text file

## Library files
* pdftotext can be installed from the link:  [pdftotext] https://github.com/jalan/pdftotext

## Method followed
* After installing pdftotext module
* Make a new file
* import the module pdftotext
```python
# Load your PDF
with open("test.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# creating a text file
file = open("test.txt", "w")
for page in pdf:
    file.write(page)
file.close()
```