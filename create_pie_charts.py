from import_from_csv import *
from get_data_for_diagrams import *


def create_basic_diagrams(which_diagram):

    # GENDER PIE CHART

    if (which_diagram == 'gender'):

        data = readCSV('csv_files/edited/survey_complete.csv')
        gender = processDataToString(data, 'To which gender do you assign to?')
        male = gender.count('male')
        print(male)
        female = gender.count('female')
        print(female)
        diverse = gender.count('diverse')
        print(diverse)
        no = gender.count('no statement')
        print(no)
        print(male + female + diverse + no)

        # source: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html

        labels = 'male', 'female', 'diverse', 'no statement'
        sizes = [male, female, diverse, no]

        fig, ax1 = plt.subplots()
        _, _, chart = ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, colors=['#003f5c', '#7a5195', '#ef5675', '#ffa600'])

        # change color of percentage text in the chart
        # source: https://stackoverflow.com/questions/27898830/python-how-to-change-autopct-text-color-to-be-white-in-a-pie-chart
        for i in range(len(chart)):
            if i == 0 or i == 1:
                chart[i].set_color('white')

        ax1.axis('equal')

        plt.savefig('diagrams/pie_charts/gender_pie_chart.png')
        plt.show()

    # BOOK FREQUENCY PIE CHART

    if (which_diagram == 'book frequency'):
    
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
        _, _, chart = ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, colors=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'])
        
        # change color of percentage text in the chart
        # source: https://stackoverflow.com/questions/27898830/python-how-to-change-autopct-text-color-to-be-white-in-a-pie-chart
        for i in range(len(chart)):
            if i == 1 or i == 2:
                chart[i].set_color('white')

        ax1.axis('equal')

        plt.savefig('diagrams/pie_charts/frequently_book_pie_chart.png')
        plt.show()

    #  AGE PIE CHART

    if (which_diagram == 'age'):

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
        _, _, chart = ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, colors=['#ffa600', '#ff6e54', '#dd5182', '#955196', '#444e86', '#003f5c'])
        
        # change color of percentage text in the chart
        # source: https://stackoverflow.com/questions/27898830/python-how-to-change-autopct-text-color-to-be-white-in-a-pie-chart
        for i in range(len(chart)):
            if i == 4 or i == 5:
                chart[i].set_color('white')
        
        ax1.axis('equal')

        plt.savefig('diagrams/pie_charts/age_pie_chart.png')
        plt.show()


def main():

    # create_basic_diagrams('gender')
    create_basic_diagrams('book frequency')
    # create_basic_diagrams('age')


if __name__ == main():
    main()