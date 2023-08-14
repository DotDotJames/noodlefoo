import numpy as np
import random
import streamlit as st

# top of page
st.set_page_config(page_title="NoodleFoo", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

# hide the Streamlit header
st.markdown("""
<style>
    header:first-of-type {
        display: none;
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# hide the Streamlit header & footer / merge / dupe?
hide_st_style = """
            <style>
            #MainMenu {display:none !important; visibility: hidden !important;}
            footer {display:none !important; visibility: hidden !important;}
            header {display:none !important; visibility: hidden !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# hide the default image pop-over
st.markdown(
    """
    <style>
        button[title='View fullscreen'] {
            display: none !important;
            visibility: hidden !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# hide labels
st.markdown(
    """
    <style>
        label {
            display: none !important;
            visibility: hidden !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# hide_script = """
# <style>
    # body {
        # display: none !important;
    # }
# </style>
# <script>
    # // Optionally, you can use JS to hide elements after some conditions/events
    # document.body.style.display = 'none';
# </script>
# """

# st.markdown(hide_script, unsafe_allow_html=True)

# unused?
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
<style>
    div[data-testid="stForm"] {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .stTextInput .stTextInput label {
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# find closest emoji
file_path = "emoji-codepoints-py.txt"

# Read the text file and store each line as a string element in a list
with open(file_path, 'r') as file:
    lines = file.readlines()
    
# Remove newline characters from each line and create the list
codes = [line.strip()[1:-1] for line in lines]
# phrase_sim = np.load('./phrase-emoji-sim.npy')

with open("phrase-emoji-sim.txt", 'r') as f:
    csv_content = f.read()
    
from io import StringIO

# Convert CSV text back to numpy array
csv_file = StringIO(csv_content)
phrase_sim = np.loadtxt(csv_file, delimiter=",")

print(phrase_sim[1][1]);

subset = phrase_sim[:,3590:3790]
highest_index = np.argmax(subset, axis=1)

words = ["peace","above","chaos"]

# for i in range(0,3918):
    # st.write(codes[i],i)

for i in range(0,3):
    word = words[i];
    h = highest_index[i] + 3590
    # st.write([words[i],h,phrase_sim[i][h],codes[h]])
    # st.write(codes[h]);

# check if the word
# is it in the list
# what is distance from list

def show_registration_modal():
    st.subheader("Register with Magic Link")

    # Get user's email
    email = st.text_input("Enter your email:")

    # Display a button to send the Magic Link
    if st.button("Send Magic Link"):
        send_magic_link(email)

def send_magic_link(email):
    # Replace with your Supabase project URL
    supabase_url = "https://your-project-id.supabase.co"
    magic_link_endpoint = f"{supabase_url}/auth/v1/magiclink"

    # Send a POST request to the Magic Link endpoint
    response = httpx.post(magic_link_endpoint, json={"email": email})

    if response.status_code == 200:
        st.success("Magic Link sent successfully!")
    else:
        st.error("Error sending Magic Link. Please try again later.")

# magic link to subscribe for updates
# Display the Magic Link button
# if st.button("Register with Magic Link"):
    # show_registration_modal()

# header bar placeholder
# st.markdown('<div id="custom-id">Your content here</div>', unsafe_allow_html=True)

# st.markdown("""
# <style>
    # #custom-id {
        # background-color: yellow;
    # }
# </style>
# """, unsafe_allow_html=True)


# todo -- figure out how to hide things that don't have IDs or classes better -- maybe some xpath
# st.markdown("""
# <script>
# function myFunction() {
# console.log("ran");
        # document.querySelectorAll('p').forEach(function(paragraph) {
        # console.log(paragraph.innerText);
            # if (paragraph.innerText === 'hide me') {
                # paragraph.style.display = 'none';
            # }
        # });
# }

        # setTimeout(function() {
        # myFunction();
    # }, 10000);
# </script>
# """, unsafe_allow_html=True)

# st.write("<p style='text-align: center;'>Noodle</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# fill first column with empty content to center-align the second column
col1.write("")

# put image in the second column
image_path = "./noodlefoo-launch.png"
col2.image(image_path, caption="", use_column_width=True)

col3.write("")

result_array = ["0.71", "0.62", "0.44", "0.121", "0.123", "0.234"]
secret_words = ["peace","above","chaos"]
secret_phrase = "peace above chaos"

def process_input(input_val):
    z = ord(input_val[0]) % 3
    z = random.randint(0, 3)
    # z = round(random.uniform(0, 1), 3)

    if 0 <= z < len(result_array):
            return round(random.uniform(0.5, 1.0), 3)
    else:
        return None  # Return None if input_val is out of range

def compute_sum():
    return sum(float(value) for value in st.session_state.processed_values.values())

def display_row(num, word):
    # Fetch processed value or default word
    display_value = st.session_state.processed_values.get(num, word)
    display_value = word
    # Fetch persisted input value or an empty string
    input_value = st.session_state.input_values.get(num, '')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write(display_value)
    with col2:
        st.session_state.input_values[num] = st.text_input("", value=input_value, key=f'input_{num}')
    with col3:
        st.write(str(st.session_state.processed_values.get(num, '')))
    with col4:
        submitted = st.button('\u23CE', key=f'submit_{num}')
        if submitted and st.session_state.input_values[num]:
            st.session_state.processed_values[num] = process_input(st.session_state.input_values[num])
            # Force rerun to immediately see the changes
            st.experimental_rerun()

# Initialize session state if not present
if 'processed_values' not in st.session_state:
    st.session_state.processed_values = {}
if 'input_values' not in st.session_state:
    st.session_state.input_values = {}
if 'shuffled_words' not in st.session_state:
    # words = ["😊","🙋‍♂️","🐰","🎂","🍸"]
    # random.shuffle(words)
    st.session_state.shuffled_words = secret_words

centered_text = f"<p style='text-align: center;'>score: {compute_sum()}</p>"
st.markdown(centered_text, unsafe_allow_html=True)
# st.write(f"")

for i, word in enumerate(st.session_state.shuffled_words, 1):
    display_row(i, codes[highest_index[i-1]+3590])

repo_dir = "./"
readme_path = "readme.md"
with open(readme_path, "r") as readme_file:
    readme_content = readme_file.read()
    st.markdown(readme_content)
    
if __name__ == "__main__":
    pass
