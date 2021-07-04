from import_from_csv import *
from matplotlib.ticker import MaxNLocator
from get_data_for_diagrams import *

def create_histogram(which_histogram):

    data = readCSV('csv_files/edited/survey_complete.csv')

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
        plt.hist(age, bins = bins, rwidth=0.9, color='turquoise', align='left') 
        plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
        ax.set_yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

        plt.savefig('diagrams/histograms/age_histogram.png')

        plt.show()

    if (which_histogram == 'time'):

        book_time, movie_time = get_book_and_movie_times()

        bins = [0, 1, 2, 3, 4, 5]

        # BOOK
        hist, bins = np.histogram(book_time, bins = bins) 
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(book_time, bins = bins, rwidth=0.9, color='turquoise', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticklabels(['in the morning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

        plt.savefig('diagrams/histograms/time_book_histogram.png')

        plt.show()

        # MOVIE
        hist, bins = np.histogram(movie_time, bins = bins) 
        # fig = plt.figure()
        ax = plt.figure().gca()
        plt.hist(movie_time, bins = bins, rwidth=0.9, color='turquoise', align='left') 
        # plt.xlim([0, 65])
        # plt.xticks(np.arange(9,61,1))
        ax.set_xticklabels(['in the morning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

        plt.savefig('diagrams/histograms/time_movie_histogram.png')

        plt.show()

    # if (which_histogram == 'age-time'):

    #     younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night = filter_by_age_and_time()




def main():
    # create_histogram('age')
    # create_histogram('time')
    create_histogram('age-time')


if __name__ ==  main():
    main()