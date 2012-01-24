def pairwiseScore(seqA, seqB): 

	dashes = []		#used for the pipes between letters
	score = 0		#keeps track of the score; +1 for match, +3 for consec. match
	consec = False		#tracks for consecutive matches
	
	for letter in range(len(seqA)):
		
		if seqA[letter] == seqB[letter]:
			
			if consec == True: score += 3
			else: score += 1
			consec = True
			dashes.append("|")
			
		else: 
			score -= 1
			consec = False
			dashes.append(" ")
	
	answer = seqA + "\n" + ''.join(dashes) + "\n" + seqB + "\n" + "Score: " + "\n" + str(score)
	return (answer)

print (pairwiseScore('ATCG', 'ATCG'))

print (pairwiseScore('CATTCATCATGCAA', 'GATAAATCTGGTCT'))
