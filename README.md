# AI_Backward_Chaining
#CMPT310 Assignment 2

##Running
The main file is located at 'backwardChaining.py'.
Making the file executable with
> chmod +x backwardChaining.py


And then run. 
The only command line arg is the filename of the problem specification
> python backwardChaining.py

##Testing
It will ask you for a file containing rules. 
Please make sure your test file is in the same directory with my main file.
I have added a rule [k] in the provided test file to show that if one rule fails and there is another rule can prove the goal, 
the goal will still be true. 
In my case, I enter a query [h]. While rule [hi] fails, we can rule [hk] to prove.
##NOTE:
When you enter a test file and you queries, please contain a double quotation marks.
For example: 
Please enter your file containing rules: 
"text_data.txt" 
Please enter your queries: 
"abc"

##Heuristics
For my algorithm, I first check if the query is in the knowledge base or not.
If yes, then go ahead and use backward_chaining. 
My backward_chaining uses recursion method, it takes goals as argument and first check its head.
Then put the rest of goals as a new goal into backward_chaining, and so on. 
If one rule fails proving the goal, but there are more other rules might be able to prove the goal.
It will call backward_chaining again with a new knowledge base excluding the rule which is fail.
Keep checking until all the rules have been checked.
