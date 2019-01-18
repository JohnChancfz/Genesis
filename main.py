#
if __name__ == '__main__':

    print 'Genesis start...'
    f = open("./files/item.md")
    i = 0
    for line in f.readlines():
        i = i + 1
        if i <= 3:
            continue
        # print "line = ", line
        elements = line.split("|")
        # print "elements = ", elements
        name = elements[0].strip()
        t = elements[1].strip()
        #
        if t.find("(") > 0:
            t1 = t[:t.find("(")]
            t2 = t[t.find("(") + 1:-1]
        else:
            t1 = t
            t2 = 0
        default = elements[2].strip()
        remark = elements[3].strip()

        print ''
        print '// ' + remark

        if t1.lower() == 'double':
            t1 = 'Double'
            # print 'private Double ' + name + ";"

        if t1.lower() in ['string', 'text', 'varchar']:
            t1 = 'String'
            # print 'private String ' + name + ";"

        if t1.lower() == 'int' or t1.lower() == 'integer':
            t1 = 'Integer'
            if name == 'id':
                print '@Id'
                print '@GeneratedValue(strategy = GenerationType.AUTO)'
                print '@Column(name = "id", nullable = false)'
            # print 'private Integer ' + name + ";"

        print 'private ' + t1 + " " + name + ";"
