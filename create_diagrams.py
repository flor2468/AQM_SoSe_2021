from import_from_csv import *
from calculate_values import *
import matplotlib.pyplot as plt

def create_basic_diagrams():

    # GENDER PIE CHART

    # data = readCSV('csv_files/edited/survey_complete.csv')
    # gender = processDataToString(data, 'To which gender do you assign to?')
    # male = gender.count('male')
    # print(male)
    # female = gender.count('female')
    # print(female)
    # diverse = gender.count('diverse')
    # print(diverse)
    # no = gender.count('no statement')
    # print(no)
    # print(male + female + diverse + no)

    # # source: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

    # labels = 'male', 'female', 'diverse', 'no statement'
    # sizes = [male, female, diverse, no]

    # fig, ax1 = plt.subplots()
    # ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, colors=['lightgreen', 'magenta', 'gold', 'mediumturquoise'])
    # ax1.axis('equal')

    # plt.savefig('diagrams/pie_charts/gender_pie_chart.png')
    # plt.show()

    # BOOK FREQUENCY PIE CHART
    
    # data = readCSV('csv_files/edited/survey_complete.csv')
    # frequently_book = processDataToString(data, "How often do you read in a book (meant here is literature you read in your free time like novels etc.)?")
    # never = frequently_book.count('never')
    # print(never)
    # seldom = frequently_book.count('seldom')
    # print(seldom)
    # sometimes = frequently_book.count('sometimes')
    # print(sometimes)
    # often = frequently_book.count('often')
    # print(often)
    # very_often = frequently_book.count('very often')
    # print(very_often)
    # print(never + seldom + sometimes + often + very_often)

    # # source: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

    # labels = 'never', 'seldom', 'sometimes', 'often', 'very often'
    # sizes = [never, seldom, sometimes, often, very_often]

    # fig, ax1 = plt.subplots()
    # ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, colors=['lightgreen', 'magenta', 'gold', 'mediumturquoise', 'orange'])
    # ax1.axis('equal')

    # plt.savefig('diagrams/pie_charts/frequently_book_pie_chart.png')
    # plt.show()

    #  AGE PIE CHART

    data = readCSV('csv_files/edited/survey_complete.csv')
    age = processDataToString(data, "How old are you?")
    grouped_ages = group_ages()
            
    # print(len(age))
    # print(age)
    # print(len(grouped_ages))
    # print(grouped_ages)

    A = grouped_ages.count('< 18')
    B = grouped_ages.count('18 - 25')
    C = grouped_ages.count('26 - 30')
    D = grouped_ages.count('31 - 40')
    E = grouped_ages.count('41 - 50')
    F = grouped_ages.count('51 - 60')
    G = grouped_ages.count('> 60')

    # print(A, B, C, D, E, F, G)
    # print(A + B + C + D + E + F + G)

    # source: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

    # labels = '< 18', '18 - 25', '26 - 30', '31 - 40', '41 - 50', '51 - 60'
    # sizes = [A, B, C, D, E, F]

    labels = '51 - 60', '41 - 50', '31 - 40', '26 - 30', '18 - 25', '< 18'
    sizes = [F, E, D, C, B, A]

    fig, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=45, colors=['lightgreen', 'magenta', 'gold', 'mediumturquoise', 'orange', 'red'])
    ax1.axis('equal')

    plt.savefig('diagrams/pie_charts/age_pie_chart.png')
    plt.show()


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


def create_bar_chart(array_1, array_2, topic):

    mean_1 = calculate_mean(array_1)
    print(mean_1)
    mean_2 = calculate_mean(array_2)
    print(mean_2)

    fig, ax = plt.subplots()
    labels = ['reading a book', 'watching a movie / a series']
    values = [mean_1, mean_2]
    ax.bar(labels, values, color=['purple', 'goldenrod'])

    plt.savefig('diagrams/bar_charts/' + str(topic) + '.png')

    plt.show()


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

    print(younger_symptoms_book)
    print(younger_symptoms_movie)
    print(older_symptoms_book)
    print(older_symptoms_movie)
    print(younger_snacks_book)
    print(younger_snacks_movie)
    print(older_snacks_book)
    print(older_snacks_movie)
    print(younger_motivation_book)
    print(younger_motivation_movie)
    print(older_motivation_book)
    print(older_motivation_movie)

    return younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_snacks_book, younger_snacks_movie, older_snacks_book, older_snacks_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie


def create_bar_chart_with_multiple_bars():

    younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_snacks_book, younger_snacks_movie, older_snacks_book, older_snacks_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie = filter_by_age_and_physical_aspects()

    mean_ysb = calculate_mean(younger_symptoms_book)
    mean_ysm = calculate_mean(younger_symptoms_movie)
    mean_osb = calculate_mean(older_symptoms_book)
    mean_osm = calculate_mean(older_symptoms_movie)
    mean_ysnab = calculate_mean(younger_snacks_book)
    mean_ysnam = calculate_mean(younger_snacks_movie)
    mean_osnab = calculate_mean(older_snacks_book)
    mean_osnam = calculate_mean(older_snacks_movie)
    mean_ymotb = calculate_mean(younger_motivation_book)
    mean_ymotm = calculate_mean(younger_motivation_movie)
    mean_omotb = calculate_mean(older_motivation_book)
    mean_omotm = calculate_mean(older_motivation_movie)

    # data = [[mean_ysb, mean_ysm, mean_ysnab, mean_ysnam, mean_ymotb, mean_ymotm], 
    #         [mean_osb, mean_osm, mean_osnab, mean_osnam, mean_omotb, mean_omotm]]

    # SYMPTOMS

    data = [[mean_ysb, mean_ysm], [mean_osb, mean_osm]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    # plt.yticks(Pos-(1/6), ["", "Level 2", "Level 3", "Level 4", "Level 5"])
    ax.bar(Pos + 0.00, data[0], color='purple', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='goldenrod', width=0.25)
    plt.xticks(Pos+0.12, ["age groups A-C", "age groups D-F"])

    book_patch = mpatches.Patch(color='purple', label='reading a book')
    movie_patch = mpatches.Patch(color='goldenrod', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_symptoms.png')

    plt.show()

    # SNACKS

    data = [[mean_ysnab, mean_ysnam], [mean_osnab, mean_osnam]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    # plt.yticks(Pos-(1/6), ["", "Level 2", "Level 3", "Level 4", "Level 5"])
    ax.bar(Pos + 0.00, data[0], color='purple', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='goldenrod', width=0.25)
    plt.xticks(Pos+0.12, ["age groups A-C", "age groups D-F"])

    book_patch = mpatches.Patch(color='purple', label='reading a book')
    movie_patch = mpatches.Patch(color='goldenrod', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_snacks.png')

    plt.show()

    # MOTIVATION

    data = [[mean_ymotb, mean_ymotm], [mean_omotb, mean_omotm]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    # plt.yticks(Pos-(1/6), ["", "Level 2", "Level 3", "Level 4", "Level 5"])
    ax.bar(Pos + 0.00, data[0], color='purple', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='goldenrod', width=0.25)
    plt.xticks(Pos+0.12, ["age groups A-C", "age groups D-F"])

    book_patch = mpatches.Patch(color='purple', label='reading a book')
    movie_patch = mpatches.Patch(color='goldenrod', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_motivation.png')

    plt.show()
    

def main():
    # create_basic_diagrams()
    # create_bar_chart()
    # convert_string_scales_to_values()

    data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()

    # create_bar_chart(symptoms_book, symptoms_movie, 'symptoms')
    # create_bar_chart(snacks_book, snacks_movie, 'snacks')
    # create_bar_chart(motivation_book, motivation_movie, 'motivation')

    filter_by_age_and_physical_aspects()
    # create_bar_chart_with_multiple_bars()


if __name__ == main():
    main()
