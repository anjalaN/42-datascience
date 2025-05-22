#!/user/bin/env python3
with open("periodic_table.txt", "r") as file:
    lines = file.readlines()  # Reads all lines into a list

elements = []  # Store parsed elements

for line in lines:
    name, attributes = line.strip().split(" = ")  # Separate element name
    properties = attributes.split(", ")  # Split individual properties

    # Convert properties into a dictionary
    element_dict = {prop.split(":")[0]: prop.split(":")[1] for prop in properties}
    
    # Store each element as a dictionary
    elements.append({"name": name, **element_dict})

print(elements)  # Check parsed data (list of dictionaries)

html_content = """
<html>
<head>
    <title>Periodic Table</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        td { border: 1px solid black; padding: 10px; text-align: center; }
    </style>
</head>
<body>
    <h1>Periodic Table</h1>
    <table>
"""

for element in elements:
    html_content += f"""
    <tr>
        <td style='border: 1px solid black; padding:10px'>
            <h4>{element['name']}</h4>
            <ul>
                <li>No {element['number']}</li>
                <li>{element['small']}</li>
                <li>{element['molar']}</li>
                <li>{element['electron']} electrons</li>
            </ul>
        </td>
    </tr>
    """

html_content += """
    </table>
</body>
</html>
"""

# Save the generated HTML file
with open("periodic_table.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully!")
