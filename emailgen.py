f = open("list", "r")
in_section = 0
headline = ""
for line in f:
    line = line.strip();
    if len(line) == 0:
        if in_section:
            print "</p>\n"
            in_section = 0
        continue
    if not in_section:
        # title
        print "<p>"
        headline = line
        in_section = 1
    elif headline != "":
        # link
        print "<a href=\"%s\"><strong>\n%s\n</strong></a><br />" % (line, headline)
        headline = ""
    else:
        attr = line.split(":")
        if len(attr) == 1 or len(attr[0]) > 17:
            # content
            print "%s" % line
        else:
            # attribute
            label = attr[0].strip()
            attr.pop(0)
            what = ":".join(attr).strip()
            print "<strong>%s: </strong>%s<br />" % (label, what)

