import random
import streamlit as st
import string
import datetime

objects = [
    "Apple", "Alarm", "Armchair", "Axe", "Apron", "Anchor", "Antenna", "Atlas", "Almond", "Airplane",
    "Ball", "Bag", "Bowl", "Bottle", "Brush", "Broom", "Book", "Bandana", "Battery", "Belt",
    "Cup", "Chair", "Candle", "Car", "Clock", "Coat", "Crayon", "Couch", "Cookie", "Camera",
    "Dog", "Desk", "Dart", "Door", "Doll", "Dish", "Drum", "Drawer", "Duvet", "Duster",
    "Egg", "Eraser", "Envelope", "Earphones", "Eyeliner", "Easel", "Edge", "Eel", "Earring", "Engine",
    "Fan", "Fork", "Frypan", "Flute", "Flower", "File", "Fleece", "Faucet", "Feather", "Frame",
    "Game", "Glass", "Guitar", "Glove", "Gate", "Gum", "Grapes", "Garlic", "Gift", "Gold",
    "Hat", "Hammer", "Hanger", "Handbag", "Hair", "Hood", "Harp", "Heels", "Herbs", "Helmet",
    "Ice", "Ink", "Iron", "Investment", "Item", "Ivy", "Indicator", "Insect", "Igloo", "Ivory",
    "Jar", "Jacket", "Juice", "Jumper", "Jam", "Joystick", "Jewel", "Journal", "Jigsaw", "Jelly",
    "Key", "Kettle", "Knife", "Kite", "Keg", "Kale", "Kit", "Knob", "Karaoke", "Knee",
    "Lamp", "Ladder", "Ladle", "Lemon", "Laptop", "Label", "Leaf", "Lock", "Locket", "Lotion",
    "Mug", "Map", "Mask", "Marker", "Mouse", "Milk", "Mat", "Muffin", "Mirror", "Mittens",
    "Nail", "Notebook", "Napkin", "Needle", "Nut", "Nose", "Nest", "Noodles", "Nailclipper", "Network",
    "Oven", "Oar", "Onion", "Oil", "Orange", "Opener", "Ostrich", "Oregano", "Owl", "Octopus",
    "Pen", "Pencil", "Plate", "Pasta", "Pillow", "Paper", "Pot", "Pumpkin", "Pants", "Purse",
    "Quilt", "Quill", "Quokka", "Quasar", "Quiz", "Queue", "Quartz", "Quiver", "Quiche", "Quilted",
    "Ring", "Rug", "Radio", "Razor", "Rice", "Racket", "Remote", "Ribbon", "Rock", "Rubberband",
    "Spoon", "Shirt", "Socks", "Soap", "Scissors", "Saddle", "Sandwich", "Shelf", "Sofa", "Stapler",
    "Table", "Towel", "Ticket", "Tea", "Tent", "Tape", "Toothbrush", "Tomato", "Tongs", "Tissue",
    "Umbrella", "Underwear", "Uniform", "Utensil", "Ukelele",
    "Vase", "Video", "Vegetable", "Vacuum", "Vinegar", "Van", "Vest", "Vine", "Vortex", "Vulture",
    "Watch", "Wallet", "Whistle", "Window", "Wrench", "Wool", "Wire", "Wagon", "Water", "Waffle",
    "Xylophone", "X-ray", "Xeriscape", "Xenolith", "Xylograph",
    "Yarn", "Yogurt", "Yacht", "Yoke", "Yellow", "Yard", "Yardstick", "Yam", "Yeti", "Yoke",
    "Zebra", "Zipper", "Zoo", "Zone", "Zest", "Zenith", "Zodiac", "Zinc", "Zapper", "Ziggurat"
]

def nice_present(locate, size, word, weight):
    present = st.markdown(f"""
    <div style='text-align: {locate}; font-size: {size}px; font-weight: {weight}'>
        {word}
    </div>
""", unsafe_allow_html=True)
    return present

def _random_letters(n):
    alphabet = list(string.ascii_lowercase)
    return "".join(random.sample(alphabet, n))

def seconds(time_delta: datetime.timedelta) -> float:
    total_seconds = time_delta.total_seconds()
    rounded_seconds = round(total_seconds, 3)
    return rounded_seconds

if "question_count" not in st.session_state:
    st.session_state.question_count = 1
if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = 0
if "name" not in st.session_state:
    st.session_state.name = random.choice(objects)
if "hidden_indices" not in st.session_state:
    st.session_state.hidden_indices = sorted(random.sample(range(len(st.session_state.name)), min(2, max(1, len(st.session_state.name) // 2))))
if "letter_show" not in st.session_state:
    st.session_state.letter_show = ["_" if i in st.session_state.hidden_indices else char for i, char in enumerate(st.session_state.name)]
if "missing_letters" not in st.session_state:
    st.session_state.missing_letters = "".join(st.session_state.name[i] for i in st.session_state.hidden_indices)
if "answers" not in st.session_state:
    correct_answer_list = list(st.session_state.missing_letters)
    incorrect_answers = [list(_random_letters(len(correct_answer_list))) for _ in range(3)]
    st.session_state.answers = random.sample([correct_answer_list] + incorrect_answers, k=4)
if "correct_guess" not in st.session_state:
    st.session_state.correct_guess = False
if "answered" not in st.session_state:
    st.session_state.answered = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

title = "English vocabulary practice game"
title = nice_present("center", 50, title, "bold")

input_name = st.text_input("Type your name:")
suggest = "Try Rick Astley"
suggest = nice_present("left", 15, suggest, "italian")
phone = st.text_input("Type your phone number: ")
locate = st.text_input("Type your location: ")
amount_word = int(st.number_input("Type how much word do you want to play:"))

if input_name.lower() == "rick astley":
    st.video(url, autoplay=True)

if input_name and phone and locate and amount_word:
    col1, col2 = st.columns(2)
    col1.markdown(f"""
        <div style='text-align: left; font-size: 25px;'>
            Point: {st.session_state.correct_answer}
        </div>
    """, unsafe_allow_html=True)
    col2.markdown(f"""
        <div style='text-align: right; font-size: 25px;'>
            Question: {st.session_state.question_count}
        </div>
    """, unsafe_allow_html=True)

    word = nice_present("center", 35, " ".join(st.session_state.letter_show), "normal")

    cols = st.columns(4)
    buttons = []

    if st.session_state.start_time is None and st.session_state.question_count == 1:
        st.session_state.start_time = datetime.datetime.now()

    for i in range(4):
        buttons.append(cols[i].button(",".join(st.session_state.answers[i]).lower(), key=f"button_{i}", disabled=st.session_state.answered))

    for i, button in enumerate(buttons):
        if st.session_state.question_count >= (amount_word+1):
            break
        if button and not st.session_state.answered:
            st.session_state.answered = True
            if "".join(st.session_state.answers[i]) == st.session_state.missing_letters:
                st.success(f"{st.session_state.name} is a correct guess!")
                st.session_state.correct_answer += 1
                st.session_state.correct_guess = True
            else:
                st.error(f"Incorrect guess. The correct answer is: {st.session_state.name}")
            if not st.session_state.question_count >= (amount_word):
                st.session_state.question_count += 1
            else:
                break

    if st.session_state.answered:
        if st.session_state.question_count >= (amount_word):
            pass
        if st.button("Next Word"):
            if st.session_state.question_count >= (amount_word):
                pass
            st.session_state.name = random.choice(objects)
            st.session_state.hidden_indices = sorted(random.sample(range(len(st.session_state.name)), min(2, max(1, len(st.session_state.name) // 2))))
            st.session_state.letter_show = ["_" if i in st.session_state.hidden_indices else char for i, char in enumerate(st.session_state.name)]
            st.session_state.missing_letters = "".join(st.session_state.name[i] for i in st.session_state.hidden_indices)
            correct_answer_list = list(st.session_state.missing_letters)
            incorrect_answers = [list(_random_letters(len(correct_answer_list))) for _ in range(3)]
            st.session_state.answers = random.sample([correct_answer_list] + incorrect_answers, k=4)
            st.session_state.correct_guess = False
            st.session_state.answered = False
            st.rerun()

    if st.session_state.question_count >= amount_word and st.session_state.start_time is not None:
        end_time = datetime.datetime.now()
        total_time = end_time - st.session_state.start_time
        time_seconds = seconds(total_time)

        information = f"""Name: {input_name}
Phone number: {phone}
Location:{locate}
Correct answer: {st.session_state.correct_answer}
Amount of question: {amount_word}
Time: {time_seconds}\n"""
        st.success(f"You have finished all the questions in {time_seconds} seconds")

        ask = st.text_input("Do you want to save your data (Yes/No):")
        if ask.lower() in ["yes", "yeh", "y", "có", "co"]:
            now = datetime.datetime.now()
            save_time = now.strftime("%H:%M:%S %d/%m/%y")
            st.download_button("Download data", information, file_name=f"English Game:{input_name}|{save_time}.txt")
        st.stop()
    elif st.session_state.question_count > 20 and st.session_state.start_time is None:
        st.warning("Start time was not recorded.")
        st.stop()

    def _random_letters(n):
        alphabet = list(string.ascii_lowercase)
        return "".join(random.sample(alphabet, n))
