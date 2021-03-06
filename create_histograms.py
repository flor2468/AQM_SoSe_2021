from import_from_csv import *
from matplotlib.ticker import MaxNLocator
from get_data_for_diagrams import *

def create_histogram(which_histogram):

    data = readCSV('csv_files/edited/survey_complete.csv')
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()

    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")

    stress_book = processDataToString(data, "How stressed do you feel after you've read a book on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ")
    stress_movie = processDataToString(data, "How stressed do you feel after you've watched a movie / a series on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ")

    pleasure_book = processDataToString(data, "How much do you like reading on a scale from 1 (not at all) to 10 (very much)? (Punkte von 1 bis 10) ")
    pleasure_movie = processDataToString(data, "How much do you like watching movies / series on a scale from 1 (not at all) to 10 (very much)? (Punkte von 1 bis 10) ")

    relax_book = processDataToString(data, "How relaxed do you feel after you've read a book on a scale from 1 (not at all relaxed) to 10 (very relaxed)? (Punkte von 1 bis 10) ")
    relax_movie = processDataToString(data, "How relaxed do you feel after you've watched a movie / a series on a scale from 1 (not at all relaxed) to 10 (very relaxed)? (Punkte von 1 bis 10) ")

    for i in range(len(motivation_book)):
        motivation_book[i] = int(motivation_book[i])

    for i in range(len(motivation_movie)):
        motivation_movie[i] = int(motivation_movie[i])

    for i in range(len(stress_book)):
        stress_book[i] = int(stress_book[i])

    for i in range(len(stress_movie)):
        stress_movie[i] = int(stress_movie[i])

    for i in range(len(pleasure_book)):
        pleasure_book[i] = int(pleasure_book[i])

    for i in range(len(pleasure_movie)):
        pleasure_movie[i] = int(pleasure_movie[i])

    for i in range(len(relax_book)):
        relax_book[i] = int(relax_book[i])

    for i in range(len(relax_movie)):
        relax_movie[i] = int(relax_movie[i])

    if (which_histogram == 'age'):

        age = processDataToString(data, "How old are you?")

        for i in range(len(age)):
            age[i] = int(age[i])

        bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
        
        hist, bins = np.histogram(age, bins = bins) 

        print(hist)
        print(bins)

        fig = plt.figure()
        ax = plt.figure().gca()

        plt.hist(age, bins = bins, rwidth=0.9, color='#955196', align='left') 
        plt.xlim([0, 65])
        ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
        ax.set_yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
        ax.set_ylabel('amount')
        ax.set_xlabel('age')

        plt.savefig('diagrams/histograms/age_histogram.png')

        plt.show()

    if (which_histogram == 'time'):

        book_time, movie_time = get_book_and_movie_times()

        bins = [0, 1, 2, 3, 4, 5]

        # BOOK
        hist, bins = np.histogram(book_time, bins = bins) 

        ax = plt.figure().gca()
        plt.hist(book_time, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticklabels(['in the morning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
        ax.set_ylabel('amount')
        ax.set_xlabel('\npart of the day')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/time_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(movie_time, bins = bins) 

        ax = plt.figure().gca()
        plt.hist(movie_time, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticklabels(['in the morning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
        ax.set_ylabel('amount')
        ax.set_xlabel('\npart of the day')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/time_movie_histogram.png')

        plt.show()

    if (which_histogram == 'symptoms'):

        print(symptoms_movie)

        bins = [1, 2, 3, 4, 5, 6]

        # BOOK
        hist, bins = np.histogram(symptoms_book, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(symptoms_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('\nfrequency')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/symptoms_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(symptoms_movie, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(symptoms_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('\nfrequency')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/symptoms_movie_histogram.png')

        plt.show()

    if (which_histogram == 'snacks'):

        print(snacks_movie)

        bins = [1, 2, 3, 4, 5, 6]

        # BOOK
        hist, bins = np.histogram(snacks_book, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(snacks_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('\nfrequency')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/snacks_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(snacks_movie, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(snacks_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('\nfrequency')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/snacks_movie_histogram.png')

        plt.show()

    if (which_histogram == 'motivation'):

        print(motivation_movie)

        bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        # BOOK
        hist, bins = np.histogram(motivation_book, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(motivation_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_ylabel('amount')
        ax.set_xlabel('motivation')

        plt.savefig('diagrams/histograms/motivation_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(motivation_movie, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(motivation_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_ylabel('amount')
        ax.set_xlabel('motivation')

        plt.savefig('diagrams/histograms/motivation_movie_histogram.png')

        plt.show()

    if (which_histogram == 'stress'):

        bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        # BOOK
        hist, bins = np.histogram(stress_book, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(stress_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
        ax.set_ylabel('amount')
        ax.set_xlabel('stress')

        plt.savefig('diagrams/histograms/stress_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(stress_movie, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(stress_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_ylabel('amount')
        ax.set_xlabel('stress')

        plt.savefig('diagrams/histograms/stress_movie_histogram.png')

        plt.show()

    if (which_histogram == 'frequence book'):

        bins = [1, 2, 3, 4, 5, 6]

        print("frequently_book")
        print(frequently_book)

        # BOOK
        hist, bins = np.histogram(frequently_book, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(frequently_book, bins = bins, rwidth=0.9, color='#955196', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('\nfrequency')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/frequence_book_histogram.png')

        plt.show()

    if (which_histogram == 'health'):

        bins = [1, 2, 3, 4, 5]

        A, B, C, D = get_dispersion_health()
        print(A, B, C, D)

        ax = plt.figure().gca()

        labels = ['A', 'B', 'C', 'D']
        answers = [A, B, C, D]
        ax.bar(labels, answers, color='#955196')
        ax.set_xticklabels(['I', 'II', 'III', 'IV'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
        ax.set_ylabel('amount')
        ax.set_xlabel('\ntype of statement')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/health_histogram.png')

        plt.show()

    if (which_histogram == 'pleasure'):

        bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        # BOOK
        hist, bins = np.histogram(pleasure_book, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(pleasure_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
        ax.set_ylabel('amount')
        ax.set_xlabel('pleasure')

        plt.savefig('diagrams/histograms/pleasure_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(pleasure_movie, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(pleasure_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
        ax.set_ylabel('amount')
        ax.set_xlabel('pleasure')

        plt.savefig('diagrams/histograms/pleasure_movie_histogram.png')

        plt.show()

    if (which_histogram == 'relax'):

        bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        # BOOK
        hist, bins = np.histogram(relax_book, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(relax_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_ylabel('amount')
        ax.set_xlabel('relaxation')

        plt.savefig('diagrams/histograms/relax_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(relax_movie, bins = bins) 
        print(hist)
        print(bins)

        ax = plt.figure().gca()
        plt.hist(relax_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 

        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_ylabel('amount')
        ax.set_xlabel('relaxation')

        plt.savefig('diagrams/histograms/relax_movie_histogram.png')

        plt.show()


def main():
    # create_histogram('age')
    # create_histogram('time')
    # create_histogram('symptoms')
    # create_histogram('snacks')
    # create_histogram('motivation')
    # create_histogram('stress')
    # create_histogram('frequence book')
    # create_histogram('health')
    # create_histogram('pleasure')
    create_histogram('relax')


if __name__ ==  main():
    main()