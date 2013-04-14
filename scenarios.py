from hc.models import Node, Account, Coin

n1 = Node("1111")
n2 = Node("2222")
n3 = Node("3333")
n4 = Node("4444")
n5 = Node("5555")

a1 = n1.account("aaaaaaa1")
a2 = n4.account("bbbbbbb2")

c1 = a1.mint(hc=100, uhc=0)

c1.approve()  # Should go through fine

f1 = a1.mint(hc=100, uhc=0)

c1.approve()  # Won't work since we already got our free hc100.0

c2, c3 = c1.split(hc=40, uhc=590000)  # We want to spend hc40.59

assert c3.value == 59.41  # This is our change

c2.approve()  # Should work, as we own this coin
c3.approve()  # Keep our change, this could be done at any later time.

c2.authorize(a2)  # Allow another account to claim. Irreversible.

c2 = a2.coin(c2.id)  # Load from a2's perspective

c2.approve()  # Won't work, since we are not the coin owner

c4 = c2.capture()  # Re-claim full ownership (i.e. whole split)

c4.approve()  # Now this will work, and enable this coin to be spent again