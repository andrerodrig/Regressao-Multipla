import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm

def save_plot(figure, path):
    fig = figure.get_figure()
    fig.savefig(path)


def regression_plot(data, x_vet, y_vet, Y_estimated):
    df_data1 = data
    
    plt.figure(figsize=(16,8))
    sns.set()
    plot_data1 = sns.scatterplot(
        x=x_vet,
        y=y_vet,
        data=df_data1
    )
    plt.plot(x_vet, Y_estimated, color="red")
    plt.show()
    return plot_data1
    

def regression_plot3d(x, y, z, Z_estimated):
    fig = plt.figure(figsize=(16,8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Plotting the surface
    ax.plot_trisurf(x, y, Z_estimated, alpha=0.7, cmap=cm.coolwarm)

    plt.show()
    return ax