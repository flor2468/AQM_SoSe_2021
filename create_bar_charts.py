from import_from_csv import *
import matplotlib.pyplot as plt
from calculate_values import *
from get_data_for_diagrams import *


def create_simple_bar_chart(array_1, array_2, topic):

    mean_1 = calculate_mean(array_1)
    mean_2 = calculate_mean(array_2)

    fig, ax = plt.subplots()
    labels = ['reading a book', 'watching a movie / a series']
    values = [mean_1, mean_2]
    ax.bar(labels, values, color=['#00283b', '#ffa600'])

    if (topic == 'symptoms' or topic == 'snacks'):

        ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_yticklabels(['never', 'seldom', 'some\ntimes', 'often', 'very\noften'])

        if (topic == 'symptoms' or topic == 'snacks'):

            ax.set_ylabel('frequency')

        box = ax.get_position()
        # [left, bottom, width, height]
        ax.set_position([box.x0 * 1.2, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

    else:

        ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax.set_ylabel('motivation')
        box = ax.get_position()
        # [left, bottom, width, height]
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

    plt.savefig('diagrams/bar_charts/mean_' + str(topic) + '.png')

    plt.show()


def create_mean_bar_chart_with_multiple_bars():

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

    data = [[mean_ysb, mean_osb], [mean_ysm, mean_osm]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    ax.bar(Pos + 0.00, data[0], color='#00283b', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='#ffa600', width=0.25)
    plt.xticks(Pos+0.12, ["A-C", "D-F"])
    ax.set_xlabel('age groups')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['never', 'seldom', 'some\ntimes', 'often', 'very\noften'])
    ax.set_ylabel('frequency')

    book_patch = mpatches.Patch(color='#00283b', label='reading a book')
    movie_patch = mpatches.Patch(color='#ffa600', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0 * 1.2, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/mean_age_symptoms.png')

    plt.show()

    # SNACKS

    data = [[mean_ysnab, mean_osnab], [mean_ysnam, mean_osnam]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    ax.bar(Pos + 0.00, data[0], color='#00283b', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='#ffa600', width=0.25)
    plt.xticks(Pos+0.12, ["A-C", "D-F"])
    ax.set_xlabel('age groups')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['never', 'seldom', 'some\ntimes', 'often', 'very\noften'])
    ax.set_ylabel('frequency')

    book_patch = mpatches.Patch(color='#00283b', label='reading a book')
    movie_patch = mpatches.Patch(color='#ffa600', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0 * 1.2, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/mean_age_snacks.png')

    plt.show()

    # MOTIVATION

    data = [[mean_ymotb, mean_omotb], [mean_ymotm, mean_omotm]]

    Pos = np.arange(2)

    fig, ax = plt.subplots()
    ax.bar(Pos + 0.00, data[0], color='#00283b', width=0.25)
    ax.bar(Pos + 0.25, data[1], color='#ffa600', width=0.25)
    plt.xticks(Pos+0.12, ["A-C", "D-F"])
    ax.set_xlabel('age groups')
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylabel('motivation')

    book_patch = mpatches.Patch(color='#00283b', label='reading a book')
    movie_patch = mpatches.Patch(color='#ffa600', label='watching a movie')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[book_patch, movie_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/mean_age_motivation.png')

    plt.show()


def create_age_time_bar_chart():

    younger_book_morning, younger_movie_morning, older_book_morning, older_movie_morning, younger_book_noon, younger_movie_noon, older_book_noon, older_movie_noon, younger_book_afternoon, younger_movie_afternoon, older_book_afternoon, older_movie_afternoon, younger_book_evening, younger_movie_evening, older_book_evening, older_movie_evening, younger_book_night, younger_movie_night, older_book_night, older_movie_night = get_dispersion_age_time()

    # BOOK

    book_data = [[younger_book_morning, younger_book_noon, younger_book_afternoon, younger_book_evening, younger_book_night], 
            [older_book_morning, older_book_noon, older_book_afternoon, older_book_evening, older_book_night]]

    Pos = np.arange(5)

    fig, ax = plt.subplots()

    ax.bar(Pos + 0.00, book_data[0], color='#004a5a', width=0.25)
    ax.bar(Pos + 0.25, book_data[1], color='#90a201', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['in the\nmorning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('part of the day')

    younger_patch = mpatches.Patch(color='#004a5a', label='A-C')
    older_patch = mpatches.Patch(color='#90a201', label='D-F')

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

    ax.bar(Pos + 0.00, movie_data[0], color='#004a5a', width=0.25)
    ax.bar(Pos + 0.25, movie_data[1], color='#90a201', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['in the\nmorning', 'at noon', 'in the\nafternoon', 'in the\nevening', 'at night'])
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('part of the day')

    younger_patch = mpatches.Patch(color='#004a5a', label='A-C')
    older_patch = mpatches.Patch(color='#90a201', label='D-F')

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

    ax.bar(Pos + 0.00, book_data[0], color='#004a5a', width=0.25)
    ax.bar(Pos + 0.25, book_data[1], color='#90a201', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
    ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_ylabel('percentage')
    ax.set_xlabel('frequency')

    younger_patch = mpatches.Patch(color='#004a5a', label='A-C')
    older_patch = mpatches.Patch(color='#90a201', label='D-F')

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

    ax.bar(Pos + 0.00, movie_data[0], color='#004a5a', width=0.25)
    ax.bar(Pos + 0.25, movie_data[1], color='#90a201', width=0.25)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xticklabels(['never', 'seldom', 'sometimes', 'often', 'very often'])
    ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_ylabel('percentage')
    ax.set_xlabel('frequency')

    younger_patch = mpatches.Patch(color='#004a5a', label='A-C')
    older_patch = mpatches.Patch(color='#90a201', label='D-F')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[younger_patch, older_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_symptoms_movie_version_1.png')

    plt.show()


def create_age_symptoms_stacked_bar_chart():

    # sources (also for following functions):
    # https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html
    # https://stackoverflow.com/questions/44309507/stacked-bar-plot-using-matplotlib

    younger_symptoms_book_never, younger_symptoms_book_seldom, younger_symptoms_book_sometimes, younger_symptoms_book_often, younger_symptoms_book_very_often, older_symptoms_book_never, older_symptoms_book_seldom, older_symptoms_book_sometimes, older_symptoms_book_often, older_symptoms_book_very_often, younger_symptoms_movie_never, younger_symptoms_movie_seldom, younger_symptoms_movie_sometimes, younger_symptoms_movie_often, younger_symptoms_movie_very_often, older_symptoms_movie_never, older_symptoms_movie_seldom, older_symptoms_movie_sometimes, older_symptoms_movie_often, older_symptoms_movie_very_often = get_dispersion_age_symptoms()

    labels = ['A-C', 'D-F']

    # BOOK
    never = [younger_symptoms_book_never, older_symptoms_book_never]
    seldom = [younger_symptoms_book_seldom, older_symptoms_book_seldom]
    sometimes = [younger_symptoms_book_sometimes, older_symptoms_book_sometimes]
    often = [younger_symptoms_book_often, older_symptoms_book_often]
    very_often = [younger_symptoms_book_very_often, older_symptoms_book_very_often]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='#00283b')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='#00525d')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='#007c50')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='#779d18')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='#00283b', label='never')
    seldom_patch = mpatches.Patch(color='#00525d', label='seldom')
    sometimes_patch = mpatches.Patch(color='#007c50', label='sometimes')
    often_patch = mpatches.Patch(color='#779d18', label='often')
    very_often_patch = mpatches.Patch(color='#ffa600', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_symptoms_book_version_2.png')

    plt.show()

    # MOVIE 
    never = [younger_symptoms_movie_never, older_symptoms_movie_never]
    seldom = [younger_symptoms_movie_seldom, older_symptoms_movie_seldom]
    sometimes = [younger_symptoms_movie_sometimes, older_symptoms_movie_sometimes]
    often = [younger_symptoms_movie_often, older_symptoms_movie_often]
    very_often = [younger_symptoms_movie_very_often, older_symptoms_movie_very_often]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='#00283b')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='#00525d')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='#007c50')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='#779d18')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')

    never_patch = mpatches.Patch(color='#00283b', label='never')
    seldom_patch = mpatches.Patch(color='#00525d', label='seldom')
    sometimes_patch = mpatches.Patch(color='#007c50', label='sometimes')
    often_patch = mpatches.Patch(color='#779d18', label='often')
    very_often_patch = mpatches.Patch(color='#ffa600', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_symptoms_movie_version_2.png')

    plt.show()


def create_age_snacks_stacked_bar_chart():

    younger_snacks_book_never, younger_snacks_book_seldom, younger_snacks_book_sometimes, younger_snacks_book_often, younger_snacks_book_very_often, older_snacks_book_never, older_snacks_book_seldom, older_snacks_book_sometimes, older_snacks_book_often, older_snacks_book_very_often, younger_snacks_movie_never, younger_snacks_movie_seldom, younger_snacks_movie_sometimes, younger_snacks_movie_often, younger_snacks_movie_very_often, older_snacks_movie_never, older_snacks_movie_seldom, older_snacks_movie_sometimes, older_snacks_movie_often, older_snacks_movie_very_often = get_dispersion_age_snacks()

    labels = ['A-C', 'D-F']

    # BOOK
    never = [younger_snacks_book_never, older_snacks_book_never]
    seldom = [younger_snacks_book_seldom, older_snacks_book_seldom]
    sometimes = [younger_snacks_book_sometimes, older_snacks_book_sometimes]
    often = [younger_snacks_book_often, older_snacks_book_often]
    very_often = [younger_snacks_book_very_often, older_snacks_book_very_often]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='#00283b')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='#00525d')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='#007c50')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='#779d18')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='#00283b', label='never')
    seldom_patch = mpatches.Patch(color='#00525d', label='seldom')
    sometimes_patch = mpatches.Patch(color='#007c50', label='sometimes')
    often_patch = mpatches.Patch(color='#779d18', label='often')
    very_often_patch = mpatches.Patch(color='#ffa600', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_snacks_book_version_2.png')

    plt.show()

    # MOVIE 
    never = [younger_snacks_movie_never, older_snacks_movie_never]
    seldom = [younger_snacks_movie_seldom, older_snacks_movie_seldom]
    sometimes = [younger_snacks_movie_sometimes, older_snacks_movie_sometimes]
    often = [younger_snacks_movie_often, older_snacks_movie_often]
    very_often = [younger_snacks_movie_very_often, older_snacks_movie_very_often]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='#00283b')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='#00525d')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='#007c50')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='#779d18')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='#00283b', label='never')
    seldom_patch = mpatches.Patch(color='#00525d', label='seldom')
    sometimes_patch = mpatches.Patch(color='#007c50', label='sometimes')
    often_patch = mpatches.Patch(color='#779d18', label='often')
    very_often_patch = mpatches.Patch(color='#ffa600', label='very often')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_snacks_movie_version_2.png')

    plt.show()


def create_age_motivation_stacked_bar_chart():

    younger_motivation_book_never, younger_motivation_book_seldom, younger_motivation_book_sometimes, younger_motivation_book_often, younger_motivation_book_very_often, older_motivation_book_never, older_motivation_book_seldom, older_motivation_book_sometimes, older_motivation_book_often, older_motivation_book_very_often, younger_motivation_movie_never, younger_motivation_movie_seldom, younger_motivation_movie_sometimes, younger_motivation_movie_often, younger_motivation_movie_very_often, older_motivation_movie_never, older_motivation_movie_seldom, older_motivation_movie_sometimes, older_motivation_movie_often, older_motivation_movie_very_often = get_dispersion_age_motivation()

    labels = ['A-C', 'D-F']

    # BOOK
    never = [younger_motivation_book_never, older_motivation_book_never]
    seldom = [younger_motivation_book_seldom, older_motivation_book_seldom]
    sometimes = [younger_motivation_book_sometimes, older_motivation_book_sometimes]
    often = [younger_motivation_book_often, older_motivation_book_often]
    very_often = [younger_motivation_book_very_often, older_motivation_book_very_often]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='#00283b')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='#00525d')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='#007c50')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='#779d18')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='#00283b', label='1, 2')
    seldom_patch = mpatches.Patch(color='#00525d', label='3, 4')
    sometimes_patch = mpatches.Patch(color='#007c50', label='5, 6')
    often_patch = mpatches.Patch(color='#779d18', label='7, 8')
    very_often_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_motivation_book_version_2.png')

    plt.show()

    # MOVIE 
    never = [younger_motivation_movie_never, older_motivation_movie_never]
    seldom = [younger_motivation_movie_seldom, older_motivation_movie_seldom]
    sometimes = [younger_motivation_movie_sometimes, older_motivation_movie_sometimes]
    often = [younger_motivation_movie_often, older_motivation_movie_often]
    very_often = [younger_motivation_movie_very_often, older_motivation_movie_very_often]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, never, width, label='never', color='#00283b')
    ax.bar(labels, seldom, width, bottom=never, label='seldom', color='#00525d')
    ax.bar(labels, sometimes, width, bottom=np.array(never)+np.array(seldom), label='sometimes', color='#007c50')
    ax.bar(labels, often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes), label='often', color='#779d18')
    ax.bar(labels, very_often, width, bottom=np.array(never)+np.array(seldom)+np.array(sometimes)+np.array(often), label='very often', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('age groups')
    
    never_patch = mpatches.Patch(color='#00283b', label='1, 2')
    seldom_patch = mpatches.Patch(color='#00525d', label='3, 4')
    sometimes_patch = mpatches.Patch(color='#007c50', label='5, 6')
    often_patch = mpatches.Patch(color='#779d18', label='7, 8')
    very_often_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[never_patch, seldom_patch, sometimes_patch, often_patch, very_often_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/age_motivation_movie_version_2.png')

    plt.show()


def frequency_stress_stacked_bar_chart(stress_book, stress_movie, data):

    never_book, never_movie, seldom_book, seldom_movie, sometimes_book, sometimes_movie, often_book, often_movie, very_often_book, very_often_movie = get_dispersion_of_data_of_scale_1_to_10(stress_book, stress_movie, data)

    labels = ['never', 'seldom', 'sometimes', 'often', 'very often']

    # BOOK
    scale_12 = [never_book[0], seldom_book[0], sometimes_book[0], often_book[0], very_often_book[0]]
    scale_34 = [never_book[1], seldom_book[1], sometimes_book[1], often_book[1], very_often_book[1]]
    scale_56 = [never_book[2], seldom_book[2], sometimes_book[2], often_book[2], very_often_book[2]]
    scale_78 = [never_book[3], seldom_book[3], sometimes_book[3], often_book[3], very_often_book[3]]
    scale_910 = [never_book[4], seldom_book[4], sometimes_book[4], often_book[4], very_often_book[4]]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, scale_12, width, label='1, 2', color='#00283b')
    ax.bar(labels, scale_34, width, bottom=scale_12, label='3, 4', color='#00525d')
    ax.bar(labels, scale_56, width, bottom=np.array(scale_12)+np.array(scale_34), label='5, 6', color='#007c50')
    ax.bar(labels, scale_78, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56), label='7, 8', color='#779d18')
    ax.bar(labels, scale_910, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56)+np.array(scale_78), label='9, 10', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('reading frequency')
    
    first_patch = mpatches.Patch(color='#00283b', label='1, 2')
    second_patch = mpatches.Patch(color='#00525d', label='3, 4')
    third_patch = mpatches.Patch(color='#007c50', label='5, 6')
    forth_patch = mpatches.Patch(color='#779d18', label='7, 8')
    fifth_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[first_patch, second_patch, third_patch, forth_patch, fifth_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/frequency_stress_book_2.png')

    plt.show()

    # MOVIE
    scale_12 = [never_movie[0], seldom_movie[0], sometimes_movie[0], often_movie[0], very_often_movie[0]]
    scale_34 = [never_movie[1], seldom_movie[1], sometimes_movie[1], often_movie[1], very_often_movie[1]]
    scale_56 = [never_movie[2], seldom_movie[2], sometimes_movie[2], often_movie[2], very_often_movie[2]]
    scale_78 = [never_movie[3], seldom_movie[3], sometimes_movie[3], often_movie[3], very_often_movie[3]]
    scale_910 = [never_movie[4], seldom_movie[4], sometimes_movie[4], often_movie[4], very_often_movie[4]]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, scale_12, width, label='1, 2', color='#00283b')
    ax.bar(labels, scale_34, width, bottom=scale_12, label='3, 4', color='#00525d')
    ax.bar(labels, scale_56, width, bottom=np.array(scale_12)+np.array(scale_34), label='5, 6', color='#007c50')
    ax.bar(labels, scale_78, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56), label='7, 8', color='#779d18')
    ax.bar(labels, scale_910, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56)+np.array(scale_78), label='9, 10', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('reading frequency')
    
    first_patch = mpatches.Patch(color='#00283b', label='1, 2')
    second_patch = mpatches.Patch(color='#00525d', label='3, 4')
    third_patch = mpatches.Patch(color='#007c50', label='5, 6')
    forth_patch = mpatches.Patch(color='#779d18', label='7, 8')
    fifth_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[first_patch, second_patch, third_patch, forth_patch, fifth_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/frequency_stress_movie_2.png')

    plt.show()


def frequency_pleasure_stacked_bar_chart(pleasure_book, pleasure_movie, data):

    never_book, never_movie, seldom_book, seldom_movie, sometimes_book, sometimes_movie, often_book, often_movie, very_often_book, very_often_movie = get_dispersion_of_data_of_scale_1_to_10(pleasure_book, pleasure_movie, data)

    labels = ['never', 'seldom', 'sometimes', 'often', 'very often']

    # BOOK
    scale_12 = [never_book[0], seldom_book[0], sometimes_book[0], often_book[0], very_often_book[0]]
    scale_34 = [never_book[1], seldom_book[1], sometimes_book[1], often_book[1], very_often_book[1]]
    scale_56 = [never_book[2], seldom_book[2], sometimes_book[2], often_book[2], very_often_book[2]]
    scale_78 = [never_book[3], seldom_book[3], sometimes_book[3], often_book[3], very_often_book[3]]
    scale_910 = [never_book[4], seldom_book[4], sometimes_book[4], often_book[4], very_often_book[4]]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, scale_12, width, label='1, 2', color='#00283b')
    ax.bar(labels, scale_34, width, bottom=scale_12, label='3, 4', color='#00525d')
    ax.bar(labels, scale_56, width, bottom=np.array(scale_12)+np.array(scale_34), label='5, 6', color='#007c50')
    ax.bar(labels, scale_78, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56), label='7, 8', color='#779d18')
    ax.bar(labels, scale_910, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56)+np.array(scale_78), label='9, 10', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('reading frequency')
    
    first_patch = mpatches.Patch(color='#00283b', label='1, 2')
    second_patch = mpatches.Patch(color='#00525d', label='3, 4')
    third_patch = mpatches.Patch(color='#007c50', label='5, 6')
    forth_patch = mpatches.Patch(color='#779d18', label='7, 8')
    fifth_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[first_patch, second_patch, third_patch, forth_patch, fifth_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/frequency_pleasure_book_2.png')

    plt.show()

    # MOVIE
    scale_12 = [never_movie[0], seldom_movie[0], sometimes_movie[0], often_movie[0], very_often_movie[0]]
    scale_34 = [never_movie[1], seldom_movie[1], sometimes_movie[1], often_movie[1], very_often_movie[1]]
    scale_56 = [never_movie[2], seldom_movie[2], sometimes_movie[2], often_movie[2], very_often_movie[2]]
    scale_78 = [never_movie[3], seldom_movie[3], sometimes_movie[3], often_movie[3], very_often_movie[3]]
    scale_910 = [never_movie[4], seldom_movie[4], sometimes_movie[4], often_movie[4], very_often_movie[4]]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, scale_12, width, label='1, 2', color='#00283b')
    ax.bar(labels, scale_34, width, bottom=scale_12, label='3, 4', color='#00525d')
    ax.bar(labels, scale_56, width, bottom=np.array(scale_12)+np.array(scale_34), label='5, 6', color='#007c50')
    ax.bar(labels, scale_78, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56), label='7, 8', color='#779d18')
    ax.bar(labels, scale_910, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56)+np.array(scale_78), label='9, 10', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('reading frequency')
    
    first_patch = mpatches.Patch(color='#00283b', label='1, 2')
    second_patch = mpatches.Patch(color='#00525d', label='3, 4')
    third_patch = mpatches.Patch(color='#007c50', label='5, 6')
    forth_patch = mpatches.Patch(color='#779d18', label='7, 8')
    fifth_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[first_patch, second_patch, third_patch, forth_patch, fifth_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/frequency_pleasure_movie_2.png')

    plt.show()


def frequency_relax_stacked_bar_chart(relax_book, relax_movie, data):

    never_book, never_movie, seldom_book, seldom_movie, sometimes_book, sometimes_movie, often_book, often_movie, very_often_book, very_often_movie = get_dispersion_of_data_of_scale_1_to_10(relax_book, relax_movie, data)

    labels = ['never', 'seldom', 'sometimes', 'often', 'very often']

    # BOOK
    scale_12 = [never_book[0], seldom_book[0], sometimes_book[0], often_book[0], very_often_book[0]]
    scale_34 = [never_book[1], seldom_book[1], sometimes_book[1], often_book[1], very_often_book[1]]
    scale_56 = [never_book[2], seldom_book[2], sometimes_book[2], often_book[2], very_often_book[2]]
    scale_78 = [never_book[3], seldom_book[3], sometimes_book[3], often_book[3], very_often_book[3]]
    scale_910 = [never_book[4], seldom_book[4], sometimes_book[4], often_book[4], very_often_book[4]]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, scale_12, width, label='1, 2', color='#00283b')
    ax.bar(labels, scale_34, width, bottom=scale_12, label='3, 4', color='#00525d')
    ax.bar(labels, scale_56, width, bottom=np.array(scale_12)+np.array(scale_34), label='5, 6', color='#007c50')
    ax.bar(labels, scale_78, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56), label='7, 8', color='#779d18')
    ax.bar(labels, scale_910, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56)+np.array(scale_78), label='9, 10', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('reading frequency')
    
    first_patch = mpatches.Patch(color='#00283b', label='1, 2')
    second_patch = mpatches.Patch(color='#00525d', label='3, 4')
    third_patch = mpatches.Patch(color='#007c50', label='5, 6')
    forth_patch = mpatches.Patch(color='#779d18', label='7, 8')
    fifth_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[first_patch, second_patch, third_patch, forth_patch, fifth_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/frequency_relax_book_2.png')

    plt.show()

    # MOVIE
    scale_12 = [never_movie[0], seldom_movie[0], sometimes_movie[0], often_movie[0], very_often_movie[0]]
    scale_34 = [never_movie[1], seldom_movie[1], sometimes_movie[1], often_movie[1], very_often_movie[1]]
    scale_56 = [never_movie[2], seldom_movie[2], sometimes_movie[2], often_movie[2], very_often_movie[2]]
    scale_78 = [never_movie[3], seldom_movie[3], sometimes_movie[3], often_movie[3], very_often_movie[3]]
    scale_910 = [never_movie[4], seldom_movie[4], sometimes_movie[4], often_movie[4], very_often_movie[4]]

    width = 0.7

    fig, ax = plt.subplots()

    ax.bar(labels, scale_12, width, label='1, 2', color='#00283b')
    ax.bar(labels, scale_34, width, bottom=scale_12, label='3, 4', color='#00525d')
    ax.bar(labels, scale_56, width, bottom=np.array(scale_12)+np.array(scale_34), label='5, 6', color='#007c50')
    ax.bar(labels, scale_78, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56), label='7, 8', color='#779d18')
    ax.bar(labels, scale_910, width, bottom=np.array(scale_12)+np.array(scale_34)+np.array(scale_56)+np.array(scale_78), label='9, 10', color='#ffa600')

    ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
    ax.set_ylabel('percentage')
    ax.set_xlabel('reading frequency')
    
    first_patch = mpatches.Patch(color='#00283b', label='1, 2')
    second_patch = mpatches.Patch(color='#00525d', label='3, 4')
    third_patch = mpatches.Patch(color='#007c50', label='5, 6')
    forth_patch = mpatches.Patch(color='#779d18', label='7, 8')
    fifth_patch = mpatches.Patch(color='#ffa600', label='9, 10')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.legend(handles=[first_patch, second_patch, third_patch, forth_patch, fifth_patch], loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

    plt.savefig('diagrams/bar_charts/frequency_relax_movie_2.png')

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

    # create_age_time_bar_chart()
    # create_age_symptoms_bar_chart()

    # create_age_symptoms_stacked_bar_chart()
    # create_age_snacks_stacked_bar_chart()
    # create_age_motivation_stacked_bar_chart()

    # frequency_stress_stacked_bar_chart()

    data = readCSV('csv_files/edited/survey_complete.csv')

    pleasure_book = processDataToString(data, "How much do you like reading on a scale from 1 (not at all) to 10 (very much)? (Punkte von 1 bis 10) ") 
    pleasure_movie = processDataToString(data, "How much do you like watching movies / series on a scale from 1 (not at all) to 10 (very much)? (Punkte von 1 bis 10) ")

    stress_book = processDataToString(data, "How stressed do you feel after you've read a book on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ") 
    stress_movie = processDataToString(data, "How stressed do you feel after you've watched a movie / a series on a scale from 1 (not at all stressed) to 10 (very stressed)? (Punkte von 1 bis 10) ")

    relax_book = processDataToString(data, "How relaxed do you feel after you've read a book on a scale from 1 (not at all relaxed) to 10 (very relaxed)? (Punkte von 1 bis 10) ")
    relax_movie = processDataToString(data, "How relaxed do you feel after you've watched a movie / a series on a scale from 1 (not at all relaxed) to 10 (very relaxed)? (Punkte von 1 bis 10) ")

    frequency_relax_stacked_bar_chart(relax_book, relax_movie, data)


if __name__ == main():
    main()