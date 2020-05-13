# Brief Recap
From the class lecture you should have seen why Git or more generally version control is important in the tech world from researchers to software engineers.
Git specifically...
* allows you to define your source of truth
* allows you to come up with whatever workflow worsts best for you via branching and pull requests
* has each personÕs "clone" contain the entire project history
* and a considerable amount more

Git also has a lot more to it than the above and a lot more than we will cover here.
This tutorial was made to act as an initial primer to help you learn some very simple first steps with Git

# Getting Started
In the course, your individual repository and group repositories will have been set up for you but this will be useful to know.

1. We will assume you are on a Linux / mac system and that you are using a terminal like iterm2 (mac) or gnome terminal (Ubuntu).
2. Either "sudo apt-get install git" or "brew install git" depending on your system.
3. Make a folder named "hello_git"
4. Enter that folder and type "git init"
5. Type 'git status' and you should see
    '''
    On branch master

    No commits yet

    nothing to commit (create/copy files and use "git add" to track)
    '''

The above steps will have initialized the folder you create as a git repository this lets git know to track the files in the folder as part of a git project.

- One quick reminder git is separate from GitHub with the latter being one of many hosting sites that let you store your git repositories.

# Adding A File to Be Committed

Now we will look at "staging" a file for a commit, that is in our case simply "adding it"

1. Create a file called 'hello_world'
2. In that file write "hello world"
3. Exit your editor type 'git status', you should see the file in red under 'untracked files'.
4. Exit your editor and type 'git add hello_world'
5. Type "git status" and you should see the file in bright green stating itÕs a new file ready for commit

If you got through all of that, good job. Now here are a few more pointers to help you along for after this brief tutorial.
- "git reset" will unstage files and changes to files that have been staged.
- "git add -A" or "git add ." will add every file in the repository for staging or add every file local to the directory you are in respectively

# Committing the file

Okay, so far, we have created a new repository and created a simple file and added it to the list of files to be committed.

Now we are actually going to make our commit.

Simply type "git commit" and hit enter. Your system's default editor should pop up and ask you for a short message.
Typically, the messages are kept short and represent to the best of your ability what you are committing, i.e. 'Added user authentication endpoint'
In this case I'll let you enter whatever you want. Use the editor to save and then exit the editor.

Congrats! At this point you should have initialized a repository, added a file and made your first commit.
These are central functions of git that  you will be using for a long time coming.


# Last word

So, we have just learned a bunch of valuable skills in Git, but git is very complex and there are many more abilities that Git has that can make your collaborative work
much easier.

I also want to point out that had you been in a collaborative setting, 'git push', would be your final step.
This sends all of your local commits the remote repository that the remote repository does not have.

Finally, here are some other things to look into, while not strictly necessary to using git, everyone in the industry does and it makes life easier:
  - Branching (If you check out branching also look at merge conflicts)
  - Bisecting
  - Diffing

