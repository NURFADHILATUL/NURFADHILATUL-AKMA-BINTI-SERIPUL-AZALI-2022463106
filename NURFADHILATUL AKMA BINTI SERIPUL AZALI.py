import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cinema_booking"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    Name = user_entry.get()
    PhoneNumber = mobile_phone_entry.get()
    Age = uage_entry.get()
    Movie = movie_var.get()
    packs = int(packs_entry.get())

    # Movie prices
    movie_prices = {
        "MIGRATION": 15,  # Replace with actual prices for each movie
        "WISH": 16,
        "WAR ON TERROR": 17,
        "NIGHT HAS COMES": 25,
    }

    # Calculate the total price based on the selected movie price and packs
    if Movie in movie_prices:
        movie_price = movie_prices[Movie]
        total_price = movie_price * packs

        # Inserting data into the database
        sql = "INSERT INTO customer_booking (Name, Phone_Number, Age, Movie, Packs, Total_Price) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Name, PhoneNumber, Age, Movie, packs, total_price)
        mycursor.execute(sql, val)
        mydb.commit()

        # Displaying the output
        output_label.config(text=f"Name:\n{Name}, Phone Number:\n{PhoneNumber}, Age:\n{Age}, Selected Movie:\n{Movie}, Packs:\n{packs}, Total Price:\n RM{total_price}")

root = tk.Tk()
root.title("ZQ CINEMA")
root.geometry("1000x1000")
root.configure(bg="cyan")

# Page Title
label = tk.Label(root, text='~~~ WELCOME TO ZQ CINEMA 3< ~~~', font=("Times New Roman", 28, "bold", ))
label.configure(bg="cyan")
label.pack(padx=10, pady=14)

# Movie List by using textbox
movie_text = tk.Text(root, height=10, width=40)
movie_text.pack(ipadx=20, ipady=10)

# The defined list by using moviebox
movie_text.insert(tk.END, "Movies & Prices:\n\n")
movie_text.insert(tk.END, "Movie 1: MIGRATION, RM15\n\n")
movie_text.insert(tk.END, "Movie 2: WISH, RM16\n\n")
movie_text.insert(tk.END, "Movie 3: WAR ON TERROR, RM17\n\n")
movie_text.insert(tk.END, "Movie 4: NIGHT HAS COMES , RM25\n")
movie_text.configure(bg="deep sky blue", fg="black", font=("Times New Roman", 14, "bold",))
movie_text.configure(state='disabled')


frame = tk.Frame(root, height=50, width=50)
frame.pack(padx=20, pady=20)

# Saving user info
insert_info_frame = tk.LabelFrame(frame, text="Insert Your Information\n\n")
insert_info_frame.grid(row=0, column=0, sticky="News", ipadx=28, ipady=28)
insert_info_frame.configure(bg="deep sky blue", fg="dark blue", font=("Arial", 20, "bold"))
 

# User Entry. Label and user can insert data thru entry
user_label = tk.Label(insert_info_frame, text="Name :\n")
user_label.grid(row=0, column=0)
user_label.configure(bg="deep sky blue",  fg="purple", font=("Arial", 12, "bold"))
user_entry = tk.Entry(insert_info_frame)
user_entry.grid(row=0, column=1)

# MP Entry. Label and user can insert data thru entry
mobile_phone_label = tk.Label(insert_info_frame, text="Mobile Phone :\n")
mobile_phone_label.grid(row=2, column=0)
mobile_phone_label.configure(bg="deep sky blue", fg="purple", font=("Arial", 12, "bold"))
mobile_phone_entry = tk.Entry(insert_info_frame)
mobile_phone_entry.grid(row=2, column=1)

# Label and user can insert data thru entry
user_age_label = tk.Label(insert_info_frame, text="Age :\n")
user_age_label.grid(row=4, column=0)
user_age_label.configure(bg="deep sky blue", fg="purple", font=("Arial", 12, "bold"))
uage_entry = tk.Entry(insert_info_frame)
uage_entry.grid(row=4, column=1)

#movie
movie=tk.Label(insert_info_frame, text="Movie :")
movie.grid(row=7, column=0)
movie.configure(bg="deep sky blue", fg="purple", font=("Arial", 12, "bold"))

# Movie Title Type
movie_var = tk.StringVar(insert_info_frame)
movie_var.set("Select Your Movie")  # Default value before your selection
trip_dropdown = tk.OptionMenu(insert_info_frame, movie_var, "MIGRATION", "WISH", "WAR ON TERROR", "NIGHT HAS COMES")
trip_dropdown.grid(row=7, column=1)
trip_dropdown.configure(bg="blue", fg="violet", font=("Arial", 12, "bold"))

# Packs Entry. Label and user can insert data thru entry
packs_label = tk.Label(insert_info_frame, text="Packs:")
packs_label.grid(row=14, column=0)
packs_label.configure(bg="deep sky blue", fg="purple", font=("Arial", 12, "bold"))
packs_entry = tk.Entry(insert_info_frame)
packs_entry.grid(row=14, column=1)

# Save Button
save_button = tk.Button(insert_info_frame, text="Save", command=collect_data)
save_button.grid(row=10, column=10)
save_button.configure(bg="blue", fg="pink", font=("Arial", 12, "bold"))

# Output Label & result
label = tk.Label(insert_info_frame, text='Total Price', font=("Arial", 12))
label.grid(row=0, column=2)
label.configure(bg="deep sky blue", fg="purple", font=("Arial", 12, "bold"))
output_label = tk.Label(insert_info_frame, text="")
output_label.grid(row=0, column=3)
output_label.configure(bg="deep sky blue", fg="dark blue", font=("Arial", 12, "bold"))


root.mainloop()

