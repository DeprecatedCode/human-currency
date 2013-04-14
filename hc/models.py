# Human Currency
import random
import string
chars = string.letters + string.digits + \
        string.letters + string.digits + \
        string.letters + string.digits

class Node(object):
    """Node contains multiple accounts."""
    
    network = {}
    
    def __init__(self, id):
        """Initialize the Node."""
        self.id = id
        self.__class__.network[id] = self
        self.accepted_coins = {}
        self.accounts = {}

    def get_account(self, id):
        """Get an account instance at this node."""
        if not id in self.accounts:
            self.accounts[id] = Account(id=id, node=self)
        return self.accounts[id]
        
    def __repr__(self):
        c = len(self.accounts)
        return "<Node hc.{} containing {} account{}>".format(
            self.id, c, 's' if c != 1 else ''
        )


class Account(object):
    """Account contains multple coins"""
    
    def __init__(self, id, node):
        """Initialize the Account"""
        self.id = id
        self.node = node
        self.coins = {}
        
    def mint(self, hc=0, uhc=0):
        """Generate a new, unapproved coin."""
        coin = Coin(node=self.node, account=self, hc=hc, uhc=uhc)
        self.coins[coin.id] = coin
        return coin
        
    @property
    def value(self):
        return sum([c.value for c in self.coins.values()])
        
    def __repr__(self):
        c = len(self.coins)
        return "<Account hc.{}.{} containing {} coin{} totaling hc{}>".format(
            self.node.id, self.id, c, 's' if c != 1 else '', self.value
        )
        

class Coin(object):
    """Coin contains an amount of HC."""
    
    def __init__(self, node, account, hc=0, uhc=0):
        self.node = node
        self.account = account
        self.hc = hc
        self.uhc = uhc
        self.id = "".join(random.sample(chars, 50))
        self.approvals = {}
        
    def approve(self):
        for key in Node.network:
            pass
        
    @property
    def value(self):
        return float(self.hc) + float(self.uhc) / 1e6
        
    @property
    def confidence(self):
        nsize = len(Node.network)
        return float(len(self.approvals)) / nzise if nzise else 0.0
        
    def __repr__(self):
        return "<Coin hc.{}.{}.{} worth hc{}>".format(
            self.node.id, self.account.id, self.id, self.value
        )