import streamlit as st
import os

# Assuming the 'gif' folder is in the same directory as your Streamlit script.
# Dynamically generate the list of GIF file paths
gif_folder = 'gif'  # Folder name
gif_files = [f"{gif_folder}/{i}.gif" for i in range(1, 11)]  # Adjust the range if you have more or fewer GIFs

# Function to display the GIF based on index
def display_gif(file_path):
    st.image(file_path, use_column_width=True)

# Navigation and session state to cycle through GIFs
if 'current_gif' not in st.session_state:
    st.session_state.current_gif = 0  # Start with the first GIF

# Centered title
st.markdown("<h1 style='text-align: center;'>WELCOME! </h1>", unsafe_allow_html=True)

# Display the current GIF
display_gif(gif_files[st.session_state.current_gif])

# Navigation buttons and contact information
col1, col2, col3 = st.columns([3, 4, 1])  # Column sizes

with col1:
    if st.session_state.current_gif > 0:  # Only show 'Previous' if not the first GIF
        if st.button('Previous'):
            st.session_state.current_gif -= 1
            st.rerun()

with col2:
    # Contact Information as clickable links
    whatsapp_number = "+6285923671003"
    st.markdown(f'<a href="https://wa.me/{whatsapp_number.replace("+", "")}" target="_blank">WhatsApp: {whatsapp_number}</a>', unsafe_allow_html=True)
    st.markdown('Social: [@code_enteng](https://twitter.com/dev_enteng)', unsafe_allow_html=True)

with col3:
    if st.session_state.current_gif < len(gif_files) - 1:  # Only show 'Next' if not the last GIF
        if st.button('Next'):
            st.session_state.current_gif += 1
            st.rerun()

# Recommendation to scroll down
st.markdown("<h2 style='text-align: center;'>⬇️ ⬇️</h2>", unsafe_allow_html=True)

# Subtitle "PORTOFOLIO"
st.markdown("<h2 style='text-align: center;'>PORTOFOLIO</h2>", unsafe_allow_html=True)

# Assuming the 'Portofolio' folder is in the same directory as your Streamlit script.
# Dynamically generate the list of MP4 file paths, sorted alphabetically
portofolio_folder = 'Portofolio'
mp4_files = sorted([os.path.join(portofolio_folder, file) for file in os.listdir(portofolio_folder) if file.endswith('.mp4')])

# Function to display the MP4 based on index
def display_mp4(file_path):
    st.video(file_path)

# Navigation and session state to cycle through MP4s
if 'current_mp4' not in st.session_state:
    st.session_state.current_mp4 = 0  # Start with the first MP4

# Display the current MP4
if mp4_files:  # Check if there are any MP4 files
    display_mp4(mp4_files[st.session_state.current_mp4])

# Navigation buttons for MP4s
col4, col5, col6 = st.columns([3, 4, 1])  # Column sizes

with col4:
    if st.session_state.current_mp4 > 0:  # Only show 'Previous' if not the first MP4
        if st.button('Previous Video'):
            st.session_state.current_mp4 -= 1
            st.rerun()

with col5:
    whatsapp_number = "+6285923671003"
    st.markdown(f'<a href="https://wa.me/{whatsapp_number.replace("+", "")}" target="_blank">WhatsApp: {whatsapp_number}</a>', unsafe_allow_html=True)
    st.markdown('Social: [@code_enteng](https://twitter.com/dev_enteng)', unsafe_allow_html=True)


with col6:
    if mp4_files and st.session_state.current_mp4 < len(mp4_files) - 1:  # Only show 'Next' if not the last MP4
        if st.button('Next Video'):
            st.session_state.current_mp4 += 1
            st.rerun()
