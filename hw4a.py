from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def probcalc(height_distribution, testx):
    """Calculates the probability that value is equal to testx, and that a value is equal to or below ttestx
    :param height_distribution: height_distribution = stats.norm(loc=mean, scale=standard_deviation)
    :param testx: x value to test
    :return: (probability that value is equal to testx, probability that a value is equal to or below ttestx)
    """
    probabilitytx = height_distribution.pdf(testx)  # Find probability that value is equal to testx
    probabilitytx.round(4)  # round for cleanliness

    belowtx = height_distribution.cdf(testx)  # Find probability that a value is equal to or below ttestx
    belowtx.round(4)  # round for cleanliness

    return probabilitytx, belowtx


def plotter(args, prob, xaxisvalues, GT=True):
    """ Creates graphs that visualize the probability of getting a value < or > than the test x value.
    :param args: (xaxisvalues, probabilities, testx, min_height, max_height, mean, standard_deviation)
    :param prob: value at which to start the shading
    :param xaxisvalues: xaxis values
    :param GT: boolean to tell whether to shade above or below prob
    :return: graphs with regions shaded and the prob noted as the label on the graph
    """
    # Unpacking args
    values = args[0]
    probabilities = args[1]
    testx = args[2]
    min_height = args[3]
    max_height = args[4]
    mean = args[5]
    stddev = args[6]

    fig, (ax1, ax2) = plt.subplots(2, sharex=True)

    # plot density curve
    ax1.plot(values, probabilities, color='k', linewidth=2, label='Probability')
    # Shade the region where height <= 44 inches
    if GT is True:  # check if to shade greater than or less than x
        shaded_region = (values >= testx)
    else:  # check if to shade greater than or less than x
        shaded_region = (values <= testx)
    ax1.fill_between(values, probabilities, where=shaded_region, facecolor='red', alpha=0.2)  # shade area

    # Remove the dead space
    axes = plt.gca()
    axes.set_xlim([min_height, max_height])
    ymin, ymax = axes.get_ylim()
    axes.set_ylim([0, ymax])

    if GT is True:  # check if to use < or >
        # states problem and cdf solution probability
        ax1.set_title(f"P(x>{testx}|N({mean},{stddev}))= {round(1-prob, 3)}", pad=20, fontsize=10, color='r')  # labels
    else:   # check if to use < or >
        # states problem and cdf solution probability
        ax1.set_title(f"P(x<{testx}|N({mean},{stddev}))= {prob}", pad=20, fontsize=10, color='r')

    # Labels for subplot1
    if GT is True:  # adding arrows to point to shaded area
        ax1.arrow(max_height-(max_height-min_height)/150, 1/(20*stddev), -(max_height-min_height)/4.8, -1/(25*stddev))
        ax1.text(max_height-(max_height-min_height)/5.3, 1/(40*stddev), f"P(x>{testx}|N({mean},{stddev}))= {round(1-prob, 3)}", fontsize=5, color='r', rotation=10)
    else:  # adding arrows to point to shaded area
        ax1.arrow((min_height+(max_height-min_height)/150), 1/(20*stddev), (max_height-min_height)/4.8, -1/(25*stddev))
        ax1.text((min_height+(max_height-min_height)/30), 1/(40*stddev), f"P(x>{testx}|N({mean},{stddev}))= {round(1-prob, 3)}", fontsize=5, color='r', rotation=-10)

    # ax1.set_ylabel("f(x)= (1/(σ*sqrt(2π))exp((((x-μ)/σ)^2)/2)", fontsize=6, color='k')  # setting label for subplot 1
    ax1.set_ylabel("Normal Distribution Formula", fontsize=6, color='k')  # setting label for subplot 1
    cdf = stats.norm.cdf(xaxisvalues, mean, stddev)  # getting cdf of values
    ax2.plot(xaxisvalues, cdf, label='CDF', color='k')  # Plot the CDF against x

    # plot lines as guidelines for easier visualization
    ax2.plot([testx, testx], [0, prob], linewidth=0.5, linestyle='--', color='red')
    ax2.plot([min_height, testx], [prob, prob], label=f"CDF Prob = {prob} @ {testx}", linewidth=0.5, linestyle='--', color='red')
    ax2.plot(testx, prob, '-ro') # point to mark prob
    ax2.legend()  # show legend

    # labels for subplot2
    ax2.set_ylabel("CDF Formula", fontsize=8, color='k') # need to add cdf formula as label

    plt.show()


def main():

    # PROBLEM a1
    # defining variables for problem a1
    mean = 0
    standard_deviation = 1
    testx = 1  # x value to test
    isGT = False  # greater than = True, Less than = False
    min_height = mean-standard_deviation * 4  # min x value on graph
    max_height = mean + standard_deviation * 4  # max x value on graph
    xaxisvalues = np.linspace(min_height, max_height, num=1000)  # get xaxis values for graphing
    height_distribution = stats.norm(loc=mean, scale=standard_deviation)  # getting values for distribution

    # Calculate probabilites using scipy.stats.norm.pdf() as height_distribution.pdf()
    probabilities = height_distribution.pdf(x=xaxisvalues)
    # packing values into a tuple for easier passing
    args = (xaxisvalues, probabilities, testx, min_height, max_height, mean, standard_deviation)

    prob = round(probcalc(height_distribution, testx)[0], 3)  # prob that a value = testx
    cdfprob = round(probcalc(height_distribution, testx)[1],3)  # prob that a value <= testx

    plotter(args, cdfprob, xaxisvalues, GT=isGT)  # call function for problem a1 graph 1


    # PROBLEM a1
    # defining variables for problem a1
    mean = 175
    standard_deviation = 3
    testx = mean + 2 * standard_deviation  # x value to test
    isGT = True  # greater than = True, Less than = False
    min_height = mean-standard_deviation * 4  # min x value on graph
    max_height = mean + standard_deviation * 4  # max x value on graph

    xaxisvalues = np.linspace(min_height, max_height, num=1000)  # get xaxis values for graphing
    height_distribution = stats.norm(loc=mean, scale=standard_deviation)  # getting values for distribution

    # Calculate probabilites using scipy.stats.norm.pdf() as height_distribution.pdf()
    probabilities = height_distribution.pdf(x=xaxisvalues)
    # packing values into a tuple for easier passing
    args = (xaxisvalues, probabilities, testx, min_height, max_height, mean, standard_deviation)

    prob = round(probcalc(height_distribution, testx)[0], 3)  # prob that a value = testx
    cdfprob = round(probcalc(height_distribution, testx)[1],3)  # prob that a value <= testx

    plotter(args, cdfprob, xaxisvalues, GT=isGT)  # call function for problem a1 graph 1


if __name__ == "__main__":
    main()