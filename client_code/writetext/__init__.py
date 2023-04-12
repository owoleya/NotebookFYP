from ._anvil_designer import writetextTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class writetext(writetextTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.draw=0
    self.drawingboard.height=300
    self.drawingboard.width=600
    # Any code you write here will run before the form opens.
  
  def drawingboard_mouse_down(self, x, y, button, **event_args):
    global draw
    c = self.drawingboard
    if button==1:
      self.draw=1
    pass

  def drawingboard_mouse_move(self, x, y, **event_args):
    """This method is called when the mouse cursor moves over this component"""
    if self.draw == 1:
      c = self.drawingboard
      c.fill_style = "#000000"
      c.fill_rect(x, y, 5, 5)
  
    pass
  
  def drawingboard_mouse_up(self, x, y, button, **event_args):
    global draw
    c = self.drawingboard
    if button==1:
      self.draw=0

    self.item['imgcontent']=self.drawingboard.get_image()
    pass
  
  def reset_click(self, **event_args):
    self.drawingboard.reset_context()
    c = self.drawingboard

    c.fill_style = "#FFFFFF"
    
    c.fill_rect(0, 0, 600, 300)
    self.item['imgcontent']=self.drawingboard.get_image()
    pass
    # Any code you write here will run before the form opens.

  def parse_click(self, **event_args):
    parse = self.drawingboard.get_image()
    
    readhand = ((anvil.server.call('text',parse)))

    self.text_box_1.text = self.text_box_1.text + readhand
    self.item['imglabel'] = self.text_box_1.text
    pass

  def drawingboard_reset(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.drawingboard
    c.fill_style = "#FFFFFF"
    c.fill_rect(0, 0, 600, 300)
    self.item['imgcontent']=self.drawingboard.get_image()
    pass



