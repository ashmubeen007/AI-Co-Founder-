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
        background-color: #131722;
        color: #f6f6f6;
    }
    
    /* Input box styling */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #2a2e39;
        background-color: #1E222D;
        color: #f6f6f6;
        padding: 15px 20px;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #6B73FF;
        box-shadow: 0 0 15px rgba(107, 115, 255, 0.4);
        background-color: #252a38;
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
        box-shadow: 0 4px 10px rgba(0, 13, 255, 0.2);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 13, 255, 0.5);
    }
    
    /* Card aesthetics for Lean Canvas (Expander) */
    div[data-testid="stExpander"] {
        background-color: #1E222D !important;
        border-radius: 12px !important;
        border: 1px solid #333947 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stExpander"]:hover {
        border-color: #6B73FF !important;
        box-shadow: 0 0 15px rgba(107, 115, 255, 0.3) !important;
    }
    div[data-testid="stExpander"] details {
        background-color: transparent !important;
    }
    div[data-testid="stExpander"] summary {
        background-color: #1E222D !important;
        color: #f6f6f6 !important;
        border-radius: 12px !important;
    }
    div[data-testid="stExpander"] summary:hover {
        background-color: #252a38 !important;
    }
    div[data-testid="stExpander"] summary p {
        color: #f6f6f6 !important;
        font-weight: bold !important;
    }
    div[data-testid="stExpander"] div[role="region"] {
        background-color: #1E222D !important;
        color: #d1d5db !important;
    }
    
    /* Headers & Text */
    h1, h2, h3, h4, h5, h6, p, .stMarkdown, label {
        color: #f6f6f6 !important;
    }
    h1 {
        background: -webkit-linear-gradient(45deg, #ff007f, #7f00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }
    .stMarkdown p {
        color: #d1d5db !important;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 18px;
        color: #a0aabf;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #6B73FF;
    }

    /* Custom CSS Classes for dynamic output cards */
    .output-card {
        background-color: #1E222D;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #333947;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        transition: all 0.3s ease;
        color: #d1d5db;
    }
    .output-card:hover {
        border-color: #6B73FF;
        box-shadow: 0 0 15px rgba(107, 115, 255, 0.3);
    }
    .output-card h3 {
        color: #f6f6f6 !important;
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
                        <div class='output-card'>
                            <h3 style='margin-top: 0; color: #4CAF50 !important;'>{i+1}. {comp.get('name', 'Unknown')}</h3>
                            <p style='color: #d1d5db; font-size: 16px;'>{comp.get('description', '')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                with tab3:
                    st.header("Pitch Deck Outline")
                    slides = data.get("pitch_deck", [])
                    for i, slide in enumerate(slides):
                        points_html = "".join([f"<li style='color: #d1d5db; margin-bottom: 8px;'>{point}</li>" for point in slide.get("points", [])])
                        st.markdown(f"""
                        <div class='output-card' style='border-left: 5px solid #6B73FF;'>
                            <h3 style='margin-top: 0;'>Slide {i+1}: {slide.get('title', 'Unknown Title')}</h3>
                            <ul style='padding-left: 20px;'>
                                {points_html}
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
                            
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
