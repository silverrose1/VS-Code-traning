# # # #
#     #
#     #
# # # #
#     #
#     #
# # # #

digit = [
'1111110',	#0
'0110000',	#1
'1101101',	#2
'1111001',	#3
'0110011',	#4
'1011011',	#5
'1011111',	#6
'1110000',	#7
'1111111',	#8
'1111011'		#9
]

def dignum(num):
	lines = ['' for i in range(7)]
	for d in str(num):
		seg = [[ '  ','  ','  ','  '] for i in range(7)]
		patrn = (digit [int(d)])
		if patrn [0]== '1':
			seg [0][0]= seg[0][1]= seg[0][2]= seg[0][3] ='# '
		if patrn [1]== '1':
			seg [0][3]= seg[1][3]= seg[2][3]= seg[3][3] ='# '
		if patrn [2]== '1':
			seg [3][3]= seg[4][3]= seg[5][3]= seg[6][3] ='# '
		if patrn [3]== '1':
			seg [6][0]= seg[6][1]= seg[6][2]= seg[6][3] ='# '
		if patrn [4]== '1':
			seg [3][0]= seg[4][0]= seg[5][0]= seg[6][0] ='# '
		if patrn [5]== '1':
			seg [0][0]= seg[1][0]= seg[2][0]= seg[3][0] ='# '
		if patrn [6]== '1':
			seg [3][0]= seg[3][1]= seg[3][2]= seg[3][3] ='# '

		for j in range(7):
			lines [j] += (''.join(seg[j])+ '  ')
      
	print('\n'.join(lines))

dignum('012345')
			
