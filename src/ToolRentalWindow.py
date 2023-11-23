# import json
# import tkinter as tk
# from io import BytesIO
#
#
# class ToolRentalWindow:
#
#     # Initialize the tool rental window
#     def __init__(self, selected_tool, selected_brand, rental_duration, exchange_currency):
#         self.selected_tool = selected_tool
#         self.selected_brand = selected_brand
#         self.rental_duration = rental_duration
#         self.exchange_currency = exchange_currency
#         self.tool_rental_window = tk.Toplevel()
#         self.tool_rental_window.geometry("600x650")
#         self.tool_rental_window.title("Tool Rental")
#         self.open_tool_rental()
#
#     def open_tool_rental(self):
#
#         # Method to open the tool rental window and display tool information
#         # Retrieves data from JSON file based on selected tool and brand
#         with open('data.json') as json_file:
#             data = json.load(json_file)
#             selected_tool_data = data.get(self.selected_tool, [])
#             if selected_tool_data:
#                 brand_details = selected_tool_data[0].get(self.selected_brand)
#                 if brand_details:
#
#                     image_url = brand_details.get('image')
#                     description = brand_details.get('description')
#                     price_per_minute = brand_details.get('price')
#                     self.display_tool_information(description, price_per_minute, image_url)
#
#     def display_tool_information(self, description, price_per_minute, image_url):
#         # Method to display tool information in the rental window
#         # Displays tool description, price, duration, converted price, and image
#         description_text = tk.Text(self.tool_rental_window, wrap=tk.WORD, width=40, height=10)
#         description_text.pack(pady=12, padx=10)
#         description_text.insert(tk.END, description)
#         description_text.configure(state='disabled')
#
#         price_label = tk.Label(self.tool_rental_window, text=f"Price per minute: ${price_per_minute}")
#         price_label.pack(pady=12, padx=10)
#
#         duration_label = tk.Label(self.tool_rental_window, text=f"Rental Duration: {self.rental_duration} minutes")
#         duration_label.pack(pady=12, padx=10)
#
#         converted_price = price_per_minute * self.rental_duration
#         converted_price_label = tk.Label(self.tool_rental_window, text=f"Total Price: {converted_price} {self.exchange_currency}")
#         converted_price_label.pack(pady=12, padx=10)
#
#         response = requests.get(image_url)
#         img_data = response.content if response.status_code == 200 else None
#
#         if img_data:
#             img = Image.open(BytesIO(img_data))
#             img = img.resize((200, 200))
#             img_tk = ImageTk.PhotoImage(img)
#             self.image_label = tk.Label(self.tool_rental_window, image=img_tk)
#             self.image_label.image = img_tk
#             self.image_label.pack(pady=12, padx=10)
#
#         rent_button = tk.Button(self.tool_rental_window, text="Rent Now!", command=self.log_rental)
#         rent_button.pack(pady=12, padx=10)
#
#     def log_rental(self):
#         # Method to log rental information when 'Rent Now!' button is clicked
#         selected_tool = self.selected_tool
#         selected_brand = self.selected_brand
#         rental_duration = self.rental_duration
#
#         # Prints selected tool, brand, and rental duration
#         print("Selected Tool:", selected_tool)
#         print("Selected Brand:", selected_brand)
#         print("Rental Duration:", rental_duration, "minutes")
#         print(" ")
