# 🇺🇸 US States Guessing Game

An interactive Python game where players guess the names of U.S. states. Correct guesses are displayed on a U.S. map at the correct coordinates using Turtle graphics.

---

## 📌 Features

- Interactive GUI using Turtle
- Validates state names
- Prevents duplicate guesses
- Displays state names at correct coordinates
- Generates a CSV of missed states for learning

---

## 🛠 Technologies Used

- Python 3
- Turtle (for map graphics)
- Pandas (for CSV data handling)

---

## 📂 Project Structure

```
US-States-Guessing-Game/
├── main.py
├── check_guessing.py
├── Table/
│   ├── map.gif
│   ├── States.csv
│   ├── Squirrel.csv
│   └── temp.txt
├── Prayer_time.csv
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Install dependencies:
```bash
pip install pandas
```
3. Run the game:
```bash
python main.py
```
4. Enter state names when prompted. Type `Exit` to quit.
5. After exiting, a CSV file will be generated listing states you missed.

---

## 🎮 Learning Outcomes

- Handling CSV data with Pandas
- Drawing and writing with Turtle
- Input validation
- Game loop logic
- Saving data to CSV

---

## 🚀 Future Improvements

- Add scoring system
- Add timer and difficulty levels
- Convert to a web version (Flask / Streamlit)
- Add animations or color feedback for correct guesses

---

Made as a fun educational project to practice Python and coordinate-based drawing.
