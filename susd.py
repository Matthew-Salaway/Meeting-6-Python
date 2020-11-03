def susdEmail(firstName, lastname, idNumber):
    firstInital = firstName[0]
    lastTwo = idNumber % 100
    email = firstInital + lastname + str(lastTwo) + "@susdgapps.org"
    return(email)
