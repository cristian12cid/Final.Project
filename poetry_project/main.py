import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests
import json

# ToolRentalApp class handles the main tool rental application
class ToolRentalApp:
    def __init__(self):
        # Initialize the main application window
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.create_main_ui()# Create the main UI elements

    def create_main_ui(self):
        # Create the main UI elements: login interface
        frame = tk.Frame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = tk.Label(master=frame, text="Login Systems", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        # Username and password entry fields
        self.entry1 = tk.Entry(master=frame)
        self.entry1.insert(0, "Your Username")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = tk.Entry(master=frame, show="*")
        self.entry2.insert(0, "Your Password")
        self.entry2.pack(pady=12, padx=10)

        # Login button triggers the 'rent_tools' method
        button = tk.Button(master=frame, text="Login", command=self.rent_tools)
        button.pack(pady=12, padx=10)

    # Method to handle tool rental upon login
    def rent_tools(self):
        username = self.entry1.get()
        password = self.entry2.get()

        # Check if credentials are valid
        if username != "Cris1" or password != "12345":

            # Show login error if credentials are incorrect
            self.display_login_error()

        else:

            # Hide the main window
            self.root.withdraw()
            tool_selection_window = ToolSelectionWindow(self.root)

            # Open tool selection window if login is successful
            tool_selection_window.show()

    # Method to display login error message
    def display_login_error(self):
        error_window = tk.Toplevel(self.root)
        error_window.title("Access Denied")

        error_label = tk.Label(error_window, text="Invalid username or password. Account not created.",
                               font=("Roboto", 14))
        error_label.pack(padx=20, pady=20)

        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack(pady=10)

# ToolSelectionWindow class manages the tool selection window
class ToolSelectionWindow:
    def __init__(self, root):
        # Initialize the tool selection window
        self.tool_selection_window = tk.Toplevel(root)
        self.tool_selection_window.geometry("350x400")
        self.tool_selection_window.title("Tool Selection")

        # Create the tool selection UI elements
        self.create_tool_selection_ui()

    def show(self):
        self.tool_selection_window.mainloop()

    def create_tool_selection_ui(self):
        # Create the UI elements for tool selection:
        # dropdowns, labels, buttons, and entry fields for tool selection and rental
        self.tool_list = [
            "Battery drill",
            "Screwdriver",
            "cutting machine",
        ]
        self.tool_variable = tk.StringVar(self.tool_selection_window, value=self.tool_list[0])
        tool_label = tk.Label(self.tool_selection_window, text="Select a Tool:")
        tool_label.grid(row=0, column=0, pady=12, padx=10)
        tool_option_menu = tk.OptionMenu(self.tool_selection_window, self.tool_variable, *self.tool_list)
        tool_option_menu.grid(row=0, column=1, pady=12, padx=10)

        self.toolbrand_list = [
            "Dewalt",
            "Festool",
            "Makita",
        ]
        self.toolbrand_variable = tk.StringVar(self.tool_selection_window, value=self.toolbrand_list[0])
        toolbrand_label = tk.Label(self.tool_selection_window, text="Select Desired Tool Brand:")
        toolbrand_label.grid(row=1, column=0, pady=12, padx=10)
        toolbrand_option_menu = tk.OptionMenu(self.tool_selection_window, self.toolbrand_variable, *self.toolbrand_list)
        toolbrand_option_menu.grid(row=1, column=1, pady=12, padx=10)

        timer_label = tk.Label(self.tool_selection_window, text="Rental Duration (in minutes):")
        timer_label.grid(row=2, column=0, pady=12, padx=10)
        self.timer_entry = tk.Entry(self.tool_selection_window)
        self.timer_entry.insert(0, "30")
        self.timer_entry.grid(row=2, column=1, pady=12, padx=10)

        currency_label = tk.Label(self.tool_selection_window, text="Select Currency:")
        currency_label.grid(row=3, column=0, pady=12, padx=10)
        self.currency_list = [
            "USD",
            "EUR",
            "GBP",
        ]
        self.currency_variable = tk.StringVar(self.tool_selection_window, value=self.currency_list[0])
        currency_option_menu = tk.OptionMenu(self.tool_selection_window, self.currency_variable, *self.currency_list)
        currency_option_menu.grid(row=3, column=1, pady=12, padx=10)

        rent_button = tk.Button(self.tool_selection_window, text="Rent", command=self.rent_clicked)
        rent_button.grid(row=4, column=0, columnspan=2, pady=12, padx=10)

        close_button = tk.Button(self.tool_selection_window, text="Close", command=self.close_tool_selection_window)
        close_button.grid(row=5, column=0, columnspan=2, pady=12, padx=10)
    def rent_clicked(self):
        # Method triggered when 'Rent' button is clicked
        # Retrieves selected tool, brand, duration, and currency
        selected_tool = self.tool_variable.get()
        selected_brand = self.toolbrand_variable.get()
        rental_duration = int(self.timer_entry.get())
        exchange_currency = self.currency_variable.get()
        ToolRentalWindow(selected_tool, selected_brand, rental_duration, exchange_currency)

    # Method to close the tool selection window and restore the main window
    def close_tool_selection_window(self):
        self.tool_selection_window.destroy()
        self.root.deiconify()

# ToolRentalWindow class manages the tool rental window
class ToolRentalWindow:

    # Initialize the tool rental window
    def __init__(self, selected_tool, selected_brand, rental_duration, exchange_currency):
        self.selected_tool = selected_tool
        self.selected_brand = selected_brand
        self.rental_duration = rental_duration
        self.exchange_currency = exchange_currency
        self.tool_rental_window = tk.Toplevel()
        self.tool_rental_window.geometry("600x650")
        self.tool_rental_window.title("Tool Rental")
        self.open_tool_rental()

    def open_tool_rental(self):

        # Method to open the tool rental window and display tool information
        # Retrieves data from JSON file based on selected tool and brand
        with open('toolsdata.json') as json_file:
            data = json.load(json_file)
            selected_tool_data = data.get(self.selected_tool, [])
            if selected_tool_data:
                brand_details = selected_tool_data[0].get(self.selected_brand)
                if brand_details:

                    image_url = brand_details.get('image')
                    description = brand_details.get('description')
                    price_per_minute = brand_details.get('price')
                    self.display_tool_information(description, price_per_minute, image_url)

    def display_tool_information(self, description, price_per_minute, image_url):
        # Method to display tool information in the rental window
        # Displays tool description, price, duration, converted price, and image
        description_text = tk.Text(self.tool_rental_window, wrap=tk.WORD, width=40, height=10)
        description_text.pack(pady=12, padx=10)
        description_text.insert(tk.END, description)
        description_text.configure(state='disabled')

        price_label = tk.Label(self.tool_rental_window, text=f"Price per minute: ${price_per_minute}")
        price_label.pack(pady=12, padx=10)

        duration_label = tk.Label(self.tool_rental_window, text=f"Rental Duration: {self.rental_duration} minutes")
        duration_label.pack(pady=12, padx=10)

        converted_price = price_per_minute * self.rental_duration
        converted_price_label = tk.Label(self.tool_rental_window, text=f"Total Price: {converted_price} {self.exchange_currency}")
        converted_price_label.pack(pady=12, padx=10)

        response = requests.get(image_url)
        img_data = response.content if response.status_code == 200 else None

        if img_data:
            img = Image.open(BytesIO(img_data))
            img = img.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label = tk.Label(self.tool_rental_window, image=img_tk)
            self.image_label.image = img_tk
            self.image_label.pack(pady=12, padx=10)

        rent_button = tk.Button(self.tool_rental_window, text="Rent Now!", command=self.log_rental)
        rent_button.pack(pady=12, padx=10)

    def log_rental(self):
        # Method to log rental information when 'Rent Now!' button is clicked
        selected_tool = self.selected_tool
        selected_brand = self.selected_brand
        rental_duration = self.rental_duration

        # Prints selected tool, brand, and rental duration
        print("Selected Tool:", selected_tool)
        print("Selected Brand:", selected_brand)
        print("Rental Duration:", rental_duration, "minutes")
        print(" ")

# Entry point to the application
if __name__ == "__main__":
    app = ToolRentalApp()
    app.root.mainloop()
