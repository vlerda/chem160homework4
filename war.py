from cards import *
ntrials=10000
fractions=[]
for i in range(ntrials):
    adeck=deck()
    ascore=0
    adeck.shuffle()
    
    bdeck=deck()
    bdeck.shuffle
    bscore=0
    
    while adeck.cardsleft()>0:
        acard1=adeck.dealcard()
        bcard1=bdeck.dealcard()
        if acard1.value()<bcard1.value():
            bscore+=2
        if acard1.value()>bcard1.value():
            ascore+=2
        if acard1.value()==bcard1.value():
            ascore+=0
            bscore+=0
    if ascore==bscore:
        fractions.append(ascore-bscore)
    if ascore<bscore:
        fractions.append(bscore-ascore)
    if ascore>bscore:
        fractions.append(ascore-bscore)
for i in range(0,54,2):
    print(i,fractions.count(i)/ntrials)
        
