/ [Home](index.md)

# Gush

**Note:** quick git push for one-way commits


Create a gush file in your desired location and create a file
```
cd /Users/myname/d/gitmagic
touch gu.sh
```


Add these into gu.sh file
```
git add .

git commit -m "Updates for $(date +%F)"

git push
```

Change mod
```
chmod u+x gu.sh
```

gu.sh 3.0:
```
git_push_with_chatgpt()
{
  
    git pull

    # sleep 3 seconds
    sleep 2

    git add .

    # path to the file
    file_path="/Users/fpr11/kact/gitmagic/gcommit-chatgpt.txt"

    # using wc command to count number of lines
    number_of_lines=`wc -l < $file_path`

    # echo $((number_of_lines))

    rando_number=`shuf -i 1-$((number_of_lines)) -n 1`

    # echo $rando_number

    line=`sed $((rando_number))!d $file_path`
    # echo $line

    git commit -m "$line: Updates for $(date +%F)"

    git push

}

git_push_with_vanilla()
{
    echo "calling Vanilla"
    
    git add .

    git commit -m "Updates for $(date +%F)"

    git push
}

# Testing
# git_push_with_chatgpt
# git_push_with_vanilla

if [ -n "$1" ] ; then
    git_push_with_vanilla
else
    git_push_with_chatgpt
fi
```


Go to bashrc / bash_profile
```
sudo gedit ~/.bash_profile

or

sudo vi ~/.bash_profile

or

sudo vi ~/.bashrc
```


Add this alias in your bash
```
alias gush="/Users/myname/d/gitmagic/gu.sh"
```

```
source ~/.bashrc

or

source ~/.bash_profile
```

Go to your desired repo and type this
```
gush
```

Chatgpt: Git funny comments
```
Made a typo in the last commit message
Accidentally committed my to-do list instead of code
Left a funny joke in the code as a Easter egg
Whoops, forgot to add the changes
Fixed the bug that was causing all the bugs
Committed a commit to fix the previous commit
Added the missing semicolon, finally
Changed all the variables to klingon
Refactored the code to be more DRY (Don't Repeat Yourself... or do, I don't care)
Changed all the variable names to characters from The Office
Turned the code upside down, just for fun
Accidentally committed my password, oops
Fixed the time machine code
Changed all the function names to cat noises
Removed all the commented out code, because I'm sick of reading it
Accidentally pushed a change from my cat's keyboard
Initial commit (I swear I didn't copy and paste this)
Fixed the bug that caused this commit message
Refactored the code for better readability (now it's just incomprehensible)
Added more comments to make the code harder to understand
Merge branch 'fix-typos' into 'master' (there were even more typos than I thought)
Reverted last commit (turns out my boss was right)
Changed variable names to x, y, and z because I'm out of letters
Added a 'fix' for the previous 'fix' that broke everything
Committed on behalf of a disgruntled coworker
Accidentally pushed a change from my cat's keyboard
Initial commit (I swear I didn't copy and paste this)
Fixed the bug that caused this commit message
Refactored the code for better readability (now it's just incomprehensible)
Added more comments to make the code harder to understand
Merge branch 'fix-typos' into 'master' (there were even more typos than I thought)
Reverted last commit (turns out my boss was right)
Changed variable names to x, y, and z because I'm out of letters
Added a 'fix' for the previous 'fix' that broke everything
Committed on behalf of a disgruntled coworker
I'm not arguing, I'm just passionately discussing the possibility of your suggestion being wrong.
I can't believe I'm committing to this.
I'm not saying it's your fault, but it can't be mine either.
Just because I have a red face doesn't mean I'm angry, it could just be a really bad sunburn.
Let's just agree to disagree and call it a merge.
I refuse to argue with someone who's not even on the same branch as me.
I'm sorry, I can't hear you over the sound of how awesome this commit is.
I can't believe I accidentally committed all my unfinished code.
I'm not saying I'm the best coder in the world, but I'm definitely not a git.
Merge conflict? More like merge convenience.
I don't always make commits, but when I do, I make them count.
I'm not saying I'm a git wizard, but I did just magic this merge conflict away.
I'm sorry, I can't do that Dave. I'm a git, not a psychic.
Why are we even having this merge conflict? Can't we just all get along?
I'm not saying I'm a git god, but I am divinely inspired when it comes to resolving merge conflicts.
Git push? More like git smashed.
I'm sorry, I can't let you do that. This repository is protected by a team of highly trained git specialists.
I may not be a ninja, but I can definitely git-fu my way out of this merge conflict.
I'm not saying my code is perfect, but at least it's better than whatever caused this merge conflict.
I'm not saying your code is bad, but it's like a koala on fire running away from a tsunami.
I'm not saying your code is bad, but it's like a one-legged man in a butt-kicking contest.
I'm not saying your code is bad, but it's like a blind squirrel trying to find a nut in a minefield.
I'm not saying your code is bad, but it's like a fish out of water flailing around on the runway.
I'm not saying your code is bad, but it's like a cat trying to play the piano with its tail.
I'm not saying your code is bad, but it's like a giraffe in a phone booth.
I'm not saying your code is bad, but it's like a chicken trying to play soccer.
I'm not saying your code is bad, but it's like a clown trying to tell a knock-knock joke in sign language.
I'm not saying your code is bad, but it's like a dolphin trying to do stand-up comedy.
I'm not saying your code is bad, but it's like a kangaroo trying to dance the tango.
I'm not saying your code is bad, but it's like a penguin trying to fly a plane.
I'm not saying your code is bad, but it's like a monkey trying to drive a car.
I'm not saying your code is bad, but it's like a llama trying to play baseball.
I'm not saying your code is bad, but it's like a frog trying to play the trumpet.
I'm not saying your code is bad, but it's like a walrus trying to play tennis.
Initial commit (because why not?)
Fixing all the things (that I probably broke in the first place)
Added even more comments because I can't remember what I wrote
Reverting to last working version because THIS ONE IS BROKEN
Merging dev and master because I can't tell the difference
Whoops, forgot to add the actual code
Making some questionable design choices because I'm feeling rebellious
Fixing a bug that only appears at 2am on a full moon
Refactoring entire codebase because I was bored
Updating dependencies because I was feeling brave
Merging in the future because I want to see if it breaks anything
Adding more TODOs because my to-do list wasn't long enough
Adding the kitchen sink because why not
Deleting all the things because I have no idea what I'm doing
Adding some magic to make it work (please don't ask how)
Fixed time machine's date and time display
Added a life to the game of life
Changed the color of the sky to match my mood
Replaced all instances of 'foo' with 'bar' because 'foo' was getting on my nerves
Turned all the 1s into 0s and vice versa because why not
Fixed the bug that only appears on my machine
Replaced all instances of 'the' with 'teh' because it's more fun that way
Changed the font to Comic Sans because it's more fun to read
Improved performance by replacing all loops with goto statements
Removed all code and replaced with a haiku
Changed all variable names to random words because I'm feeling lucky
Added a feature to randomly change the background color every 5 minutes
Updated the time machine's flux capacitor
Changed all instances of 'object-oriented' to 'object-confused'
Replaced all instances of 'hello world' with 'goodbye world' because I'm feeling sad today
Changed all instances of 'foo' to 'bar' because I was feeling unoriginal
Added a secret feature that only activates on the 31st of February
Fixed a bug that only appears when the moon is full
Added a feature that randomly replaces words with cat noises
Refactored entire codebase to be written in emoji
Replaced all instances of 'the' with 'be' because I was feeling silly
Changed all variable names to be inspired by 'The Hitchhiker's Guide to the Galaxy'
Replaced all instances of 'hello world' with 'howdy y'all'
Added a feature that turns everything upside down
Changed the font to Wingdings because it's more fun to read
Replaced all instances of 'good morning' with 'meow'
Deleted all code and replaced it with a picture of a cat
Changed all numbers to be written in binary because why not
Added a feature that turns everything into a rainbow
Added a feature that allows users to change the color of the sky
"Merge branch 'fix-typos' into 'develop'... Now with even more typos!"
"Revert 'Revert last revert'... this is getting out of hand."
"Initial commit... finally."
"Merge branch 'fix-everything' into 'develop'... well, almost everything."
"Merge branch 'fix-grammar' into 'develop'... still better than nothing."
"Revert 'Fix all the things'... some things are better left broken."
"Merge branch 'fix-spelling' into 'develop'... let's hope we got it right this time."
"Update README.md... because no one reads it anyway."
"Merge branch 'fix-merge-conflict' into 'develop'... took us long enough."
"Revert 'Fix merge conflict'... and introduce new ones, yay!"
"Merge branch 'fix-typos' into 'develop'... Now with even more typos!"
"Revert 'Revert last revert'... this is getting out of hand."
"Initial commit... finally."
"Merge branch 'fix-everything' into 'develop'... well, almost everything."
"Merge branch 'fix-grammar' into 'develop'... still better than nothing."
"Revert 'Fix all the things'... some things are better left broken."
"Merge branch 'fix-spelling' into 'develop'... let's hope we got it right this time."
"Update README.md... because no one reads it anyway."
"Merge branch 'fix-merge-conflict' into 'develop'... took us long enough."
"Revert 'Fix merge conflict'... and introduce new ones, yay!"
```

##### Gush Demo
[Gush Demo](https://www.loom.com/share/97a5d65c0d44493e8cf7bfce07f61ed0)

#### Caution:
Remember, gush file helps only on one-way commits like error_logs, daily_logs. When you work on big projects, please try not to use gush file
