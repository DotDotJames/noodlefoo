import streamlit as st
import random

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

# st.markdown("""
# <style>
    # header:first-of-type {
        # display: none;
        # visibility: hidden;
    # }
# </style>
# """, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
    
st.markdown(
    """
    <style>
        button[title='View fullscreen'] {
            display: none !important;
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


# st.markdown('<div id="custom-id">Your content here</div>', unsafe_allow_html=True)

# st.markdown("""
# <style>
    # #custom-id {
        # background-color: yellow;
    # }
# </style>
# """, unsafe_allow_html=True)


st.markdown("""
<script>
function myFunction() {
console.log("ran");
        document.querySelectorAll('p').forEach(function(paragraph) {
        console.log(paragraph.innerText);
            if (paragraph.innerText === 'hide me') {
                paragraph.style.display = 'none';
            }
        });
}

        setTimeout(function() {
        myFunction();
    }, 10000);
</script>
""", unsafe_allow_html=True)

import streamlit as st
import random

st.write("<p style='text-align: center;'>Noodle</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# Fill the first column with empty content to center-align the second column
col1.write("")

# Display the image in the second column
image_path = "./noodle-50.png"
col2.image(image_path, caption="", use_column_width=True)

col3.write("")

result_array = ["0.71", "0.62", "0.44", "0.121", "0.123", "0.234"]

def process_input(input_val):
    z = ord(input_val[0]) % 6
    z = random.randint(0, 5)
    # z = round(random.uniform(0, 1), 3)
    js_code = f"""
        <script>console.log("{z}");</script>
    """
    st.write(js_code)
    if 0 <= z < len(result_array):
        return round(random.uniform(0.5, 1.0), 3)
        # return result_array[z]
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
        st.text(st.session_state.processed_values.get(num, ''))
    with col4:
        submitted = st.button('🛩', key=f'submit_{num}')
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
    words = ["😊","🙋‍♂️","🐰","🎂","🍸"]
    random.shuffle(words)
    st.session_state.shuffled_words = words[:5]

centered_text = f"<p style='text-align: center;'>score: {compute_sum()}</p>"
st.markdown(centered_text, unsafe_allow_html=True)
# st.write(f"")

for i, word in enumerate(st.session_state.shuffled_words, 1):
    display_row(i, word)

repo_dir = "./"
readme_path = f"{repo_dir}/README.md"
with open(readme_path, "r") as readme_file:
    readme_content = readme_file.read()
    st.markdown(readme_content)
    
if __name__ == "__main__":
    pass
