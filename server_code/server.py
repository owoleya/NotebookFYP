import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

import datetime
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
@anvil.server.callable
def add_note(name):
    listed=[]
    newnote = app_tables.notes.add_row(label=name, created_date=datetime.now(),imgs=listed)
    return dict(newnote)

@anvil.server.callable
def update_note(title,new):
    new['created_date'] = datetime.now()
    next = app_tables.notes.get(label=title)
    next.update(**new)
    pass

@anvil.server.callable
def open_note(title):
    next = app_tables.notes.get(label=title)
    return next

@anvil.server.callable
def delete_note(title):
    next = app_tables.notes.get(label=title)
    next.delete()
    pass

@anvil.server.callable
def addImage(lb,data):
  current = app_tables.notes.get(label=lb)
  newimg = app_tables.notedata.add_row(**data)
  current["imgs"] += [newimg]

@anvil.server.callable
def delImage(lb,data):
  current = app_tables.notes.get(label=lb)
  current["imgs"] = [r for r in current["imgs"] if r != data]
