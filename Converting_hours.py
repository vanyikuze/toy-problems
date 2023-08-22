def converting_hours(hrs, mins, period) :
    if hrs <= 9 and mins <= 59 and period == 'am' :
        converted = '0' + str(hrs) + str(mins) + 'hrs'
        return converted
    elif hrs >= 10 and mins <= 59 and period == 'am' :
        converted = str(hrs) + str(min) + 'hrs'
        return converted
    elif hrs <= 12 and mins <= 59 and period == 'pm' :
        after_noon = hrs + 12
        converted = str(after_noon) + str(mins) + 'hrs'
        return converted 
    

