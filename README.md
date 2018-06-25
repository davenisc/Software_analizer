# Software_analizer
With this script you can optimize your time, do a quick analysis before analyzing, with other tools that may take a little  more time to give you a result. 

I have integrated two of my scripts, Software analizer and RegShot Filter to obtain more information about the analyzed software, for this I must make use of a Windows virtual machine to obtain the result of RegShot in a doc.txt, in this way Software analizer with RegShot Filter help will give the information found.

<a href="https://ibb.co/faHZAT"><img src="https://preview.ibb.co/dJ8wPo/Software_analizer.jpg" alt="Software_analizer" border="0"></a><br /><a target='_blank' href=''></a><br />

<a href="https://ibb.co/dJcvH8"><img src="https://preview.ibb.co/hXFhx8/Software_analizer2.jpg" alt="Software_analizer2" border="0"></a><br /><a target='_blank' href=''></a><br />

<a href="https://ibb.co/i0sZAT"><img src="https://preview.ibb.co/hy9sx8/Software_analizer3.jpg" alt="Software_analizer3" border="0"></a><br /><a target='_blank' href=''></a><br />

<a href="https://ibb.co/cDWcVT"><img src="https://preview.ibb.co/kg2Uc8/Software_analizer4.jpg" alt="Software_analizer4" border="0"></a><br /><a target='_blank' href=''></a><br />


It is recommended to use Kali Linux to use this script, since this operating system already has 98% of the tools and libraries used by Software_Analizer.py v 1.0.0 otherwise you must install the following:

bookstores

1. pip install PrettyTable
2. pip install tqdm
3. pip install colorama


Tools

1. md5sum
2. automater
3. exiftool


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

For questions and suggestions you can contact me at sysvd@protonmail.com or on Twitter @DaveNISC
