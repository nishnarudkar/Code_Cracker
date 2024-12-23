import streamlit as st
import art


print(art.logo)
def caesar_cipher(text, shift, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    shift = -shift if mode == "Decode" else shift  
    
    for char in text:
        if char.isalpha(): 
            is_upper = char.isupper()
            char = char.lower()
            shifted_position = (alphabet.index(char) + shift) % len(alphabet)
            new_char = alphabet[shifted_position]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char 
    
    return result

st.title("Code Cracker Tool")
st.write("Encrypt or decrypt your messages with the Code cracker!")

mode = st.radio("Choose an option:", ("Encode", "Decode"))
text = st.text_area("Enter your message:")
shift = st.number_input("Enter the shift amount:", min_value=1, step=1)


if st.button("Run Code Cracker"):
    if text.strip():
        result = caesar_cipher(text, shift, mode)
        st.success(f"Result ({mode}d): {result}")
    else:
        st.warning("Please enter a message to process.")


st.write("---")
st.caption("Made with ❤️ using Streamlit by Nishant Narudkar")
