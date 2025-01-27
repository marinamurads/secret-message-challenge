import requests
from bs4 import BeautifulSoup

# Fetch the data from the public Google Doc
def fetch_data_from_google_doc(url):
    # Get the content from the public Google Doc URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table that contains the x, character, y data
    table = soup.find('table')
    
    # Extract all rows
    rows = table.find_all('tr')
    data = []
    
    # Loop through each row and extract x, character, y values
    for row in rows[1:]:  # Skipping the header row
        cols = row.find_all('td')
        if len(cols) >= 3:
            x = int(cols[0].text.strip())  # x-coordinate
            character = cols[1].text.strip()  # character
            y = int(cols[2].text.strip())  # y-coordinate
            data.append((x, character, y))
    
    return data

# Function to build the grid from the parsed data
def build_grid(data):
    if not data:
        return ""
    
    # Find the maximum x and y values from the data to determine grid size
    max_x = max([x for x, _, _ in data])
    max_y = max([y for _, _, y in data])
    
    # Create an empty grid initialized with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Place characters in the grid at their specified x, y positions
    for x, char, y in data:
        grid[y][x] = char
    
    # Convert the grid into a string for printing
    # Reverse the grid rows to print from top to bottom
    grid_str = "\n".join(["".join(row) for row in reversed(grid)])
    
    # Clean up trailing spaces from each row to avoid unnecessary blank space
    grid_str = "\n".join([row.rstrip() for row in grid_str.splitlines()])
    
    return grid_str

# Main function to fetch data and print the grid
def print_message_from_doc(url):
    data = fetch_data_from_google_doc(url)
    grid = build_grid(data)
    print(grid)

# Example usage (add the URL for file)
url = ''
print_message_from_doc(url)











