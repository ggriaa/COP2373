# File Name: MariaGalante_ProgrammingExercise_13.py
# Name: Maria Galante
# Date: 2026-04-21

"""
Programming Exercise 13

This program creates a SQLite database named population_MG.db.
It stores population data for 10 Florida cities beginning in 2025.
The program simulates growth or decline for the next 20 years
and allows the user to choose a city to display a graph.
"""

import random
import sqlite3
import matplotlib.pyplot as plt


# Store constant values.
DB_NAME = "population_MG.db"
START_YEAR = 2025
END_YEAR = 2045


def create_database():
    """
    Create the database and population table.

    Parameters:
        None

    Variables:
        connection (object): Database connection object.
        cursor (object): Used to execute SQL commands.

    Steps:
        1. Connect to database.
        2. Create population table.
        3. Save changes.
        4. Close connection.

    Return:
        None
    """

    # Connect to database.
    connection = sqlite3.connect(DB_NAME)

    # Create cursor object.
    cursor = connection.cursor()

    # Create table if it does not exist.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # Save changes.
    connection.commit()

    # Close connection.
    connection.close()


def insert_population_data():
    """
    Insert 2025 population data and simulate 20 years.

    Parameters:
        None

    Variables:
        connection (object): Database connection object.
        cursor (object): Used to execute SQL commands.
        cities (dictionary): Florida cities and populations.
        city (string): Current city name.
        population (integer): Starting population.
        current_population (integer): Updated value.
        growth_rate (float): Random yearly rate.
        year (integer): Current year.

    Steps:
        1. Connect to database.
        2. Delete old records.
        3. Insert 2025 populations.
        4. Simulate years 2026-2045.
        5. Save changes.
        6. Close connection.

    Return:
        None
    """

    # Connect to database.
    connection = sqlite3.connect(DB_NAME)

    # Create cursor object.
    cursor = connection.cursor()

    # Remove old data.
    cursor.execute("DELETE FROM population")

    # Store city names and starting populations.
    cities = {
        "Tampa": 420000,
        "Orlando": 330000,
        "Miami": 470000,
        "Jacksonville": 990000,
        "St Petersburg": 270000,
        "Hialeah": 220000,
        "Tallahassee": 205000,
        "Fort Lauderdale": 185000,
        "Cape Coral": 245000,
        "Gainesville": 150000
    }

    # Process each city.
    for city, population in cities.items():

        # Insert 2025 population.
        cursor.execute(
            "INSERT INTO population VALUES (?, ?, ?)",
            (city, START_YEAR, population)
        )

        # Store current population.
        current_population = population

        # Simulate next 20 years.
        for year in range(START_YEAR + 1, END_YEAR + 1):

            # Generate growth or decline rate.
            growth_rate = random.uniform(-0.02, 0.04)

            # Update population.
            current_population = int(
                current_population * (1 + growth_rate)
            )

            # Insert yearly population.
            cursor.execute(
                "INSERT INTO population VALUES (?, ?, ?)",
                (city, year, current_population)
            )

    # Save changes.
    connection.commit()

    # Close connection.
    connection.close()


def show_population_graph():
    """
    Ask user for a city and graph population data.

    Parameters:
        None

    Variables:
        connection (object): Database connection object.
        cursor (object): Used to execute SQL commands.
        city_list (list): Stores city names.
        choice (integer): User menu choice.
        selected_city (string): Chosen city.
        records (list): Query results.
        years (list): X-axis values.
        populations (list): Y-axis values.

    Steps:
        1. Show city menu.
        2. Ask for user choice.
        3. Retrieve city data.
        4. Build graph lists.
        5. Display chart.

    Return:
        None
    """

    # Connect to database.
    connection = sqlite3.connect(DB_NAME)

    # Create cursor object.
    cursor = connection.cursor()

    # Store city options.
    city_list = [
        "Tampa",
        "Orlando",
        "Miami",
        "Jacksonville",
        "St Petersburg",
        "Hialeah",
        "Tallahassee",
        "Fort Lauderdale",
        "Cape Coral",
        "Gainesville"
    ]

    # Display menu.
    print("Choose a Florida city:\n")

    for index, city in enumerate(city_list, start=1):
        print(index, "-", city)

    # Get user selection.
    choice = int(input("\nEnter option number: "))

    # Determine selected city.
    selected_city = city_list[choice - 1]

    # Retrieve city data.
    cursor.execute("""
        SELECT year, population
        FROM population
        WHERE city = ?
        ORDER BY year
    """, (selected_city,))

    records = cursor.fetchall()

    # Create lists for graph data.
    years = []
    populations = []

    # Separate values into lists.
    for row in records:
        years.append(row[0])
        populations.append(row[1])

    # Create graph.
    plt.plot(years, populations, marker="o")
    plt.title("Population Growth for " + selected_city)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()

    # Close connection.
    connection.close()


def main():
    """
    Run the full program.

    Parameters:
        None

    Steps:
        1. Create database.
        2. Insert population data.
        3. Show graph menu.

    Return:
        None
    """

    create_database()
    insert_population_data()
    show_population_graph()


if __name__ == "__main__":
    main()