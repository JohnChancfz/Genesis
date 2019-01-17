#
if __name__ == '__main__':

    print 'Genesis start...'
    f = open("./files/item.md")
    i = 0
    for line in f.readlines():
        i = i + 1
        if i <= 3:
            continue
        print "line = ", line
        elements = line.split("|")
        print "elements = ", elements
        name = elements[0].strip()
        type = elements[1].strip()
        #
        default = elements[2].strip()
        remark = elements[3].strip()

        if type.lower() in ['string', 'text', 'varchar']:
            print 'private String ' + name + ";"

        if type == 'int' or type == 'Integer':
            print 'private Integer ' + name + ";"
