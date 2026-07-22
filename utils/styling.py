import streamlit as st
import base64


def apply_background(image_path="assets/background.png"):
    """
    Apply a professional glassmorphism theme
    across all Streamlit pages.
    """

    with open(image_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>

        /* ---------- App Background ---------- */

        .stApp {{

            background-image:
                linear-gradient(
                    rgba(255,255,255,0.80),
                    rgba(245,249,255,0.82)
                ),
                url("data:image/png;base64,{encoded}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}


        /* ---------- Main Container ---------- */

        .block-container {{

            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;

        }}


        /* ---------- Sidebar ---------- */

        section[data-testid="stSidebar"] {{

            background: rgba(255,255,255,0.78);

            backdrop-filter: blur(18px);

            border-right: 1px solid rgba(255,255,255,0.40);

        }}


        /* ---------- Metric Cards ---------- */

        div[data-testid="stMetric"] {{

            background: rgba(255,255,255,0.35);

            backdrop-filter: blur(18px);

            border-radius: 18px;

            padding: 20px;

            border: 1px solid rgba(255,255,255,0.40);

            box-shadow: 0 8px 30px rgba(0,0,0,0.08);

            transition: 0.3s;

        }}

        div[data-testid="stMetric"]:hover {{

            transform: translateY(-4px);

            box-shadow: 0 12px 35px rgba(0,0,0,0.15);

        }}


        /* ---------- Tables ---------- */

        div[data-testid="stDataFrame"] {{

            background: rgba(255,255,255,0.55);

            backdrop-filter: blur(15px);

            border-radius: 18px;

            padding: 12px;

            border: 1px solid rgba(255,255,255,0.35);

        }}


        /* ---------- Plotly Charts ---------- */

        div[data-testid="stPlotlyChart"] {{

            background: rgba(255,255,255,0.45);

            backdrop-filter: blur(15px);

            border-radius: 18px;

            padding: 15px;

            border: 1px solid rgba(255,255,255,0.35);

        }}


        /* ---------- Buttons ---------- */

        .stButton > button {{

            background: linear-gradient(
                135deg,
                #1565C0,
                #42A5F5
            );

            color: white;

            border: none;

            border-radius: 10px;

            padding: 0.6rem 1.3rem;

            font-weight: bold;

            transition: 0.3s;

        }}

        .stButton > button:hover {{

            transform: scale(1.04);

            box-shadow: 0 8px 20px rgba(33,150,243,0.35);

        }}


        /* ---------- Inputs ---------- */

        .stTextInput input,
        .stNumberInput input,
        .stSelectbox {{

            border-radius: 10px;

        }}


        /* ---------- Headings ---------- */

        h1 {{

            color: #0D47A1;

            font-weight: 800;

        }}

        h2 {{

            color: #1565C0;

            font-weight: 700;

        }}

        h3 {{

            color: #1976D2;

            font-weight: 700;

        }}


        /* ---------- Divider ---------- */

        hr {{

            border: none;

            height: 1px;

            background: rgba(0,0,0,0.08);

        }}


        /* ---------- Success / Info ---------- */

        div[data-testid="stAlert"] {{

            border-radius: 15px;

        }}

        </style>
        """,
        unsafe_allow_html=True
    )