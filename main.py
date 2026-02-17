from turtle import Turtle, Screen
import pandas

# --- 1. Screen & Map Setup ---
image = "Table/New_file/map.gif"
screen = Screen()
screen.title("U.S. State Names Game")
screen.setup(900, 600)

# Add the map image to the screen's shapes
screen.addshape(image)

# Create the map turtle and give it the image shape
turtle_map = Turtle()
turtle_map.shape(image)

# Create the writer turtle (invisible, used only for text)
writer = Turtle()
writer.penup()
writer.hideturtle()

# --- 2. Data Loading ---
# Ensure your path to the CSV is correct
The_states = pandas.read_csv("./Table/States.csv")
all_state_list = The_states.state.to_list()
guessed_status = []

# --- 3. Game Loop ---
while len(guessed_status) < 50:
    # .title() converts "alabama" or "ALABAMA" to "Alabama"
    Answer_output = screen.textinput(title=f"{len(guessed_status)}/50 States Correct",
                                     prompt="Please enter the name of a state:").title()

    # Secret exit to stop the game
    if Answer_output == "Exit":
        break

    if Answer_output in all_state_list and Answer_output not in guessed_status:
        guessed_status.append(Answer_output)

        # Pull the specific row for the state
        state_data = The_states[The_states.state == Answer_output]

        # Convert pandas Series to integers using .item()
        x_cor = int(state_data.x.item())
        y_cor = int(state_data.y.item())

        # Use the WRITER turtle to go and write
        writer.goto(x_cor, y_cor)
        writer.write(Answer_output, align="center", font=("Arial", 8, "normal"))

# Keep the window open until clicked
screen.exitonclick()