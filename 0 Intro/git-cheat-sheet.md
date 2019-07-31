# Git-In-It
Git basics and common commands. Your one-stop-shop to all things Git!

#### git checkout -b
Creates a new branch. It's recommended to create a new branch per feature. When working in groups, it's helpful to add your initials to the branch name. This helps teammates quickly identify who is working on what features.

```bash
# git checkout -b <new_branch>
git checkout -b submit-btn

#git checkout -b <new_branch -user_initial>
git checkout -b new-user-form-LN
```

#### git branch
Returns the current branch you are working on.
```bash
# git branch to see current branch
git branch
```

#### git checkout <branch_name>
Switches from current branch to existing branch. Be sure to save changes in current branch before switching!

```bash
# Double check which branch you are on
git branch

# git checkout <branch_name> to switch between existing branches
git checkout new-user-form-LN
```

#### git reset
Unstages local files that were staged in git add.
```bash
# Unstages specific file
git reset script.py

# Unstages all files
git reset
```

#### git reset --hard HEAD
```bash
# throws away all your uncommitted changes
git reset --hard HEAD
```

#### git merge <branch_name>
```bash
# Double check which branch you are on
git branch

# git checkout <branch_name> to switch to main branch
git checkout deployment

# git merge feature branch into main branch
git merge new-user-form-LN
```

#### git branch -d <branch_name>
Once feature branches are merged and you have confirmed they are not needed, you can delete it. Though, many teams keep all branches for records.

```bash
# Double check you're not in the branch you want to delete
git branch

#### git branch -d <branch_name>
git branch -d new-user-form-LN
```


#### git add files with the same extension
```bash
# Git add all files with the same extension
git add '*txt'
```

#### git remove files with the same extension
```bash
# Git remove all files with the same extension
git rm '*txt'
```

#### git log
Shows history of commits.
```bash
# git log to see history of commits
git log
```
#### git remote add origin <remote_repo_url>
Adds a remote repository to a git folder.
```bash
# Git add remote repo
git remote add origin https://github.com/try-git/try_git.git
```
#### git remote rm origin
Removes remote repo from Git folder. *Please check with your lead before running this command.*
```bash
# Git remove remote repo
git remote rm origin https://github.com/try-git/try_git.git
```
#### git push origin master
Pushes master branch to remote repo. Though, if you created a deployment branch to test merge conflicts, the command will be:
```bash
# Git push deployment branch
git push origin deployment
```
#### git pull origin master
Pulls down recent changes to your local repo. Though, if you created a deployment branch to test merge conflicts, the command will be:
```bash
# Git pull deployment branch
git pull origin deployment
```
#### git diff HEAD
Shows differences the most recent commits.

```bash
#Shows differences between most recent commits.
git diff HEAD
```

#### git diff --staged
Shows differences the most recent commits in staged files.

```bash
#Shows differences between most recent commits of staged files.
git diff --staged
```

#### git checkout --<file_name>
Resets file to last commit.

```bash
git checkout -- myfile.py
```

## Tips
- When adding a commit message, it's helpful to capitalize file names.

```bash
git commit -m "created README.md file"
```

### Shortcuts
- Pressing the arrow up key will display previous inputs. This is helpful when you're running the same commands repeatedly.
- When typing in a file name, you can press TAB after a few letters, the terminal will guess the file name. If there are multiple names, terminal will display all files that match the first couple of letters you've typed. File names are case sensitive.

### Git Aliases
Creating aliases will save you time by allowing you to type shortcuts.

#### git config --global alias.co checkout
```bash
#turns
git checkout
#to
git co
```

#### git config --global alias.br branch
```bash
#turns
git branch
#to
git br
```

#### git config --global alias.ci commit
```bash
#turns
git commit -m "Your commit message"
#to
git ci -m "Your commit message"
```

#### git config --global alias.st status
```bash
#turns
git status
#to
git st
```
#### git config --global alias.a add
```bash
#turns
git add <file_name>
#to
git a <file_name>
```

#### git config --global alias.last 'log -1 HEAD'
```bash
#git last to show last commit
git last
commit 66bb74542905b760f8b319b00739800d5ecaaef1
Author: Lisa <lnguyen6@apple.com>
Date:   Tue Jun 27 09:43:30 2017 -0700
```

### Avoiding Merge Conflicts

1. Group chat
* Starting a group chat is a great way to keep everyone on the same page. It's great place to announce what features you're taking next and to ask for help. I like to announce when I've pushed to deployment so my teammates can pull the latest changes.

2. Pull before push!
* Though you should pull changes from the remote repo before making changes on your local repo, it's possible a teammate has pushed changes to the remote repo while you were working. It's best practice to pull all changes from the remote repo before pushing up changes from your local repo. Remember to tell your team you've pushed!

3. NEVER PUSH TO MASTER
* Create a new deployment branch before making any changes. Use this deployment branch to check merge conflicts. Once all branches are merged into the deployment branch and all is fine, THEN merge the deployment branch into the master branch.

## Want to learn more?
If you'd like to go into more depth, try [Git Real](http://gitreal.codeschool.com/?utm_source=github&utm_medium=codeschool_option&utm_campaign=trygit) with Code School or Codecademy's [tutorial](https://www.codecademy.com/learn/learn-git). It will take a few hours.
