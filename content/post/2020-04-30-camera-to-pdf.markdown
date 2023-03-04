---
layout: post
title:  "Digital Archiving: Camera to PDF"
date:   2020-04-30 12:00:33 -0700
categories: Blog update 
---

I wanted to get a system up and running for scanning my own books and documents into digital, primarily PDF formats, without being destructive or expensive, and I have managed to take care of that today. I set a camera up on a tripod, rested a book on a cardboard rest at a 45 degree angle, and captured every page behind a sheet of glass as I turned the pages. Once I took the pictures of the individual pages, I loaded them onto my computer, and cleaned the pages up with scantailor, a program that can change the files to clean up lighting, orientation, margins etc. I found that this program worked pretty good with the defaults, and dumped every page into .tif files. The images could converted into individual pdfs with tiff2pdf, another free tool that worked well with a script to convert it all over. Lastly, I had to combine all of the individual PDF pages into the finished document; this was the hardest step for me. I had taken pictures of every file on one side, then the other, so my pages were out of order. I then had to use pdfunite to alternate the page numbers, which I did manually. For anything longer than what I did, I would have worked on getting the page numbers sequentially, or work out a good way to script it out. 

Overall, it was a good experience and something I will be doing more of. Stay tuned, for more advanced or in-depth write-ups of procedures and tooling.
