import streamlit as st
import google.generativeai as genai

#Page Configuration
st.set_page_config(
    page_title="Gemini AI Text Generation",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Title
st.title("🤖 Text Generation with Gemini 2.5 Flash lattest version")

# Sidebar for API key input
api_key=st.sidebar.text_input(
    "Enter your Gemini API Key",
    type="password",
    placeholder="Enter your API-key"
)
if api_key:
    genai.configure(api_key=api_key)
    model=genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
    #model = genai.GenerativeModel('gemini-1.5-flash')
    prompt=st.text_area('Enter your promt here',height=150)
    
    if st.button("Generate"):
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(prompt)
                st.success("Response generated successfully!")
                st.write(response.text)
                st.write("Response:", response.text)
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.warning("Please enter your Gemini API key in the sidebar to use the app.")
   
# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Gemini AI Designed by Mrs. A. Sai Vamhi")
