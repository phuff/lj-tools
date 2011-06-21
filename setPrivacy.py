import fileinput
import time
from mechanize import Browser

username="<username>"
password="<password>"
journalUrl = "http://<username>.livejournal.com"
editUrl = "http://www.livejournal.com/editjournal.bml?journal=<username>&itemid="
mech = Browser()
mech.open(journalUrl)
mech.select_form(nr=0)
mech["user"] = username
mech["password"] = password
mech.submit()

for line in fileinput.input():
    print line, 
    itemId = line.rstrip()
    entryEditUrl = editUrl + itemId
    mech.open(entryEditUrl)
    mech.select_form(name="updateForm")
    mech["security"] = ["private"]
    mech.submit(name="action:save", label="Save Entry")
    time.sleep(1)

