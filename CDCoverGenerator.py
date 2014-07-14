import sys
import Image
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
        if img.width>1000 or img.height >1000:
            whRatio = img.width/img.height
            outWidth = 1000 if whRatio >=1 else 1000*whRatio
            outHeight = 1000 if whRatio <=1 else 1000/whRatio
            try:
                img=img.resize((outWidth, outHeight))
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