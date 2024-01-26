# OpenSpace Organizer

Welcome to the OpenSpace Organizer! This Python program is designed to facilitate the random reassignment of colleagues to seats in an open office space with multiple tables.

## Features

- Colleagues are randomly assigned to seats across multiple tables.
- Easily adjust the number of tables and seats per table according to your office space configuration.
- Load colleague names from an text file to populate the workspace.

## Project Structure

The project is organized as follows:

- `main.py`: The main script to launch the OpenSpace Organizer.
- `src/`: Contains source code files.
  - `utils.py`: Utility functions.
  - `table.py`: Defines the `Table` and `Seat` classes.
  - `openspace.py`: Defines the `OpenSpace` class.
- `colleagues.xlsx`: Excel file containing colleague names.

## Getting Started

1. Clone this repository:

   git clone git@github.com:sahar-mahmoudi/openspace-organizer.git