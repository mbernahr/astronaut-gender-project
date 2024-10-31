# SPDX-FileCopyrightText: 2024 Marius Bernahrndt
#
# SPDX-License-Identifier: CC-BY-4.0

# Imports
import json
import matplotlib.pyplot as plt
from collections import Counter
import os


# Method, to count genders
def count_gender(data):
    genders = [astronaut["sex_or_genderLabel"] for astronaut in data]
    return Counter(genders)


def main():
    # Read JSON
    with open('../Data/astronauts.json', 'r') as file:
        data = json.load(file)

    # Count genders
    gender_counts = count_gender(data)

    # Data for giagram
    labels = list(gender_counts.keys())
    values = list(gender_counts.values())

    # Barplot
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values)
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.title("Number of Male and Female Astronauts")

    # Check if ordner exists
    os.makedirs('../Results', exist_ok=True)

    # Safe picture
    output_path = '../Results/gender_count.png'
    plt.savefig(output_path)
    print(f"Diagram saved to {output_path}")


if __name__ == "__main__":
    main()
