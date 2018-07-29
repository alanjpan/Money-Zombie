# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 11:49:02 2018

@author: Alan Jerry Pan, CPA, CSc
@affiliation: Shanghai Jiaotong University

Program used for experimental study of (i) international business, specially "money zombies"*, (ii) marketing, specially branding, (iii) information networking through the use of tender, and (iv) information asymmetry in decision making (business) and risk-taking. Can also be modified to study infectious sickness spreads in medicine.

*"Money zombies" are individuals that are susceptible to other individuals' influence due to a significant amount of resources provided to the recipient individual. As the most widely observable scenario, 'money zombies' persistently operate against their home nation's interests in favor of a foreign nation that has provided the 'money zombie' with a significant amount of resources.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Money Zombie [Computer software]. Github repository <https://github.com/alanjpan/Money-Zombie>

Simulated variable values are composites from from Credit Suisse (2017), OECD (2015), PISA (2012), CIA (2011), and World Bank (2011). Blank values are estimated using regression from available values.

Futher expansions may include dynamic field and competition, corporations that expand zombification operations, comparative advantages per nation, a morality and loyalty system, and other detailed expansions.

Note this software's license is GNU GPLv3.
"""

import random
import sys
import time

secure_random = random.SystemRandom()

nationid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nations = ['india', 's korea', 'china', 'japan', 'canada', 'usa', 'uk', 'germany', 'france', 'italy', 'australia', 'other asia', 'other n america', 'other europe', 'other oceania', 'latin america', 'africa']
turnstaken = [1, 4, 5, 4, 4, 4, 3, 3, 2, 3, 3, 4, 4, 5, 5, 4, 5]

npop = 7439583000
wealth = [4987000000000, 6586000000000, 29000000000000, 23682000000000, 7407000000000, 93560000000000, 14073000000000, 13714000000000, 12969000000000, 10853000000000, 7329000000000, 16293000000000, 38000000000, 28030000000000, 1162000000000, 8107000000000, 2499000000000]
totalpop = [1334860000, 51635000, 1393160000, 126490000, 37176000, 327550000, 66040000, 82741000, 67272000, 60484000, 25010000, 1530000000, 211297000, 472312000, 14891000, 422535000, 1216130000]
zombiepop = [133486, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zombify = [3735, 127546, 20815, 187224, 199238, 285635, 213097, 165746, 192784, 179435, 293039, 10648, 180, 59346, 78035, 19186, 2054]
GINI = [.351, .295, .422, .379, .318, .391, .351, .293, .295, .333, .337, .364, .341, .466, .505, .381, .346]
PISA = [.100, .701, .707, .672, .666, .609, .562, .610, .635, .604, .630, .300, .400, .200, .100, .300, .400]

popularsupport = .999
electionswon = 1

def init():
    global wealth
    global totalpop
    global zombify
    global zombiepop
    global popularsupport
    global turns
    global electionswon
    
    turns = 1
    popularsupport = .999
    electionswon = 1
    
    for i in range(len(wealth)):
        wealth[i] = wealth[i] / 1000
    for j in range(len(totalpop)):
        totalpop[j] = totalpop[j] / 1000
    for k in range(len(zombify)):
        zombify[k] = zombify[k] / 1000
    
    for l in range(len(zombiepop)):
        zombiepop[l] = 0
    zombiepop[0] = 133486
    
def dramatype(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.10)

def providemap():
    print('\n')
    dramatype('Prime Minister, here is your report.')
    print('\n|||||VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV|\n')
    zcontrol = 0
    for i in nationid:
        pcontrol = int((zombiepop[i] / totalpop[i]) * 100)
        zcontrol += zombiepop[i]
        print(str(i) + ')' + nations[i] + ' is under ' + str(pcontrol) + ' percent money control.')

    if (zcontrol / npop) > .500:
        victory()
    
def senddelegate(target, amount):
    global zombiepop
    global wealth
    
    gainz = 0
    lossz = 0    
    targetvuln = GINI[target]
    targetdef = PISA[target]
    select = min(totalpop[target] - amount, amount)
    if select > 0:
        moneyattacked = targetvuln * select
    else:
        moneyattacked = abs(select)
    for i in range(int(moneyattacked)):
        roll = round(random.random(), 3)
        if targetdef <= roll:
            zombiepop[target] += 1
            wealth[0] -= zombify[target]
            gainz += 1
        else:
            totalpop[0] -= 1
            totalpop[target] += 1
            wealth[0] -= zombify[0]
            wealth[target] += zombify[0]
            zombiepop[0] -= 1
            lossz += 1
    print('\nindia gained ' + "{:,}".format(gainz * 1000) + ' and lost ' + "{:,}".format(lossz * 1000) + ' money zombies!\n')

def zombietide():
    asiaz = zombiepop[11] + zombiepop[0] + zombiepop[1] + zombiepop[2] + zombiepop[3]
    americaz = zombiepop[12] + zombiepop[4] + zombiepop[5]
    europez = zombiepop[13] + zombiepop[6] + zombiepop[7] + zombiepop[8] + zombiepop[9]
    oceaniaz = zombiepop[14] + zombiepop[10]
    latinz = zombiepop[15]
    africaz = zombiepop[16]
    
    asiaztide = 0
    if asiaz > 0:
        for i in range(0, 4):
            asiaztide = int(PISA[i] * zombiepop[i] / 100)
        zombiepop[0] += int(asiaztide / 5)
        zombiepop[1] += int(asiaztide / 5)
        zombiepop[2] += int(asiaztide / 5)
        zombiepop[3] += int(asiaztide / 5)
        zombiepop[11] += int(asiaztide / 5)
        asiaztide = int(PISA[11] * zombiepop[11] / 100)
        zombiepop[0] += int(asiaztide)
        zombiepop[1] += int(asiaztide)
        zombiepop[2] += int(asiaztide)
        zombiepop[3] += int(asiaztide)
   
    americaztide = 0
    if americaz > 0:
        for i in range(4, 6):
            americaztide = int(PISA[i] * zombiepop[i] / 100)
        zombiepop[4] += int(americaztide / 3)
        zombiepop[5] += int(americaztide / 3)
        zombiepop[12] += int(americaztide / 3)
        americaztide = int(PISA[12] * zombiepop[12] / 100)
        zombiepop[4] += int(americaztide)
        zombiepop[5] += int(americaztide)

    europeztide = 0
    if europez > 0:
        for i in range(6, 10):
            europeztide = int(PISA[i] * zombiepop[i] / 100)
        zombiepop[6] += int(europeztide / 5)
        zombiepop[7] += int(europeztide / 5)
        zombiepop[8] += int(europeztide / 5)
        zombiepop[9] += int(europeztide / 5)
        zombiepop[13] += int(europeztide / 5)
        europeztide = int(PISA[13] * zombiepop[13] / 100)
        zombiepop[4] += int(europeztide)
        zombiepop[5] += int(europeztide)

    oceaniaztide = 0
    if oceaniaz > 0:
        oceaniaztide = int(PISA[10] * zombiepop[i] / 100)
        zombiepop[10] += int(oceaniaztide / 2)
        zombiepop[14] += int(oceaniaztide / 2)
        oceaniaztide = int(PISA[14] * zombiepop[14] / 100)
        zombiepop[10] += int(oceaniaztide)

    latinztide = 0
    if latinz > 0:
        latinztide = int(PISA[15] * zombiepop[i] / 100)
        zombiepop[15] += int(latinztide)
        
    africaztide = 0
    if africaz > 0:
        africaztide = int(PISA[16] * zombiepop[i] / 100)
        zombiepop[16] += int(africaztide)
    
    ztide = asiaztide + americaztide + europeztide + oceaniaztide + latinztide + africaztide
    for i in range(10, 17):
        zombiepop[i] += int(PISA[i] * GINI[i] * ztide / 100)
        
def MAKEITRAIN():
    global turns
    global popularsupport
    global electionswon

    init()
    while (zombiepop[0] > 0) and (totalpop[0] > 0) and (wealth[0] > 0):
        print()
        dramatype('. . .YEAR ' + str(int(turns / 12)) + ' MONTH ' + str(turns % 12))
        providemap()
        
        dramatype('Where do you want to send a business delegation?')
        target = int(input().lower())
        
        print('\nHow many thousands of delegates? (0-' + "{:,}".format(zombiepop[0]) + ')')
        amount = int(input())
        if amount <= zombiepop[0]:
            senddelegate(target, amount)
                #print('You spend the month pondering over what is a number.\n')
        else:
            print('You spend the month counting the number of people on your side.\n')
        
        #print('You continue to devise your master plan.\n')
                    
        zombietide()

        if target == 0:
            turns += 1
        elif target == 8:
            turns += 2
        elif target == 6 or target == 7 or target == 9 or target == 10:
            turns += 3
        elif target == 1 or target == 3 or target == 4 or target == 5 or target == 11 or target == 12 or target == 15:
            turns += 4
        elif target == 2 or target == 13 or target == 14 or target == 16:
            turns += 5
        turns += 1
        if int(turns / (60 * electionswon)) >= 1:
            for i in range(nationid):
                psupport = totalpop[i]
                zsupport = zombiepop[i]
            popularsupport = round(popularsupport - ((zsupport / psupport)/50), 3)
            print('\n_ooooooooooooELECTIONSoooooooooooo_\n')
            print('You have ' + str(popularsupport * 100) + ' popular support! Those that do not support you are foreign agents.\n')
            dramatype('. . . . . . . . . . . . . . The votes are in!')
            if round(random.random(), 3) <= popularsupport:
                print('\nYou will continue to serve as Prime Minister! Congratulations Minister!')
                electionswon += 1
            else:
                print('\nElections lost. You start the long and perilous journey to return to the spice village whence you came.')
                gameover()
            

def victory():
    print('\n\nzo__zo__zo__zo__zo__zo__zo__nMn_!SUCCESS!\n')
    print('You lead india to a new golden age by conquering the world with money.\n')
    print('This feat took ' + str(int(turns / 12)) + ' months and ' + str(turns % 12) + ' months.')
    print('Congratulations, Prime Minister!\n')
    print('\n\nPlay again? (ye/no)')
    if input().lower().startswith('ye'):
        main()
    else:
        sys.exit()
    
def gameover():
    print('\n\n$$$$$$$$$$$$$$$|$R$I$P$|$$$$$$$$$$$$$$$\n')
    print('You have been swallowed by money. You survived  ' + str(turns) + ' months.\n')    
    print('Play again? (ye/no)')
    if input().lower().startswith('ye'):
        main()
    else:
        sys.exit()
        
def main():    
    print('\n\n_no$___no$___[MONEY ZOMBIE]___no$___no$\n')
    print('You, Prime Minister of india, desire to control the world through money. This is achieved by obtaining over 50% control of the human population through money. Ironically, you lead the most vulnerable nation to be exploiting other nations. But the people have voted. You WILL lead the people of India to be the world\'s number one manipulator through money. Can you survive until you are voted out as Prime Minister? (ye/no)\n')
    if input().lower().startswith('ye'):
        MAKEITRAIN()
    else:
        gameover()
        
main()