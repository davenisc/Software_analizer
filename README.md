# Software_analizer
With this script you can optimize your time, do a quick analysis before analyzing, with other tools that may take a little  more time to give you a result. 

I have integrated two of my scripts, Software analizer and RegShot Filter to obtain more information about the analyzed software, for this I must make use of a Windows virtual machine to obtain the result of RegShot in a doc.txt, in this way Software analizer with RegShot Filter help will give the information found.

<a href="https://ibb.co/Dfmjsg3"><img src="https://i.ibb.co/hFrTh1p/1.jpg" alt="1" border="0"></a>

<a href="https://ibb.co/Xb7n214"><img src="https://i.ibb.co/bPs4WT3/2.jpg" alt="2" border="0"></a>

<a href="https://ibb.co/mCsHHQv"><img src="https://i.ibb.co/5WD55qY/3.jpg" alt="3" border="0"></a>

<a href="https://ibb.co/r2BtC13"><img src="https://i.ibb.co/1GCnDwM/4.jpg" alt="4" border="0"></a>

<a href="https://ibb.co/dthCRbt"><img src="https://i.ibb.co/jzp0SVz/5.jpg" alt="5" border="0"></a>


It is recommended to use Kali Linux to use this script, since this operating system already has 98% of the tools and libraries used by Software_Analizer.py v 1.2.0 otherwise you must install the following:

bookstores

1. pip install PrettyTable
2. pip install tqdm
3. pip install colorama


Tools

1. md5sum
2. automater
3. exiftool
4. strings
5. sha256sum
6. sha1sum
7. Type


To install Exiftool follow the next steps:

1. Download https://www.sno.phy.queensu.ca/~phil/exiftool/index.html 
current version V 11.03
2. cd (your download directory)
3. gzip -dc Image-ExifTool-11.03.tar.gz | tar -xf -
4. cd Image-ExifTool-11.03
5. perl Makefile.PL
6. make test
7. sudo make install
  
more information: https://www.sno.phy.queensu.ca/~phil/exiftool/install.html
  

https://www.youtube.com/watch?v=J8Iigh68RJg

This script is free! automates tools such as exiftool, automater and md5sum to be able to function

For questions and suggestions you can contact me at info@davenisc.com or on Twitter @DaveNISC
