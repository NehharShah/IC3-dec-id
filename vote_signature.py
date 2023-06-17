from web3.auto import w3

# Private key
# private_key = '0x222a55949038a9610f50fb23b5883af3b4ecb3c3bb792cbcefbd1542c692be01'

def gen_key() -> (str, str):
    # Generate a private key
    acct = w3.eth.account.create()
    private_key = acct._private_key.hex()

    # Generate an Ethereum address
    acct_address = acct.address

    return private_key, acct_address

def sign_vote(vote: int, private_key: str) -> str:
    # Convert the integer to bytes
    option_bytes = vote.to_bytes(32, byteorder='big')

    # Create a hash of the message
    hash_message = w3.solidity_keccak(['bytes32'], [option_bytes])

    # Sign the hashed message
    signed_message = w3.eth.account.signHash(hash_message, private_key=private_key)

    signature = signed_message.signature.hex()

    return signature
