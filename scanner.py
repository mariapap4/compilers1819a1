"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?
NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις

	return c
	# anything else
	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
	
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 'q0': { '0':'q1','1':'q1','2':'q1','3':'q3' },
       		    'q1': { '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2' },
       		    'q2': { '0':'q5'},
       		    'q3': { '0':'q4', '1':'q4', '2':'q4', '3':'q4', '4':'q4', '5':'q4'},
		    'q4': { '0':'q5'},
		    'q5': { '0':'q6','1':'q6','2':'q6','3':'q6','4':'q6','5':'q6','6':'q6','7':'q6','8':'q6','9':'q6'},
		    'q6': { '0':'q7','1':'q7','2':'q7','3':'q7','4':'q7','5':'q7','6':'q7','7':'q7','8':'q7','9':'q7'},
		    'q7': { 'G':'q8','K':'q11','M':'q13'},
	            'q8': { '0':'q9','1':'q9','2':'q9','3':'q9','4':'q9','5':'q9','6':'q9','7':'q9','8':'q9','9':'q9'},
	            'q9': { '0':'q10','1':'q10','2':'q10','3':'q10','4':'q10','5':'q10','6':'q10','7':'q10','8':'q10','9':'q10'},
	           'q10': { 'M':'q13', 'K':'q11'},
	           'q11': { 'T':'q12'},
	           'q13': {'P':'q14'},
	           'q14': {'S':'q12'},
	        }

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 'q12':'WIND_TOKEN',
       			
     	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	
