from brownie import SooToken, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(100, "ether")
#100 SOO tokens minted
# To override the decimal places, refer to
# https://docs.openzeppelin.com/contracts/4.x/erc20#a-note-on-decimals

def deploy_token():
    account = get_account()
    soo_token = SooToken.deploy(INITIAL_SUPPLY, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify", False))
    print(f"SooToken minted at {soo_token.address}")
    return soo_token

def main():
    deploy_token()