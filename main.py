#
if __name__ == '__main__':

    print 'Genesis start...'
    f = open("./files/item.md")

    for line in f.readlines():
        print line
