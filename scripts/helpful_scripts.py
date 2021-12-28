from brownie import accounts, network, config

# no need to mock pricefeed contract address since it's forked from mainnet
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"] 
# if local blockchain, we need to mock the pricefeed contract
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]



def get_account(index=None, id=None):
    # accounts[0] from brownie accounts
    # accounts.add("env") from env variable
    # accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    # using metamask wallet, private key added to .env file and referenced in brownie-config
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    return None



