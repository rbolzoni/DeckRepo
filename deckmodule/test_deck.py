import deckmodule as dck


def test_card():
    a=dck.Card(2, 5)
    assert a.value()==58
    
def test_eq():
    a=dck.Card(1, 13)
    b=dck.Card(1, 13)
    assert a==b
    
def test_decksize():
    a=dck.Deck()
    assert(len(a.cards)==52)
    
def test_deck():
    a=dck.Deck()
    assert(max(b.suit for b in a.cards)==4) #max suit should be 4
    assert(max(b.rank for b in a.cards)==14) #max rank should be 14