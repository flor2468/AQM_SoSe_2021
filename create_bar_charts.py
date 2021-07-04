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


def create_mean_bar_chart_with_multiple_bars():

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


def create_age_time_bar_chart():

    # younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night = filter_by_age_and_time()

    younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night = get_dispersion_age_time()

    # BOOK

    book_data = [[younger_book_morning, younger_book_noon, younger_book_afternoon, younger_book_evening, younger_book_night], 
            [older_book_morning, older_book_noon, older_book_afternoon, older_book_evening, older_book_night]]

    Pos = np.arange(5)

    fig, ax = plt.subplots()

    ax.bar(Pos + 0.00, book_data[0], color='lightgreen', width=0.25)
    ax.bar(Pos + 0.25, book_data[1], color='orange', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['in the\nmorning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('part of the day')
    # plt.text(-0.5, -1.7, '* of getting physically active after the activity')

    younger_patch = mpatches.Patch(color='lightgreen', label='age groups A-C')
    older_patch = mpatches.Patch(color='orange', label='age groups D-F')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height])
    ax.legend(handles=[younger_patch, older_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_time_book.png')

    plt.show()

    # MOVIE

    movie_data = [[younger_movie_morning, younger_movie_noon, younger_movie_afternoon, younger_movie_evening, younger_movie_night], 
            [older_movie_morning, older_movie_noon, older_movie_afternoon, older_movie_evening, older_movie_night]]

    Pos = np.arange(5)

    fig, ax = plt.subplots()

    ax.bar(Pos + 0.00, movie_data[0], color='lightgreen', width=0.25)
    ax.bar(Pos + 0.25, movie_data[1], color='orange', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['in the\nmorning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('part of the day')
    # plt.text(-0.5, -1.7, '* of getting physically active after the activity')

    younger_patch = mpatches.Patch(color='lightgreen', label='age groups A-C')
    older_patch = mpatches.Patch(color='orange', label='age groups D-F')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height])
    ax.legend(handles=[younger_patch, older_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_time_movie.png')

    plt.show()


def create_age_symptoms_bar_chart():
    
    younger_symptoms_book_never, younger_symptoms_book_seldom, younger_symptoms_book_sometimes, younger_symptoms_book_often, younger_symptoms_book_very_often, older_symptoms_book_never, older_symptoms_book_seldom, older_symptoms_book_sometimes, older_symptoms_book_often, older_symptoms_book_very_often, younger_symptoms_movie_never, younger_symptoms_movie_seldom, younger_symptoms_movie_sometimes, younger_symptoms_movie_often, younger_symptoms_movie_very_often, older_symptoms_movie_never, older_symptoms_movie_seldom, older_symptoms_movie_sometimes, older_symptoms_movie_often, older_symptoms_movie_very_often = get_dispersion_age_symptoms()

    # BOOK
    book_data = [[younger_symptoms_book_never, younger_symptoms_book_seldom, younger_symptoms_book_sometimes, younger_symptoms_book_often, younger_symptoms_book_very_often], 
            [older_symptoms_book_never, older_symptoms_book_seldom, older_symptoms_book_sometimes, older_symptoms_book_often, older_symptoms_book_very_often]]

    Pos = np.arange(5)

    fig, ax = plt.subplots()

    ax.bar(Pos + 0.00, book_data[0], color='lightgreen', width=0.25)
    ax.bar(Pos + 0.25, book_data[1], color='orange', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
    # ax.xaxis.set_ticks_position('top')
    ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_ylabel('percentage')
    ax.set_xlabel('frequency *')
    # plt.text(-0.5, -1.7, '* of getting physically active after the activity')

    younger_patch = mpatches.Patch(color='lightgreen', label='age groups A-C')
    older_patch = mpatches.Patch(color='orange', label='age groups D-F')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[younger_patch, older_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_symptoms_book_version_1.png')

    plt.show()

    # MOVIE
    movie_data = [[younger_symptoms_movie_never, younger_symptoms_movie_seldom, younger_symptoms_movie_sometimes, younger_symptoms_movie_often, younger_symptoms_movie_very_often], 
            [older_symptoms_movie_never, older_symptoms_movie_seldom, older_symptoms_movie_sometimes, older_symptoms_movie_often, older_symptoms_movie_very_often]]

    Pos = np.arange(5)

    fig, ax = plt.subplots()

    ax.bar(Pos + 0.00, movie_data[0], color='lightgreen', width=0.25)
    ax.bar(Pos + 0.25, movie_data[1], color='orange', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
    # ax.xaxis.set_ticks_position('top')
    ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_ylabel('percentage')
    ax.set_xlabel('frequency *')
    # plt.text(-0.5, -1.7, '* of getting physically active after the activity')

    younger_patch = mpatches.Patch(color='lightgreen', label='age groups A-C')
    older_patch = mpatches.Patch(color='orange', label='age groups D-F')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[younger_patch, older_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_symptoms_movie_version_1.png')

    plt.show()


def create_age_symptoms_stacked_bar_chart():

    younger_symptoms_book_never, younger_symptoms_book_seldom, younger_symptoms_book_sometimes, younger_symptoms_book_often, younger_symptoms_book_very_often, older_symptoms_book_never, older_symptoms_book_seldom, older_symptoms_book_sometimes, older_symptoms_book_often, older_symptoms_book_very_often, younger_symptoms_movie_never, younger_symptoms_movie_seldom, younger_symptoms_movie_sometimes, younger_symptoms_movie_often, younger_symptoms_movie_very_often, older_symptoms_movie_never, older_symptoms_movie_seldom, older_symptoms_movie_sometimes, older_symptoms_movie_often, older_symptoms_movie_very_often = get_dispersion_age_symptoms()

    labels = ['age groups A-C', 'age groups D-F']

    # BOOK
    never = [younger_symptoms_book_never, older_symptoms_book_never]
    # print(never)
    seldom = [younger_symptoms_book_seldom, older_symptoms_book_seldom]
    # print(seldom)
    sometimes = [younger_symptoms_book_sometimes, older_symptoms_book_sometimes]
    # print(sometimes)
    often = [younger_symptoms_book_often, older_symptoms_book_often]
    # print(often)
    very_often = [younger_symptoms_book_very_often, older_symptoms_book_very_often]
    # print(very_often)

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='lightgreen')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='purple')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='gold')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='magenta')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='cyan')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='lightgreen', label='never')
    seldom_patch = mpatches.Patch(color='purple', label='seldom')
    sometimes_patch = mpatches.Patch(color='gold', label='sometimes')
    often_patch = mpatches.Patch(color='magenta', label='often')
    very_often_patch = mpatches.Patch(color='cyan', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_symptoms_book_version_2.png')

    plt.show()

    # MOVIE 
    never = [younger_symptoms_movie_never, older_symptoms_movie_never]
    # print(never)
    seldom = [younger_symptoms_movie_seldom, older_symptoms_movie_seldom]
    # print(seldom)
    sometimes = [younger_symptoms_movie_sometimes, older_symptoms_movie_sometimes]
    # print(sometimes)
    often = [younger_symptoms_movie_often, older_symptoms_movie_often]
    # print(often)
    very_often = [younger_symptoms_movie_very_often, older_symptoms_movie_very_often]
    # print(very_often)

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='lightgreen')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='purple')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='gold')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='magenta')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='cyan')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')

    never_patch = mpatches.Patch(color='lightgreen', label='never')
    seldom_patch = mpatches.Patch(color='purple', label='seldom')
    sometimes_patch = mpatches.Patch(color='gold', label='sometimes')
    often_patch = mpatches.Patch(color='magenta', label='often')
    very_often_patch = mpatches.Patch(color='cyan', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)


    plt.savefig('diagrams/bar_charts/age_symptoms_movie_version_2.png')

    plt.show()


def create_age_snacks_stacked_bar_chart():

    younger_snacks_book_never, younger_snacks_book_seldom, younger_snacks_book_sometimes, younger_snacks_book_often, younger_snacks_book_very_often, older_snacks_book_never, older_snacks_book_seldom, older_snacks_book_sometimes, older_snacks_book_often, older_snacks_book_very_often, younger_snacks_movie_never, younger_snacks_movie_seldom, younger_snacks_movie_sometimes, younger_snacks_movie_often, younger_snacks_movie_very_often, older_snacks_movie_never, older_snacks_movie_seldom, older_snacks_movie_sometimes, older_snacks_movie_often, older_snacks_movie_very_often = get_dispersion_age_snacks()

    labels = ['age groups A-C', 'age groups D-F']

    # BOOK
    never = [younger_snacks_book_never, older_snacks_book_never]
    # print(never)
    seldom = [younger_snacks_book_seldom, older_snacks_book_seldom]
    # print(seldom)
    sometimes = [younger_snacks_book_sometimes, older_snacks_book_sometimes]
    # print(sometimes)
    often = [younger_snacks_book_often, older_snacks_book_often]
    # print(often)
    very_often = [younger_snacks_book_very_often, older_snacks_book_very_often]
    # print(very_often)

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='lightgreen')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='purple')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='gold')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='magenta')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='cyan')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='lightgreen', label='never')
    seldom_patch = mpatches.Patch(color='purple', label='seldom')
    sometimes_patch = mpatches.Patch(color='gold', label='sometimes')
    often_patch = mpatches.Patch(color='magenta', label='often')
    very_often_patch = mpatches.Patch(color='cyan', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_snacks_book_version_2.png')

    plt.show()

    # MOVIE 
    never = [younger_snacks_movie_never, older_snacks_movie_never]
    # print(never)
    seldom = [younger_snacks_movie_seldom, older_snacks_movie_seldom]
    # print(seldom)
    sometimes = [younger_snacks_movie_sometimes, older_snacks_movie_sometimes]
    # print(sometimes)
    often = [younger_snacks_movie_often, older_snacks_movie_often]
    # print(often)
    very_often = [younger_snacks_movie_very_often, older_snacks_movie_very_often]
    # print(very_often)

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='lightgreen')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='purple')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='gold')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='magenta')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='cyan')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='lightgreen', label='never')
    seldom_patch = mpatches.Patch(color='purple', label='seldom')
    sometimes_patch = mpatches.Patch(color='gold', label='sometimes')
    often_patch = mpatches.Patch(color='magenta', label='often')
    very_often_patch = mpatches.Patch(color='cyan', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)


    plt.savefig('diagrams/bar_charts/age_snacks_movie_version_2.png')

    plt.show()


def create_age_motivation_stacked_bar_chart():

    younger_motivation_book_never, younger_motivation_book_seldom, younger_motivation_book_sometimes, younger_motivation_book_often, younger_motivation_book_very_often, older_motivation_book_never, older_motivation_book_seldom, older_motivation_book_sometimes, older_motivation_book_often, older_motivation_book_very_often, younger_motivation_movie_never, younger_motivation_movie_seldom, younger_motivation_movie_sometimes, younger_motivation_movie_often, younger_motivation_movie_very_often, older_motivation_movie_never, older_motivation_movie_seldom, older_motivation_movie_sometimes, older_motivation_movie_often, older_motivation_movie_very_often = get_dispersion_age_motivation()

    labels = ['age groups A-C', 'age groups D-F']

    # BOOK
    never = [younger_motivation_book_never, older_motivation_book_never]
    # print(never)
    seldom = [younger_motivation_book_seldom, older_motivation_book_seldom]
    # print(seldom)
    sometimes = [younger_motivation_book_sometimes, older_motivation_book_sometimes]
    # print(sometimes)
    often = [younger_motivation_book_often, older_motivation_book_often]
    # print(often)
    very_often = [younger_motivation_book_very_often, older_motivation_book_very_often]
    # print(very_often)

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='lightgreen')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='purple')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='gold')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='magenta')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='cyan')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='lightgreen', label='1, 2')
    seldom_patch = mpatches.Patch(color='purple', label='3, 4')
    sometimes_patch = mpatches.Patch(color='gold', label='5, 6')
    often_patch = mpatches.Patch(color='magenta', label='7, 8')
    very_often_patch = mpatches.Patch(color='cyan', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_motivation_book_version_2.png')

    plt.show()

    # MOVIE 
    never = [younger_motivation_movie_never, older_motivation_movie_never]
    # print(never)
    seldom = [younger_motivation_movie_seldom, older_motivation_movie_seldom]
    # print(seldom)
    sometimes = [younger_motivation_movie_sometimes, older_motivation_movie_sometimes]
    # print(sometimes)
    often = [younger_motivation_movie_often, older_motivation_movie_often]
    # print(often)
    very_often = [younger_motivation_movie_very_often, older_motivation_movie_very_often]
    # print(very_often)

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='lightgreen')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='purple')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='gold')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='magenta')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='cyan')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='lightgreen', label='1, 2')
    seldom_patch = mpatches.Patch(color='purple', label='3, 4')
    sometimes_patch = mpatches.Patch(color='gold', label='5, 6')
    often_patch = mpatches.Patch(color='magenta', label='7, 8')
    very_often_patch = mpatches.Patch(color='cyan', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_motivation_movie_version_2.png')

    plt.show()



def main():
    data = readCSV('csv_files/edited/survey_complete.csv')
    motivation_book = processDataToString(data, "How motivated are you to become physically active after you've read a book on a scale of 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    motivation_movie = processDataToString(data, "How motivated are you to become physically active after you've watched a movie / a series on a scale from 1 (not at all motivated) to 10 (very motivated)? (Punkte von 1 bis 10) ")
    symptoms_book, symptoms_movie, snacks_book, snacks_movie, frequently_book = convert_string_scales_to_values()

    # create_simple_bar_chart(symptoms_book, symptoms_movie, 'symptoms')
    # create_simple_bar_chart(snacks_book, snacks_movie, 'snacks')
    # create_simple_bar_chart(motivation_book, motivation_movie, 'motivation')

    # create_mean_bar_chart_with_multiple_bars()

    create_age_time_bar_chart()
    # create_age_symptoms_bar_chart()

    # create_age_symptoms_stacked_bar_chart()
    # create_age_snacks_stacked_bar_chart()
    # create_age_motivation_stacked_bar_chart()


if __name__ == main():
    main()