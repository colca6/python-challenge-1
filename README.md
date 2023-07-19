# python-challenge

My repo is "python-challenge-1".  I had issues, which resulted in deleting one, "python-challenge", then when I recreated, it automatically got the dash1 at the end. I went with it, HOWEVER, then it said it couldn't find files because it was still looking for the old "python-challenge" folder.

With the help of BCS Learning assistant, I recreated it in the Documents portion of my drive, not Desktop like before.

So you should be looking at "python-challenge-1", and the project is at "C:\Users\carlc\Documents\python-challenge-1" on my machine. 

I also had an issue for both parts, where in VSCode, I had to use PyBank or PyPoll in my path.  

Like this:  csvpath = os.path.join('PyBank','Resources','budget_data.csv')  This would run fine in VSCode, but not when you try from command line.  So I took it out of the above path.  Don't really understand why that's happening.

**************************

Ok, this was a challenging project. I spent a good amount of time looking up stuff, either in all of our exercises from class, or googling, and I also have a DataCamp membership, so I've been going through their lessons on topics covered in class.

I think my biggest issue is figuring out how to do what I think I need to do. I am from the VB6 world, but I haven't coded in a long time. The idea that you can be so freewheeling with variables and data types is really throwing me off, I need to get used to that.

I found our exercises most helpful for the parts about reading and writing to the csv or text files.  Some of the solutions were similar to previous homework.

PyPoll, I knew it would involve a list and a dictionary (probably other ways to do it) so I focused on that.  I struggled to figure out what I needed, and after a while, realized I just needed the 3 names and counts of each row, since "Ballot ID" and "County" are essentially meaningless for this exercise.  I can't remember where I found it, but the "for" loop that used "not" in it was very helpful, if the name was in list already, ignore and move on, otherwise add it. Easy 3 item list.

PyPoll-2, I knew I needed a dictionary which had the data associated with each candidate name. This was difficult to figure out, until I realized that the key part of the dictionary must be unique. Therefore, if I iterate through, with the key being one name, and use an integer as the value, incrementing by one for each row, I essentially make a counter, which gets reset back to 0 when the key changes to the next candidate. Here are 2 online sources I found helpful:

https://datagy.io/python-count-occurrences-in-list/
https://www.geeksforgeeks.org/python-create-dictionary-from-the-list/?ref=ml_lbp      --methods 1 and 2

PyPoll-3, I still don't really understand how the "list comprehension" works, but I know that it is used to get matching paired data, so once I had the "greatest number of votes" set to the "winner" variable, I just needed to get the candidate name that matched that number.  To do this, I simply copied several examples, all pretty much the same. Don't really understand it, but it works!

Some output came out with curly brackets, which I deleted using a method I found here:
https://stackoverflow.com/questions/40097863/how-to-remove-the-all-the-curly-bracket-in-dictionary-of-dictionaries