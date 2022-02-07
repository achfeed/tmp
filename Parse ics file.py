in_file = "C:/Users/ahamid/Downloads/tiesto.ics"

from icalendar import Calendar, Event    # icalendar.__version__ == 4.0.9
from dateutil import parser              # dateutil.__version__ == 2.8.1

g = open(in_file,'rb')
gcal = Calendar.from_ical(g.read())
title = ''   # ici sera stocké le titre que l'événement google calendar porte (ex : Daily)
start_time = '' # Date et heure de début
end_time = '' # Date et heure de fin
for component in gcal.walk():
    if component.name == "VEVENT":
        title = str(component.get('summary'))
        not_formated_start_time = component.get('dtstart').to_ical().decode("utf-8") 
        start_time = parser.parse(not_formated_start_time).replace(tzinfo=None)
        not_formated_end_time = component.get('dtend').to_ical().decode("utf-8") 
        end_time = parser.parse(not_formated_end_time).replace(tzinfo=None)
        # d'autres éléments peuvent être récupérés mais ne sont pas toujours présents dans un fichier ics :
        try:
            print('--- ATTENDEE : \n', component.get('ATTENDEE'))
        except:
            print('no ettendees')
            
        try:
            print('\n--- X-GOOGLE-CONFERENCE : \n', component.get('X-GOOGLE-CONFERENCE'))
        except:
            print('not a google conference')
        
        try:
            print('\n--- DESCRIPTION : \n', component.get('DESCRIPTION'))
        except:
            print('no description')
        
        try:
            print('\n--- LOCATION : \n', component.get('LOCATION'))
        except:
            print('no location')
g.close()

print(title)       # type : str
print(start_time)  # type : datetime.datetime
print(end_time)    # type : datetime.datetime
