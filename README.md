Tool Rental Application
This Python-based tool rental application provides a user-friendly interface for browsing and renting various tools from different categories and brands. The application leverages Tkinter for the graphical interface and seamlessly integrates with a structured JSON file containing detailed tool information.


Features
User Authentication
Login Interface: Users can log in using predefined credentials to access the tool selection functionality.
Tool Selection and Rental
Category and Brand Selection: Users can select tool categories and brands, specify rental duration, and choose the desired payment currency.
Tool Information Display: Detailed tool information, including descriptions, pricing, and images, is presented for user review before confirming a tool rental.
Rent Tool: Users can confirm and complete the tool rental process after reviewing the details.
JSON Data Integration
Structured Data Handling: Tool information is retrieved from a structured JSON file, categorizing tools and differentiating them by brand.
File-Based Data Storage: Information such as images, descriptions, and pricing for each tool is stored in a JSON file, ensuring easy maintenance and scalability.


Installation
Clone the repository:
git clone https://github.com/your-username/tool-rental-app.git

Navigate to the project directory:
cd tool-rental-app

Install Poetry (if not already installed):
Refer to Poetry's official installation guide for platform-specific instructions.
Install project dependencies:
poetry install

Usage
Activate the Poetry virtual environment:
poetry shell

Run the application:
python tool_rental_app.py
Login: Use the login interface to log in with predefined credentials.
Username: Cris1
Password:12345

Tool Selection: Choose a tool category, brand, specify the rental duration, and select the currency for payment.

Tool Information: Review the detailed tool information displayed, including description, price per minute, and an image.

Rent Tool: Confirm the tool rental after reviewing the details.


JSON File Structure
The application utilizes a structured JSON file to store tool information. The file format is as follows:

json

{
    "cutting machine": [
        {
            "Makita": {
                "image": "URL",
                "description": "Description",
                "price": 1
            },
            ...
        }
    ],
    ...
}
The JSON file organizes tools into categories such as "cutting machine," "Screwdriver," and "Battery drill," each containing details for different brands like "Makita," "Festool," and "Dewalt." Information includes image URLs, descriptions, and prices for each tool under corresponding categories and brands.

Contributing
Contributions are welcomed! To contribute to this project:

Fork the repository.
Create a new branch (git checkout -b feature/add-new-feature).
Make modifications and commit changes (git commit -am 'Add new feature').
Push the branch to your forked repository (git push origin feature/add-new-feature).
Create a pull request.

