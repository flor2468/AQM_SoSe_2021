from import_from_csv import *
from matplotlib.ticker import MaxNLocator
from get_data_for_diagrams import *

def create_histogram(which_histogram):

    data = readCSV('csv_files/edited/survey_complete.csv')
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()
    # data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")

    if (which_histogram == 'age'):

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
        

        ax = plt.figure().gca()
        plt.hist(age, bins = bins, rwidth=0.9, color='#955196', align='left') 
        plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
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
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(book_time, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticklabels(['in the morning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
        ax.set_ylabel('amount')
        ax.set_xlabel('part of the day')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/time_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(movie_time, bins = bins) 
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(movie_time, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticklabels(['in the morning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
        ax.set_ylabel('amount')
        ax.set_xlabel('part of the day')
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
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(symptoms_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never\n(1)', 'seldom\n(2)', 'sometimes\n(3)', 'often\n(4)', 'very often\n(5)'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('frequency *')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/symptoms_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(symptoms_movie, bins = bins) 
        print(hist)
        print(bins)
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(symptoms_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never\n(1)', 'seldom\n(2)', 'sometimes\n(3)', 'often\n(4)', 'very often\n(5)'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('frequency *')
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
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(snacks_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never\n(1)', 'seldom\n(2)', 'sometimes\n(3)', 'often\n(4)', 'very often\n(5)'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('frequency *')
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        plt.savefig('diagrams/histograms/snacks_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(snacks_movie, bins = bins) 
        print(hist)
        print(bins)
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(snacks_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(['never\n(1)', 'seldom\n(2)', 'sometimes\n(3)', 'often\n(4)', 'very often\n(5)'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35])
        ax.set_ylabel('amount')
        ax.set_xlabel('frequency *')
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
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(motivation_book, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_ylabel('amount')
        ax.set_xlabel('motivation *')

        plt.savefig('diagrams/histograms/motivation_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(motivation_movie, bins = bins) 
        print(hist)
        print(bins)
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(motivation_movie, bins = bins, rwidth=0.9, color='#007c50', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_xticklabels(['1', '2', '3', '4', '5', '6','7', '8', '9', '10'])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_ylabel('amount')
        ax.set_xlabel('motivation *')

        plt.savefig('diagrams/histograms/motivation_movie_histogram.png')

        plt.show()



def main():
    create_histogram('age')
    create_histogram('time')
    create_histogram('symptoms')
    create_histogram('snacks')
    create_histogram('motivation')


if __name__ ==  main():
    main()