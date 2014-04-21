main:
	; Set Motor Speed Low
	output C.5 
	
	; Drive forward
	forward A
	forward B
	pause 2000
	
	; Right turn
	goto doRight
	
	halt A
	halt B

doRight:
	halt A
	halt B
	forward A
	pause 1000
	halt A
	goto main