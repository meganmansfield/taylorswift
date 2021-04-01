#suggest a song to match your relationship
import numpy as np
import csv, os
from . import PACKAGEDIR

__all__ = ['taylorswift']

def taylorswift():
	data=[]

	with open(os.path.join(PACKAGEDIR,'Grades.csv'),'rt') as f:
		data=[row for row in csv.reader(f,delimiter=',')]

	numsongs=149

	title=[0]*numsongs
	album=[0]*numsongs
	allhappy=np.zeros(numsongs)
	alldate=np.zeros(numsongs)
	selffeel=np.zeros(numsongs)
	glassfull=np.zeros(numsongs)
	stages=np.zeros(numsongs)
	tempo=np.zeros(numsongs)
	seriousness=np.zeros(numsongs)
	future=np.zeros(numsongs)
	malefeel=np.zeros(numsongs)
	together=np.zeros(numsongs)

	i=0
	for number in range(2,numsongs+2):
		set=data[number]
		title[i]=set[0]
		album[i]=set[1]
		allhappy[i]=float(set[2])
		alldate[i]=float(set[3])
		selffeel[i]=float(set[4])
		glassfull[i]=float(set[5])
		stages[i]=float(set[6])
		tempo[i]=float(set[7])
		seriousness[i]=float(set[8])
		future[i]=float(set[9])
		malefeel[i]=float(set[10])
		together[i]=float(set[11])
		i+=1

	texts=np.loadtxt(os.path.join(PACKAGEDIR, 'answertext.txt'),delimiter='#',dtype='str')

	######################################################################################
	print('''
	    For these first four questions, if you are in a relationship, answer them with respect to your current relationship. If you are not currently in a relationship, answer them by considering either your most recent past relationship, or a potential relationship on the horizon, whichever you prefer.
	    
	    Which of these best describes your relationship?
	    1 - Our relationship ended because of cataclysmic past offenses. OR Our relationship has some serious problems.
	    2 - My feelings were a bit hurt when our relationship ended. OR Our relationship is going ok but has some problems.
	    3 - Our relationship ended, but not in a horribly bad way. It just ended. OR I feel pretty mediocre about the quality of our relationship.
	    4 - I wish I was in a relationship, but I don't think it will happen right now. OR I'm happy without a relationship right now.
	    5 - My relationship is pretty casual at the moment, not official or anything. OR I look back fondly on my past relationship, without feeling hurt or angry.
	    6 - My relationship is going well and we're thinking about long-term commitment.
	    7 - I'm getting married and/or comitting to this relationship for the rest of my life.
	    ''')
	trel1=float(input('Please enter a number from 1 to 7: '))
	if trel1<1:
		assert trel1>1, "You must enter an integer between 1 and 7"
	elif trel1>7:
		assert trel1<7, "You must enter an integer between 1 and 7"
	rel1=int(trel1)-4

	print('''
	What does the future of your relationship look like?
	1 - We're never speaking again.
	2 - We're probably going to see each other again at some point, but we won't be in touch much at all.
	3 - We might talk a bit less than we did in the past.
	4 - I'm not sure what our future is.
	5 - We've got some casual future plans but nothing serious lined up. OR We might hang out but I'm not sure.
	6 - We're going to be spending a fair amount of time together in the future.
	7 - We're going to be spending a large amount of time together. Like maybe getting married.
	''')
	trel2=float(input('Please enter a number from 1 to 7: '))
	if trel2<1:
		assert trel2>1, "You must enter an integer between 1 and 7"
	elif trel2>7:
		assert trel2<7, "You must enter an integer between 1 and 7"
	rel2=int(trel2)-4

	print('''
	What are the other person's feelings about you?
	1 - They've told me they hate me.
	2 - I think they don't like me that much. OR They've insulted me some.
	3 - They're nice to me but they see me as just a friend.
	4 - I'm not sure and/or they haven't made it clear to me.
	5 - They maybe have some non-platonic feelings for me but I'm not sure how strong they are.
	6 - They've told me that they have some feelings for me.
	7 - They have openly declared their love for me to the world.
	''')
	trel3=float(input('Please enter a number from 1 to 7: '))
	if trel3<1:
		assert trel3>1, "You must enter an integer between 1 and 7"
	elif trel3>7:
		assert trel3<7, "You must enter an integer between 1 and 7"
	rel3=int(trel3)-4

	print('''
	Which of these best describes how you spend your time together?
	1 - There are significant barriers that prevent us from being together.
	2 - There aren't any insurmountable barriers between us, but we never do anything together.
	3 - We do some things together but spend most of our time doing things alone.
	4 - We do about the same amount of stuff together as we do alone.
	5 - We do some things alone but spend most of our time doing things together.
	6 - We do pretty much everything together.
	7 - We do everything together, and even when we aren't together I only think about us being together.
	''')
	trel4=float(input('Please enter a number from 1 to 7: '))
	if trel4<1:
		assert trel4>1, "You must enter an integer between 1 and 7"
	elif trel4>7:
		assert trel4<7, "You must enter an integer between 1 and 7"
	rel4=int(trel4)-4

	print('''
	    For these next two questions, think about how you feel about your life overall.
	    
	Which of these best describes how you feel about yourself?
	1 - I have a lot of problems and they're all my fault.
	2 - I have a lot of problems, but I don't think they're all my fault.
	3 - I don't have a ton of significant problems, but sometimes I think I could do better.
	4 - I'm not really sure how I feel.
	5 - I feel pretty good about myself, and am just a little insecure on occasion.
	6 - I have a few concerns but feel very good overall.
	7 - I'm awesome, my life is awesome, this is the bomb.
	''')
	thap1=float(input('Please enter a number from 1 to 7: '))
	if thap1<1:
		assert thap1>1, "You must enter an integer between 1 and 7"
	elif thap1>7:
		assert thap1<7, "You must enter an integer between 1 and 7"
	hap1=int(thap1)-4

	print('''
	Which of these describes your emotional state?
	1 - You're really angry about something and/or really depressed about something.
	2 - You don't like how your life is going and you just want to make a deal to get your old life back.
	3 - You know something's wrong with your life but you want to ignore it.
	4 - You've accepted the bad things that have happened to you and are ready to move on from them.
	5 - You're feeling pretty neutral and you're waiting for life to make you happy.
	6 - You're actively working to make yourself happy.
	7 - You're actively working to make yourself happy and trying to make sure that everyone else is happy too.
	''')
	thap3=float(input('Please enter a number from 1 to 7: '))
	if thap3<1:
		assert thap3>1, "You must enter an integer between 1 and 7"
	elif thap3>7:
		assert thap3<7, "You must enter an integer between 1 and 7"
	hap3=int(thap3)-4

	selferr=np.array([selffeel[i]-hap1 for i in range(0,numsongs)])
	stageserr=np.array([stages[i]-hap3 for i in range(0,numsongs)])
	seriouserr=np.array([seriousness[i]-rel1 for i in range(0,numsongs)])
	futureerr=np.array([future[i]-rel2 for i in range(0,numsongs)])
	maleerr=np.array([malefeel[i]-rel3 for i in range(0,numsongs)])
	togethererr=np.array([together[i]-rel4 for i in range(0,numsongs)])

	neterr=np.zeros(numsongs)
	for i in range(0,numsongs):
		neterr=selferr**2.+stageserr**2.+seriouserr**2.+futureerr**2.+maleerr**2.+togethererr**2.

	oklist=np.zeros(20)
	index=0
	for n in range(0,40):
	    if any(np.abs(neterr)==n):
	        ok=np.where(np.abs(neterr)==n)[0]
	        for x in ok:
	            oklist[index]=x
	            index+=1
	        if index>4:
	            break

	okintlist=[int(i) for i in oklist]
	finalok=okintlist[0:5]

	print('Here are the top five songs that match your mood:')
	for x,item in enumerate(finalok):
	    n=x+1
	    print(str(n)+': '+title[item])
	    print(texts[item])




