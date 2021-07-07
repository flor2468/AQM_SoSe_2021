from import_from_csv import *

def group_ages():

    data = readCSV('csv_files/edited/survey_complete.csv')
    age = processDataToString(data, "How old are you?")
    grouped_ages = []
    
    for i in range(len(age)):
        if (int(age[i])) < 18:
            grouped_ages.append('< 18')
        if (int(age[i])) >= 18 and (int(age[i])) <= 25:
            grouped_ages.append('18 - 25')
        if (int(age[i])) >= 26 and (int(age[i])) <= 30:
            grouped_ages.append('26 - 30')
        if (int(age[i])) >= 31 and (int(age[i])) <= 40:
            grouped_ages.append('31 - 40')
        if (int(age[i])) >= 41 and (int(age[i])) <= 50:
            grouped_ages.append('41 - 50')
        if (int(age[i])) >= 51 and (int(age[i])) <= 60:
            grouped_ages.append('51 - 60')
        if (int(age[i])) >= 61:
            grouped_ages.append('> 60')

    return grouped_ages


def convert_string_scales_to_values():

    # never = 1
    # seldom = 2
    # sometimes = 3
    # often = 4
    # very often = 5

    data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    symptoms_book = processDataToString(data, "How often do you have symptoms like a headache, burning eyes etc. after you've read?")
    symptoms_movie = processDataToString(data, "How often do you have symptoms like a headache, burning eyes etc. after you've watched a movie / a series?")
    snacks_book = processDataToString(data, "How often do you eat snacks during reading?")
    snacks_movie = processDataToString(data, "How often do you eat snacks during watching a movie / a series?")
    frequently_book = processDataToString(data, "How often do you read in a book (meant here is literature you read in your free time like novels etc.)?")
    
    # print(motivation_book)
    # print(motivation_movie)
    # print(symptoms_book)
    # print(symptoms_movie)
    # print(snacks_book)
    # print(snacks_movie)

    for i in range(len(symptoms_book)):
        if symptoms_book[i] == 'never':
            symptoms_book[i] = 1
        if symptoms_book[i] == 'seldom':
            symptoms_book[i] = 2
        if symptoms_book[i] == 'sometimes':
            symptoms_book[i] = 3
        if symptoms_book[i] == 'often':
            symptoms_book[i] = 4
        if symptoms_book[i] == 'very often':
            symptoms_book[i] = 5

    # print(symptoms_book)

    for i in range(len(symptoms_movie)):
        if symptoms_movie[i] == 'never':
            symptoms_movie[i] = 1
        if symptoms_movie[i] == 'seldom':
            symptoms_movie[i] = 2
        if symptoms_movie[i] == 'sometimes':
            symptoms_movie[i] = 3
        if symptoms_movie[i] == 'often':
            symptoms_movie[i] = 4
        if symptoms_movie[i] == 'very often':
            symptoms_movie[i] = 5

    # print(symptoms_movie)

    for i in range(len(snacks_book)):
        if snacks_book[i] == 'never':
            snacks_book[i] = 1
        if snacks_book[i] == 'seldom':
            snacks_book[i] = 2
        if snacks_book[i] == 'sometimes':
            snacks_book[i] = 3
        if snacks_book[i] == 'often':
            snacks_book[i] = 4
        if snacks_book[i] == 'very often':
            snacks_book[i] = 5

    # print(snacks_book)

    for i in range(len(snacks_movie)):
        if snacks_movie[i] == 'never':
            snacks_movie[i] = 1
        if snacks_movie[i] == 'seldom':
            snacks_movie[i] = 2
        if snacks_movie[i] == 'sometimes':
            snacks_movie[i] = 3
        if snacks_movie[i] == 'often':
            snacks_movie[i] = 4
        if snacks_movie[i] == 'very often':
            snacks_movie[i] = 5

    # print(snacks_movie)

    for i in range(len(frequently_book)):
        if frequently_book[i] == 'never':
            frequently_book[i] = 1
        if frequently_book[i] == 'seldom':
            frequently_book[i] = 2
        if frequently_book[i] == 'sometimes':
            frequently_book[i] = 3
        if frequently_book[i] == 'often':
            frequently_book[i] = 4
        if frequently_book[i] == 'very often':
            frequently_book[i] = 5

    # print(frequently_book)

    return symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book


def filter_by_age_and_physical_aspects():

    grouped_ages = group_ages()
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()
    data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    younger_symptoms_book = []
    younger_symptoms_movie = []
    older_symptoms_book = []
    older_symptoms_movie = []
    younger_snacks_book = []
    younger_snacks_movie = []
    older_snacks_book = []
    older_snacks_movie = []
    younger_motivation_book = []
    younger_motivation_movie = []
    older_motivation_book = []
    older_motivation_movie = []

    for i in range(len(grouped_ages)):
        if grouped_ages[i] == '< 18' or grouped_ages[i] == '18 - 25' or grouped_ages[i] == '26 - 30':
            younger_symptoms_book.append(symptoms_book[i])
            younger_symptoms_movie.append(symptoms_movie[i])
            younger_snacks_book.append(snacks_book[i])
            younger_snacks_movie.append(snacks_movie[i])
            younger_motivation_book.append(int(motivation_book[i]))
            younger_motivation_movie.append(int(motivation_movie[i]))
        if grouped_ages[i] == '31 - 40' or grouped_ages[i] == '41 - 50' or grouped_ages[i] == '51 - 60':
            older_symptoms_book.append(symptoms_book[i])
            older_symptoms_movie.append(symptoms_movie[i])
            older_snacks_book.append(snacks_book[i])
            older_snacks_movie.append(snacks_movie[i])
            older_motivation_book.append(int(motivation_book[i]))
            older_motivation_movie.append(int(motivation_movie[i]))

    # print(younger_symptoms_book)
    # print(younger_symptoms_movie)
    # print(older_symptoms_book)
    # print(older_symptoms_movie)
    # print(younger_snacks_book)
    # print(younger_snacks_movie)
    # print(older_snacks_book)
    # print(older_snacks_movie)
    # print(younger_motivation_book)
    # print(younger_motivation_movie)
    # print(older_motivation_book)
    # print(older_motivation_movie)

    return younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_snacks_book, younger_snacks_movie, older_snacks_book, older_snacks_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie


def filter_by_age_and_time():

    data = readCSV('csv_files/edited/survey_complete.csv')
    grouped_ages = group_ages()
    book_time, movie_time = get_book_and_movie_times()

    morning_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (in the morning)")
    noon_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (at noon)")
    afternoon_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (in the afternoon)")
    evening_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (in the evening)")
    night_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (at night)")

    morning_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (in the morning)")
    noon_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (at noon)")
    afternoon_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (in the afternoon)")
    evening_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (in the evening)")
    night_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (at night)")

    younger_book_morning = 0
    younger_movie_morning = 0
    older_book_morning = 0
    older_movie_morning = 0
    younger_book_noon = 0
    younger_movie_noon = 0
    older_book_noon = 0
    older_movie_noon = 0
    younger_book_afternoon = 0
    younger_movie_afternoon = 0
    older_book_afternoon = 0
    older_movie_afternoon = 0
    younger_book_evening = 0
    younger_movie_evening = 0
    older_book_evening = 0
    older_movie_evening = 0
    younger_book_night = 0
    younger_movie_night = 0
    older_book_night = 0
    older_movie_night = 0

    for i in range(len(grouped_ages)):
        if grouped_ages[i] == '< 18' or grouped_ages[i] == '18 - 25' or grouped_ages[i] == '26 - 30':
            if morning_book[i] == '1':
                younger_book_morning += 1
            if morning_movie[i] == '1':
                younger_movie_morning += 1
            if noon_book[i] == '1':
                younger_book_noon += 1
            if noon_movie[i] == '1':
                younger_movie_noon += 1
            if afternoon_book[i] == '1':
                younger_book_afternoon += 1
            if afternoon_movie[i] == '1':
                younger_movie_afternoon += 1
            if evening_book[i] == '1':
                younger_book_evening += 1
            if evening_movie[i] == '1':
                younger_movie_evening += 1
            if night_book[i] == '1':
                younger_book_night += 1
            if night_movie[i] == '1':
                younger_movie_night += 1
        if grouped_ages[i] == '31 - 40' or grouped_ages[i] == '41 - 50' or grouped_ages[i] == '51 - 60':
            if morning_book[i] == '1':
                older_book_morning += 1
            if morning_movie[i] == '1':
                older_movie_morning += 1
            if noon_book[i] == '1':
                older_book_noon += 1
            if noon_movie[i] == '1':
                older_movie_noon += 1
            if afternoon_book[i] == '1':
                older_book_afternoon += 1
            if afternoon_movie[i] == '1':
                older_movie_afternoon += 1
            if evening_book[i] == '1':
                older_book_evening += 1
            if evening_movie[i] == '1':
                older_movie_evening += 1
            if night_book[i] == '1':
                older_book_night += 1
            if night_movie[i] == '1':
                older_movie_night += 1

    return younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night


def get_age_dispersion():

    data = readCSV('csv_files/edited/survey_complete.csv')
    grouped_ages = group_ages()
    younger_sum = 0
    older_sum = 0

    for i in range(len(grouped_ages)):
        if grouped_ages[i] == '< 18' or grouped_ages[i] == '18 - 25' or grouped_ages[i] == '26 - 30':
            younger_sum += 1
        if grouped_ages[i] == '31 - 40' or grouped_ages[i] == '41 - 50' or grouped_ages[i] == '51 - 60':
            older_sum += 1

    return younger_sum, older_sum


def get_dispersion_age_time():

    younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night = filter_by_age_and_time()
    younger_sum, older_sum = get_age_dispersion()


    # young_book_sum = younger_book_morning + younger_book_noon + younger_book_afternoon + younger_book_evening + younger_book_night
    # young_movie_sum = younger_movie_morning + younger_movie_noon + younger_movie_afternoon + younger_movie_evening + younger_movie_night
    
    # old_book_sum = older_book_morning + older_book_noon + older_book_afternoon + older_book_evening + older_book_night
    # old_movie_sum = older_movie_morning + older_movie_noon + older_movie_afternoon + older_movie_evening + older_movie_night
    
    younger_book_morning = younger_book_morning / younger_sum
    younger_book_noon = younger_book_noon / younger_sum
    younger_book_afternoon = younger_book_afternoon / younger_sum
    younger_book_evening = younger_book_evening / younger_sum
    younger_book_night = younger_book_night / younger_sum

    print(younger_sum)
    print(younger_book_morning)
    print(younger_book_noon)
    print(younger_book_afternoon)
    print(younger_book_evening)
    print(younger_book_night)

    older_book_morning = older_book_morning / older_sum
    older_book_noon = older_book_noon / older_sum
    older_book_afternoon = older_book_afternoon / older_sum
    older_book_evening = older_book_evening / older_sum
    older_book_night = older_book_night / older_sum

    print(older_sum)
    print(older_book_morning)
    print(older_book_noon)
    print(older_book_afternoon)
    print(older_book_evening)
    print(older_book_night)

    younger_movie_morning = younger_movie_morning / younger_sum
    younger_movie_noon = younger_movie_noon / younger_sum
    younger_movie_afternoon = younger_movie_afternoon / younger_sum
    younger_movie_evening = younger_movie_evening / younger_sum
    younger_movie_night = younger_movie_night / younger_sum

    print(younger_sum)
    print(younger_movie_morning)
    print(younger_movie_noon)
    print(younger_movie_afternoon)
    print(younger_movie_evening)
    print(younger_movie_night)

    older_movie_morning = older_movie_morning / older_sum
    older_movie_noon = older_movie_noon / older_sum
    older_movie_afternoon = older_movie_afternoon / older_sum
    older_movie_evening = older_movie_evening / older_sum
    older_movie_night = older_movie_night / older_sum

    print(older_sum)
    print(older_movie_morning)
    print(older_movie_noon)
    print(older_movie_afternoon)
    print(older_movie_evening)
    print(older_movie_night)

    return younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night



def get_book_and_movie_times():

    data = readCSV('csv_files/edited/survey_complete.csv')
    book_time = []
    movie_time = []

    morning_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (in the morning)")
    noon_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (at noon)")
    afternoon_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (in the afternoon)")
    evening_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (in the evening)")
    night_book = processDataToString(data, "At which time of the day do you read normally? (Multiple choices are possible.) (at night)")

    morning_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (in the morning)")
    noon_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (at noon)")
    afternoon_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (in the afternoon)")
    evening_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (in the evening)")
    night_movie = processDataToString(data, "At which time of the day do you watch movies / series normally? (Multiple choices are possible.) (at night)")

    # print(morning_book)
    # print(len(morning_book))
    # print(noon_book)
    # print(len(noon_book))
    # print(afternoon_book)
    # print(len(afternoon_book))
    # print(evening_book)
    # print(len(evening_book))
    # print(night_book)
    # print(len(night_book))

    for i in range(len(morning_book)):
        if (morning_book[i] == '1'):
            book_time.append('in the morning')
        
    for i in range(len(noon_book)):
        if (noon_book[i] == '1'):
            book_time.append('at noon')

    for i in range(len(afternoon_book)):
        if (afternoon_book[i] == '1'):
            book_time.append('in the afternoon')

    for i in range(len(evening_book)):
        if (evening_book[i] == '1'):
            book_time.append('in the evening')

    for i in range(len(night_book)):
        if (night_book[i] == '1'):
            book_time.append('at night')

    # print(book_time)
    # print(len(book_time))

    for i in range(len(morning_movie)):
        if (morning_movie[i] == '1'):
            movie_time.append('in the morning')
        
    for i in range(len(noon_movie)):
        if (noon_movie[i] == '1'):
            movie_time.append('at noon')

    for i in range(len(afternoon_movie)):
        if (afternoon_movie[i] == '1'):
            movie_time.append('in the afternoon')

    for i in range(len(evening_movie)):
        if (evening_movie[i] == '1'):
            movie_time.append('in the evening')

    for i in range(len(night_movie)):
        if (night_movie[i] == '1'):
            movie_time.append('at night')

    # print(movie_time)
    # print(len(movie_time))

    return book_time, movie_time


# def filter_by_age_and_symptoms():
    
#     data = readCSV('csv_files/edited/survey_complete.csv')
#     grouped_ages = group_ages()


def filter_by_age_and_symptoms():

    data = readCSV('csv_files/edited/survey_complete.csv')
    grouped_ages = group_ages()
    # younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_snacks_book, younger_snacks_movie, older_snacks_book, older_snacks_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie = filter_by_age_and_physical_aspects()
    
    symptoms_book = processDataToString(data, "How often do you have symptoms like a headache, burning eyes etc. after you've read?")
    symptoms_movie = processDataToString(data, "How often do you have symptoms like a headache, burning eyes etc. after you've watched a movie / a series?")

    younger_symptoms_book_never = 0
    younger_symptoms_book_seldom = 0
    younger_symptoms_book_sometimes = 0
    younger_symptoms_book_often = 0
    younger_symptoms_book_very_often = 0

    older_symptoms_book_never = 0
    older_symptoms_book_seldom = 0
    older_symptoms_book_sometimes = 0
    older_symptoms_book_often = 0
    older_symptoms_book_very_often = 0

    younger_symptoms_movie_never = 0
    younger_symptoms_movie_seldom = 0
    younger_symptoms_movie_sometimes = 0
    younger_symptoms_movie_often = 0
    younger_symptoms_movie_very_often = 0
    
    older_symptoms_movie_never = 0
    older_symptoms_movie_seldom = 0
    older_symptoms_movie_sometimes = 0
    older_symptoms_movie_often = 0
    older_symptoms_movie_very_often = 0

    for i in range(len(grouped_ages)):
        if grouped_ages[i] == '< 18' or grouped_ages[i] == '18 - 25' or grouped_ages[i] == '26 - 30':
            if symptoms_book[i] == 'never':
                younger_symptoms_book_never += 1
            if symptoms_book[i] == 'seldom':
                younger_symptoms_book_seldom += 1
            if symptoms_book[i] == 'sometimes':
                younger_symptoms_book_sometimes += 1
            if symptoms_book[i] == 'often':
                younger_symptoms_book_often += 1
            if symptoms_book[i] == 'very often':
                younger_symptoms_book_very_often += 1
            if symptoms_movie[i] == 'never':
                younger_symptoms_movie_never += 1
            if symptoms_movie[i] == 'seldom':
                younger_symptoms_movie_seldom += 1
            if symptoms_movie[i] == 'sometimes':
                younger_symptoms_movie_sometimes += 1
            if symptoms_movie[i] == 'often':
                younger_symptoms_movie_often += 1
            if symptoms_movie[i] == 'very often':
                younger_symptoms_movie_very_often += 1
        if grouped_ages[i] == '31 - 40' or grouped_ages[i] == '41 - 50' or grouped_ages[i] == '51 - 60':
            if symptoms_book[i] == 'never':
                older_symptoms_book_never += 1
            if symptoms_book[i] == 'seldom':
                older_symptoms_book_seldom += 1
            if symptoms_book[i] == 'sometimes':
                older_symptoms_book_sometimes += 1
            if symptoms_book[i] == 'often':
                older_symptoms_book_often += 1
            if symptoms_book[i] == 'very often':
                older_symptoms_book_very_often += 1
            if symptoms_movie[i] == 'never':
                older_symptoms_movie_never += 1
            if symptoms_movie[i] == 'seldom':
                older_symptoms_movie_seldom += 1
            if symptoms_movie[i] == 'sometimes':
                older_symptoms_movie_sometimes += 1
            if symptoms_movie[i] == 'often':
                older_symptoms_movie_often += 1
            if symptoms_movie[i] == 'very often':
                older_symptoms_movie_very_often += 1

    return younger_symptoms_book_never, younger_symptoms_book_seldom, younger_symptoms_book_sometimes, younger_symptoms_book_often, younger_symptoms_book_very_often, older_symptoms_book_never, older_symptoms_book_seldom, older_symptoms_book_sometimes, older_symptoms_book_often, older_symptoms_book_very_often, younger_symptoms_movie_never, younger_symptoms_movie_seldom, younger_symptoms_movie_sometimes, younger_symptoms_movie_often, younger_symptoms_movie_very_often, older_symptoms_movie_never, older_symptoms_movie_seldom, older_symptoms_movie_sometimes, older_symptoms_movie_often, older_symptoms_movie_very_often

def filter_by_age_and_snacks():

    data = readCSV('csv_files/edited/survey_complete.csv')
    grouped_ages = group_ages()
    # younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_snacks_book, younger_snacks_movie, older_snacks_book, older_snacks_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie = filter_by_age_and_physical_aspects()
    
    snacks_book = processDataToString(data, "How often do you eat snacks during reading?")
    snacks_movie = processDataToString(data, "How often do you eat snacks during watching a movie / a series?")

    younger_snacks_book_never = 0
    younger_snacks_book_seldom = 0
    younger_snacks_book_sometimes = 0
    younger_snacks_book_often = 0
    younger_snacks_book_very_often = 0

    older_snacks_book_never = 0
    older_snacks_book_seldom = 0
    older_snacks_book_sometimes = 0
    older_snacks_book_often = 0
    older_snacks_book_very_often = 0

    younger_snacks_movie_never = 0
    younger_snacks_movie_seldom = 0
    younger_snacks_movie_sometimes = 0
    younger_snacks_movie_often = 0
    younger_snacks_movie_very_often = 0
    
    older_snacks_movie_never = 0
    older_snacks_movie_seldom = 0
    older_snacks_movie_sometimes = 0
    older_snacks_movie_often = 0
    older_snacks_movie_very_often = 0

    for i in range(len(grouped_ages)):
        if grouped_ages[i] == '< 18' or grouped_ages[i] == '18 - 25' or grouped_ages[i] == '26 - 30':
            if snacks_book[i] == 'never':
                younger_snacks_book_never += 1
            if snacks_book[i] == 'seldom':
                younger_snacks_book_seldom += 1
            if snacks_book[i] == 'sometimes':
                younger_snacks_book_sometimes += 1
            if snacks_book[i] == 'often':
                younger_snacks_book_often += 1
            if snacks_book[i] == 'very often':
                younger_snacks_book_very_often += 1
            if snacks_movie[i] == 'never':
                younger_snacks_movie_never += 1
            if snacks_movie[i] == 'seldom':
                younger_snacks_movie_seldom += 1
            if snacks_movie[i] == 'sometimes':
                younger_snacks_movie_sometimes += 1
            if snacks_movie[i] == 'often':
                younger_snacks_movie_often += 1
            if snacks_movie[i] == 'very often':
                younger_snacks_movie_very_often += 1
        if grouped_ages[i] == '31 - 40' or grouped_ages[i] == '41 - 50' or grouped_ages[i] == '51 - 60':
            if snacks_book[i] == 'never':
                older_snacks_book_never += 1
            if snacks_book[i] == 'seldom':
                older_snacks_book_seldom += 1
            if snacks_book[i] == 'sometimes':
                older_snacks_book_sometimes += 1
            if snacks_book[i] == 'often':
                older_snacks_book_often += 1
            if snacks_book[i] == 'very often':
                older_snacks_book_very_often += 1
            if snacks_movie[i] == 'never':
                older_snacks_movie_never += 1
            if snacks_movie[i] == 'seldom':
                older_snacks_movie_seldom += 1
            if snacks_movie[i] == 'sometimes':
                older_snacks_movie_sometimes += 1
            if snacks_movie[i] == 'often':
                older_snacks_movie_often += 1
            if snacks_movie[i] == 'very often':
                older_snacks_movie_very_often += 1

    return younger_snacks_book_never, younger_snacks_book_seldom, younger_snacks_book_sometimes, younger_snacks_book_often, younger_snacks_book_very_often, older_snacks_book_never, older_snacks_book_seldom, older_snacks_book_sometimes, older_snacks_book_often, older_snacks_book_very_often, younger_snacks_movie_never, younger_snacks_movie_seldom, younger_snacks_movie_sometimes, younger_snacks_movie_often, younger_snacks_movie_very_often, older_snacks_movie_never, older_snacks_movie_seldom, older_snacks_movie_sometimes, older_snacks_movie_often, older_snacks_movie_very_often


def filter_by_age_and_motivation():

    data = readCSV('csv_files/edited/survey_complete.csv')
    grouped_ages = group_ages()
    # younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_snacks_book, younger_snacks_movie, older_snacks_book, older_snacks_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie = filter_by_age_and_physical_aspects()
    
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")

    younger_motivation_book_never = 0
    younger_motivation_book_seldom = 0
    younger_motivation_book_sometimes = 0
    younger_motivation_book_often = 0
    younger_motivation_book_very_often = 0

    older_motivation_book_never = 0
    older_motivation_book_seldom = 0
    older_motivation_book_sometimes = 0
    older_motivation_book_often = 0
    older_motivation_book_very_often = 0

    younger_motivation_movie_never = 0
    younger_motivation_movie_seldom = 0
    younger_motivation_movie_sometimes = 0
    younger_motivation_movie_often = 0
    younger_motivation_movie_very_often = 0
    
    older_motivation_movie_never = 0
    older_motivation_movie_seldom = 0
    older_motivation_movie_sometimes = 0
    older_motivation_movie_often = 0
    older_motivation_movie_very_often = 0

    younger_motivation_book_A = 0

    for i in range(len(grouped_ages)):
        if grouped_ages[i] == '< 18' or grouped_ages[i] == '18 - 25' or grouped_ages[i] == '26 - 30':
            if motivation_book[i] == '1' or motivation_book[i] == '2':
                younger_motivation_book_never += 1
            if motivation_book[i] == '3' or motivation_book[i] == '4':
                younger_motivation_book_seldom += 1
            if motivation_book[i] == '5' or motivation_book[i] == '6':
                younger_motivation_book_sometimes += 1
            if motivation_book[i] == '7' or motivation_book[i] == '8':
                younger_motivation_book_often += 1
            if motivation_book[i] == '9' or motivation_book[i] == '10':
                younger_motivation_book_very_often += 1
            if motivation_movie[i] == '1' or motivation_movie[i] == '2':
                younger_motivation_movie_never += 1
            if motivation_movie[i] == '3' or motivation_movie[i] == '4':
                younger_motivation_movie_seldom += 1
            if motivation_movie[i] == '5' or motivation_movie[i] == '6':
                younger_motivation_movie_sometimes += 1
            if motivation_movie[i] == '7' or motivation_movie[i] == '8':
                younger_motivation_movie_often += 1
            if motivation_movie[i] == '9' or motivation_movie[i] == '10':
                younger_motivation_movie_very_often += 1
        if grouped_ages[i] == '31 - 40' or grouped_ages[i] == '41 - 50' or grouped_ages[i] == '51 - 60':
            if motivation_book[i] == '1' or motivation_book[i] == '2':
                older_motivation_book_never += 1
            if motivation_book[i] == '3' or motivation_book[i] == '4':
                older_motivation_book_seldom += 1
            if motivation_book[i] == '5' or motivation_book[i] == '6':
                older_motivation_book_sometimes += 1
            if motivation_book[i] == '7' or motivation_book[i] == '8':
                older_motivation_book_often += 1
            if motivation_book[i] == '9' or motivation_book[i] == '10':
                older_motivation_book_very_often += 1
            if motivation_movie[i] == '1' or motivation_movie[i] == '2':
                older_motivation_movie_never += 1
            if motivation_movie[i] == '3' or motivation_movie[i] == '4':
                older_motivation_movie_seldom += 1
            if motivation_movie[i] == '5' or motivation_movie[i] == '6':
                older_motivation_movie_sometimes += 1
            if motivation_movie[i] == '7' or motivation_movie[i] == '8':
                older_motivation_movie_often += 1
            if motivation_movie[i] == '9' or motivation_movie[i] == '10':
                older_motivation_movie_very_often += 1

    return younger_motivation_book_never, younger_motivation_book_seldom, younger_motivation_book_sometimes, younger_motivation_book_often, younger_motivation_book_very_often, older_motivation_book_never, older_motivation_book_seldom, older_motivation_book_sometimes, older_motivation_book_often, older_motivation_book_very_often, younger_motivation_movie_never, younger_motivation_movie_seldom, younger_motivation_movie_sometimes, younger_motivation_movie_often, younger_motivation_movie_very_often, older_motivation_movie_never, older_motivation_movie_seldom, older_motivation_movie_sometimes, older_motivation_movie_often, older_motivation_movie_very_often


def get_dispersion_age_symptoms():

    younger_symptoms_book_never, younger_symptoms_book_seldom, younger_symptoms_book_sometimes, younger_symptoms_book_often, younger_symptoms_book_very_often, older_symptoms_book_never, older_symptoms_book_seldom, older_symptoms_book_sometimes, older_symptoms_book_often, older_symptoms_book_very_often, younger_symptoms_movie_never, younger_symptoms_movie_seldom, younger_symptoms_movie_sometimes, younger_symptoms_movie_often, younger_symptoms_movie_very_often, older_symptoms_movie_never, older_symptoms_movie_seldom, older_symptoms_movie_sometimes, older_symptoms_movie_often, older_symptoms_movie_very_often = filter_by_age_and_symptoms()
    younger_sum, older_sum = get_age_dispersion()

    younger_symptoms_book_never = younger_symptoms_book_never / younger_sum
    younger_symptoms_book_seldom = younger_symptoms_book_seldom / younger_sum
    younger_symptoms_book_sometimes = younger_symptoms_book_sometimes / younger_sum
    younger_symptoms_book_often = younger_symptoms_book_often / younger_sum
    younger_symptoms_book_very_often = younger_symptoms_book_very_often / younger_sum

    # print(younger_symptoms_book_never)
    # print(younger_symptoms_book_seldom)
    # print(younger_symptoms_book_sometimes)
    # print(younger_symptoms_book_often)
    # print(younger_symptoms_book_very_often)
    # print(younger_symptoms_book_never + younger_symptoms_book_seldom + younger_symptoms_book_sometimes + younger_symptoms_book_often + younger_symptoms_book_very_often)

    younger_symptoms_movie_never = younger_symptoms_movie_never / younger_sum
    younger_symptoms_movie_seldom = younger_symptoms_movie_seldom / younger_sum
    younger_symptoms_movie_sometimes = younger_symptoms_movie_sometimes / younger_sum
    younger_symptoms_movie_often = younger_symptoms_movie_often / younger_sum
    younger_symptoms_movie_very_often = younger_symptoms_movie_very_often / younger_sum

    older_symptoms_book_never = older_symptoms_book_never / older_sum
    older_symptoms_book_seldom = older_symptoms_book_seldom / older_sum
    older_symptoms_book_sometimes = older_symptoms_book_sometimes / older_sum
    older_symptoms_book_often = older_symptoms_book_often / older_sum
    older_symptoms_book_very_often = older_symptoms_book_very_often / older_sum

    older_symptoms_movie_never = older_symptoms_movie_never / older_sum
    older_symptoms_movie_seldom = older_symptoms_movie_seldom / older_sum
    older_symptoms_movie_sometimes = older_symptoms_movie_sometimes / older_sum
    older_symptoms_movie_often = older_symptoms_movie_often / older_sum
    older_symptoms_movie_very_often = older_symptoms_movie_very_often / older_sum

    return younger_symptoms_book_never, younger_symptoms_book_seldom, younger_symptoms_book_sometimes, younger_symptoms_book_often, younger_symptoms_book_very_often, older_symptoms_book_never, older_symptoms_book_seldom, older_symptoms_book_sometimes, older_symptoms_book_often, older_symptoms_book_very_often, younger_symptoms_movie_never, younger_symptoms_movie_seldom, younger_symptoms_movie_sometimes, younger_symptoms_movie_often, younger_symptoms_movie_very_often, older_symptoms_movie_never, older_symptoms_movie_seldom, older_symptoms_movie_sometimes, older_symptoms_movie_often, older_symptoms_movie_very_often


def get_dispersion_age_snacks():

    younger_snacks_book_never, younger_snacks_book_seldom, younger_snacks_book_sometimes, younger_snacks_book_often, younger_snacks_book_very_often, older_snacks_book_never, older_snacks_book_seldom, older_snacks_book_sometimes, older_snacks_book_often, older_snacks_book_very_often, younger_snacks_movie_never, younger_snacks_movie_seldom, younger_snacks_movie_sometimes, younger_snacks_movie_often, younger_snacks_movie_very_often, older_snacks_movie_never, older_snacks_movie_seldom, older_snacks_movie_sometimes, older_snacks_movie_often, older_snacks_movie_very_often = filter_by_age_and_snacks()
    younger_sum, older_sum = get_age_dispersion()

    younger_snacks_book_never = younger_snacks_book_never / younger_sum
    younger_snacks_book_seldom = younger_snacks_book_seldom / younger_sum
    younger_snacks_book_sometimes = younger_snacks_book_sometimes / younger_sum
    younger_snacks_book_often = younger_snacks_book_often / younger_sum
    younger_snacks_book_very_often = younger_snacks_book_very_often / younger_sum

    # print(younger_snacks_book_never)
    # print(younger_snacks_book_seldom)
    # print(younger_snacks_book_sometimes)
    # print(younger_snacks_book_often)
    # print(younger_snacks_book_very_often)
    # print(younger_snacks_book_never + younger_snacks_book_seldom + younger_snacks_book_sometimes + younger_snacks_book_often + younger_snacks_book_very_often)

    younger_snacks_movie_never = younger_snacks_movie_never / younger_sum
    younger_snacks_movie_seldom = younger_snacks_movie_seldom / younger_sum
    younger_snacks_movie_sometimes = younger_snacks_movie_sometimes / younger_sum
    younger_snacks_movie_often = younger_snacks_movie_often / younger_sum
    younger_snacks_movie_very_often = younger_snacks_movie_very_often / younger_sum

    older_snacks_book_never = older_snacks_book_never / older_sum
    older_snacks_book_seldom = older_snacks_book_seldom / older_sum
    older_snacks_book_sometimes = older_snacks_book_sometimes / older_sum
    older_snacks_book_often = older_snacks_book_often / older_sum
    older_snacks_book_very_often = older_snacks_book_very_often / older_sum

    older_snacks_movie_never = older_snacks_movie_never / older_sum
    older_snacks_movie_seldom = older_snacks_movie_seldom / older_sum
    older_snacks_movie_sometimes = older_snacks_movie_sometimes / older_sum
    older_snacks_movie_often = older_snacks_movie_often / older_sum
    older_snacks_movie_very_often = older_snacks_movie_very_often / older_sum

    return younger_snacks_book_never, younger_snacks_book_seldom, younger_snacks_book_sometimes, younger_snacks_book_often, younger_snacks_book_very_often, older_snacks_book_never, older_snacks_book_seldom, older_snacks_book_sometimes, older_snacks_book_often, older_snacks_book_very_often, younger_snacks_movie_never, younger_snacks_movie_seldom, younger_snacks_movie_sometimes, younger_snacks_movie_often, younger_snacks_movie_very_often, older_snacks_movie_never, older_snacks_movie_seldom, older_snacks_movie_sometimes, older_snacks_movie_often, older_snacks_movie_very_often 
    

def get_dispersion_age_motivation():

    younger_motivation_book_never, younger_motivation_book_seldom, younger_motivation_book_sometimes, younger_motivation_book_often, younger_motivation_book_very_often, older_motivation_book_never, older_motivation_book_seldom, older_motivation_book_sometimes, older_motivation_book_often, older_motivation_book_very_often, younger_motivation_movie_never, younger_motivation_movie_seldom, younger_motivation_movie_sometimes, younger_motivation_movie_often, younger_motivation_movie_very_often, older_motivation_movie_never, older_motivation_movie_seldom, older_motivation_movie_sometimes, older_motivation_movie_often, older_motivation_movie_very_often = filter_by_age_and_motivation()
    younger_sum, older_sum = get_age_dispersion()

    younger_motivation_book_never = younger_motivation_book_never / younger_sum
    younger_motivation_book_seldom = younger_motivation_book_seldom / younger_sum
    younger_motivation_book_sometimes = younger_motivation_book_sometimes / younger_sum
    younger_motivation_book_often = younger_motivation_book_often / younger_sum
    younger_motivation_book_very_often = younger_motivation_book_very_often / younger_sum

    print(younger_motivation_book_never)
    print(younger_motivation_book_seldom)
    print(younger_motivation_book_sometimes)
    print(younger_motivation_book_often)
    print(younger_motivation_book_very_often)
    print()
    print(younger_motivation_book_never + younger_motivation_book_seldom + younger_motivation_book_sometimes + younger_motivation_book_often + younger_motivation_book_very_often)
    print()

    younger_motivation_movie_never = younger_motivation_movie_never / younger_sum
    younger_motivation_movie_seldom = younger_motivation_movie_seldom / younger_sum
    younger_motivation_movie_sometimes = younger_motivation_movie_sometimes / younger_sum
    younger_motivation_movie_often = younger_motivation_movie_often / younger_sum
    younger_motivation_movie_very_often = younger_motivation_movie_very_often / younger_sum

    print(younger_motivation_movie_never)
    print(younger_motivation_movie_seldom)
    print(younger_motivation_movie_sometimes)
    print(younger_motivation_movie_often)
    print(younger_motivation_movie_very_often)
    print()
    print(younger_motivation_movie_never + younger_motivation_movie_seldom + younger_motivation_movie_sometimes + younger_motivation_movie_often + younger_motivation_movie_very_often)

    older_motivation_book_never = older_motivation_book_never / older_sum
    older_motivation_book_seldom = older_motivation_book_seldom / older_sum
    older_motivation_book_sometimes = older_motivation_book_sometimes / older_sum
    older_motivation_book_often = older_motivation_book_often / older_sum
    older_motivation_book_very_often = older_motivation_book_very_often / older_sum

    older_motivation_movie_never = older_motivation_movie_never / older_sum
    older_motivation_movie_seldom = older_motivation_movie_seldom / older_sum
    older_motivation_movie_sometimes = older_motivation_movie_sometimes / older_sum
    older_motivation_movie_often = older_motivation_movie_often / older_sum
    older_motivation_movie_very_often = older_motivation_movie_very_often / older_sum

    return younger_motivation_book_never, younger_motivation_book_seldom, younger_motivation_book_sometimes, younger_motivation_book_often, younger_motivation_book_very_often, older_motivation_book_never, older_motivation_book_seldom, older_motivation_book_sometimes, older_motivation_book_often, older_motivation_book_very_often, younger_motivation_movie_never, younger_motivation_movie_seldom, younger_motivation_movie_sometimes, younger_motivation_movie_often, younger_motivation_movie_very_often, older_motivation_movie_never, older_motivation_movie_seldom, older_motivation_movie_sometimes, older_motivation_movie_often, older_motivation_movie_very_often


def filter_by_frequency_and_stress():

    data = readCSV('csv_files/edited/survey_complete.csv')
    # grouped_ages = group_ages()
    # symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()
    # younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_stress_book, younger_stress_movie, older_stress_book, older_stress_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie = filter_by_age_and_physical_aspects()
    
    stress_book = processDataToString(data, "How stressed do you feel after you've read a book on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ")
    
    print(stress_book)
    
    stress_movie = processDataToString(data, "How stressed do you feel after you've watched a movie / a series on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ")

    print(stress_movie)

    frequently_book = processDataToString(data, "How often do you read in a book (meant here is literature you read in your free time like novels etc.)?")

    print(len(frequently_book))
    print(len(stress_book))
    print(len(stress_movie))

    never_stress_book_12 = 0
    never_stress_book_34 = 0
    never_stress_book_56 = 0
    never_stress_book_78 = 0
    never_stress_book_910 = 0

    seldom_stress_book_12 = 0
    seldom_stress_book_34 = 0
    seldom_stress_book_56 = 0
    seldom_stress_book_78 = 0
    seldom_stress_book_910 = 0

    sometimes_stress_book_12 = 0
    sometimes_stress_book_34 = 0
    sometimes_stress_book_56 = 0
    sometimes_stress_book_78 = 0
    sometimes_stress_book_910 = 0

    often_stress_book_12 = 0
    often_stress_book_34 = 0
    often_stress_book_56 = 0
    often_stress_book_78 = 0
    often_stress_book_910 = 0

    very_often_stress_book_12 = 0
    very_often_stress_book_34 = 0
    very_often_stress_book_56 = 0
    very_often_stress_book_78 = 0
    very_often_stress_book_910 = 0

    never_stress_movie_12 = 0
    never_stress_movie_34 = 0
    never_stress_movie_56 = 0
    never_stress_movie_78 = 0
    never_stress_movie_910 = 0

    seldom_stress_movie_12 = 0
    seldom_stress_movie_34 = 0
    seldom_stress_movie_56 = 0
    seldom_stress_movie_78 = 0
    seldom_stress_movie_910 = 0

    sometimes_stress_movie_12 = 0
    sometimes_stress_movie_34 = 0
    sometimes_stress_movie_56 = 0
    sometimes_stress_movie_78 = 0
    sometimes_stress_movie_910 = 0

    often_stress_movie_12 = 0
    often_stress_movie_34 = 0
    often_stress_movie_56 = 0
    often_stress_movie_78 = 0
    often_stress_movie_910 = 0

    very_often_stress_movie_12 = 0
    very_often_stress_movie_34 = 0
    very_often_stress_movie_56 = 0
    very_often_stress_movie_78 = 0
    very_often_stress_movie_910 = 0

    never_count = 0
    seldom_count = 0
    sometimes_count = 0
    often_count = 0
    very_often_count = 0

    for i in range(len(frequently_book)):
        if frequently_book[i] == 'never':

            never_count += 1

            if stress_book[i] == '1' or stress_book == '2':
                never_stress_book_12 += 1
            if stress_book[i] == '3' or stress_book == '3':
                never_stress_book_34 += 1
            if stress_book[i] == '5' or stress_book == '6':
                never_stress_book_56 += 1
            if stress_book[i] == '7' or stress_book == '8':
                never_stress_book_78 += 1
            if stress_book[i] == '9' or stress_book == '10':
                never_stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie == '2':
                never_stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie == '3':
                never_stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie == '6':
                never_stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie == '8':
                never_stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie == '10':
                never_stress_movie_910 += 1

        if frequently_book[i] == 'seldom':

            seldom_count += 1

            # print("hallo")
            if stress_book[i] == '1' or stress_book == '2':
                seldom_stress_book_12 += 1
                print("seldom 12")
            if stress_book[i] == '3' or stress_book == '3':
                seldom_stress_book_34 += 1
                print("seldom 34")
            if stress_book[i] == '5' or stress_book == '6':
                seldom_stress_book_56 += 1
                print("seldom 56")
            if stress_book[i] == '7' or stress_book == '8':
                seldom_stress_book_78 += 1
                print("seldom 78")
            if stress_book[i] == '9' or stress_book == '10':
                seldom_stress_book_910 += 1
                print("seldom 910")

            if stress_movie[i] == '1' or stress_movie == '2':
                seldom_stress_movie_12 += 1
                # print("hallo")
            if stress_movie[i] == '3' or stress_movie == '3':
                seldom_stress_movie_34 += 1
                # print("hallo")
            if stress_movie[i] == '5' or stress_movie == '6':
                seldom_stress_movie_56 += 1
                # print("hallo")
            if stress_movie[i] == '7' or stress_movie == '8':
                seldom_stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie == '10':
                seldom_stress_movie_910 += 1

        if frequently_book[i] == 'sometimes':

            sometimes_count += 1

            if stress_book[i] == '1' or stress_book == '2':
                sometimes_stress_book_12 += 1
            if stress_book[i] == '3' or stress_book == '3':
                sometimes_stress_book_34 += 1
            if stress_book[i] == '5' or stress_book == '6':
                sometimes_stress_book_56 += 1
            if stress_book[i] == '7' or stress_book == '8':
                sometimes_stress_book_78 += 1
            if stress_book[i] == '9' or stress_book == '10':
                sometimes_stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie == '2':
                sometimes_stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie == '3':
                sometimes_stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie == '6':
                sometimes_stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie == '8':
                sometimes_stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie == '10':
                sometimes_stress_movie_910 += 1

        if frequently_book[i] == 'often':

            often_count += 1

            if stress_book[i] == '1' or stress_book == '2':
                often_stress_book_12 += 1
            if stress_book[i] == '3' or stress_book == '3':
                often_stress_book_34 += 1
            if stress_book[i] == '5' or stress_book == '6':
                often_stress_book_56 += 1
            if stress_book[i] == '7' or stress_book == '8':
                often_stress_book_78 += 1
            if stress_book[i] == '9' or stress_book == '10':
                often_stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie == '2':
                often_stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie == '3':
                often_stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie == '6':
                often_stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie == '8':
                often_stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie == '10':
                often_stress_movie_910 += 1

        if frequently_book[i] == 'very often':

            very_often_count += 1

            if stress_book[i] == '1' or stress_book == '2':
                very_often_stress_book_12 += 1
            if stress_book[i] == '3' or stress_book == '3':
                very_often_stress_book_34 += 1
            if stress_book[i] == '5' or stress_book == '6':
                very_often_stress_book_56 += 1
            if stress_book[i] == '7' or stress_book == '8':
                very_often_stress_book_78 += 1
            if stress_book[i] == '9' or stress_book == '10':
                very_often_stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie == '2':
                very_often_stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie == '3':
                very_often_stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie == '6':
                very_often_stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie == '8':
                very_often_stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie == '10':
                very_often_stress_movie_910 += 1

    print(never_count)
    print(seldom_count)
    print(sometimes_count)
    print(often_count)
    print(very_often_count)

    print(never_stress_book_12)
    print(never_stress_book_34)
    print(never_stress_book_56)
    print(never_stress_book_78)
    print(never_stress_book_910)
    print()

    print(never_stress_movie_12)
    print(never_stress_movie_34)
    print(never_stress_movie_56)
    print(never_stress_movie_78)
    print(never_stress_movie_910)
    print()

    print(seldom_stress_book_12)
    print(seldom_stress_book_34)
    print(seldom_stress_book_56)
    print(seldom_stress_book_78)
    print(seldom_stress_book_910)
    print()

    print(seldom_stress_movie_12)
    print(seldom_stress_movie_34)
    print(seldom_stress_movie_56)
    print(seldom_stress_movie_78)
    print(seldom_stress_movie_910)
    print()

    print(sometimes_stress_book_12)
    print(sometimes_stress_book_34)
    print(sometimes_stress_book_56)
    print(sometimes_stress_book_78)
    print(sometimes_stress_book_910)
    print()

    print(sometimes_stress_movie_12)
    print(sometimes_stress_movie_34)
    print(sometimes_stress_movie_56)
    print(sometimes_stress_movie_78)
    print(sometimes_stress_movie_910)
    print()

    print(often_stress_book_12)
    print(often_stress_book_34)
    print(often_stress_book_56)
    print(often_stress_book_78)
    print(often_stress_book_910)
    print()

    print(often_stress_movie_12)
    print(often_stress_movie_34)
    print(often_stress_movie_56)
    print(often_stress_movie_78)
    print(often_stress_movie_910)
    print()

    print(very_often_stress_book_12)
    print(very_often_stress_book_34)
    print(very_often_stress_book_56)
    print(very_often_stress_book_78)
    print(very_often_stress_book_910)
    print()

    print(very_often_stress_movie_12)
    print(very_often_stress_movie_34)
    print(very_often_stress_movie_56)
    print(very_often_stress_movie_78)
    print(very_often_stress_movie_910)
    print()

    return never_stress_book_12, never_stress_book_34, never_stress_book_56, never_stress_book_78, never_stress_book_910, seldom_stress_book_12, seldom_stress_book_34, seldom_stress_book_56, seldom_stress_book_78, seldom_stress_book_910, sometimes_stress_book_12, sometimes_stress_book_34, sometimes_stress_book_56, sometimes_stress_book_78, sometimes_stress_book_910, often_stress_book_12, often_stress_book_34, often_stress_book_56, often_stress_book_78, often_stress_book_910, very_often_stress_book_12, very_often_stress_book_34, very_often_stress_book_56, very_often_stress_book_78, very_often_stress_book_910, never_stress_movie_12, never_stress_movie_34, never_stress_movie_56, never_stress_movie_78, never_stress_movie_910, seldom_stress_movie_12, seldom_stress_movie_34, seldom_stress_movie_56, seldom_stress_movie_78, seldom_stress_movie_910, sometimes_stress_movie_12, sometimes_stress_movie_34, sometimes_stress_movie_56, sometimes_stress_movie_78, sometimes_stress_movie_910, often_stress_movie_12, often_stress_movie_34, often_stress_movie_56, often_stress_movie_78, often_stress_movie_910, very_often_stress_movie_12, very_often_stress_movie_34, very_often_stress_movie_56, very_often_stress_movie_78, very_often_stress_movie_910


def get_frequency_dispersion():

    data = readCSV('csv_files/edited/survey_complete.csv')
    # symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()
    frequently_book = processDataToString(data, "How often do you read in a book (meant here is literature you read in your free time like novels etc.)?")
    
    print(frequently_book)
    
    never_sum = 0
    seldom_sum = 0
    sometimes_sum = 0
    often_sum = 0
    very_often_sum = 0

    for i in range(len(frequently_book)):
        if (frequently_book[i] == 'never'):
            never_sum += 1
        if (frequently_book[i] == 'seldom'):
            seldom_sum += 1
        if (frequently_book[i] == 'sometimes'):
            sometimes_sum += 1
        if (frequently_book[i] == 'often'):
            often_sum += 1
        if (frequently_book[i] == 'very often'):
            very_often_sum += 1

    return never_sum, seldom_sum, sometimes_sum, often_sum, very_often_sum


def get_dispersion_frequency_stress():

    never_stress_book_12, never_stress_book_34, never_stress_book_56, never_stress_book_78, never_stress_book_910, seldom_stress_book_12, seldom_stress_book_34, seldom_stress_book_56, seldom_stress_book_78, seldom_stress_book_910, sometimes_stress_book_12, sometimes_stress_book_34, sometimes_stress_book_56, sometimes_stress_book_78, sometimes_stress_book_910, often_stress_book_12, often_stress_book_34, often_stress_book_56, often_stress_book_78, often_stress_book_910, very_often_stress_book_12, very_often_stress_book_34, very_often_stress_book_56, very_often_stress_book_78, very_often_stress_book_910, never_stress_movie_12, never_stress_movie_34, never_stress_movie_56, never_stress_movie_78, never_stress_movie_910, seldom_stress_movie_12, seldom_stress_movie_34, seldom_stress_movie_56, seldom_stress_movie_78, seldom_stress_movie_910, sometimes_stress_movie_12, sometimes_stress_movie_34, sometimes_stress_movie_56, sometimes_stress_movie_78, sometimes_stress_movie_910, often_stress_movie_12, often_stress_movie_34, often_stress_movie_56, often_stress_movie_78, often_stress_movie_910, very_often_stress_movie_12, very_often_stress_movie_34, very_often_stress_movie_56, very_often_stress_movie_78, very_often_stress_movie_910 = filter_by_frequency_and_stress()
    never_sum, seldom_sum, sometimes_sum, often_sum, very_often_sum = get_frequency_dispersion()

    print(never_sum)
    print(seldom_sum)
    print(sometimes_sum)
    print(often_sum)
    print(very_often_sum)
    print()

    if (never_sum != 0):
        never_stress_book_12 = never_stress_book_12 / never_sum
        never_stress_book_34 = never_stress_book_34 / never_sum
        never_stress_book_56 = never_stress_book_56 / never_sum
        never_stress_book_78 = never_stress_book_78 / never_sum
        never_stress_book_910 = never_stress_book_910 / never_sum

        never_stress_movie_12 = never_stress_movie_12 / never_sum
        never_stress_movie_34 = never_stress_movie_34 / never_sum
        never_stress_movie_56 = never_stress_movie_56 / never_sum
        never_stress_movie_78 = never_stress_movie_78 / never_sum
        never_stress_movie_910 = never_stress_movie_910 / never_sum

    print(never_stress_book_12)
    print(never_stress_book_34)
    print(never_stress_book_56)
    print(never_stress_book_78)
    print(never_stress_book_910)
    print()

    print(never_stress_movie_12)
    print(never_stress_movie_34)
    print(never_stress_movie_56)
    print(never_stress_movie_78)
    print(never_stress_movie_910)
    print()

    if (seldom_sum != 0):

        seldom_stress_book_12 = seldom_stress_book_12 / seldom_sum
        seldom_stress_book_34 = seldom_stress_book_34 / seldom_sum
        seldom_stress_book_56 = seldom_stress_book_56 / seldom_sum
        seldom_stress_book_78 = seldom_stress_book_78 / seldom_sum
        seldom_stress_book_910 = seldom_stress_book_910 / seldom_sum

        seldom_stress_movie_12 = seldom_stress_movie_12 / seldom_sum
        seldom_stress_movie_34 = seldom_stress_movie_34 / seldom_sum
        seldom_stress_movie_56 = seldom_stress_movie_56 / seldom_sum
        seldom_stress_movie_78 = seldom_stress_movie_78 / seldom_sum
        seldom_stress_movie_910 = seldom_stress_movie_910 / seldom_sum

    print(seldom_stress_book_12)
    print(seldom_stress_book_34)
    print(seldom_stress_book_56)
    print(seldom_stress_book_78)
    print(seldom_stress_book_910)
    print()

    print(seldom_stress_movie_12)
    print(seldom_stress_movie_34)
    print(seldom_stress_movie_56)
    print(seldom_stress_movie_78)
    print(seldom_stress_movie_910)
    print()

    if (sometimes_sum != 0):

        sometimes_stress_book_12 = sometimes_stress_book_12 / sometimes_sum
        sometimes_stress_book_34 = sometimes_stress_book_34 / sometimes_sum
        sometimes_stress_book_56 = sometimes_stress_book_56 / sometimes_sum
        sometimes_stress_book_78 = sometimes_stress_book_78 / sometimes_sum
        sometimes_stress_book_910 = sometimes_stress_book_910 / sometimes_sum

        sometimes_stress_movie_12 = sometimes_stress_movie_12 / sometimes_sum
        sometimes_stress_movie_34 = sometimes_stress_movie_34 / sometimes_sum
        sometimes_stress_movie_56 = sometimes_stress_movie_56 / sometimes_sum
        sometimes_stress_movie_78 = sometimes_stress_movie_78 / sometimes_sum
        sometimes_stress_movie_910 = sometimes_stress_movie_910 / sometimes_sum

    print(sometimes_stress_book_12)
    print(sometimes_stress_book_34)
    print(sometimes_stress_book_56)
    print(sometimes_stress_book_78)
    print(sometimes_stress_book_910)
    print()

    print(sometimes_stress_movie_12)
    print(sometimes_stress_movie_34)
    print(sometimes_stress_movie_56)
    print(sometimes_stress_movie_78)
    print(sometimes_stress_movie_910)
    print()

    if (often_sum != 0):

        often_stress_book_12 = often_stress_book_12 / often_sum
        often_stress_book_34 = often_stress_book_34 / often_sum
        often_stress_book_56 = often_stress_book_56 / often_sum
        often_stress_book_78 = often_stress_book_78 / often_sum
        often_stress_book_910 = often_stress_book_910 / often_sum

        often_stress_movie_12 = often_stress_movie_12 / often_sum
        often_stress_movie_34 = often_stress_movie_34 / often_sum
        often_stress_movie_56 = often_stress_movie_56 / often_sum
        often_stress_movie_78 = often_stress_movie_78 / often_sum
        often_stress_movie_910 = often_stress_movie_910 / often_sum

    print(often_stress_book_12)
    print(often_stress_book_34)
    print(often_stress_book_56)
    print(often_stress_book_78)
    print(often_stress_book_910)
    print()

    print(often_stress_movie_12)
    print(often_stress_movie_34)
    print(often_stress_movie_56)
    print(often_stress_movie_78)
    print(often_stress_movie_910)
    print()

    if (very_often_sum != 0):

        very_often_stress_book_12 = very_often_stress_book_12 / very_often_sum
        very_often_stress_book_34 = very_often_stress_book_34 / very_often_sum
        very_often_stress_book_56 = very_often_stress_book_56 / very_often_sum
        very_often_stress_book_78 = very_often_stress_book_78 / very_often_sum
        very_often_stress_book_910 = very_often_stress_book_910 / very_often_sum

        very_often_stress_movie_12 = very_often_stress_movie_12 / very_often_sum
        very_often_stress_movie_34 = very_often_stress_movie_34 / very_often_sum
        very_often_stress_movie_56 = very_often_stress_movie_56 / very_often_sum
        very_often_stress_movie_78 = very_often_stress_movie_78 / very_often_sum
        very_often_stress_movie_910 = very_often_stress_movie_910 / very_often_sum

    print(very_often_stress_book_12)
    print(very_often_stress_book_34)
    print(very_often_stress_book_56)
    print(very_often_stress_book_78)
    print(very_often_stress_book_910)
    print()

    print(very_often_stress_movie_12)
    print(very_often_stress_movie_34)
    print(very_often_stress_movie_56)
    print(very_often_stress_movie_78)
    print(very_often_stress_movie_910)
    print()

    return never_stress_book_12, never_stress_book_34, never_stress_book_56, never_stress_book_78, never_stress_book_910, seldom_stress_book_12, seldom_stress_book_34, seldom_stress_book_56, seldom_stress_book_78, seldom_stress_book_910, sometimes_stress_book_12, sometimes_stress_book_34, sometimes_stress_book_56, sometimes_stress_book_78, sometimes_stress_book_910, often_stress_book_12, often_stress_book_34, often_stress_book_56, often_stress_book_78, often_stress_book_910, very_often_stress_book_12, very_often_stress_book_34, very_often_stress_book_56, very_often_stress_book_78, very_often_stress_book_910, never_stress_movie_12, never_stress_movie_34, never_stress_movie_56, never_stress_movie_78, never_stress_movie_910, seldom_stress_movie_12, seldom_stress_movie_34, seldom_stress_movie_56, seldom_stress_movie_78, seldom_stress_movie_910, sometimes_stress_movie_12, sometimes_stress_movie_34, sometimes_stress_movie_56, sometimes_stress_movie_78, sometimes_stress_movie_910, often_stress_movie_12, often_stress_movie_34, often_stress_movie_56, often_stress_movie_78, often_stress_movie_910, very_often_stress_movie_12, very_often_stress_movie_34, very_often_stress_movie_56, very_often_stress_movie_78, very_often_stress_movie_910



def test_function():

    data = readCSV('csv_files/edited/survey_complete.csv')

    stress_book = processDataToString(data, "How stressed do you feel after you've read a book on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ")
    print(stress_book)
    print()
    
    stress_movie = processDataToString(data, "How stressed do you feel after you've watched a movie / a series on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ")
    print(stress_movie)
    print()

    frequently_book = processDataToString(data, "How often do you read in a book (meant here is literature you read in your free time like novels etc.)?")
    print(frequently_book)
    print()

    print(len(frequently_book))
    print(len(stress_book))
    print(len(stress_movie))
    print()


    stress_book_12 = 0
    stress_book_34 = 0
    stress_book_56 = 0
    stress_book_78 = 0
    stress_book_910 = 0
    never_book = []

    stress_movie_12 = 0
    stress_movie_34 = 0
    stress_movie_56 = 0
    stress_movie_78 = 0
    stress_movie_910 = 0
    never_movie = []

    for i in range(len(frequently_book)):
        # print(frequently_book[i])
        # print(stress_book[i])
        # print(stress_movie[i])
        # print()

        if frequently_book[i] == 'never':
            print(stress_book[i])
            # print(stress_movie[i])
            if stress_book[i] == '1' or stress_book[i] == '2':
                stress_book_12 += 1
            if stress_book[i] == '3' or stress_book[i] == '4':
                stress_book_34 += 1
            if stress_book[i] == '5' or stress_book[i] == '6':
                stress_book_56 += 1
            if stress_book[i] == '7' or stress_book[i] == '8':
                stress_book_78 += 1
            if stress_book[i] == '9' or stress_book[i] == '10':
                stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie[i] == '2':
                stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie[i] == '4':
                stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie[i] == '6':
                stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie[i] == '8':
                stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie[i] == '10':
                stress_movie_910 += 1

    never_book.append(stress_book_12)
    never_book.append(stress_book_34)
    never_book.append(stress_book_56)
    never_book.append(stress_book_78)
    never_book.append(stress_book_910)

    never_movie.append(stress_movie_12)
    never_movie.append(stress_movie_34)
    never_movie.append(stress_movie_56)
    never_movie.append(stress_movie_78)
    never_movie.append(stress_movie_910)


    stress_book_12 = 0
    stress_book_34 = 0
    stress_book_56 = 0
    stress_book_78 = 0
    stress_book_910 = 0
    seldom_book = []

    stress_movie_12 = 0
    stress_movie_34 = 0
    stress_movie_56 = 0
    stress_movie_78 = 0
    stress_movie_910 = 0
    seldom_movie = []

    for i in range(len(frequently_book)):
        # print(frequently_book[i])
        # print(stress_book[i])
        # print(stress_movie[i])
        # print()

        if frequently_book[i] == 'seldom':
            print(stress_book[i])
            # print(stress_movie[i])
            if stress_book[i] == '1' or stress_book[i] == '2':
                stress_book_12 += 1
            if stress_book[i] == '3' or stress_book[i] == '4':
                stress_book_34 += 1
            if stress_book[i] == '5' or stress_book[i] == '6':
                stress_book_56 += 1
            if stress_book[i] == '7' or stress_book[i] == '8':
                stress_book_78 += 1
            if stress_book[i] == '9' or stress_book[i] == '10':
                stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie[i] == '2':
                stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie[i] == '4':
                stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie[i] == '6':
                stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie[i] == '8':
                stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie[i] == '10':
                stress_movie_910 += 1

    seldom_book.append(stress_book_12)
    seldom_book.append(stress_book_34)
    seldom_book.append(stress_book_56)
    seldom_book.append(stress_book_78)
    seldom_book.append(stress_book_910)

    seldom_movie.append(stress_movie_12)
    seldom_movie.append(stress_movie_34)
    seldom_movie.append(stress_movie_56)
    seldom_movie.append(stress_movie_78)
    seldom_movie.append(stress_movie_910)


    stress_book_12 = 0
    stress_book_34 = 0
    stress_book_56 = 0
    stress_book_78 = 0
    stress_book_910 = 0
    sometimes_book = []

    stress_movie_12 = 0
    stress_movie_34 = 0
    stress_movie_56 = 0
    stress_movie_78 = 0
    stress_movie_910 = 0
    sometimes_movie = []

    for i in range(len(frequently_book)):
        # print(frequently_book[i])
        # print(stress_book[i])
        # print(stress_movie[i])
        # print()

        if frequently_book[i] == 'sometimes':
            print(stress_book[i])
            # print(stress_movie[i])
            if stress_book[i] == '1' or stress_book[i] == '2':
                stress_book_12 += 1
            if stress_book[i] == '3' or stress_book[i] == '4':
                stress_book_34 += 1
            if stress_book[i] == '5' or stress_book[i] == '6':
                stress_book_56 += 1
            if stress_book[i] == '7' or stress_book[i] == '8':
                stress_book_78 += 1
            if stress_book[i] == '9' or stress_book[i] == '10':
                stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie[i] == '2':
                stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie[i] == '4':
                stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie[i] == '6':
                stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie[i] == '8':
                stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie[i] == '10':
                stress_movie_910 += 1

    sometimes_book.append(stress_book_12)
    sometimes_book.append(stress_book_34)
    sometimes_book.append(stress_book_56)
    sometimes_book.append(stress_book_78)
    sometimes_book.append(stress_book_910)

    sometimes_movie.append(stress_movie_12)
    sometimes_movie.append(stress_movie_34)
    sometimes_movie.append(stress_movie_56)
    sometimes_movie.append(stress_movie_78)
    sometimes_movie.append(stress_movie_910)


    stress_book_12 = 0
    stress_book_34 = 0
    stress_book_56 = 0
    stress_book_78 = 0
    stress_book_910 = 0
    often_book = []

    stress_movie_12 = 0
    stress_movie_34 = 0
    stress_movie_56 = 0
    stress_movie_78 = 0
    stress_movie_910 = 0
    often_movie = []

    for i in range(len(frequently_book)):
        # print(frequently_book[i])
        # print(stress_book[i])
        # print(stress_movie[i])
        # print()

        if frequently_book[i] == 'often':
            print(stress_book[i])
            # print(stress_movie[i])
            if stress_book[i] == '1' or stress_book[i] == '2':
                stress_book_12 += 1
            if stress_book[i] == '3' or stress_book[i] == '4':
                stress_book_34 += 1
            if stress_book[i] == '5' or stress_book[i] == '6':
                stress_book_56 += 1
            if stress_book[i] == '7' or stress_book[i] == '8':
                stress_book_78 += 1
            if stress_book[i] == '9' or stress_book[i] == '10':
                stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie[i] == '2':
                stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie[i] == '4':
                stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie[i] == '6':
                stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie[i] == '8':
                stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie[i] == '10':
                stress_movie_910 += 1

    often_book.append(stress_book_12)
    often_book.append(stress_book_34)
    often_book.append(stress_book_56)
    often_book.append(stress_book_78)
    often_book.append(stress_book_910)

    often_movie.append(stress_movie_12)
    often_movie.append(stress_movie_34)
    often_movie.append(stress_movie_56)
    often_movie.append(stress_movie_78)
    often_movie.append(stress_movie_910)


    stress_book_12 = 0
    stress_book_34 = 0
    stress_book_56 = 0
    stress_book_78 = 0
    stress_book_910 = 0
    very_often_book = []

    stress_movie_12 = 0
    stress_movie_34 = 0
    stress_movie_56 = 0
    stress_movie_78 = 0
    stress_movie_910 = 0
    very_often_movie = []

    for i in range(len(frequently_book)):
        # print(frequently_book[i])
        # print(stress_book[i])
        # print(stress_movie[i])
        # print()

        if frequently_book[i] == 'very often':
            print(stress_book[i])
            # print(stress_movie[i])
            if stress_book[i] == '1' or stress_book[i] == '2':
                stress_book_12 += 1
            if stress_book[i] == '3' or stress_book[i] == '4':
                stress_book_34 += 1
            if stress_book[i] == '5' or stress_book[i] == '6':
                stress_book_56 += 1
            if stress_book[i] == '7' or stress_book[i] == '8':
                stress_book_78 += 1
            if stress_book[i] == '9' or stress_book[i] == '10':
                stress_book_910 += 1

            if stress_movie[i] == '1' or stress_movie[i] == '2':
                stress_movie_12 += 1
            if stress_movie[i] == '3' or stress_movie[i] == '4':
                stress_movie_34 += 1
            if stress_movie[i] == '5' or stress_movie[i] == '6':
                stress_movie_56 += 1
            if stress_movie[i] == '7' or stress_movie[i] == '8':
                stress_movie_78 += 1
            if stress_movie[i] == '9' or stress_movie[i] == '10':
                stress_movie_910 += 1

    very_often_book.append(stress_book_12)
    very_often_book.append(stress_book_34)
    very_often_book.append(stress_book_56)
    very_often_book.append(stress_book_78)
    very_often_book.append(stress_book_910)

    very_often_movie.append(stress_movie_12)
    very_often_movie.append(stress_movie_34)
    very_often_movie.append(stress_movie_56)
    very_often_movie.append(stress_movie_78)
    very_often_movie.append(stress_movie_910)


    print()
    # print(stress_book_12)
    # print(stress_book_34)
    # print(stress_book_56)
    # print(stress_book_78)
    # print(stress_book_910)
    print(never_book)
    print(never_movie)
    print(seldom_book)
    print(seldom_movie)
    print(sometimes_book)
    print(sometimes_movie)
    print(often_book)
    print(often_movie)
    print(very_often_book)
    print(very_often_movie)

    return never_book, never_movie, seldom_book, seldom_movie, sometimes_book, sometimes_movie, often_book, often_movie, very_often_book, very_often_movie


def test_function_2():

    never_sum, seldom_sum, sometimes_sum, often_sum, very_often_sum = get_frequency_dispersion()
    never_book, never_movie, seldom_book, seldom_movie, sometimes_book, sometimes_movie, often_book, often_movie, very_often_book, very_often_movie = test_function()

    if (never_sum != 0):
        for i in range(len(never_book)):
            never_book[i] = never_book[i] / never_sum
            never_movie[i] = never_movie[i] / never_sum

    if (seldom_sum != 0):
        for i in range(len(seldom_book)):
            seldom_book[i] = seldom_book[i] / seldom_sum
            seldom_movie[i] = seldom_movie[i] / seldom_sum

    if (sometimes_sum != 0):
        for i in range(len(sometimes_book)):
            sometimes_book[i] = sometimes_book[i] / sometimes_sum
            sometimes_movie[i] = sometimes_movie[i] / sometimes_sum

    if (often_sum != 0):
        for i in range(len(often_book)):
            often_book[i] = often_book[i] / often_sum
            often_movie[i] = often_movie[i] / often_sum

    if (very_often_sum != 0):
        for i in range(len(very_often_book)):
            very_often_book[i] = very_often_book[i] / very_often_sum
            very_often_movie[i] = very_often_movie[i] / very_often_sum

    print()
    print(never_book)
    print(never_movie)
    print(seldom_book)
    print(seldom_movie)
    print(sometimes_book)
    print(sometimes_movie)
    print(often_book)
    print(often_movie)
    print(very_often_book)
    print(very_often_movie)

    return never_book, never_movie, seldom_book, seldom_movie, sometimes_book, sometimes_movie, often_book, often_movie, very_often_book, very_often_movie


def get_dispersion_health():

    data = readCSV('csv_files/edited/survey_complete.csv')
    health = processDataToString(data, "What do you think is healthier?")

    A = 0
    B = 0
    C = 0
    D = 0

    for i in range(len(health)):
        if health[i] == "Reading a book is healthier.":
            A += 1
        if health[i] == "Watching a movie/ a series is healthier":
            B += 1
        if health[i] == "Both is equally healthy.":
            C += 1
        if health[i] == "Both is equally unhealthy.":
            D += 1

    return A, B, C, D


def main():
    # get_dispersion_age_symptoms()
    # get_dispersion_age_snacks()
    # get_dispersion_age_motivation()

    # filter_by_frequency_and_stress()
    # get_dispersion_frequency_stress()

    # test_function()
    test_function_2()

if __name__ == main():
    main()