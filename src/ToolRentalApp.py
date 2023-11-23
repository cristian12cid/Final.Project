# import tkinter as tk
#
#
# from ToolSelectionWindow import ToolSelectionWindow
#
#
# class ToolRentalApp:
#     def __init__(self):
#         # Initialize the main application window
#         self.root = tk.Tk()
#         self.root.geometry("500x350")
#         self.create_main_ui()# Create the main UI elements
#
#     def create_main_ui(self):
#         # Create the main UI elements: login interface
#         frame = tk.Frame(master=self.root)
#         frame.pack(pady=20, padx=60, fill="both", expand=True)
#
#         label = tk.Label(master=frame, text="Login Systems", font=("Roboto", 24))
#         label.pack(pady=12, padx=10)
#
#         # Username and password entry fields
#         self.entry1 = tk.Entry(master=frame)
#         self.entry1.insert(0, "Your Username")
#         self.entry1.pack(pady=12, padx=10)
#
#         self.entry2 = tk.Entry(master=frame, show="*")
#         self.entry2.insert(0, "Your Password")
#         self.entry2.pack(pady=12, padx=10)
#
#         # Login button triggers the 'rent_tools' method
#         button = tk.Button(master=frame, text="Login", command=self.rent_tools)
#         button.pack(pady=12, padx=10)
#
#     # Method to handle tool rental upon login
#     def rent_tools(self):
#         username = self.entry1.get()
#         password = self.entry2.get()
#
#         # Check if credentials are valid
#         if username != "Cris1" or password != "12345":
#
#             # Show login error if credentials are incorrect
#             self.display_login_error()
#
#         else:
#
#             # Hide the main window
#             self.root.withdraw()
#             tool_selection_window = ToolSelectionWindow(self.root)
#
#             # Open tool selection window if login is successful
#             tool_selection_window.show()
#
#     # Method to display login error message
#     def display_login_error(self):
#         error_window = tk.Toplevel(self.root)
#         error_window.title("Access Denied")
#
#         error_label = tk.Label(error_window, text="Invalid username or password. Account not created.",
#                                font=("Roboto", 14))
#         error_label.pack(padx=20, pady=20)
#
#         ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
#         ok_button.pack(pady=10)
