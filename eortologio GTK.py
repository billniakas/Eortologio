import gi
import datetime
import subprocess
import sqlite3
import easter
import re
sqlite_file = 'saints.db'
conn = sqlite3.connect(sqlite_file)
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="Εορτολόγιο")                       # Δημιουργία παραθύρου
        self.set_default_size(450,500)                                     # Ορισμός διαστάσεων

        # Προσθήκη Scrollbar

        self.scrolledwindow = Gtk.ScrolledWindow()
        self.add(self.scrolledwindow)

        # Προσθήκη εικονιδίου

        self.icon=("calendar")
        pixbuf24 = Gtk.IconTheme.get_default().load_icon(self.icon, 24, 0)
        pixbuf32 = Gtk.IconTheme.get_default().load_icon(self.icon, 32, 0)
        pixbuf48 = Gtk.IconTheme.get_default().load_icon(self.icon, 48, 0)
        pixbuf64 = Gtk.IconTheme.get_default().load_icon(self.icon, 64, 0)
        pixbuf96 = Gtk.IconTheme.get_default().load_icon(self.icon, 96, 0)
        self.set_icon_list([pixbuf24, pixbuf32, pixbuf48, pixbuf64, pixbuf96])


        # Προσθήκη Tray Icon

        self.staticon = Gtk.StatusIcon ()
        self.staticon.set_from_file("calendar-512.png")
        #self.staticon.connect ("activate", self.trayicon_activate)
        #self.staticon.connect ("popup_menu", self.trayicon_popup)
        self.staticon.connect('popup-menu', self.on_right_click)
        self.staticon.connect('popup-menu', self.showhide)
        #self.staticon.set_visible(True)
        text="Δεξί κλικ για περισσότερα"
        self.staticon.set_tooltip_text(text)


        # Δημιουργία στοιχείων παραθύρου

        self.set_border_width(10)
        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)     # Τα κουτιά να είναι κατακόρυφα
        self.add(hbox)                                                     # Προσθήκη στο παράθυρο

        self.scrolledwindow.add(hbox)

        self.fixed_object = Gtk.Fixed()

        self.today_button = Gtk.Button(label="Σήμερα")
        self.today_button.connect("clicked", self.today_button_clicked)
        self.today_button.set_size_request(80,20)

        self.fixed_object.put(self.today_button,0,0)
        hbox.pack_start(self.fixed_object, False, False, 0)

        self.search = Gtk.SearchEntry()
        #self.search.set_text("Εισαγωγή ονόματος για αναζήτηση")
        self.search.connect("search-changed", self.seek_name)
        hbox.pack_start(self.search, False, False, 0)                      # Προσθήκη στο παράθυρο

        self.calendar = Gtk.Calendar()                                     # Δημιουργία ημερολογίου
        self.calendar.connect("day-selected", self.on_date_clicked)        # σύνδεση ημερολογίου με event day clicked και με συνάρτηση
        hbox.pack_start(self.calendar, False, True, 0)                     # Προσθήκη στο παράθυρο

        self.button = Gtk.Button(label="Υπολογισμός Πάσχα")                # Δημιουργία κουμπιού

        self.button.connect("clicked", self.on_button_clicked)             # σύνδεση ημερολογίου με event day clicked και με συνάρτηση
        hbox.pack_end(self.button, False, True, 0)                         # Προσθήκη στο παράθυρο
        self.label0 = Gtk.Label(label="Επιλέξτε την ημερομηνία για να δείτε την αντίστοιχη εορτή")
        hbox.pack_start(self.label0, False, False, 0)

        self.label_kinites = Gtk.Label()
        hbox.pack_start(self.label_kinites, False, False, 0)

        self.label1 = Gtk.Label()
        hbox.pack_start(self.label1, False, False, 0)


    def on_button_clicked(self, button):
        date=list(self.calendar.get_date())
        #year=str(date[0])
        #easter=subprocess.getoutput("./easter.sh "+year)  # κλήση του bash script
        message = easter.easter(date[0])                   # κλήση της συνάρτησης easter από το module easter
        self.label1.set_text(message)
        self.label0.set_text(" ")
        self.label_kinites.set_text(" ")

    def on_date_clicked(self, button):
        date=list(self.calendar.get_date())
        message="Επιλέξατε την "+str(date[2])+"/"+str(date[1]+1)+"/"+str(date[0])
        day=str(date[2])+"/"+str(date[1]+1)
        year=str(date[0])

        print(day)
        #giortazei=subprocess.getoutput("./eortes.sh "+day)
        today=datetime.datetime.now().date()
        if str(date[0])+"-"+str(date[1]+1)+"-"+str(date[2]) == str(today) or str(date[0])+"-0"+str(date[1]+1)+"-0"+str(date[2]) == str(today) or str(date[0])+"-0"+str(date[1]+1)+"-"+str(date[2]) == str(today):
            message="Σήμερα"

        self.label0.set_text(message)
        MainWindow.eortes(self)


    def eortes(self):
        date=list(self.calendar.get_date())
        month=date[1]+1
        day=date[2]
        year=date[0]

        if easter.kinites(year,month,day) is not False:
            print(easter.kinites(year,month,day))
            self.label_kinites.set_text(easter.kinites(year,month,day))
            self.label_kinites.set_line_wrap(True)
            #self.label_kinites.set_justify(Gtk.Justification.LEFT)

        else:
            self.label_kinites.set_text(" ")
            self.label_kinites.set_line_wrap(True)


        c = conn.cursor()
        c.execute('SELECT * FROM Saints WHERE Month = {} AND Day = {} AND source like "saint.gr"'.format(month,day))
        all_rows = c.fetchall()
        result=list(all_rows[0])

        for row in result[0:-3]:
            self.label1.set_text(row.replace("<b>", "").replace("</b>",""))
            self.label1.set_line_wrap(True)
            self.label1.set_justify(Gtk.Justification.LEFT)
            self.set_default_size(500,450)

    # Αναζητηση ονόματος
    
    def seek_name(self,text):
        print(self.search.get_text())
        text="Έγραψες "+self.search.get_text()
        onoma=self.search.get_text().capitalize()
        c = conn.cursor()

        c.execute('select *,Month,Day from Saints where Daily_feasts like "%{}%" and source like "saint.gr"'.format(onoma))
        all_rows = c.fetchall()
        name_list=list(all_rows)
        seek_text=""
        
        for i in range(len(name_list)):
            date=str(name_list[i][-4])+"/"+str(name_list[i][-5])
            for name in name_list[i][0:-5]:
                seektext=name.replace("<b>"," ").replace("</b>"," ")
                
            result=re.findall(r'.*{}.*'.format(onoma), seektext)
            if len(result) == 0:
                pass
            else:
                seek_text+="Στις "+date+" γιορτάζει:\n"+result[0]+"\n\n"
    
        #conn.close()
        #self.label1.set_text(text)
        self.label0.set_text("Αναζήτηση ονόματος/εορτής")
        self.label1.set_text(seek_text)
            
        self.label1.set_line_wrap(True)
        self.label1.set_justify(Gtk.Justification.LEFT)


    def today_button_clicked(self, button):
        today=str(datetime.datetime.now().date())
        self.calendar.select_month(int(today[5:7])-1,int(today[0:4]))
        self.calendar.select_day(int(today[8:10]))


            
    # Λειτουργίες και events tray icon
    # -----------------------------
    # [SNIPPET_NAME: Systray icon]
    # [SNIPPET_CATEGORIES: PyGTK]
    # [SNIPPET_DESCRIPTION: Shows a system tray icon with a menu  ]
    # [SNIPPET_AUTHOR: João Pinto <joao.pinto@getdeb.net>]
    # [SNIPPET_LICENSE: GPL]
    # -----------------------------
            
    def on_right_click(self, icon, event_button, activate_time):
                self.make_menu(event_button, activate_time)

    def make_menu(self, event_button, activate_time):
            menu = Gtk.Menu()

            # show about dialog
            about = Gtk.MenuItem(label="Περί Εορτολογίου")
            about.show()
            menu.append(about)
            about.connect('activate', self.show_about_dialog)

            # add quit item
            quit = Gtk.MenuItem(label="Έξοδος")
            quit.show()
            menu.append(quit)
            quit.connect('activate', Gtk.main_quit)

            # show/hide dialog
            showhide = Gtk.MenuItem(label="Εμφάνιση/Απόκρυψη")
            showhide.show()
            menu.append(showhide)
            about.connect('activate', self.showhide)

            def position():
                lambda w,x: self.staticon.position_menu(menu,self.staticon)
                       
            menu.show_all ()
            menu.popup(None, None, position(), self.staticon, 0, activate_time)

    def  show_about_dialog(self, widget):
            about_dialog = Gtk.AboutDialog()
            about_dialog.set_destroy_with_parent (True)
            about_dialog.set_logo_icon_name(self.icon)
            about_dialog.set_icon_name ("Εορτολόγιο GTK")
            about_dialog.set_name('Εορτολόγιο')
            about_dialog.set_version('1.0')
            about_dialog.set_copyright("(C) 2019 Βασίλης Νιάκας")
            about_dialog.set_comments(("Ένα απλό εορτολόγιο σε Python \n Βασισμένο σε ενα fork του Paschalis Sposito \n Γιατί μπορούμε και γιατί θέλουμε :)"))
            about_dialog.set_authors(['Βασίλης Νιάκας https://billniakas.com'])
            about_dialog.set_license_type(Gtk.License.GPL_3_0)
            about_dialog.set_website("https://github.com/billniakas")
            about_dialog.run()
            about_dialog.destroy()
            
    def showhide():
        if Gtk.Window.iconify() is True:
            Gtk.Window.deiconify()
        else:
            Gtk.Window.iconify()

if __name__ == "__main__":
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
