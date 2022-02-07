in_file = "C:/Users/ahamid/Downloads/tiesto.ics"

from icalendar import Calendar, Event    # icalendar.__version__ == 4.0.9
g = open(in_file,'rb')
gcal = Calendar.from_ical(g.read())
title = ''   # ici sera stocké le titre que l'événement google calendar porte (ex : Daily)
start_time = '' # Date et heure de début (à besoin d'être parsée, je le ferais et modifierais ici)
end_time = '' # Date et heure de fin (à besoin d'être parsée, je le ferais et modifierais ici)
for component in gcal.walk():
    if component.name == "VEVENT":
        title = component.get('summary')
        start_time = component.get('dtstart').to_ical().decode("utf-8") 
        end_time = component.get('dtend').to_ical().decode("utf-8") 
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
