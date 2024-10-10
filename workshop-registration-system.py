workshops = []# list
applications = []#queue
registrations = []#stack

#record workshops

def recordWorkshop(workshop):
    workshops.append(workshop)
#call function recordWorkshop()
recordWorkshop('workshop 1')
recordWorkshop('workshop 2')
recordWorkshop('workshop 3')
print('the list of available workshops is:')
print(workshops)

#record attendee applications

def recordApplications(user,workshop):
    application = {
        "username": user,
        "workshopname":  workshop
    }
    if workshop in workshops:
        applications.append(application)
    else:
        print('the workshop you are applying for is not available')

#call function recordApplications()

recordApplications('Ramba','workshop 1')
recordApplications('Rwibutso','workshop 2')
print('the list of valid applications:')
print(applications)

def processApplications():
    if applications:
        application = applications.pop(0)
        registrations.append(application)
    else:
       print('the queue is empty') 
processApplications()
processApplications()
    
print("the processed registrations are the following:")
print(registrations)

def undoRegistrations():
    if registrations:
        registrations.pop()
    else:
       print('the registrations list is empty') 
undoRegistrations()
print("the processed registrations are the following:")
print(registrations)

