
## Calculate the Hashes for the File 

First, click ```Cleanup``` to remove any previous work.

{Cleanup}(sh hash/cleanup.sh)

Upload the file you just downloaded into the hash-lab folder, in the file tree to the left, as follows:

 - Right-click on ```hash-lab``` and select the ```Upload``` option from the menu.
 
 - Select the ```Upload...``` option from the Upload file dialog. 
   The UPLOAD FILES dialog opens
 
 - Click the ```Browse For Files``` option in the dialog
   Another Dialog opens showing files on your computer, including the file that you just downloaded.
 
 - Click on that file (e.g., ```Apache_OpenOffice_4.1.3_Win_x86_langpack_en-US.exe``` and select Open

 - Click the ```CLOSE``` button in the UPLOAD FILES dialog.

You should see the file in the ```hash-lab``` folder in the file tree on the left. (However, you may first need to click on the ```hash-lab``` folder to see its contents.) Now you can use you partner's public key to encrypt messages to send over a public channel, like the Internet.

 - Click the ```Calculate hashes``` button below and the MD5 and SHA256 hashes will be displayed below.

{Calculate hashes}(python hash/hashfile.py hash-lab)

 - Enter the hash values below.
 
{Save!|assessment}(free-text-2244206358)

{Save!|assessment}(free-text-1127751824)


 - Go to the source web site for the file you downloaded: **[click here.](open_preview https://www.openoffice.org/download/index.html panel=0)** 

 - Notice that the site includes **links for MD5 and SHA256 hashes of the file.** Now proceed to the lab's next step, in which you'll download those hash values so that you can compare them to the hash values you calculated in this step.
