**************
*Fair Rations*
**************

	"You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread to a straight line 
	of N subjects. Each ith subject already has B_i loaves of bread.
	 
	Times are hard and your castle's food stocks are dwindling, so you must distribute as few loaves as 
	possible according to the following rules:

		1) Every time you give a loaf of bread to some person , you must also give a loaf of bread to the 
		person immediately in front of or behind them in the line (i.e., persons  or ). In other words, 
		you can only give a loaf of bread each to two adjacent people at a time.
			
		2) After all the bread is distributed, each person must have an even number of loaves.
			Given the number of loaves already held by each citizen, find and print the minimum number of 
			loaves you must distribute to satisfy the two rules above. If this is not possible, print NO."


Check the .pdf for more details. Here are the sample cases:

Sample Input 0
>5
>2 3 4 5 6

Sample Output 0
>4

Sample Input 1
>2
>1 2

Sample Output 1
>NO
