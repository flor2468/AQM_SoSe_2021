from import_from_csv import *
from calculate_values import *
import matplotlib.pyplot as plt

def create_basic_diagrams():

    # source: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

    #  AGE PIE CHART

    data = readCSV('csv_files/edited/survey_complete.csv')
    age = processDataToString(data, "How old are you?")
    grouped_ages = group_ages()

    A = grouped_ages.count('< 18')
    B = grouped_ages.count('18 - 25')
    C = grouped_ages.count('26 - 30')
    D = grouped_ages.count('31 - 40')
    E = grouped_ages.count('41 - 50')
    F = grouped_ages.count('51 - 60')
    G = grouped_ages.count('> 60')

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


def create_histogram():

    data = readCSV('csv_files/edited/survey_complete.csv')
    age = processDataToString(data, "How old are you?")

    for i in range(len(age)):
        age[i] = int(age[i])

    bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
    
    # bins = np.arange(len(bins)) - 0.5
    hist, bins = np.histogram(age, bins = bins) 

    print(hist)
    print(bins)
    fig = plt.figure()
    from matplotlib.ticker import MaxNLocator

    ax = plt.figure().gca()
    plt.hist(age, bins = bins, rwidth=0.9, color='turquoise', align='left') 
    plt.xlim([0, 65])
    # plt.xticks(np.arange(9,61,1))
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
    ax.set_yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    plt.savefig('diagrams/histograms/age_histogram.png')

    plt.show()
    

def main():

    data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()

    filter_by_age_and_physical_aspects()
    create_histogram()


if __name__ == main():
    main()
