import re

s = """ <tag1 value = "value">
 (<tag2 name = "name">
 (<tag3 another = "another" final = "final">
 </tag3>)
 </tag2>)
 </tag1>"""
# s = """ <tag1 value = "value">
# </tag1>
# <tag2 name = "name">
# <tag3 another = "another" final = "final">
# </tag3>
# </tag2>"""
query=""" tag1~value
 tag1.tag2.tag3~name
 tag1.tag2.tag3~final """
def formatqueries():
    qlines=query.splitlines()
    qlistoflines=[]
    tagstofind={}
    for line in qlines:
        qlistoflines.append(re.sub("\(|\)|\/|<|>|\"","",line.strip()))
    for line in qlistoflines:
        currenttag=line.split("~")[0]
    # attributetocheck=re.findall("(?<=\~)\w+",line)
    attributetocheck=line.split("~")[1]
    if(currenttag in tagstofind.keys()):
        tagstofind[currenttag].append(attributetocheck)
    else:
        tagstofind[currenttag]=[attributetocheck]
    return tagstofind


def formatHRML():
    lines=s.splitlines()
    listOfLines=[]
    alltags={}
    opentags=[]
    previoustag=""
    for lines in lines:
        listOfLines.append(re.sub("\(|\)|\/|<|>|\"","",lines.strip()))
    print(listOfLines)
    for value in listOfLines:
        currenttag=re.findall("tag\d",value)[0]
        print(currenttag)
        if(currenttag not in opentags):
            opentags.append(currenttag)
            print("Current open tags")
            print(opentags)

            attributes = re.findall("\w+\s*=\s*\w+",value)
            print(attributes)
            if(previoustag ==""):
                previoustag=currenttag
            else:
                previoustag=previoustag+"."+currenttag
                alltags[previoustag]=attributes
                alltags[currenttag]=attributes
    else:
        print("Current open tags")
        print(opentags)
        opentags.remove(currenttag)
        previoustags=previoustag.split(".")
        if(currenttag in previoustags):
            previoustags.remove(currenttag)
            previoustag=".".join(previoustags)
    return alltags
if __name__=='__main__':
    print(formatHRML())
    print(formatqueries())
