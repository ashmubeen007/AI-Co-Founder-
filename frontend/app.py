import streamlit as st
import requests

# Configure Streamlit page
st.set_page_config(
    page_title="AI Co-Founder",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a modern, beautiful look
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #fafafa;
    }
    
    /* Input box styling */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e0e0e0;
        padding: 15px 20px;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #4CAF50;
        box-shadow: 0 6px 12px rgba(76, 175, 80, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 12px;
        background: linear-gradient(135deg, #6B73FF 0%, #000DFF 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 25px; /* Alignment with input box */
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0, 13, 255, 0.3);
    }
    
    /* Card aesthetics for Lean Canvas */
    div[data-testid="stExpander"] {
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: none;
        margin-bottom: 10px;
    }
    
    /* Headers */
    h1 {
        background: -webkit-linear-gradient(45deg, #ff007f, #7f00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }
    h2, h3 {
        color: #333333;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.title("One-Sentence AI Co-Founder 🚀")
st.markdown("<h4 style='text-align: center; color: #666;'>Type one sentence about your startup idea, and I'll generate your business plan, find competitors, and build your pitch deck.</h4>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# The prominent input box layout
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    input_col, btn_col = st.columns([4, 1])
    with input_col:
        idea = st.text_input("Describe your startup idea in one sentence:", placeholder="e.g., An app that matches dog owners with reliable local dog walkers based on personality types.", label_visibility="collapsed")
    with btn_col:
        submit_button = st.button("Generate My Startup", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

if submit_button and idea:
    with st.spinner("🧠 Analyzing your idea, sizing the market, and preparing the blueprint..."):
        try:
            # Call FastAPI backend
            response = requests.post("http://localhost:8000/generate", json={"sentence": idea})
            
            if response.status_code == 200:
                data = response.json()
                
                # --- Result Display ---
                st.success("Your startup blueprint is ready!")
                
                tab1, tab2, tab3 = st.tabs(["🧩 Lean Canvas", "🔍 Competitors", "📊 Pitch Deck"])
                
                with tab1:
                    st.header("Lean Canvas")
                    lc = data.get("lean_canvas", {})
                    
                    col_a, col_b = st.columns(2)
                    with col_a:
                        with st.expander("🚨 Problem", expanded=True):
                            val = lc.get("problem", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                        with st.expander("💡 Solution", expanded=True):
                            val = lc.get("solution", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                        with st.expander("🎯 Unique Value Proposition", expanded=True):
                            val = lc.get("unique_value_proposition", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                        with st.expander("🏎️ Unfair Advantage", expanded=True):
                            val = lc.get("unfair_advantage", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                        with st.expander("💸 Cost Structure", expanded=True):
                            val = lc.get("cost_structure", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                    
                    with col_b:
                        with st.expander("👥 Customer Segments", expanded=True):
                            val = lc.get("customer_segments", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                        with st.expander("📈 Key Metrics", expanded=True):
                            val = lc.get("key_metrics", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                        with st.expander("📣 Channels", expanded=True):
                            val = lc.get("channels", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)
                        with st.expander("💰 Revenue Streams", expanded=True):
                            val = lc.get("revenue_streams", "N/A")
                            st.write("\n".join(val) if isinstance(val, list) else val)

                with tab2:
                    st.header("Top Competitors")
                    competitors = data.get("competitors", [])
                    for i, comp in enumerate(competitors):
                        st.markdown(f"""
                        <div style='background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;'>
                            <h3 style='margin-top: 0; color: #4CAF50;'>{i+1}. {comp.get('name', 'Unknown')}</h3>
                            <p style='color: #555; font-size: 16px;'>{comp.get('description', '')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                with tab3:
                    st.header("Pitch Deck Outline")
                    slides = data.get("pitch_deck", [])
                    for i, slide in enumerate(slides):
                        with st.container():
                            st.markdown(f"""
                            <div style='border-left: 5px solid #6B73FF; padding-left: 20px; margin-bottom: 30px; background: white; padding: 20px; border-radius: 0 12px 12px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
                                <h3 style='margin-top: 0; color: #1E1E1E;'>Slide {i+1}: {slide.get('title', 'Unknown Title')}</h3>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            points = slide.get("points", [])
                            for point in points:
                                st.markdown(f"- {point}")
                                
                            if i < len(slides) - 1:
                                st.markdown("<hr style='border: 1px solid #f0f0f0;'>", unsafe_allow_html=True)
                            
            else:
                st.error(f"Error from server: {response.status_code}")
                try:
                    error_data = response.json()
                    st.write(error_data.get("detail", response.text))
                except:
                    st.write(response.text)
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend server. Is FastAPI running on port 8000?")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
elif submit_button and not idea:
    st.warning("Please enter your startup idea first!")
