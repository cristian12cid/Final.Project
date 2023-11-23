# import tkinter as tk
#
# from ToolRentalWindow import ToolRentalWindow
#
#
# class ToolSelectionWindow:
#     def __init__(self, root):
#         # Initialize the tool selection window
#         self.tool_selection_window = tk.Toplevel(root)
#         self.tool_selection_window.geometry("350x400")
#         self.tool_selection_window.title("Tool Selection")
#
#         # Create the tool selection UI elements
#         self.create_tool_selection_ui()
#
#     def show(self):
#         self.tool_selection_window.mainloop()
#
#     def create_tool_selection_ui(self):
#         # Create the UI elements for tool selection:
#         # dropdowns, labels, buttons, and entry fields for tool selection and rental
#         self.tool_list = [
#             "Battery drill",
#             "Screwdriver",
#             "cutting machine",
#         ]
#         self.tool_variable = tk.StringVar(self.tool_selection_window, value=self.tool_list[0])
#         tool_label = tk.Label(self.tool_selection_window, text="Select a Tool:")
#         tool_label.grid(row=0, column=0, pady=12, padx=10)
#         tool_option_menu = tk.OptionMenu(self.tool_selection_window, self.tool_variable, *self.tool_list)
#         tool_option_menu.grid(row=0, column=1, pady=12, padx=10)
#
#         self.toolbrand_list = [
#             "Dewalt",
#             "Festool",
#             "Makita",
#         ]
#         self.toolbrand_variable = tk.StringVar(self.tool_selection_window, value=self.toolbrand_list[0])
#         toolbrand_label = tk.Label(self.tool_selection_window, text="Select Desired Tool Brand:")
#         toolbrand_label.grid(row=1, column=0, pady=12, padx=10)
#         toolbrand_option_menu = tk.OptionMenu(self.tool_selection_window, self.toolbrand_variable, *self.toolbrand_list)
#         toolbrand_option_menu.grid(row=1, column=1, pady=12, padx=10)
#
#         timer_label = tk.Label(self.tool_selection_window, text="Rental Duration (in minutes):")
#         timer_label.grid(row=2, column=0, pady=12, padx=10)
#         self.timer_entry = tk.Entry(self.tool_selection_window)
#         self.timer_entry.insert(0, "30")
#         self.timer_entry.grid(row=2, column=1, pady=12, padx=10)
#
#         currency_label = tk.Label(self.tool_selection_window, text="Select Currency:")
#         currency_label.grid(row=3, column=0, pady=12, padx=10)
#         self.currency_list = [
#             "USD",
#             "EUR",
#             "GBP",
#         ]
#         self.currency_variable = tk.StringVar(self.tool_selection_window, value=self.currency_list[0])
#         currency_option_menu = tk.OptionMenu(self.tool_selection_window, self.currency_variable, *self.currency_list)
#         currency_option_menu.grid(row=3, column=1, pady=12, padx=10)
#
#         rent_button = tk.Button(self.tool_selection_window, text="Rent", command=self.rent_clicked)
#         rent_button.grid(row=4, column=0, columnspan=2, pady=12, padx=10)
#
#         close_button = tk.Button(self.tool_selection_window, text="Close", command=self.close_tool_selection_window)
#         close_button.grid(row=5, column=0, columnspan=2, pady=12, padx=10)
#     def rent_clicked(self):
#         # Method triggered when 'Rent' button is clicked
#         # Retrieves selected tool, brand, duration, and currency
#         selected_tool = self.tool_variable.get()
#         selected_brand = self.toolbrand_variable.get()
#         rental_duration = int(self.timer_entry.get())
#         exchange_currency = self.currency_variable.get()
#         ToolRentalWindow(selected_tool, selected_brand, rental_duration, exchange_currency)
#
#     # Method to close the tool selection window and restore the main window
#     def close_tool_selection_window(self):
#         self.tool_selection_window.destroy()
#         self.root.deiconify()
