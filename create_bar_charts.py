from import_from_csv import *
import matplotlib.pyplot as plt
from calculate_values import *
from get_data_for_diagrams import *


def create_simple_bar_chart(array_1, array_2, topic):

    mean_1 = calculate_mean(array_1)
    print(mean_1)
    mean_2 = calculate_mean(array_2)
    print(mean_2)

    fig, ax = plt.subplots()
    labels = ['reading a book', 'watching a movie / a series']
    values = [mean_1, mean_2]
    ax.bar(labels, values, color=['purple', 'goldenrod'])

    if (topic == 'symptoms' or topic == 'snacks'):

        ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_yticklabels(['never\n(1)', 'seldom\n(2)', 'some\ntimes\n(3)', 'often\n(4)', 'very\noften\n(5)'])

        if (topic == 'symptoms'):

            ax.set_ylabel('frequency *')
            # plt.text(-0.5, -1.0, '*  of having symptoms like \na headache, burning eyes etc.')

        if (topic == 'snacks'):

            ax.set_ylabel('frequency *')
            # plt.text(-0.5, -1.0, '*  of eating snacks during the activity')

        box = ax.get_position()
        # [left, bottom, width, height]
        ax.set_position([box.x0 * 1.2, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

    else:
        ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax.set_ylabel('motivation *')
        # plt.text(-0.5, -1.7, '* of getting physically active after the activity')

        box = ax.get_position()
        # [left, bottom, width, height]
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])


    plt.savefig('diagrams/bar_charts/mean_' + str(topic) + '.png')

    plt.show()


def create_bar_chart_with_multiple_bars():

    younger_symptoms_book, younger_symptoms_movie, older_symptoms_book, older_symptoms_movie, younger_snacks_book, younger_snacks_movie, older_snacks_book, older_snacks_movie, younger_motivation_book, younger_motivation_movie, older_motivation_book, older_motivation_movie = filter_by_age_and_physical_aspects()

    mean_ysb = calculate_mean(younger_symptoms_book)
    mean_ysm = calculate_mean(younger_symptoms_movie)
    # print(younger_symptoms_book)
    # print(mean_ysb)
    # print(younger_symptoms_movie)
    # print(mean_ysm)
    mean_osb = calculate_mean(older_symptoms_book)
    mean_osm = calculate_mean(older_symptoms_movie)
    # print(older_symptoms_book)
    # print(mean_osb)
    # print(older_symptoms_movie)
    # print(mean_osm)
    mean_ysnab = calculate_mean(younger_snacks_book)
    mean_ysnam = calculate_mean(younger_snacks_movie)
    # print(younger_snacks_book)
    # print(mean_ysnab)
    # print(younger_snacks_movie)
    # print(mean_ysnam)
    mean_osnab = calculate_mean(older_snacks_book)
    mean_osnam = calculate_mean(older_snacks_movie)
    # print(older_snacks_book)
    # print(mean_osnab)
    # # print(older_snacks_movie)
    # print(mean_osnam)
    mean_ymotb = calculate_mean(younger_motivation_book)
    mean_ymotm = calculate_mean(younger_motivation_movie)
    # print(younger_motivation_book)
    # print(mean_ymotb)
    # print(younger_motivation_movie)
    # print(mean_ymotm)
    mean_omotb = calculate_mean(older_motivation_book)
    mean_omotm = calculate_mean(older_motivation_movie)
    # print(older_motivation_book)
    # print(mean_omotb)
    # print(older_motivation_movie)
    # print(mean_omotm)

    # data = [[mean_ysb, mean_ysm, mean_ysnab, mean_ysnam, mean_ymotb, mean_ymotm], 
    #         [mean_osb, mean_osm, mean_osnab, mean_osnam, mean_omotb, mean_omotm]]

    # SYMPTOMS

    data = [[mean_ysb, mean_osb], [mean_ysm, mean_osm]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    # plt.yticks(Pos-(1/6), ["", "Level 2", "Level 3", "Level 4", "Level 5"])
    ax.bar(Pos + 0.00, data[0], color='purple', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='goldenrod', width=0.25)
    plt.xticks(Pos+0.12, ["age groups A-C", "age groups D-F"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['never\n(1)', 'seldom\n(2)', 'some\ntimes\n(3)', 'often\n(4)', 'very\noften\n(5)'])
    ax.set_ylabel('frequency *')
    # plt.text(-0.5, -1.0, '*  of having symptoms like \na headache, burning eyes etc.')

    book_patch = mpatches.Patch(color='purple', label='reading a book')
    movie_patch = mpatches.Patch(color='goldenrod', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0 * 1.2, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/mean_age_symptoms.png')

    plt.show()

    # SNACKS

    data = [[mean_ysnab, mean_osnab], [mean_ysnam, mean_osnam]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    # plt.yticks(Pos-(1/6), ["", "Level 2", "Level 3", "Level 4", "Level 5"])
    ax.bar(Pos + 0.00, data[0], color='purple', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='goldenrod', width=0.25)
    plt.xticks(Pos+0.12, ["age groups A-C", "age groups D-F"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['never\n(1)', 'seldom\n(2)', 'some\ntimes\n(3)', 'often\n(4)', 'very\noften\n(5)'])
    ax.set_ylabel('frequency *')
    # plt.text(-0.5, -1.0, '*  of eating snacks during the activity')

    book_patch = mpatches.Patch(color='purple', label='reading a book')
    movie_patch = mpatches.Patch(color='goldenrod', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0 * 1.2, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/mean_age_snacks.png')

    plt.show()

    # MOTIVATION

    data = [[mean_ymotb, mean_omotb], [mean_ymotm, mean_omotm]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    # plt.yticks(Pos-(1/6), ["", "Level 2", "Level 3", "Level 4", "Level 5"])
    ax.bar(Pos + 0.00, data[0], color='purple', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='goldenrod', width=0.25)
    plt.xticks(Pos+0.12, ["age groups A-C", "age groups D-F"])
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylabel('motivation *')
    # plt.text(-0.5, -1.7, '* of getting physically active after the activity')

    book_patch = mpatches.Patch(color='purple', label='reading a book')
    movie_patch = mpatches.Patch(color='goldenrod', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/mean_age_motivation.png')

    plt.show()


def create_histogram_bar_chart():

    younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night = filter_by_age_and_time()

    


def main():
    data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()

    # create_simple_bar_chart(symptoms_book, symptoms_movie, 'symptoms')
    # create_simple_bar_chart(snacks_book, snacks_movie, 'snacks')
    # create_simple_bar_chart(motivation_book, motivation_movie, 'motivation')

    create_bar_chart_with_multiple_bars()


if __name__ == main():
    main()