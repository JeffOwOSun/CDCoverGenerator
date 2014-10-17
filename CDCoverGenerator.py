from __future__ import division
import sys
from PIL import Image
import time
from os.path import splitext

def main():
    try:
        files=sys.argv[1:]
    except IndexError:
        print "Please drag and drop your original cover scan onto the .py file"
        raw_input("Press ENTER to continue...")
        return
        
    for infile in files:
        try:
            img = Image.open(infile)        
        except Exception as e:
            print "Error opening file %s, %s!" % infile, e
            continue
        
        flagResized = False
        img.width, img.height = img.size
        if img.width>1.8*img.height:
            img = img.crop((img.width - img.height, 0, img.width, img.height))
            img.width, img.height = img.size
            
        if img.width>1000 or img.height >1000:
            ratio = min(1000/img.width, 1000/img.height)
            size = ratio*img.width, ratio*img.height
            try:
                img.thumbnail(size, Image.ANTIALIAS)
            except Exception as e:
                print e
            flagResized = True
            
        f, ext = splitext(infile)
        #if format is different, no matter resized or not, directly save
        if ext.lower() != ".jpg":
            try:
                outfile = f + ".jpg"
                img.save(outfile)
            except IOError as e:
                print "cannot save %s, %s!" % infile, e
                continue
        #if format is the same, but resized, then rename the outfile as infile_small.jpg
        elif flagResized:
            try:
                outfile = f + "_small.jpg"
                img.save(outfile)
            except IOError as e:
                print "cannot save %s, %s!" % infile, e
                continue
        #format is still the same, and unresized, then no processing is required.
        else:
            print "the file %s is already in jpg format and resized!" % infile
            continue
            
    #print img.format, img.size, img.mode
    
    #print img.width, img.height
if __name__=="__main__":
    main()
    #time.sleep(5)