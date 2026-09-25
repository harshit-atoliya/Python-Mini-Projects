import hashlib

# Calculate a SHA-1 hash for each file so their contents can be compared.
try:
    def hash_file(filename1,filename2):
        h1=hashlib.sha1()
        h2=hashlib.sha1()

        with open(filename1,'rb') as f:
                chunk=0
                while chunk !=b'':
                    chunk=f.read(1024)
                    h1.update(chunk)
        with open(filename2,'rb') as f:
                chunk=0

                while chunk !=b'':
                    chunk=f.read(1024)
                    h2.update(chunk)
                return h1.hexdigest(),h2.hexdigest()

    # Compare the two sample files in this project folder.
    msg1,msg2=hash_file('text.txt','text1.txt')
    if msg1!=msg2:
        print("Files are not identical")
    else:
        print("Files are identical")    
except FileNotFoundError:
    # Show a helpful message when either file cannot be opened.
        print("Please enter valid files locations!")