from hc.models import Node, Account, Coin

n1 = Node("n1")
n2 = Node("n2")
n3 = Node("n3")
n4 = Node("n4")
n5 = Node("n5")

print ""
print "Created nodes n1..n5"

a1 = n1.account("a1")
a2 = n4.account("a2")

print "Created account a1 on node n1"
print "Created account a2 on node n4"

c1 = a1.mint(hc=100, uhc=0)

c1.approve()  # Should go through fine

f1 = a1.mint(hc=100, uhc=0)

c1.approve()  # Won't work since we already got our free hc100.0

c2, c3 = c1.split(hc=40, uhc=590000)  # We want to spend hc40.59

assert c1.value == 0.0
assert c2.value == 40.59  # This is to spend
assert c3.value == 59.41  # This is our change

c2.approve()  # Should work, as we own this coin
c3.approve()  # Keep our change, this could be done at any later time.

a2.accept(c2)  # Allow another account to claim. Irreversible.

c2 = a2.coin(c2.id)  # Load from a2's perspective

c2.approve()  # Won't work, since we are not the coin owner

c4 = a2.capture(c2)  # Re-claim full ownership (i.e. whole split)

c4.approve()  # Now this will work, and enable this coin to be spent again