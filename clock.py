import gi
from datetime import datetime
import time
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GLib

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="GTK Clock")                       
        self.set_border_width(5)
        
        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)     
        self.add(hbox) 

        self.label = Gtk.Label()
        hbox.pack_start(self.label, False, False, 0)
 
       
    def displayclock(self):
            datetimenow = str(datetime.now().time())[:8]
            self.label.set_label(datetimenow)
            return True
        

    def startclocktimer(self):
        GLib.timeout_add(100, self.displayclock)
        

if __name__ == "__main__":
    
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    win.startclocktimer()

    Gtk.main()
