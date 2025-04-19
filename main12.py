import random
import streamlit as st
import string
import datetime

objects = [
    "Stone", "Tree", "Water", "House", "Car", "Book", "Chair", "Table", "Lamp", "Phone",
    "Computer", "Paper", "Pen", "Pencil", "Door", "Window", "Floor", "Ceiling", "Wall", "Roof",
    "Garden", "Flower", "Grass", "Cloud", "Sun", "Moon", "Star", "Sky", "Bird", "Fish",
    "Cat", "Dog", "Horse", "Cow", "Sheep", "Pig", "Chicken", "Duck", "Leaf", "Branch",
    "Root", "Soil", "Sand", "Rock", "Mountain", "River", "Lake", "Ocean", "Island", "Beach",
    "Forest", "Path", "Road", "Bridge", "Building", "Room", "Kitchen", "Bedroom", "Bathroom", "Living room",
    "Office", "School", "Hospital", "Store", "Park", "City", "Town", "Village", "Country", "World",
    "Planet", "Galaxy", "Universe", "Ball", "Toy", "Game", "Food", "Drink", "Clothes", "Shoes",
    "Hat", "Bag", "Jewelry", "Watch", "Clock", "Radio", "Television", "Camera", "Music", "Art",
    "Painting", "Sculpture", "Photograph", "Movie", "Play", "Dance", "Song", "Instrument", "Tool", "Hammer",
    "Saw", "Screwdriver", "Wrench", "Knife", "Fork", "Spoon", "Plate", "Bowl", "Cup", "Glass",
    "Bottle", "Box", "Basket", "Bag", "Key", "Lock", "Money", "Coin", "Bill", "Card",
    "Ticket", "Stamp", "Letter", "Package", "Map", "Globe", "Flag", "Anthem", "Language", "Culture",
    "History", "Science", "Math", "Physics", "Chemistry", "Biology", "Medicine", "Technology", "Internet", "Software",
    "Hardware", "Data", "Information", "Idea", "Thought", "Feeling", "Emotion", "Love", "Hate", "Joy",
    "Sadness", "Anger", "Fear", "Surprise", "Hope", "Dream", "Memory", "Time", "Day", "Night",
    "Week", "Month", "Year", "Century", "Decade", "Moment", "Second", "Minute", "Hour", "Spring",
    "Summer", "Autumn", "Winter", "Fire", "Wind", "Earth", "Metal", "Wood", "Plastic", "Glass",
    "Fabric", "Leather", "Rubber", "Paint", "Brush", "Canvas", "Clay", "Needle", "Thread", "Button",
    "Zipper", "Mirror", "Comb", "Brush", "Towel", "Soap", "Shampoo", "Toothbrush", "Toothpaste", "Towel",
    "Bed", "Pillow", "Blanket", "Sheet", "Desk", "Shelf", "Drawer", "Plant", "Pot", "Fence",
    "Gate", "Wall", "Light", "Shadow", "Sound", "Noise", "Silence", "Smell", "Taste", "Touch",
    "Heat", "Cold", "Pressure", "Movement", "Speed", "Direction", "Distance", "Shape", "Size", "Color",
    "Texture", "Pattern", "Number", "Symbol", "Sign", "Word", "Sentence", "Paragraph", "Page", "Chapter",
    "Title", "Author", "Reader", "Library", "Museum", "Gallery", "Stadium", "Theater", "Airport", "Station",
    "Ship", "Boat", "Train", "Bus", "Bike", "Motorcycle", "Map", "Compass", "Guide", "Journey",
    "Adventure", "Story", "Poem", "Journal", "Diary", "Recipe", "Ingredient", "Meal", "Snack", "Dessert",
    "Candy", "Fruit", "Vegetable", "Meat", "Bread", "Cheese", "Milk", "Juice", "Coffee", "Tea",
    "Soda", "Water", "Spice", "Herb", "Salt", "Pepper", "Sugar", "Oil", "Vinegar", "Sauce",
    "Soup", "Salad", "Sandwich", "Pizza", "Cake", "Cookie", "Ice cream", "Chocolate", "Present", "Gift",
    "Party", "Balloon", "Candle", "Music", "Game", "Friend", "Family", "Person", "Child", "Adult",
    "Man", "Woman", "King", "Queen", "President", "Doctor", "Teacher", "Student", "Artist", "Writer",
    "Singer", "Dancer", "Actor", "Athlete", "Soldier", "Police", "Firefighter", "Judge", "Lawyer", "Engineer",
    "Scientist", "Chef", "Baker", "Farmer", "Pilot", "Driver", "Sailor", "Guard", "Worker", "Leader",
    "Follower", "Citizen", "Neighbor", "Stranger", "Guest", "Host", "Baby", "Toddler", "Teenager", "Elder",
    "Ancestor", "Descendant", "Body", "Head", "Hair", "Eye", "Ear", "Nose", "Mouth", "Tongue",
    "Tooth", "Neck", "Shoulder", "Arm", "Hand", "Finger", "Leg", "Foot", "Toe", "Skin",
    "Bone", "Muscle", "Heart", "Brain", "Blood", "Breath", "Voice", "Shadow", "Reflection", "Echo",
    "Silence", "Whisper", "Shout", "Laugh", "Cry", "Smile", "Frown", "Gesture", "Nod", "Shake",
    "Point", "Touch", "Hold", "Grab", "Throw", "Catch", "Push", "Pull", "Lift", "Carry",
    "Drop", "Walk", "Run", "Jump", "Skip", "Crawl", "Climb", "Swim", "Fly", "Drive",
    "Sail", "Ride", "Fall", "Stand", "Sit", "Lie", "Sleep", "Wake", "Eat", "Drink",
    "Cook", "Clean", "Wash", "Dry", "Open", "Close", "Turn", "Look", "See", "Hear",
    "Smell", "Taste", "Feel", "Think", "Know", "Learn", "Teach", "Speak", "Listen",
    "Read", "Write", "Count", "Add", "Subtract", "Multiply", "Divide", "Measure", "Weigh", "Compare",
    "Choose", "Decide", "Plan", "Organize", "Create", "Build", "Repair", "Destroy", "Protect", "Attack",
    "Defend", "Win", "Lose", "Play", "Work", "Rest", "Travel", "Explore", "Discover", "Imagine",
    "Believe", "Hope", "Dream", "Remember", "Forget", "Understand", "Question", "Answer", "Explain", "Describe",
    "Discuss", "Argue", "Agree", "Disagree", "Help", "Support", "Care", "Love", "Hate", "Forgive",
    "Punish", "Reward", "Control", "Lead", "Follow", "Serve", "Obey", "Rule", "Law", "Justice",
    "Peace", "War", "Victory", "Defeat", "Freedom", "Prison", "Danger", "Safety", "Secret", "Truth",
    "Lie", "Mistake", "Accident", "Chance", "Luck", "Fate", "Destiny", "Beginning", "End",
    "Middle", "Past", "Present", "Future", "Now", "Then", "Soon", "Late", "Early", "Always",
    "Never", "Often", "Sometimes", "Rarely", "Every", "Some", "Few", "Many", "All",
    "None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Hundred", "Thousand", "Million", "Billion", "Trillion", "First", "Second", "Last", "Next",
    "Previous", "Other", "Same", "Different", "Big", "Small", "Long", "Short", "Tall", "Wide",
    "Narrow", "Deep", "Shallow", "High", "Low", "Fast", "Slow", "Heavy", "Light",
    "Hard", "Soft", "Rough", "Smooth", "Sharp", "Blunt", "Hot", "Cold", "Warm", "Cool",
    "Wet", "Dry", "Clean", "Dirty", "Empty", "Full", "Open", "Closed", "New", "Old",
    "Young", "Adult", "Dead", "Alive", "Strong", "Weak", "Healthy", "Sick", "Happy", "Sad",
    "Angry", "Afraid", "Surprised", "Calm", "Excited", "Bored", "Tired", "Busy", "Free",
    "Easy", "Difficult", "Good", "Bad", "Right", "Wrong", "True", "False", "Beautiful", "Ugly",
    "Interesting", "Boring", "Important", "Unimportant", "Possible", "Impossible", "Necessary", "Unnecessary", "Usual", "Unusual",
    "Normal", "Strange", "Real", "Fake", "Natural", "Artificial", "Public", "Private", "Local", "Global",
    "National", "International", "Political", "Economic", "Social", "Cultural", "Religious", "Scientific", "Medical", "Educational",
    "Technical", "Artistic", "Literary", "Musical", "Dramatic", "Sporting", "Outdoor", "Indoor", "Domestic", "Foreign",
    "Ancient", "Modern", "Future", "Past", "Present", "Simple", "Complex", "Organized", "Chaotic", "Silent", "Noisy",
    "Bright", "Dark", "Clear", "Cloudy", "Visible", "Invisible", "Solid", "Liquid", "Gas", "Empty",
    "Full", "Whole", "Part", "Single", "Double", "Multiple", "Few", "Many", "Some",
    "All", "None", "Each", "Every", "Other", "Same", "Different", "More", "Less",
    "Most", "Least", "Enough", "Too much", "Too little", "Equal", "Unequal", "Similar", "Unique", "Common",
    "Rare", "General", "Specific", "Abstract", "Concrete", "Positive", "Negative", "Neutral", "Active",
    "Passive", "Direct", "Indirect", "Formal", "Informal", "Official", "Unofficial", "Legal", "Illegal",
    "Moral", "Immoral", "Ethical", "Unethical", "Logical", "Illogical", "Rational", "Irrational", "Creative", "Destructive",
    "Constructive", "Productive", "Efficient", "Inefficient", "Safe", "Dangerous", "Secure", "Unsafe", "Healthy", "Unhealthy",
    "Pleasant", "Unpleasant", "Comfortable", "Uncomfortable", "Convenient", "Inconvenient", "Expensive", "Cheap", "Valuable", "Worthless",
    "Useful", "Useless", "Necessary", "Unnecessary", "Optional", "Compulsory", "Voluntary", "Forced", "Free", "Limited",
    "Unlimited", "Temporary", "Permanent", "Brief", "Long", "Quick", "Slow", "Early", "Late",
    "Punctual", "Delayed", "Ready", "Unready", "Prepared", "Unprepared", "Organized", "Disorganized", "Neat", "Messy",
    "Clean", "Dirty", "Empty", "Full", "Open", "Closed", "Front", "Back", "Side",
    "Top", "Bottom", "Inside", "Outside", "Above", "Below", "Under", "Over", "Near",
    "Far", "Left", "Right", "Center", "Edge", "Corner", "Middle", "Beginning", "End",
    "Once", "Twice", "Again", "Still", "Yet", "Already", "Soon", "Later", "Now",
    "Then", "Today", "Tomorrow", "Yesterday", "Always", "Never", "Often", "Sometimes", "Rarely",
    "Usually", "Frequently", "Seldom", "Occasionally", "Constantly", "Continuously", "Gradually", "Suddenly", "Slowly", "Quickly",
    "Carefully", "Carelessly", "Easily", "Difficultly", "Well", "Badly", "Loudly", "Quietly", "Softly", "Hardly",
    "Clearly", "Vaguely", "Definitely", "Maybe", "Perhaps", "Probably", "Possibly", "Certainly", "Absolutely", "Exactly",
    "Almost", "Nearly", "Slightly", "Greatly", "Completely", "Partially", "Together", "Apart", "Alone", "Together",
    "Also", "Too", "Even", "Only", "Just", "Simply", "Merely", "However", "But",
    "And", "Or", "Nor", "So", "Therefore", "Because", "Since", "Although", "While",
    "If", "Unless", "Until", "Before", "After", "During", "While", "Towards", "Away",
    "Through", "Across", "Around", "Along", "Beside", "Between", "Among", "Inside", "Outside",
    "Above", "Below", "Under", "Over", "Near", "Far", "Left", "Right", "Up",
    "Down", "Forward", "Backward", "Here", "There", "Everywhere", "Nowhere", "Somewhere", "Anywhere", "Inside",
    "Outside", "Within", "Without", "Beyond", "Against", "Upon", "Onto", "Into", "Out of",
    "From", "To", "Of", "In", "At", "On", "By", "With",
    "About", "For", "Like", "As", "Than", "That", "This", "These", "Those",
    "Which", "What", "Who", "Whom", "Whose", "Why", "How", "When", "Where",
    "Whether", "If", "Though", "Although", "Because", "Since", "While", "Until", "Unless",
    "Before", "After", "During", "About", "Against", "Along", "Among", "Around", "At",
    "Behind", "Below", "Beneath", "Beside", "Between", "Beyond", "By", "Down", "During", "Except",
    "For", "From", "In", "Inside", "Into", "Like", "Near", "Of", "Off",
    "On", "Onto", "Out", "Outside", "Over", "Past", "Since", "Through", "Throughout", "To",
    "Toward", "Under", "Underneath", "Until", "Up", "Upon", "With", "Without", "A", "An",
    "The", "Some", "Any", "No", "Every", "All", "Few", "Many", "Most",
    "Least", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
    "Nine", "Ten", "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh",
    "Eighth", "Ninth", "Tenth", "Next", "Last", "Other", "Another", "Each", "Every",
    "Either", "Neither", "Both", "Several", "Various", "Numerous", "Certain", "Such", "Same",
    "Different", "Big", "Small", "Long", "Short", "Tall", "Wide", "Narrow", "Deep",
    "Shallow", "High", "Low", "Fast", "Slow", "Heavy", "Light", "Hard", "Soft",
    "Rough", "Smooth", "Sharp", "Blunt", "Hot", "Cold", "Warm", "Cool", "Wet",
    "Dry", "Clean", "Dirty", "Empty", "Full", "Open", "Closed", "New", "Old",
    "Young", "Adult", "Dead", "Alive", "Strong", "Weak", "Healthy", "Sick", "Happy",
    "Sad", "Angry", "Afraid", "Surprised", "Calm", "Excited", "Bored", "Tired", "Busy",
    "Free", "Easy", "Difficult", "Good", "Bad", "Right", "Wrong", "True",
    "False", "Beautiful", "Ugly", "Interesting", "Boring", "Important", "Unimportant", "Possible", "Impossible",
    "Necessary", "Unnecessary", "Usual", "Unusual", "Normal", "Strange", "Real", "Fake", "Natural",
    "Artificial", "Public", "Private", "Local", "Global", "National", "International", "Political", "Economic",
    "Social", "Cultural", "Religious", "Scientific", "Medical", "Educational", "Technical", "Artistic", "Literary",
    "Musical", "Dramatic", "Sporting", "Outdoor", "Indoor", "Domestic", "Foreign", "Ancient", "Modern",
    "Future", "Past", "Present", "Simple", "Complex", "Organized", "Chaotic", "Silent", "Noisy",
    "Bright", "Dark", "Clear", "Cloudy", "Visible", "Invisible", "Solid", "Liquid", "Gas",
    "Empty", "Full", "Whole", "Part", "Single", "Double", "Multiple", "Few",
    "Many", "Some", "All", "None", "Each", "Every", "Other", "Same",
    "Different", "More", "Less", "Most"]

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

if "check" not in st.session_state:
    st.session_state.check = 0
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

url = "https://youtu.be/dQw4w9WgXcQ"
url2 = "https://youtu.be/LO8k-Y9luYU?t=8"
url3 = "https://youtu.be/ecJSxFzvSKk"

title = "English vocabulary practice test"
title = nice_present("center", 50, title, "bold")

input_name = st.text_input("Type your name:")
suggest = "Try Rick Astley"
suggest = nice_present("left", 15, suggest, "italian")
phone = st.text_input("Type your phone number: ")
locate = st.text_input("Type your location: ")
amount_word = int(st.number_input("Type how much word do you want to play:"))
suggest_word = "Don't type too much"
suggest_word = nice_present("left", 15, suggest_word, "italian")

if input_name.lower() == "rick astley":
    st.video(url, autoplay=True)
if amount_word >= 70:
    st.video(url2, autoplay=True)
if str(phone).lower() in ["30/4", "30-4", "30.4", "30 4"]:
    st.video(url3, autoplay=True)

if input_name and amount_word:
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
        if st.session_state.check >= (amount_word):
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
                st.session_state.check += 1
            else:
                break

    if st.session_state.answered:
        if st.session_state.check >= (amount_word):
            pass
        if st.button("Next Word"):
            if st.session_state.check >= (amount_word):
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

    if st.session_state.check >= amount_word and st.session_state.start_time is not None:
        end_time = datetime.datetime.now()
        total_time = end_time - st.session_state.start_time
        time_seconds = seconds(total_time)

        if phone == None:
            phone = "No answer"
        if locate == None:
            locate = "No answer"
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
