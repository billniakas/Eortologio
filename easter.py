import datetime


date=str(datetime.datetime.now().date()).replace("-","/")
today=[date[0:4],date[5:7],date[8:10]]

#############################################################################
def easter(y):
    a=y%19
    b=y%4
    c=y%7
    d=(16+19*a)%30
    e=((2*b)+(4*c)+(6*d))%7 
    day=3+d+e

    if day <= 30:
        month=4
        if y < int(today[0]):
            return("Το Πάσχα το έτος {} ήταν στις {} Απριλίου".format(y,day))
        elif y > int(today[0]):
            return("Το Πάσχα το έτος {} θα είναι στις {} Απριλίου".format(y,day))
        else:
            if int(date[2]) > month:
                return("Το Πάσχα φέτος ήταν στις {} Απριλίου".format(day))
            else:
                return("Το Πάσχα φέτος θα είναι στις {} Απριλίου".format(day))
########################################################################   
    else:
        month=5
        if y < int(today[0]):
            return("Το Πάσχα το έτος {} ήταν στις {} Μαϊου".format(y,day-30))
        elif y > int(today[0]):
            return("Το Πάσχα το έτος {} θα είναι στις {} Μαϊου".format(y,day-30))
        else:
            if int(date[2]) > month:
                return("Το Πάσχα φέτος ήταν στις {} Μαϊου".format(day-30))
            else:
                return("Το Πάσχα φέτος θα είναι στις {} Μαϊου".format(day-30))


def kinites(y,mhnas, mera):
    a=y%19
    b=y%4
    c=y%7
    d=(16+19*a)%30
    e=((2*b)+(4*c)+(6*d))%7 
    day=3+d+e

    if day <= 30:
        
        month=4
    else:
        day=30-day
        month=5
    
    # print(day,month)

    easter = datetime.date(y, month, day)
    
    # print(easter-datetime.timedelta(days=5))

    kinitesdic={
    str(easter-datetime.timedelta(days=70)):"Τελώνου και Φαρισαίου - Αρχή Τριωδίου	-70",
    str(easter-datetime.timedelta(days=63)):"Του Ασώτου",
    str(easter-datetime.timedelta(days=59)):"Τσικνοπέμπτη",
    str(easter-datetime.timedelta(days=57)):"Ψυχοσάββατο Α'",
    str(easter-datetime.timedelta(days=56)):"Της Απόκρεω",
    str(easter-datetime.timedelta(days=49)):"Τυροφάγου",
    str(easter-datetime.timedelta(days=48)):"Καθαρά Δευτέρα",
    str(easter-datetime.timedelta(days=43)):"Αγίου Θεοδώρου (Θεόδωρος, Θεοδώρα, Δώρα, Ντόρα, Θόδωρος, Θοδώρα, Θοδωρής, Θοδωράκης, Θώδης, Θώδος, Δώρης)",
    str(easter-datetime.timedelta(days=42)):"Κυριακή της Ορθοδοξίας (Ορθοδοξία, Λωξάνδρα, Λωξάντρα, Ρωξάνη, Αξία)",
    str(easter-datetime.timedelta(days=35)):"Γρηγορίου του Παλαμά (Γρηγόριος, Γρηγόρης, Γρηγορία, Γόλης) (σημείωση: εορτάζεται και στις 14 Νοε)",
    str(easter-datetime.timedelta(days=8)):"Σάββατο του Λαζάρου (Λάζαρος, Λάζος)",
    str(easter-datetime.timedelta(days=7)):"Κυριακή των Βαίων (Βάϊος, Βάϊα, Βάγια, Βαία, Δάφνη)",
    str(easter-datetime.timedelta(days=6)):"Μεγάλη Δευτέρα (Πάγκαλος)",
    str(easter-datetime.timedelta(days=5)):"Μεγάλη Τρίτη",
    str(easter-datetime.timedelta(days=4)):"Μεγάλη Τετάρτη",
    str(easter-datetime.timedelta(days=3)):"Μεγάλη Πέμπτη (Αλήθεια)",
    str(easter-datetime.timedelta(days=2)):"Μεγάλη Παρασκευή",
    str(easter-datetime.timedelta(days=1)):"Μεγάλο Σάββατο",
    str(easter):"ΤΟ ΑΓΙΟ ΠΑΣΧΑ (Αναστάσιος, Αναστασία, Τάσος, Αναστάσης, Ανέστης, Λάμπρος, Λαμπρινή, Λαμπρίνα, Πασχάλης, Πασχαλίνα, Λίνα, Στασινός)",
    str(easter+datetime.timedelta(days=1)):"2α Διακαινησίμου - Δευτέρα",
    str(easter+datetime.timedelta(days=2)):"3η Διακαινησίμου - Τρίτη (Λαμπροτρίτη) - (Ραφαήλ, Νικόλαος και Ειρήνη Αγιοι Μυτιλήνης)",
    str(easter+datetime.timedelta(days=3)):"4η Διακαινησίμου - Τετάρτη (Θεοχάρης)",
    str(easter+datetime.timedelta(days=4)):"5η Διακαινησίμου - Πέμπτη",
    str(easter+datetime.timedelta(days=5)):"6η Διακαινησίμου - Παρασκευή",
    str(easter+datetime.timedelta(days=5)):"Ζωοδόχου Πηγής (Πηγή, Κρήνη, Κρηνιώ, Ζήσης, Ζησούλα, Ζήσιμος, Ζωή, Ζώης, Ζωϊτσα, Ζωζώ, Παναγιώτης, Πάνος, Πανούσος, Παναγής, Πανάγος, Γιώτης, Πολυζώης, Παναγιώτα, Γιώτα, Παναγιούλα, Γιούλα, Παναγούλα )",
    str(easter+datetime.timedelta(days=6)):"7η Διακαινησίμου - Σαββάτο",
    str(easter+datetime.timedelta(days=7)):"Του Θωμά (Θωμάς, Θωμαή, Τόμας)",
    str(easter+datetime.timedelta(days=14)):"Των Μυροφόρων (Μυροφόρα)",
    str(easter+datetime.timedelta(days=21)):"Του Παραλύτου (Βηθεσδά)",
    str(easter+datetime.timedelta(days=39)):"Ανάληψη του Χριστού (Νεφέλη)",
    str(easter+datetime.timedelta(days=48)):"Ψυχοσάββατο Β'",
    str(easter+datetime.timedelta(days=49)):"Πεντηκοστή",
    str(easter+datetime.timedelta(days=50)):"Αγ. Πνεύματος (Τριάδα, Τριάς, Κόρη, Κορίνα, Κορίνος)",
    str(easter+datetime.timedelta(days=56)):"Αγίων Πάντων"}

    if len(str(mhnas))==1:
        mhnas="0"+str(mhnas)
    kinites = None
    while kinites == None:
        try:
            kinites = kinitesdic[str(y)+"-"+str(mhnas)+"-"+str(mera)]
            return kinites
        except KeyError:
            return False
    
    
    
    











    
