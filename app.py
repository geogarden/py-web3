from web3 import Web3
print ("Czy jestem połączeny do sieci :")
infura_url = "https://mainnet.infura.io/v3/18bd591f8eab4e13b814bb7edb464c96"
web3 = Web3(Web3.HTTPProvider(infura_url))
print (web3.isConnected())
print ("Aktualny numer bloku :  ", (web3.eth.blockNumber))
balance = web3.eth.getBalance("0xd35F56CF93c38F51f735144F5f26D937C8EB7ce9")
print (web3.fromWei(balance, "ether"))
