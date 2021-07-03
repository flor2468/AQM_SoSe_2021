from import_from_csv import *
from calculate_values import *
import matplotlib.pyplot as plt

def create_basic_diagrams():

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
    
    data = readCSV('csv_files/edited/survey_complete.csv')
    frequently_book = processDataToString(data, "How often do you read in a book (meant here is literature you read in your free time like novels etc.)?")
    never = frequently_book.count('never')
    print(never)
    seldom = frequently_book.count('seldom')
    print(seldom)
    sometimes = frequently_book.count('sometimes')
    print(sometimes)
    often = frequently_book.count('often')
    print(often)
    very_often = frequently_book.count('very often')
    print(very_often)
    print(never + seldom + sometimes + often + very_often)

    # source: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

    labels = 'never', 'seldom', 'sometimes', 'often', 'very often'
    sizes = [never, seldom, sometimes, often, very_often]

    fig, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, colors=['lightgreen', 'magenta', 'gold', 'mediumturquoise', 'orange'])
    ax1.axis('equal')

    plt.savefig('diagrams/pie_charts/frequently_book_pie_chart.png')
    plt.show()


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


def main():
    create_basic_diagrams()
    # create_bar_chart()
    # convert_string_scales_to_values()

    data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()

    # create_bar_chart(symptoms_book, symptoms_movie, 'symptoms')
    # create_bar_chart(snacks_book, snacks_movie, 'snacks')
    # create_bar_chart(motivation_book, motivation_movie, 'motivation')


if __name__ == main():
    main()
