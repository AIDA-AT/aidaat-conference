import click
import pandas as pd
import numpy as np
from simplification.cutil import simplify_coords
import matplotlib.pyplot as plt


def simplify_coordinator(coord_curve, epsilon=0.00001):
    """
    Ramer–Douglas–Peucker simplification

    Args:
        coord_curve (list[list[float, float]]): a list of lat, lon coordinates
        epsilon (float):
    Returns:
        list[list[float, float]]
    """
    coord_curve = np.asarray(coord_curve, order='C')
    return simplify_coords(coord_curve, epsilon)


def main(input_path):
    """

    Args:
        input_path (str): input path to csv flight data

    Returns:

    """

    raw_df = pd.read_csv(input_path, parse_dates=['Time'])

    # query data by FID
    flight_id = 'FID_000'
    df = raw_df[raw_df['FID'] == flight_id]

    # sort data by Time
    df = df.sort_values(by='Time', ascending=True)
    print(df.head())

    # extract latitude and longitude
    coords = df.as_matrix(columns=['Latitude', 'Longitude'])

    # simplify trajectory
    sim_coords = simplify_coordinator(coord_curve=coords)
    print("Total points before simplification %s" % len(coords))
    print("Total points after simplification %s" % len(sim_coords))

    plt.figure(figsize=(10, 10))

    p1 = plt.scatter(x=coords[:, 1], y=coords[:, 0])
    p2 = plt.scatter(x=sim_coords[:, 1], y=sim_coords[:, 0])
    plt.legend((p1, p2),
               ('Original data-points', 'Simplified data-points'),
               scatterpoints=1,
               loc='higher right',
               ncol=2,
               fontsize=11)
    plt.savefig("ori_vs_sim.png")
    plt.show()


@click.command()
@click.option(
    '--input_path',
    type=str,
    required=True,
    help='Full path to the trajectory file in CSV format')
def cli(input_path):
    main(input_path=input_path)


if __name__ == '__main__':
    cli()
