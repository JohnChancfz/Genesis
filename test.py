# -*- coding: utf-8 -*-

if __name__ == '__main__':

    print 'Genesis start...'
    md_file = open("./files/Item.md")
    java_seq = []
    # line no
    i = 0
    for line in md_file.readlines():
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

        java_seq.append('\n')
        java_seq.append('// ' + remark + '\n')

        if t1.lower() == 'double':
            t1 = 'Double'
            # print 'private Double ' + name + ";"

        if t1.lower() in ['string', 'text', 'varchar']:
            t1 = 'String'
            # print 'private String ' + name + ";"

        if t1.lower() == 'int' or t1.lower() == 'integer':
            t1 = 'Integer'
            if name == 'id':
                java_seq.append('@Id' + '\n')
                java_seq.append('@GeneratedValue(strategy = GenerationType.AUTO)' + '\n')
                java_seq.append('@Column(name = "id", nullable = false)' + '\n')
            # print 'private Integer ' + name + ";"

        java_seq.append('private ' + t1 + ' ' + name + ';' + '\n')

    java_file = open("./out/entity/Item.java", 'w')
    java_file.writelines(java_seq)
    java_file.close()
    md_file.close()
