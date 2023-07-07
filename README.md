# ciccarello_automation_fixes
# With the changes in this repo, I got the beginning of your index.py working to correctly create a folder with my chosen name and test #1 passes

1. All changes are on **"fixes"** branch.  Can't merge to main with divergent branches.
2. Also look at Pull Requests and you'll see specifics of what was changed
3. Carefully compare your code to the code in this repo

- I only messed with automation/create_folder.py , tests/test_automation.py , index.py
- You have some file name mismatches that were causing import errors for testing and in your import statements index.py.  Make sure to look closely at the starter code if you are changing the names of things.  For example, you called your function make_folder( ) vs create_folder( ), so imports and things like line 20 in index.py were killing your program right away.
- You also had some indentation errors in create_folder.py with your ifs lined up with def meaning they weren't recognized as part of the function.
- You had "new_file" hardcoded in make_folder and I made some changes within the function and in your if name == main to ask for and pass in a user-specified folder name.  You'll see that it correctly created a folder named "kim"
- You'll see I commented out a lot of code.  The way I troubleshoot is to work one piece at a time and comment out everything I don't need to use.  Then uncomment the piece and move on.

  
