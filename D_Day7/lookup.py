import re
import optparse,sys

def Main():
    parser=optparse.OptionParser("lookup.py -w word -f filename ")

    parser.add_option('-w',dest='word' ,type='string',help='specify a word to search for')
    parser.add_option('-f',dest='fname',type='string',help='specify a file to search')

    (options,args)=parser.parse_args()
    

    if (options.word==None)| (options.fname==None):
        print parser.usage
        sys.exit()

    else:
        word=options.word
        fname=options.fname

    searchfile=open(fname,"r")
    linenum=0

    for line in searchfile.readlines():
        line=line.strip('\n\r')
        linenum +=1

        searchres=re.search(word,line,re.M|re.I)

        if searchres:
            print str(linenum)+':'+line



if __name__ == '__main__':
    Main()
    
