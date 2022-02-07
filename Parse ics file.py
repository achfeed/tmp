in_file = "C:/Users/ahamid/Downloads/tiesto.ics"

from icalendar import Calendar, Event    # icalendar.__version__ == 4.0.9
g = open(in_file,'rb')
gcal = Calendar.from_ical(g.read())
title = ''
start_time = ''
end_time = ''
for component in gcal.walk():
    if component.name == "VEVENT":
        title = component.get('summary')
        start_time = component.get('dtstart').to_ical().decode("utf-8") 
        end_time = component.get('dtend').to_ical().decode("utf-8") 
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