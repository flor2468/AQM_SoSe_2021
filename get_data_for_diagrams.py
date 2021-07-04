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


# def main():
#     get_dispersion_age_time()


# if __name__ == main():
#     main()