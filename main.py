
from cryptography.hazmat.primitives.asymmetric import rsa

#generating private key using rsa 
def gneratekeys():
   private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,
   ) 

   public_key = private_key.public_key()
   return private_key,public_key



if __name__=="__main__":
   pr,pu=gneratekeys()
   print(pr,pu)