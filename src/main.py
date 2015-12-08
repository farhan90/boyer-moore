"""Simple program to implement the Boyer-Moore
string search algorithm"""

def get_bad_match_table(pattern):
	bad_match_table={}
	i=0
	bad_match_table['ast']=len(pattern)
	for c in pattern:
		bad_match_table[c]=max(1,len(pattern)-1-i)
		i=i+1

	return bad_match_table



def match_pattern(src,pattern):
	if len(src)<len(pattern):
		return False

	bad_match_table=get_bad_match_table(pattern)
	i=0
	j=len(pattern)-1
	val=False
	while j>=0 and i<len(src):
		if pattern[j] != src[i]:
			if src[i] in bad_match_table:
				i=i+bad_match_table[src[i]]
			else:
				i=i+bad_match_table['ast']
			j=len(pattern)-1
			val=False
			continue
		
		"""This means first character in src matches
		but since we are doing a match of the
		rightmost character we need to advance""" 
		if i==0 and j!=0:
			i=i+bad_match_table[src[i]]

	
		i=i-1
		j=j-1
		val=True
	
			
	return val


def main():
	print get_bad_match_table("look")
	print match_pattern("I should look for the code","look")

if __name__=='__main__':
	main()
