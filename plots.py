import matplotlib.pyplot as plt
import numpy as np


def read_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        nodes = []
        times = []
        for line in lines:
            data = line.split(', ')
            nodes.append(int(data[0]))
            times.append(float(data[1]))
        return nodes, times


def plot_median_nodes(depth1_alfabeta, depth1_second, depth1_third, depth2_alfabeta, depth2_second, depth2_third,
                      depth3_alfabeta, depth3_second, depth3_third, output_file):
    #nodes1_fs, _ = read_data(depth1_alfabeta)
    nodes2_fs, _ = read_data(depth2_alfabeta)
    nodes3_fs, _ = read_data(depth3_alfabeta)

    #nodes1_sc, _ = read_data(depth1_second)
    nodes2_sc, _ = read_data(depth2_second)
    nodes3_sc, _ = read_data(depth3_second)

    #nodes1_td, _ = read_data(depth1_third)
    nodes2_td, _ = read_data(depth2_third)
    nodes3_td, _ = read_data(depth3_third)

    median_nodes_fs = [np.median(nodes2_fs), np.median(nodes3_fs)]
    median_nodes_sc = [np.median(nodes2_sc), np.median(nodes3_sc)]
    median_nodes_td = [np.median(nodes2_td), np.median(nodes3_td)]

    fig, ax = plt.subplots()
    bar_width = 0.3
    index = np.arange(len(median_nodes_fs))

    ax.bar(index, median_nodes_fs, bar_width, color='blue', alpha=0.6, label='Strategia 1')
    ax.bar(index + bar_width, median_nodes_sc, bar_width, color='orange', alpha=0.6, label='Strategia2')
    ax.bar(index + bar_width*2, median_nodes_td, bar_width, color='green', alpha=0.6, label='Strategia3')

    ax.set_xlabel('Maksymalna głębokość')
    ax.set_ylabel('Węzły')
    ax.set_title('Mediana węzłów w zależności od strategii')
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(['2', '3'])

    ax.legend()

    plt.savefig(output_file + "_nodes.png")
    plt.close()


def plot_median_time(depth1_alfabeta, depth1_second, depth1_third, depth2_alfabeta, depth2_second, depth2_third,
                      depth3_alfabeta, depth3_second, depth3_third, output_file):
    #_, nodes1_fs = read_data(depth1_alfabeta)
    _, nodes2_fs = read_data(depth2_alfabeta)
    _, nodes3_fs = read_data(depth3_alfabeta)

    #_, nodes1_sc = read_data(depth1_second)
    _, nodes2_sc = read_data(depth2_second)
    _, nodes3_sc = read_data(depth3_second)

    #_, nodes1_td = read_data(depth1_third)
    _, nodes2_td = read_data(depth2_third)
    _, nodes3_td = read_data(depth3_third)

    median_nodes_fs = [np.median(nodes2_fs), np.median(nodes3_fs)]
    median_nodes_sc = [np.median(nodes2_sc), np.median(nodes3_sc)]
    median_nodes_td = [np.median(nodes2_td), np.median(nodes3_td)]

    fig, ax = plt.subplots()
    bar_width = 0.3
    index = np.arange(len(median_nodes_fs))

    ax.bar(index, median_nodes_fs, bar_width, color='blue', alpha=0.6, label='Strategia 1')
    ax.bar(index + bar_width, median_nodes_sc, bar_width, color='orange', alpha=0.6, label='Strategia 2')
    ax.bar(index + bar_width*2, median_nodes_td, bar_width, color='green', alpha=0.6, label='Strategia 3')

    ax.set_xlabel('Maksymalna głębokość')
    ax.set_ylabel('Czas (s)')
    ax.set_title('Mediana czasu przeszukiwania w zależności od strategii')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(['2', '3'])

    ax.legend()

    plt.savefig(output_file + "_time.png")
    plt.close()

def read_results(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        wins_1 = sum([1 for line in lines if line.strip() == '2'])
        wins_2 = sum([1 for line in lines if line.strip() == '3'])
        return wins_1, wins_2

def plot_win_ratio(wins_1, wins_2, output_file):
    total_games = wins_1 + wins_2
    win_ratio_1 = wins_1 / total_games
    win_ratio_2 = wins_2 / total_games

    labels = ['Strategia 2', 'Strategia 3']
    sizes = [win_ratio_1, win_ratio_2]
    colors = ['lightblue', 'lightcoral']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Współczynnik zwycięstw strategii')
    plt.axis('equal')

    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    # wins_1, wins_2 = read_results("second_vs_third.txt")
    # plot_win_ratio(wins_1, wins_2, "win_ratio23.png")
    plot_median_nodes("depth1alfabeta.txt", "depth1second.txt", "depth1third.txt", "depth2alfabeta.txt",
                      "depth2second.txt", "depth2third.txt", "depth3alfabeta.txt", "depth3second.txt",
                      "depth3third.txt", "median_strategy2")
    plot_median_time("depth1alfabeta.txt", "depth1second.txt", "depth1third.txt", "depth2alfabeta.txt",
                      "depth2second.txt", "depth2third.txt", "depth3alfabeta.txt", "depth3second.txt",
                      "depth3third.txt", "median_strategy2")

