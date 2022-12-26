
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
#generating private key using rsa 
#make function to sign the message 
#make a verification function => uses pu , sign , message
def gneratekeys():
   private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,
   ) 

   public_key = private_key.public_key()
   return private_key,public_key

def sign(message,private_key):
   message=bytes(message,'utf-8')
   signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
  )
   return signature

def verify(signature,message,public_key):

 try:
  message=bytes(message,'utf-8')
  public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
  )
  print("The message is Verified ")
 except:
   print("The message does no match")
    
if __name__=="__main__":
   pr,pu=gneratekeys()
   # print(pr,pu)
   message="Think of this message as a transaction message"
   incorrectMessage = "this is not the correct meesage"
   signature =sign(message,pr)
   verify(signature,message,pu)
   
