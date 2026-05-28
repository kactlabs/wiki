/ [Home](index.md)

# 100 Linux Commands — With Definitions

---

## Category 1: File & Directory Commands

### 1. ls — List Directory Contents

**Definition:** ls stands for **List**. It displays the files and directories present in the current or specified directory. It is one of the most frequently used Linux commands.

```bash
ls          # basic list
ls -l       # long format (permissions, size, date)
ls -a       # show hidden files (starting with .)
ls -la      # long format + hidden files
ls -lh      # human-readable sizes (KB, MB)
ls /home    # list contents of specific path
```

**Output Example:**
```
-rw-r--r-- 1 user group 1024 May 28 file.txt
drwxr-xr-x 2 user group 4096 May 28 folder/
```

---

### 2. cd — Change Directory

**Definition:** cd stands for **Change Directory**. It is used to navigate between directories (folders) in the Linux file system. Without any argument, it takes you to the home directory.

```bash
cd /var/log     # go to specific path
cd ..           # move one level up (parent directory)
cd ~            # go to home directory
cd -            # go back to previous directory
cd /            # go to root directory
```

---

### 3. pwd — Print Working Directory

**Definition:** pwd stands for **Print Working Directory**. It displays the full absolute path of the directory you are currently in. Useful when you are navigating deep into the file system.

```bash
pwd
# Output: /home/user/documents/projects
```

---

### 4. mkdir — Make Directory

**Definition:** mkdir stands for **Make Directory**. It creates one or more new directories. The `-p` flag allows creation of nested directories in a single command without errors.

```bash
mkdir myfolder              # create one directory
mkdir dir1 dir2 dir3        # create multiple at once
mkdir -p parent/child/sub   # create nested directories
mkdir -v newfolder          # verbose (shows what was created)
```

---

### 5. rmdir — Remove Directory

**Definition:** rmdir stands for **Remove Directory**. It deletes an empty directory. If the directory contains files or subdirectories, it will not work — use `rm -r` instead.

```bash
rmdir emptyfolder           # remove empty folder
rmdir -p a/b/c              # remove nested empty dirs
rmdir dir1 dir2             # remove multiple empty dirs
```

---

### 6. touch — Create Empty File / Update Timestamp

**Definition:** touch is used to create a new empty file if it doesn't exist. If the file already exists, it updates the file's access and modification timestamp without changing its content.

```bash
touch newfile.txt               # create empty file
touch f1.txt f2.txt f3.txt      # create multiple files
touch -m file.txt               # update modification time only
touch -t 202505281200 file.txt  # set specific timestamp
```

---

### 7. cp — Copy Files or Directories

**Definition:** cp stands for **Copy**. It copies files or directories from one location to another. The original file remains unchanged. The `-r` flag is required to copy directories recursively.

```bash
cp file1.txt file2.txt          # copy and rename
cp file.txt /home/user/         # copy to another directory
cp -r folder1/ folder2/         # copy entire directory
cp -i src dest                  # ask before overwriting
cp -v file1 file2               # show what is being copied
cp -p file1 file2               # preserve permissions & timestamps
```

---

### 8. mv — Move or Rename Files

**Definition:** mv stands for **Move**. It moves files or directories from one location to another. It is also used to rename files and directories. Unlike cp, the original is removed after moving.

```bash
mv old.txt new.txt              # rename file
mv file.txt /home/user/docs/    # move to another location
mv folder1/ /tmp/               # move directory
mv -i src dest                  # prompt before overwrite
mv -v file1 file2               # verbose output
```

---

### 9. rm — Remove Files or Directories

**Definition:** rm stands for **Remove**. It permanently deletes files or directories. Unlike Windows, there is no Recycle Bin — deleted files cannot be recovered easily. Use with extreme caution.

```bash
rm file.txt             # delete a single file
rm f1.txt f2.txt        # delete multiple files
rm -r folder/           # delete folder and all contents
rm -f file.txt          # force delete without prompt
rm -rf folder/          # force delete folder recursively
rm -i file.txt          # ask confirmation before deleting
```

> ⚠️ **WARNING:** `rm -rf /` will destroy the entire operating system!

---

### 10. find — Search Files & Directories

**Definition:** find is a powerful command used to search for files and directories based on name, type, size, permissions, date modified, and more. It searches recursively through the directory tree.

```bash
find / -name "file.txt"         # find by exact name
find . -name "*.log"            # find all .log files here
find /home -type d              # find directories only
find /home -type f              # find files only
find . -size +10M               # files larger than 10MB
find . -mtime -7                # modified in last 7 days
find . -perm 755                # files with specific permission
find . -empty                   # find empty files/folders
```

---

## Category 2: File Viewing Commands

### 11. cat — Concatenate and Display File

**Definition:** cat stands for **Concatenate**. It reads and displays the content of one or more files on the terminal. It can also be used to create files, combine files, and append content to files.

```bash
cat file.txt                    # display file content
cat file1.txt file2.txt         # display two files together
cat file1 >> file2              # append file1 content to file2
cat > newfile.txt               # create file (Ctrl+D to save)
cat -n file.txt                 # display with line numbers
cat -A file.txt                 # show special characters
```

---

### 12. more — View File Page by Page

**Definition:** more is a file viewing command that displays content one screen at a time. It is useful for reading long files. However, it only allows forward scrolling — you cannot go back.

```bash
more file.txt           # view page by page
more -n 5 file.txt      # show 5 lines per screen
more +10 file.txt       # start viewing from line 10
```

**Controls:**
```
SPACE     → Next page
ENTER     → Next line
q         → Quit
/keyword  → Search forward
```

---

### 13. less — Advanced File Viewer

**Definition:** less is an improved version of more. It allows both forward and backward scrolling, supports searching, and is faster with large files because it does not load the entire file at once.

```bash
less file.txt           # open file in less
less +F file.txt        # follow mode (like tail -f)
less -N file.txt        # show line numbers
```

**Controls:**
```
Arrow Up/Down   → Scroll line by line
Page Up/Down    → Scroll page by page
/keyword        → Search forward
?keyword        → Search backward
g               → Go to beginning
G               → Go to end
q               → Quit
```

---

### 14. head — Display First Lines of File

**Definition:** head displays the first 10 lines of a file by default. It is used to quickly preview the beginning of a file without opening the entire file. The number of lines can be customized.

```bash
head file.txt           # first 10 lines (default)
head -n 20 file.txt     # first 20 lines
head -n -5 file.txt     # all lines except last 5
head -c 200 file.txt    # first 200 bytes/characters
```

---

### 15. tail — Display Last Lines of File

**Definition:** tail displays the last 10 lines of a file by default. It is especially useful for reading log files. The `-f` (follow) option allows real-time monitoring of a file as new content is added.

```bash
tail file.txt           # last 10 lines
tail -n 20 file.txt     # last 20 lines
tail -f /var/log/syslog # live monitor log file
tail -c 100 file.txt    # last 100 bytes
tail -n +5 file.txt     # all lines starting from line 5
```

---

### 16. grep — Global Regular Expression Print

**Definition:** grep stands for **Global Regular Expression Print**. It searches for a specific pattern or keyword within files and prints matching lines. It is one of the most powerful text-searching tools in Linux.

```bash
grep "error" file.txt           # basic search
grep -i "error" file.txt        # case-insensitive
grep -r "error" /var/logs/      # search in all files in directory
grep -n "error" file.txt        # show line numbers
grep -v "error" file.txt        # lines that do NOT match
grep -c "error" file.txt        # count of matching lines
grep -l "error" *.txt           # list files containing match
grep -w "error" file.txt        # match whole word only
grep "^Start" file.txt          # lines starting with "Start"
grep "end$" file.txt            # lines ending with "end"
```

---

### 17. nano — Simple Terminal Text Editor

**Definition:** nano is a beginner-friendly, terminal-based text editor. It is simple to use with on-screen keyboard shortcuts displayed at the bottom. It is ideal for quick file edits.

```bash
nano file.txt           # open or create file
nano +10 file.txt       # open at line 10
nano -l file.txt        # show line numbers
```

**Keyboard Shortcuts:**
```
Ctrl+O    → Save file
Ctrl+X    → Exit
Ctrl+K    → Cut line
Ctrl+U    → Paste line
Ctrl+W    → Search
Ctrl+G    → Help
```

---

### 18. vim — Vi Improved Text Editor

**Definition:** vim stands for **Vi IMproved**. It is a powerful, advanced text editor with two main modes — Insert Mode (for typing) and Command Mode (for navigation and operations). It has a steep learning curve but is extremely efficient.

```bash
vim file.txt    # open file
```

**Modes & Shortcuts:**
```
i         → Enter Insert mode (start typing)
Esc       → Return to Command mode
:w        → Save
:q        → Quit
:wq       → Save and quit
:q!       → Quit without saving
dd        → Delete entire line
yy        → Copy (yank) line
p         → Paste
u         → Undo
Ctrl+R    → Redo
/keyword  → Search
:%s/old/new/g → Replace all occurrences
```

---

## Category 3: Permission Commands

### 19. chmod — Change File Mode/Permissions

**Definition:** chmod stands for **Change Mode**. It changes the read, write, and execute permissions of a file or directory for the owner, group, and others. Permissions can be set using numbers (octal) or symbols.

```bash
chmod 755 script.sh     # rwxr-xr-x
chmod 644 file.txt      # rw-r--r--
chmod +x file.sh        # add execute permission
chmod -w file.txt       # remove write permission
chmod u+x file.sh       # give execute to owner only
chmod -R 755 folder/    # apply to all files in folder
```

**Permission Table:**
```
Number  Symbol  Meaning
  7      rwx    Read + Write + Execute
  6      rw-    Read + Write
  5      r-x    Read + Execute
  4      r--    Read only
  0      ---    No permission

Position 1 → Owner
Position 2 → Group
Position 3 → Others
```

---

### 20. chown — Change Ownership

**Definition:** chown stands for **Change Owner**. It changes the owner and/or group of a file or directory. Only the root user (superuser) can change file ownership in most cases.

```bash
chown alice file.txt            # change owner to alice
chown alice:developers file.txt # change owner and group
chown -R alice /var/www/        # change ownership recursively
chown :developers file.txt      # change group only
```

---

### 21. chgrp — Change Group Ownership

**Definition:** chgrp stands for **Change Group**. It changes the group ownership of a file or directory. This is useful when multiple users belonging to the same group need access to a file.

```bash
chgrp developers file.txt       # change group
chgrp -R developers folder/     # recursive change
chgrp -v staff file.txt         # verbose output
```

---

## Category 4: System Info Commands

### 22. uname — Unix Name / System Information

**Definition:** uname stands for **Unix Name**. It displays system information such as the operating system name, kernel version, machine type, and hostname. The `-a` flag shows all available information.

```bash
uname           # just OS name: Linux
uname -a        # all info
uname -r        # kernel release version
uname -m        # machine hardware: x86_64
uname -n        # hostname
uname -s        # kernel name
```

---

### 23. whoami — Display Current User

**Definition:** whoami displays the username of the currently logged-in user. It is useful in scripts or when switching between users to confirm your current identity.

```bash
whoami
# Output: john

sudo whoami
# Output: root
```

---

### 24. hostname — Show or Set Hostname

**Definition:** hostname displays or sets the name of the current machine (computer) on the network. The hostname is used to identify the system on a network.

```bash
hostname            # show current hostname
hostname -I         # show IP address(es)
hostname -f         # show fully qualified domain name
sudo hostname newname  # temporarily change hostname
```

---

### 25. uptime — System Running Time

**Definition:** uptime shows how long the system has been running since the last boot, along with the current time, number of logged-in users, and the system load averages for the past 1, 5, and 15 minutes.

```bash
uptime
# Output: 14:32:10 up 5 days, 3:20, 2 users, load average: 0.10, 0.15, 0.12

uptime -p   # pretty format: up 5 days, 3 hours
uptime -s   # since when system started: 2026-05-23 11:12:05
```

---

### 26. date — Display or Set Date and Time

**Definition:** date displays the current system date and time. It can also be used to display date in custom formats or (with root privileges) to set the system date and time.

```bash
date                            # full date and time
date +"%Y-%m-%d"                # 2026-05-28
date +"%d/%m/%Y"                # 28/05/2026
date +"%H:%M:%S"                # 14:35:22
date +"%A, %B %d, %Y"          # Thursday, May 28, 2026
sudo date -s "2026-05-28 10:00:00"  # set date/time
```

---

### 27. df — Disk Free / Disk Space Usage

**Definition:** df stands for **Disk Free**. It shows the available and used disk space on all mounted file systems. The `-h` option displays sizes in human-readable format (KB, MB, GB).

```bash
df          # all filesystems (in blocks)
df -h       # human-readable sizes
df -T       # show filesystem type (ext4, xfs, etc.)
df -i       # show inode usage
df /home    # disk usage of specific partition
```

**Output Example:**
```
Filesystem   Size  Used  Avail  Use%  Mounted on
/dev/sda1     50G   20G    28G   42%  /
```

---

### 28. du — Disk Usage of Files/Directories

**Definition:** du stands for **Disk Usage**. It shows the disk space consumed by files and directories. Unlike df which shows partition-level usage, du shows file/folder-level usage.

```bash
du file.txt             # size of a file
du -h folder/           # human-readable folder size
du -sh folder/          # summary only (total size)
du -sh *                # size of all items in current dir
du -ah /home            # all files with sizes
du --max-depth=1 /var   # only one level deep
```

---

### 29. free — Display Memory Usage

**Definition:** free displays the total, used, and available RAM and swap memory of the system. The `-h` option makes the output human-readable. Essential for monitoring system memory.

```bash
free            # memory in kilobytes
free -h         # human-readable (MB/GB)
free -m         # in megabytes
free -g         # in gigabytes
free -s 5       # update every 5 seconds
```

**Output Example:**
```
              total   used   free   shared  buff   available
Mem:           7.7G   3.2G   2.1G    300M   2.4G      4.0G
Swap:          2.0G   100M   1.9G
```

---

## Category 5: Process Management Commands

### 30. ps — Process Status

**Definition:** ps stands for **Process Status**. It displays a snapshot of currently running processes. It shows the process ID (PID), terminal, CPU/memory usage, and command name.

```bash
ps              # processes in current terminal
ps aux          # all processes from all users (detailed)
ps -ef          # full format listing
ps -u username  # processes by specific user
ps aux | grep firefox  # find specific process
```

**Output Columns:**
```
PID   → Process ID
TTY   → Terminal type
TIME  → CPU time used
CMD   → Command name
%CPU  → CPU usage
%MEM  → Memory usage
```

---

### 31. top — Live Process Monitor

**Definition:** top is an interactive real-time process viewer. It continuously updates and shows running processes sorted by CPU usage. It also displays system-wide statistics like CPU, memory, and load average.

```bash
top             # open live process monitor
top -u john     # show only john's processes
top -n 5        # refresh 5 times then exit
```

**Controls inside top:**
```
q       → Quit
k       → Kill a process (enter PID)
M       → Sort by memory usage
P       → Sort by CPU usage
h       → Help
```

---

### 32. kill — Terminate Process by PID

**Definition:** kill sends a signal to a process to terminate it. By default, it sends the SIGTERM signal (graceful stop). The `-9` flag sends SIGKILL (force kill — cannot be ignored by the process).

```bash
kill 1234           # graceful kill (SIGTERM)
kill -9 1234        # force kill (SIGKILL)
kill -l             # list all signal types
kill -15 1234       # same as default SIGTERM
```

> Get PID using `ps aux` or `pgrep processname`

---

### 33. killall — Kill All Processes by Name

**Definition:** killall kills all running processes with a given name. Unlike kill which requires a PID, killall uses the process name directly. Useful when multiple instances of a program are running.

```bash
killall firefox         # kill all firefox processes
killall -9 chrome       # force kill all chrome
killall -u john         # kill all processes by user john
killall -v nginx        # verbose — show what was killed
```

---

### 34. bg and fg — Background & Foreground Jobs

**Definition:**
- **bg** sends a paused/stopped process to the background so the terminal is free.
- **fg** brings a background process back to the foreground.

```bash
# Step 1: Run a process, then press Ctrl+Z to pause it
# Step 2:
bg          # resume it in background
fg          # bring it back to foreground
fg %1       # bring job number 1 to foreground
jobs        # list all background/stopped jobs
```

---

## Category 6: Networking Commands

### 35. ping — Test Network Connectivity

**Definition:** ping sends ICMP Echo Request packets to a host and waits for a reply. It is used to check whether a remote system is reachable and to measure the round-trip response time.

```bash
ping google.com         # ping continuously
ping -c 4 google.com    # send only 4 packets
ping -i 2 google.com    # send packet every 2 seconds
ping -s 100 google.com  # set packet size to 100 bytes
ping 192.168.1.1        # ping by IP address
```

---

### 36. ifconfig — Network Interface Configuration

**Definition:** ifconfig stands for **Interface Configuration**. It displays and configures network interface parameters such as IP address, MAC address, and network status. (Modern systems also use `ip` command.)

```bash
ifconfig            # show all network interfaces
ifconfig eth0       # show specific interface
ifconfig eth0 up    # enable interface
ifconfig eth0 down  # disable interface
ip addr show        # modern alternative to ifconfig
```

---

### 37. wget — Web Get / Download Files

**Definition:** wget stands for **Web Get**. It is a non-interactive command-line tool for downloading files from the internet using HTTP, HTTPS, or FTP protocols. It supports resuming interrupted downloads.

```bash
wget https://example.com/file.zip           # download file
wget -O myfile.zip https://example.com/f    # save with custom name
wget -c https://example.com/largefile.zip   # resume interrupted download
wget -b https://example.com/file            # download in background
wget --limit-rate=500k URL                  # limit download speed
```

---

### 38. ssh — Secure Shell Remote Login

**Definition:** ssh stands for **Secure Shell**. It allows encrypted remote login to another computer over a network. It replaces older, insecure protocols like Telnet. Used extensively for server administration.

```bash
ssh user@192.168.1.100          # connect to remote server
ssh -p 2222 user@host           # connect on custom port
ssh user@host "ls /var/www"     # run command on remote server
ssh-keygen                      # generate SSH key pair
ssh-copy-id user@host           # copy public key to server
```

---

## Category 7: Archive & Compression Commands

### 39. tar — Tape Archive

**Definition:** tar stands for **Tape Archive**. It is used to create, view, or extract archive files (.tar, .tar.gz, .tar.bz2). It bundles multiple files into a single file and can also compress them.

```bash
# Create archive
tar -cvf archive.tar folder/        # create .tar
tar -czvf archive.tar.gz folder/    # create compressed .tar.gz
tar -cjvf archive.tar.bz2 folder/   # create .bz2

# Extract archive
tar -xvf archive.tar                # extract .tar
tar -xzvf archive.tar.gz            # extract .tar.gz
tar -xvf archive.tar -C /home/      # extract to specific folder

# View contents without extracting
tar -tvf archive.tar
```

**Flags:**
```
c → Create    x → Extract
v → Verbose   f → Filename
z → gzip      j → bzip2
t → List contents
```

---

### 40. zip / unzip — Compress and Extract ZIP Files

**Definition:** zip compresses files into a .zip archive, which is universally compatible with all operating systems including Windows. unzip extracts the contents of a .zip file.

```bash
# zip
zip archive.zip file1.txt file2.txt # zip multiple files
zip -r archive.zip folder/           # zip entire folder
zip -e secure.zip file.txt           # zip with password
zip -u archive.zip newfile.txt       # add file to existing zip

# unzip
unzip archive.zip                   # extract here
unzip archive.zip -d /home/user/    # extract to specific folder
unzip -l archive.zip                # list contents without extracting
unzip -o archive.zip                # overwrite without asking
```

---

## Category 8: User Management Commands

### 41. useradd — Add New User

**Definition:** useradd creates a new user account on the system. It sets up the user's home directory, default shell, and group membership. Requires root/sudo privileges.

```bash
sudo useradd john               # create user (minimal)
sudo useradd -m john            # create user with home directory
sudo useradd -m -s /bin/bash john  # with home dir + bash shell
sudo useradd -G developers john    # add to supplementary group
sudo useradd -e 2026-12-31 john    # set account expiry date
```

---

### 42. usermod — Modify User Account

**Definition:** usermod stands for **User Modify**. It modifies an existing user account's properties such as username, home directory, shell, group membership, and lock status.

```bash
sudo usermod -aG sudo john         # add user to sudo group
sudo usermod -s /bin/zsh john      # change default shell
sudo usermod -d /home/newdir john  # change home directory
sudo usermod -l newname oldname    # rename user
sudo usermod -L john               # lock user account
sudo usermod -U john               # unlock user account
```

---

### 43. userdel — Delete User Account

**Definition:** userdel stands for **User Delete**. It removes a user account from the system. The `-r` flag also removes the user's home directory and mail spool.

```bash
sudo userdel john           # delete user (keep home dir)
sudo userdel -r john        # delete user + home directory
sudo userdel -f john        # force delete even if logged in
```

---

### 44. passwd — Change User Password

**Definition:** passwd is used to set or change a user's password. Regular users can change their own password; root can change any user's password. It also manages password expiry policies.

```bash
passwd                  # change your own password
sudo passwd john        # change another user's password
sudo passwd -l john     # lock user password
sudo passwd -u john     # unlock user password
sudo passwd -e john     # force password change on next login
passwd -S john          # show password status
```

---

### 45. su — Switch User

**Definition:** su stands for **Switch User**. It allows you to switch to another user account within the same terminal session. Using `su -` loads the target user's full environment.

```bash
su john             # switch to john (keep current env)
su - john           # switch to john (load john's env)
su -                # switch to root user
su -c "command"     # run single command as another user
exit                # return to original user
```

---

### 46. sudo — Superuser Do

**Definition:** sudo stands for **Superuser Do**. It allows a permitted user to execute a command as the superuser (root) or another user. It provides temporary elevated privileges without switching accounts.

```bash
sudo apt update             # run command as root
sudo -i                     # open root shell
sudo -u john command        # run as specific user
sudo -l                     # list allowed commands
sudo !!                     # repeat last command with sudo
sudo -k                     # forget cached credentials
```

---

## Category 9: Package Management Commands

### 47. apt — Advanced Package Tool (Debian/Ubuntu)

**Definition:** apt stands for **Advanced Package Tool**. It is the package manager for Debian-based systems (Ubuntu, Mint). It handles installing, updating, upgrading, and removing software packages.

```bash
sudo apt update                 # refresh package list
sudo apt upgrade                # upgrade all packages
sudo apt install nginx          # install a package
sudo apt remove nginx           # remove package (keep config)
sudo apt purge nginx            # remove package + config
sudo apt autoremove             # remove unused dependencies
apt search keyword              # search for packages
apt show nginx                  # show package details
apt list --installed            # list installed packages
```

---

### 48. yum / dnf — Package Manager (RHEL/CentOS/Fedora)

**Definition:** yum (Yellowdog Updater Modified) and dnf (Dandified YUM) are package managers for Red Hat-based systems. dnf is the modern replacement for yum with better performance and dependency resolution.

```bash
sudo yum install httpd          # install package
sudo yum remove httpd           # remove package
sudo yum update                 # update all packages
yum search keyword              # search packages
yum info httpd                  # package details

# dnf (modern replacement)
sudo dnf install nginx
sudo dnf remove nginx
sudo dnf upgrade
dnf list installed
```

---

### 49. dpkg — Debian Package Manager

**Definition:** dpkg stands for **Debian Package**. It is the low-level package manager for .deb files. Unlike apt, it does not resolve dependencies automatically. Used for installing local .deb packages.

```bash
sudo dpkg -i package.deb       # install .deb file
sudo dpkg -r package            # remove package
sudo dpkg -l                    # list all installed packages
dpkg -l | grep nginx            # check if package installed
dpkg -s nginx                   # show package status
sudo dpkg --configure -a        # fix broken packages
```

---

## Category 10: Disk & Storage Commands

### 50. mount — Mount File Systems

**Definition:** mount attaches a file system (from a disk, partition, or USB) to a directory in the Linux file tree so it can be accessed. Without arguments, it shows all currently mounted file systems.

```bash
mount                               # show all mounted filesystems
sudo mount /dev/sdb1 /mnt/usb      # mount USB drive
sudo mount -t ext4 /dev/sda2 /data # mount with filesystem type
sudo mount -o ro /dev/sdb1 /mnt    # mount as read-only
mount | grep sda                    # check specific mounts
```

---

### 51. umount — Unmount File Systems

**Definition:** umount (not "unmount") detaches a mounted file system from the directory tree. Always unmount before physically removing a USB drive or external disk to prevent data corruption.

```bash
sudo umount /mnt/usb            # unmount by mount point
sudo umount /dev/sdb1           # unmount by device
sudo umount -l /mnt/usb        # lazy unmount (when busy)
sudo umount -f /mnt/nfs        # force unmount (NFS)
```

---

### 52. fdisk — Partition Table Manipulator

**Definition:** fdisk is a command-line utility for managing disk partition tables. It can create, delete, resize, and list partitions. Requires root privileges and extreme caution.

```bash
sudo fdisk -l                   # list all disks and partitions
sudo fdisk -l /dev/sda          # list partitions on specific disk
sudo fdisk /dev/sdb             # open interactive partition editor
```

**Interactive Commands:**
```
m → Help menu
p → Print partition table
n → Create new partition
d → Delete partition
w → Write changes and exit
q → Quit without saving
```

---

### 53. lsblk — List Block Devices

**Definition:** lsblk stands for **List Block Devices**. It displays all available block devices (hard drives, SSDs, USB drives, partitions) in a tree format showing their mount points and sizes.

```bash
lsblk                   # list all block devices
lsblk -f               # show filesystem type
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT  # custom columns
lsblk /dev/sda         # specific device only
```

**Output Example:**
```
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0   500G  0 disk
├─sda1   8:1    0   512M  0 part /boot
├─sda2   8:2    0   450G  0 part /
└─sda3   8:3    0    50G  0 part /home
```

---

## Category 11: Text Processing Commands

### 54. sort — Sort Lines of Text

**Definition:** sort arranges lines of text in a file alphabetically, numerically, or in reverse order. It can sort by specific columns and remove duplicates. Does not modify the original file.

```bash
sort file.txt               # alphabetical sort
sort -r file.txt            # reverse sort
sort -n numbers.txt         # numeric sort
sort -k 2 file.txt          # sort by 2nd column
sort -u file.txt            # sort and remove duplicates
sort -t "," -k 3 data.csv  # sort CSV by 3rd field
sort -h sizes.txt           # sort human-readable sizes (1K, 2M)
```

---

### 55. cut — Cut Sections from Lines

**Definition:** cut extracts specific columns or fields from each line of a file. It is useful for parsing structured text like CSV files, log files, or command output.

```bash
cut -c 1-5 file.txt         # characters 1 to 5
cut -c 1,3,5 file.txt       # specific characters
cut -d "," -f 2 data.csv    # 2nd field (comma delimiter)
cut -d ":" -f 1 /etc/passwd # usernames from passwd file
cut -d " " -f 1-3 file.txt  # first 3 space-separated fields
```

---

### 56. awk — Pattern Scanning and Processing

**Definition:** awk is a powerful text-processing language that scans files line by line, splits each line into fields, and performs actions based on patterns. Named after its creators (Aho, Weinberger, Kernighan).

```bash
awk '{print $1}' file.txt           # print first column
awk '{print $1, $3}' file.txt       # print 1st and 3rd columns
awk -F "," '{print $2}' data.csv    # CSV: print 2nd field
awk '/error/ {print}' log.txt       # print lines containing "error"
awk '{print NR, $0}' file.txt       # print with line numbers
awk '{sum += $1} END {print sum}' nums.txt  # sum first column
awk 'length > 80' file.txt          # lines longer than 80 chars
```

---

### 57. sed — Stream Editor

**Definition:** sed stands for **Stream Editor**. It performs text transformations on files or input streams — find and replace, insert, delete lines — without opening the file in an editor. Extremely useful for automation.

```bash
sed 's/old/new/' file.txt           # replace first occurrence per line
sed 's/old/new/g' file.txt          # replace all occurrences
sed -i 's/old/new/g' file.txt       # edit file in-place
sed -n '5,10p' file.txt             # print lines 5 to 10
sed '3d' file.txt                   # delete line 3
sed '/pattern/d' file.txt           # delete lines matching pattern
sed '2i\New line' file.txt          # insert text at line 2
sed 's/[0-9]//g' file.txt           # remove all numbers
```

---

### 58. wc — Word Count

**Definition:** wc stands for **Word Count**. It counts the number of lines, words, and characters (bytes) in a file. Useful for quick file statistics and in pipelines.

```bash
wc file.txt             # lines, words, characters
wc -l file.txt          # count lines only
wc -w file.txt          # count words only
wc -c file.txt          # count bytes
wc -m file.txt          # count characters
wc -l *.txt             # line count for multiple files
cat file.txt | wc -l    # count lines from pipe
```

---

### 59. diff — Compare Files Line by Line

**Definition:** diff compares two files line by line and shows the differences between them. It is essential for code reviews, patch creation, and verifying file changes.

```bash
diff file1.txt file2.txt        # show differences
diff -u file1.txt file2.txt     # unified format (like git diff)
diff -y file1.txt file2.txt     # side-by-side comparison
diff -r dir1/ dir2/             # compare directories recursively
diff -q file1 file2             # only report if files differ
diff --color file1 file2        # colorized output
```

**Output Symbols:**
```
<   → Line from file1
>   → Line from file2
--- → File1 header
+++ → File2 header
```

---

### 60. tee — Read from Input and Write to File

**Definition:** tee reads from standard input and writes to both standard output (screen) and one or more files simultaneously. Named after the T-splitter in plumbing.

```bash
echo "hello" | tee file.txt         # write to screen + file
echo "hello" | tee -a file.txt      # append instead of overwrite
command | tee output.log            # save command output + display
command | tee file1.txt file2.txt   # write to multiple files
ls -la | tee listing.txt | grep ".txt"  # chain with other commands
```

---

## Category 12: Network Diagnostics Commands

### 61. curl — Client URL

**Definition:** curl stands for **Client URL**. It transfers data to or from a server using various protocols (HTTP, HTTPS, FTP). More versatile than wget — supports uploads, headers, authentication, and API calls.

```bash
curl https://example.com            # fetch webpage content
curl -O https://example.com/file    # download file (keep name)
curl -o myfile.txt URL              # download with custom name
curl -I https://example.com         # show headers only
curl -X POST -d "data" URL         # send POST request
curl -H "Content-Type: application/json" URL  # custom header
curl -u user:pass URL               # basic authentication
curl -L URL                         # follow redirects
```

---

### 62. netstat — Network Statistics

**Definition:** netstat stands for **Network Statistics**. It displays network connections, routing tables, interface statistics, and listening ports. (Being replaced by `ss` on modern systems.)

```bash
netstat -tuln           # show listening ports (TCP/UDP)
netstat -an             # all connections (numeric)
netstat -tp             # TCP connections with process names
netstat -r              # routing table
netstat -i              # network interface statistics
netstat -s              # protocol statistics
netstat -plant          # all listening TCP with PIDs
```

---

### 63. ss — Socket Statistics

**Definition:** ss stands for **Socket Statistics**. It is the modern replacement for netstat — faster and more detailed. It displays information about network sockets including TCP, UDP, and Unix sockets.

```bash
ss -tuln                # listening TCP/UDP ports
ss -t                   # all TCP connections
ss -u                   # all UDP connections
ss -p                   # show process using socket
ss -s                   # summary statistics
ss state established    # only established connections
ss -o                   # show timer information
```

---

### 64. traceroute — Trace Packet Route

**Definition:** traceroute shows the path (route) that packets take from your computer to a destination host. It displays each hop (router) along the way with response times, useful for diagnosing network issues.

```bash
traceroute google.com           # trace route to host
traceroute -n google.com        # numeric only (skip DNS)
traceroute -m 20 google.com    # max 20 hops
traceroute -w 3 google.com     # 3 second timeout per hop
traceroute -p 443 google.com   # use specific port
```

---

### 65. nslookup — Name Server Lookup

**Definition:** nslookup queries DNS (Domain Name System) servers to find the IP address of a domain name or the domain name of an IP address. Essential for DNS troubleshooting.

```bash
nslookup google.com             # find IP of domain
nslookup 8.8.8.8               # reverse lookup (IP to domain)
nslookup google.com 8.8.8.8    # query specific DNS server
nslookup -type=MX gmail.com    # find mail servers
nslookup -type=NS example.com  # find name servers
nslookup -type=A example.com   # find A records (IPv4)
```

---

## Category 13: Service & Daemon Commands

### 66. systemctl — System Control (systemd)

**Definition:** systemctl is the primary command for managing systemd services (daemons) on modern Linux systems. It starts, stops, enables, disables, and checks the status of services.

```bash
sudo systemctl start nginx      # start service
sudo systemctl stop nginx       # stop service
sudo systemctl restart nginx    # restart service
sudo systemctl reload nginx     # reload config without restart
sudo systemctl status nginx     # check service status
sudo systemctl enable nginx     # start on boot
sudo systemctl disable nginx    # don't start on boot
systemctl list-units --type=service  # list all services
```

---

### 67. journalctl — Query systemd Journal Logs

**Definition:** journalctl is used to view logs collected by systemd's journal. It provides powerful filtering by service, time, priority, and more. Replaces traditional syslog for systemd-based systems.

```bash
journalctl                          # all logs
journalctl -u nginx                 # logs for specific service
journalctl -f                       # follow logs in real-time
journalctl --since "1 hour ago"     # logs from last hour
journalctl --since "2026-05-28"     # logs since specific date
journalctl -p err                   # only error-level logs
journalctl -b                       # logs since last boot
journalctl --disk-usage             # check log storage size
```

---

### 68. crontab — Schedule Recurring Tasks

**Definition:** crontab (cron table) is used to schedule commands or scripts to run automatically at specified intervals. Each user has their own crontab. Essential for automation and maintenance tasks.

```bash
crontab -e              # edit your crontab
crontab -l              # list your scheduled jobs
crontab -r              # remove all your cron jobs
sudo crontab -u john -l # view another user's crontab
```

**Cron Format:**
```
* * * * * command
│ │ │ │ │
│ │ │ │ └── Day of week (0-7, Sun=0 or 7)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

**Examples:**
```bash
0 2 * * * /backup.sh        # daily at 2:00 AM
*/5 * * * * /check.sh       # every 5 minutes
0 9 * * 1 /report.sh       # every Monday at 9 AM
0 0 1 * * /monthly.sh      # first day of every month
```

---

## Category 14: File Transfer & Sync Commands

### 69. scp — Secure Copy

**Definition:** scp stands for **Secure Copy**. It copies files between hosts over an encrypted SSH connection. It works like cp but across networks. Simple and secure for one-time file transfers.

```bash
scp file.txt user@host:/path/          # upload to remote
scp user@host:/path/file.txt ./        # download from remote
scp -r folder/ user@host:/path/        # copy directory recursively
scp -P 2222 file.txt user@host:/path/  # custom SSH port
scp user1@host1:/f user2@host2:/f      # copy between two remotes
```

---

### 70. rsync — Remote Sync

**Definition:** rsync stands for **Remote Sync**. It efficiently synchronizes files between locations (local or remote). It only transfers changed portions of files, making it faster than scp for repeated transfers and backups.

```bash
rsync -av source/ dest/                     # sync locally
rsync -av folder/ user@host:/backup/        # sync to remote
rsync -av user@host:/data/ ./local/         # sync from remote
rsync -avz folder/ user@host:/path/         # compress during transfer
rsync -av --delete source/ dest/            # mirror (delete extra files)
rsync -av --exclude="*.log" src/ dest/      # exclude patterns
rsync -avP large_file user@host:/path/      # show progress
```

**Flags:**
```
-a → Archive mode (preserves permissions, timestamps)
-v → Verbose
-z → Compress during transfer
-P → Show progress + allow resume
--delete → Remove files in dest not in source
```

---

## Category 15: Environment & Shell Commands

### 71. echo — Display Text / Variables

**Definition:** echo prints text or variable values to the terminal. It is widely used in shell scripts for displaying messages, writing to files, and debugging. Supports escape characters with `-e` flag.

```bash
echo "Hello World"              # print text
echo $HOME                      # print variable value
echo $PATH                      # show PATH variable
echo -n "no newline"            # print without trailing newline
echo -e "line1\nline2"          # interpret escape characters
echo "text" > file.txt          # write to file (overwrite)
echo "text" >> file.txt         # append to file
```

---

### 72. export — Set Environment Variables

**Definition:** export sets environment variables that are available to the current shell session and all child processes. Without export, a variable is only available in the current shell.

```bash
export MY_VAR="hello"           # set and export variable
export PATH=$PATH:/new/path     # add to PATH
export JAVA_HOME=/usr/lib/jvm/java-11
export -p                       # list all exported variables
unset MY_VAR                    # remove variable
```

> Add to `~/.bashrc` or `~/.bash_profile` for permanent variables.

---

### 73. alias — Create Command Shortcuts

**Definition:** alias creates a shortcut name for a longer command. It saves time for frequently used commands. Aliases are temporary unless added to shell configuration files like `.bashrc`.

```bash
alias ll='ls -la'               # create alias
alias gs='git status'           # git shortcut
alias rm='rm -i'                # always ask before delete
alias ..='cd ..'                # quick parent directory
alias cls='clear'               # clear screen shortcut
unalias ll                      # remove alias
alias                           # list all aliases
```

---

### 74. history — Command History

**Definition:** history displays the list of previously executed commands in the current shell session. It allows re-running past commands and searching through command history.

```bash
history                 # show all history
history 20              # show last 20 commands
history | grep ssh      # search history
!50                     # re-run command number 50
!!                      # re-run last command
!ssh                    # re-run last command starting with "ssh"
history -c              # clear history
```

---

### 75. source — Execute Script in Current Shell

**Definition:** source (or `.`) reads and executes commands from a file in the current shell environment. Unlike running a script normally, changes made (variables, aliases) persist in the current session.

```bash
source ~/.bashrc            # reload bash config
source .env                 # load environment variables
. ~/.bash_profile           # same as source (dot notation)
source myscript.sh          # run script in current shell
```

---

### 76. env — Display Environment Variables

**Definition:** env displays all current environment variables or runs a command in a modified environment. Useful for debugging, checking configurations, and running programs with temporary variable changes.

```bash
env                         # show all environment variables
env | grep PATH             # filter specific variable
env -i command              # run command with empty environment
env VAR=value command       # run command with temporary variable
printenv HOME               # print specific variable
```

---

## Category 16: I/O Redirection & Piping

### 77. Redirection Operators — >, >>, <, 2>

**Definition:** Redirection operators control where command input comes from and where output goes. They redirect standard output (stdout), standard error (stderr), and standard input (stdin) to/from files.

```bash
command > file.txt          # redirect stdout to file (overwrite)
command >> file.txt         # redirect stdout to file (append)
command < input.txt         # use file as stdin
command 2> error.log        # redirect stderr to file
command 2>&1                # redirect stderr to stdout
command > out.txt 2>&1      # redirect both stdout + stderr
command &> all.log          # shorthand: redirect both to file
```

**File Descriptors:**
```
0 → stdin  (standard input)
1 → stdout (standard output)
2 → stderr (standard error)
```

---

### 78. Pipe Operator — |

**Definition:** The pipe operator `|` sends the output of one command as input to another command. It allows chaining multiple commands together to create powerful data processing pipelines.

```bash
ls -la | grep ".txt"            # filter ls output
cat file.txt | sort | uniq      # sort and remove duplicates
ps aux | grep nginx             # find nginx processes
history | tail -20              # last 20 commands
cat log.txt | wc -l             # count lines in file
du -sh * | sort -hr | head -5   # top 5 largest items
dmesg | less                    # view kernel messages paginated
```

---

### 79. xargs — Build and Execute Commands from Input

**Definition:** xargs reads items from standard input and executes a command with those items as arguments. Essential for converting piped output into command arguments, especially with find.

```bash
find . -name "*.log" | xargs rm          # delete found files
find . -name "*.txt" | xargs grep "error"  # search in found files
echo "f1 f2 f3" | xargs touch           # create multiple files
cat urls.txt | xargs wget                # download list of URLs
find . -name "*.tmp" | xargs -I {} mv {} /tmp/  # move with placeholder
echo "1 2 3" | xargs -n 1               # one argument per line
```

---

## Category 17: System Monitoring Commands

### 80. htop — Interactive Process Viewer

**Definition:** htop is an enhanced, colorful, interactive process viewer. It is a modern alternative to top with mouse support, easier process management, and a more user-friendly interface. (May need installation.)

```bash
htop                    # open interactive viewer
htop -u john            # show only john's processes
htop -p 1234,5678      # monitor specific PIDs
htop -t                 # tree view (show parent-child)
```

**Controls:**
```
F2        → Setup/Config
F3        → Search process
F4        → Filter
F5        → Tree view
F6        → Sort by column
F9        → Kill process
F10       → Quit
Space     → Tag process
```

---

### 81. vmstat — Virtual Memory Statistics

**Definition:** vmstat stands for **Virtual Memory Statistics**. It reports system performance data including processes, memory, swap, I/O, and CPU activity. Useful for identifying system bottlenecks.

```bash
vmstat                  # one-time snapshot
vmstat 2                # update every 2 seconds
vmstat 2 10             # update every 2 sec, 10 times
vmstat -s               # memory statistics summary
vmstat -d               # disk statistics
```

**Output Columns:**
```
procs: r (running), b (blocked)
memory: swpd, free, buff, cache
swap: si (swap in), so (swap out)
io: bi (blocks in), bo (blocks out)
cpu: us (user), sy (system), id (idle), wa (wait)
```

---

### 82. iostat — I/O Statistics

**Definition:** iostat stands for **Input/Output Statistics**. It monitors system I/O device loading by observing the time devices are active relative to their average transfer rates. Part of the `sysstat` package.

```bash
iostat                  # basic CPU and I/O stats
iostat -x               # extended statistics
iostat 2 5              # update every 2 sec, 5 times
iostat -d               # device statistics only
iostat -p sda           # specific device stats
iostat -m               # display in MB/s
```

---

### 83. dmesg — Display Kernel Messages

**Definition:** dmesg stands for **Display Message**. It prints the kernel ring buffer messages — hardware detection, driver loading, errors, and system events since boot. Essential for hardware troubleshooting.

```bash
dmesg                       # all kernel messages
dmesg | tail -20            # last 20 messages
dmesg | grep -i error       # find errors
dmesg | grep -i usb         # USB device messages
dmesg -T                    # human-readable timestamps
dmesg --level=err           # only error level
sudo dmesg -c               # clear ring buffer
```

---

### 84. lsof — List Open Files

**Definition:** lsof stands for **List Open Files**. In Linux, everything is a file (including network connections, devices, pipes). lsof shows which files are opened by which processes — invaluable for debugging.

```bash
lsof                            # all open files (huge output)
lsof -u john                    # files opened by user john
lsof -i :80                     # processes using port 80
lsof -i :443                    # processes using port 443
lsof -p 1234                    # files opened by PID 1234
lsof /var/log/syslog            # who is using this file
lsof -i TCP                     # all TCP connections
lsof +D /home/john/             # all open files in directory
```

---

### 85. nmon — Nigel's Performance Monitor

**Definition:** nmon is an interactive system performance monitoring tool that displays CPU, memory, network, disk, and process information in a single dashboard. Excellent for real-time server monitoring.

```bash
nmon                    # open interactive monitor
```

**Controls:**
```
c → CPU stats
m → Memory stats
d → Disk stats
n → Network stats
t → Top processes
q → Quit
```

---

## Category 18: File Link Commands

### 86. ln — Create Links

**Definition:** ln stands for **Link**. It creates links between files. A hard link is another name for the same file data. A symbolic (soft) link is a pointer/shortcut to another file path.

```bash
ln file.txt hardlink.txt            # create hard link
ln -s /path/to/file symlink.txt     # create symbolic link
ln -s /path/to/dir linkdir          # symlink to directory
ln -sf /new/target symlink.txt      # force overwrite existing link
ls -l symlink.txt                   # verify link target
readlink symlink.txt                # show where symlink points
```

**Differences:**
```
Hard Link:
  - Points to same inode (file data)
  - Cannot link to directories
  - Cannot cross filesystems
  - Original deletion doesn't break it

Symbolic Link:
  - Points to file path (like shortcut)
  - Can link to directories
  - Can cross filesystems
  - Breaks if original is deleted
```

---

## Category 19: Firewall & Security Commands

### 87. iptables — IP Packet Filter Rules

**Definition:** iptables is the traditional Linux firewall tool. It filters network packets based on rules you define — allowing, blocking, or redirecting traffic based on IP, port, protocol, and more.

```bash
sudo iptables -L                        # list all rules
sudo iptables -L -n -v                  # detailed with numbers
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # allow HTTP
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT  # allow HTTPS
sudo iptables -A INPUT -s 192.168.1.100 -j DROP      # block IP
sudo iptables -D INPUT 3               # delete rule number 3
sudo iptables -F                        # flush (delete) all rules
sudo iptables-save > /etc/iptables.rules  # save rules
```

---

### 88. ufw — Uncomplicated Firewall

**Definition:** ufw stands for **Uncomplicated Firewall**. It is a user-friendly frontend for iptables, designed to make firewall management simple. Default on Ubuntu systems.

```bash
sudo ufw status                 # check firewall status
sudo ufw enable                 # enable firewall
sudo ufw disable                # disable firewall
sudo ufw allow 22               # allow SSH
sudo ufw allow 80/tcp           # allow HTTP
sudo ufw allow 443/tcp          # allow HTTPS
sudo ufw deny 3306              # block MySQL port
sudo ufw delete allow 80        # remove rule
sudo ufw allow from 192.168.1.0/24  # allow subnet
sudo ufw status numbered        # show rules with numbers
```

---

### 89. fail2ban — Intrusion Prevention

**Definition:** fail2ban monitors log files for suspicious activity (like repeated failed login attempts) and automatically bans offending IP addresses using firewall rules. Protects against brute-force attacks.

```bash
sudo systemctl start fail2ban       # start service
sudo systemctl status fail2ban      # check status
sudo fail2ban-client status         # show active jails
sudo fail2ban-client status sshd    # SSH jail details
sudo fail2ban-client set sshd banip 1.2.3.4    # manually ban IP
sudo fail2ban-client set sshd unbanip 1.2.3.4  # unban IP
sudo fail2ban-client reload         # reload configuration
```

---

## Category 20: Miscellaneous Utility Commands

### 90. watch — Execute Command Repeatedly

**Definition:** watch runs a command repeatedly at regular intervals (default 2 seconds) and displays the output full-screen. Useful for monitoring changing data like disk usage, processes, or network status.

```bash
watch df -h                 # monitor disk space every 2s
watch -n 5 free -h          # memory usage every 5 seconds
watch -d ls -la             # highlight differences
watch -n 1 "ps aux | wc -l"  # count processes every second
watch -g command            # exit when output changes
```

---

### 91. screen — Terminal Multiplexer

**Definition:** screen allows you to create multiple virtual terminal sessions within one SSH connection. Sessions persist even if you disconnect, making it ideal for long-running processes on remote servers.

```bash
screen                      # start new session
screen -S mysession         # start named session
screen -ls                  # list all sessions
screen -r mysession         # reattach to session
screen -d -r mysession      # detach elsewhere and reattach here
```

**Controls:**
```
Ctrl+A, D     → Detach from session
Ctrl+A, C     → Create new window
Ctrl+A, N     → Next window
Ctrl+A, P     → Previous window
Ctrl+A, K     → Kill current window
Ctrl+A, "     → List windows
```

---

### 92. tmux — Terminal Multiplexer (Modern)

**Definition:** tmux is a modern terminal multiplexer — more powerful than screen. It allows splitting terminals into panes, creating multiple windows, and maintaining persistent sessions across disconnections.

```bash
tmux                        # start new session
tmux new -s mysession       # start named session
tmux ls                     # list sessions
tmux attach -t mysession    # attach to session
tmux kill-session -t name   # kill session
```

**Controls (prefix: Ctrl+B):**
```
Ctrl+B, D     → Detach
Ctrl+B, C     → New window
Ctrl+B, %     → Split vertically
Ctrl+B, "     → Split horizontally
Ctrl+B, N     → Next window
Ctrl+B, P     → Previous window
Ctrl+B, Arrow → Switch pane
Ctrl+B, X     → Close pane
```

---

### 93. at — Schedule One-Time Task

**Definition:** at schedules a command or script to run once at a specific future time. Unlike crontab (recurring), at is for one-time scheduled execution.

```bash
at 10:00 AM                     # schedule for 10 AM today
at 2:30 PM tomorrow             # schedule for tomorrow
at now + 30 minutes             # 30 minutes from now
at now + 2 hours                # 2 hours from now
atq                             # list pending jobs
atrm 3                          # remove job number 3
```

**Usage:**
```bash
at 3:00 PM
> /home/user/backup.sh
> Ctrl+D                        # press Ctrl+D to save
```

---

### 94. cal — Display Calendar

**Definition:** cal displays a simple calendar in the terminal. It can show the current month, a specific month, or an entire year. Useful for quick date reference without leaving the terminal.

```bash
cal                     # current month
cal 2026                # entire year 2026
cal 6 2026              # June 2026
cal -3                  # previous, current, next month
cal -y                  # full current year
ncal                    # alternative layout (weeks vertical)
```

---

### 95. bc — Basic Calculator

**Definition:** bc stands for **Basic Calculator**. It is a command-line calculator that supports arbitrary precision arithmetic, variables, and mathematical functions. Useful in scripts for calculations.

```bash
echo "5 + 3" | bc              # basic addition: 8
echo "10 / 3" | bc             # integer division: 3
echo "scale=2; 10/3" | bc      # decimal division: 3.33
echo "2^10" | bc               # power: 1024
echo "sqrt(144)" | bc -l       # square root: 12
echo "ibase=2; 1010" | bc      # binary to decimal: 10
```

**Interactive mode:**
```bash
bc -l           # open calculator with math library
scale=4         # set decimal places
3.14 * 5^2     # calculate area
quit            # exit
```

---

### 96. clear — Clear Terminal Screen

**Definition:** clear clears all visible text from the terminal screen, giving you a fresh view. The command history and previous output still exist — they are just scrolled out of view.

```bash
clear               # clear screen
clear -x            # clear without scrollback
reset               # full terminal reset (fixes garbled display)
# Shortcut: Ctrl+L  (same as clear)
```

---

### 97. shutdown — Power Off or Restart System

**Definition:** shutdown safely powers off or restarts the system. It notifies logged-in users, stops services gracefully, and syncs filesystems before halting. Preferred over direct power-off.

```bash
sudo shutdown now               # shutdown immediately
sudo shutdown -h now            # halt immediately
sudo shutdown -h +10            # shutdown in 10 minutes
sudo shutdown -h 22:00          # shutdown at 10 PM
sudo shutdown -r now            # restart immediately
sudo shutdown -r +5 "Rebooting for updates"  # restart with message
sudo shutdown -c                # cancel scheduled shutdown
sudo reboot                     # shortcut for restart
sudo poweroff                   # shortcut for power off
```

---

### 98. w — Who is Logged In and What They're Doing

**Definition:** w displays information about currently logged-in users and their activities. It shows username, terminal, login time, idle time, and the command they are currently running.

```bash
w                   # show all logged-in users
w john              # show specific user only
```

**Output Example:**
```
USER   TTY    FROM           LOGIN@  IDLE  WHAT
john   pts/0  192.168.1.5   09:30   0.00s vim app.py
alice  pts/1  192.168.1.10  10:15   5:00  top
```

---

### 99. id — Display User Identity

**Definition:** id displays the user ID (UID), group ID (GID), and all group memberships of the current or specified user. Useful for verifying permissions and group access.

```bash
id                  # current user's UID, GID, groups
id john             # specific user's info
id -u               # just UID number
id -g               # just primary GID
id -G               # all group IDs
id -nG              # all group names
```

**Output Example:**
```
uid=1000(john) gid=1000(john) groups=1000(john),27(sudo),44(video),100(users)
```

---

### 100. man — Manual Pages

**Definition:** man stands for **Manual**. It displays the official documentation (manual page) for any Linux command. It is the built-in help system — the first place to look when you need detailed information about a command.

```bash
man ls              # manual for ls command
man chmod           # manual for chmod
man -k keyword      # search manuals by keyword
man 5 passwd        # specific section (5 = file formats)
man -f command      # one-line description (whatis)
```

**Navigation:**
```
Space       → Next page
b           → Previous page
/keyword    → Search forward
n           → Next search result
q           → Quit
```

**Manual Sections:**
```
1 → User commands
2 → System calls
3 → Library functions
4 → Special files
5 → File formats
6 → Games
7 → Miscellaneous
8 → System admin commands
```

---

## Master Summary Table

| # | Command | Full Form | Purpose |
|---|---------|-----------|---------|
| 1 | ls | List | List directory contents |
| 2 | cd | Change Directory | Navigate directories |
| 3 | pwd | Print Working Directory | Show current path |
| 4 | mkdir | Make Directory | Create folders |
| 5 | rmdir | Remove Directory | Delete empty folders |
| 6 | touch | — | Create file / update timestamp |
| 7 | cp | Copy | Copy files/folders |
| 8 | mv | Move | Move or rename |
| 9 | rm | Remove | Delete files/folders |
| 10 | find | — | Search files |
| 11 | cat | Concatenate | Display file content |
| 12 | more | — | Page-by-page viewer |
| 13 | less | — | Scrollable viewer |
| 14 | head | — | Show first lines |
| 15 | tail | — | Show last lines |
| 16 | grep | Global Reg. Exp. Print | Search text patterns |
| 17 | nano | — | Simple text editor |
| 18 | vim | Vi Improved | Advanced text editor |
| 19 | chmod | Change Mode | Change permissions |
| 20 | chown | Change Owner | Change file owner |
| 21 | chgrp | Change Group | Change group |
| 22 | uname | Unix Name | System info |
| 23 | whoami | — | Current user |
| 24 | hostname | — | Machine name |
| 25 | uptime | — | How long system running |
| 26 | date | — | Current date/time |
| 27 | df | Disk Free | Partition disk usage |
| 28 | du | Disk Usage | File/folder size |
| 29 | free | — | RAM usage |
| 30 | ps | Process Status | List processes |
| 31 | top | — | Live process monitor |
| 32 | kill | — | Kill process by PID |
| 33 | killall | — | Kill by process name |
| 34 | bg/fg | Background/Foreground | Job control |
| 35 | ping | — | Test connectivity |
| 36 | ifconfig | Interface Config | Network info |
| 37 | wget | Web Get | Download files |
| 38 | ssh | Secure Shell | Remote login |
| 39 | tar | Tape Archive | Archive files |
| 40 | zip/unzip | — | Compress/extract ZIP |
| 41 | useradd | User Add | Create new user |
| 42 | usermod | User Modify | Modify user account |
| 43 | userdel | User Delete | Delete user account |
| 44 | passwd | Password | Change password |
| 45 | su | Switch User | Switch user account |
| 46 | sudo | Superuser Do | Run as root |
| 47 | apt | Advanced Package Tool | Package manager (Debian) |
| 48 | yum/dnf | Yellowdog Updater / Dandified YUM | Package manager (RHEL) |
| 49 | dpkg | Debian Package | Install .deb files |
| 50 | mount | — | Mount file systems |
| 51 | umount | — | Unmount file systems |
| 52 | fdisk | Fixed Disk | Manage partitions |
| 53 | lsblk | List Block Devices | Show disks/partitions |
| 54 | sort | — | Sort lines of text |
| 55 | cut | — | Extract columns/fields |
| 56 | awk | Aho Weinberger Kernighan | Text processing language |
| 57 | sed | Stream Editor | Find/replace in files |
| 58 | wc | Word Count | Count lines/words/chars |
| 59 | diff | Difference | Compare files |
| 60 | tee | — | Write to file + screen |
| 61 | curl | Client URL | Transfer data (HTTP/API) |
| 62 | netstat | Network Statistics | Show network connections |
| 63 | ss | Socket Statistics | Modern netstat replacement |
| 64 | traceroute | — | Trace packet route |
| 65 | nslookup | Name Server Lookup | DNS query tool |
| 66 | systemctl | System Control | Manage services |
| 67 | journalctl | Journal Control | View system logs |
| 68 | crontab | Cron Table | Schedule recurring tasks |
| 69 | scp | Secure Copy | Copy files over SSH |
| 70 | rsync | Remote Sync | Sync files efficiently |
| 71 | echo | — | Display text/variables |
| 72 | export | — | Set environment variables |
| 73 | alias | — | Create command shortcuts |
| 74 | history | — | Command history |
| 75 | source | — | Execute script in current shell |
| 76 | env | Environment | Display environment variables |
| 77 | >, >>, < | Redirection | I/O redirection |
| 78 | \| | Pipe | Chain commands together |
| 79 | xargs | Extended Arguments | Build commands from input |
| 80 | htop | — | Interactive process viewer |
| 81 | vmstat | Virtual Memory Stats | System performance data |
| 82 | iostat | I/O Statistics | Disk I/O monitoring |
| 83 | dmesg | Display Message | Kernel messages |
| 84 | lsof | List Open Files | Show open files/ports |
| 85 | nmon | Nigel's Monitor | System performance dashboard |
| 86 | ln | Link | Create hard/symbolic links |
| 87 | iptables | IP Tables | Firewall rules |
| 88 | ufw | Uncomplicated Firewall | Simple firewall management |
| 89 | fail2ban | — | Intrusion prevention |
| 90 | watch | — | Repeat command periodically |
| 91 | screen | — | Terminal multiplexer |
| 92 | tmux | Terminal Multiplexer | Modern terminal multiplexer |
| 93 | at | — | Schedule one-time task |
| 94 | cal | Calendar | Display calendar |
| 95 | bc | Basic Calculator | Command-line calculator |
| 96 | clear | — | Clear terminal screen |
| 97 | shutdown | — | Power off/restart system |
| 98 | w | — | Who is logged in |
| 99 | id | Identity | Display user UID/GID |
| 100 | man | Manual | Command documentation |
