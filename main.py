import streamlit as st
import pandas as pd
import joblib
from textwrap import dedent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AirFare AI",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# LOAD MODEL FILES
# ============================================================

@st.cache_resource
def load_files():
    model = joblib.load("linear_regression_model.pkl")
    scaler = joblib.load("scaler.pkl")
    feature_columns = joblib.load("feature_columns.pkl")

    return model, scaler, feature_columns


model, scaler, feature_columns = load_files()


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    dedent("""
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 8% 5%,
                rgba(37, 99, 235, 0.16),
                transparent 28%
            ),
            radial-gradient(
                circle at 92% 10%,
                rgba(14, 165, 233, 0.12),
                transparent 30%
            ),
            #06111f;

        color: #f8fafc;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 42px !important;
        padding-bottom: 50px !important;
        padding-left: 40px !important;
        padding-right: 40px !important;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero-card {
        width: 100%;
        box-sizing: border-box;

        padding: 42px 46px;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(12, 31, 53, 0.98),
                rgba(9, 38, 67, 0.94)
            );

        border: 1px solid rgba(56, 189, 248, 0.20);

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.30);

        margin-bottom: 42px;
    }

    .hero-icon {
        font-size: 42px;
        line-height: 1;
        margin-bottom: 16px;
    }

    .hero-title {
        font-size: 46px;
        line-height: 1.1;
        font-weight: 800;
        letter-spacing: -1.5px;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #60a5fa,
                #38bdf8
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin: 0;
    }

    .hero-subtitle {
        margin-top: 14px;

        color: #94a3b8;

        font-size: 16px;
        line-height: 1.7;
    }


    /* ========================================================
       SECTION
       ======================================================== */

    .section-title {
        color: #f8fafc;

        font-size: 24px;
        font-weight: 750;

        margin: 0 0 7px 0;
    }

    .section-description {
        color: #94a3b8;

        font-size: 14px;

        margin: 0 0 26px 0;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    label {
        color: #cbd5e1 !important;

        font-size: 14px !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="select"] > div {
        background: #0d1b2d !important;

        border: 1px solid #263a53 !important;

        border-radius: 12px !important;

        min-height: 44px;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #38bdf8 !important;
    }

    input {
        background: #0d1b2d !important;

        color: #f8fafc !important;

        border: 1px solid #263a53 !important;

        border-radius: 12px !important;
    }

    input:focus {
        border-color: #38bdf8 !important;
    }


    /* ========================================================
       BUTTON
       ======================================================== */

    .stButton {
        margin-top: 20px;
        margin-bottom: 8px;
    }

    .stButton > button {
        width: 100%;

        height: 56px;

        border: none;
        border-radius: 14px;

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #0ea5e9
            );

        color: #ffffff;

        font-size: 16px;
        font-weight: 700;

        box-shadow:
            0 12px 30px rgba(37, 99, 235, 0.25);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 18px 38px rgba(14, 165, 233, 0.30);
    }


    /* ========================================================
       RESULT CARD
       ======================================================== */

    .result-wrapper {
        width: 100%;
        margin-top: 34px;
        margin-bottom: 34px;
    }

    .result-card {
        width: 100%;
        box-sizing: border-box;

        padding: 38px 30px 34px 30px;

        border-radius: 24px;

        text-align: center;

        background:
            linear-gradient(
                135deg,
                rgba(11, 43, 72, 0.96),
                rgba(8, 31, 55, 0.96)
            );

        border: 1px solid rgba(56, 189, 248, 0.28);

        box-shadow:
            0 20px 55px rgba(0, 0, 0, 0.30);
    }

    .result-label {
        color: #94a3b8;

        font-size: 13px;
        font-weight: 600;

        letter-spacing: 4px;

        text-transform: uppercase;

        margin: 0 0 12px 0;
    }

    .result-price {
        color: #38bdf8;

        font-size: 52px;
        line-height: 1.15;

        font-weight: 800;

        margin: 0;
    }

    .result-note {
        color: #64748b;

        font-size: 13px;

        margin: 12px 0 0 0;
    }


    /* ========================================================
       SUMMARY
       ======================================================== */

    .summary-card {
        width: 100%;
        box-sizing: border-box;

        min-height: 96px;

        padding: 19px 20px;

        border-radius: 17px;

        background:
            rgba(13, 27, 45, 0.78);

        border: 1px solid rgba(148, 163, 184, 0.12);
    }

    .summary-value {
        color: #60a5fa;

        font-size: 18px;
        font-weight: 700;

        line-height: 1.35;

        margin: 0;
    }

    .summary-label {
        color: #64748b;

        font-size: 11px;
        font-weight: 600;

        letter-spacing: 1.5px;

        margin-top: 8px;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        width: 100%;

        text-align: center;

        color: #64748b;

        font-size: 12px;

        margin-top: 52px;

        padding-top: 24px;

        border-top:
            1px solid rgba(148, 163, 184, 0.10);
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 20px !important;
            padding-right: 20px !important;
        }

        .hero-card {
            padding: 30px 25px;
        }

        .hero-title {
            font-size: 36px;
        }

        .result-price {
            font-size: 42px;
        }

    }

    </style>
    """),
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    dedent("""
    <div class="hero-card">
        <div class="hero-icon">✈️</div>
        <div class="hero-title">AirFare AI</div>
        <div class="hero-subtitle">
            Intelligent Airline Ticket Price Prediction<br>
            Estimate your flight fare using machine learning.
        </div>
    </div>
    """),
    unsafe_allow_html=True
)


# ============================================================
# SECTION HEADER
# ============================================================

st.markdown(
    dedent("""
    <div class="section-title">
        🛫 Flight Information
    </div>

    <div class="section-description">
        Enter your flight details below to estimate the expected ticket price.
    </div>
    """),
    unsafe_allow_html=True
)


# ============================================================
# ROW 1
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    airline = st.selectbox(
        "Airline",
        [
            "AirAsia",
            "Air_India",
            "GO_FIRST",
            "Indigo",
            "SpiceJet",
            "Vistara"
        ]
    )


with col2:

    source_city = st.selectbox(
        "Source City",
        [
            "Bangalore",
            "Chennai",
            "Delhi",
            "Hyderabad",
            "Kolkata",
            "Mumbai"
        ]
    )


with col3:

    destination_city = st.selectbox(
        "Destination City",
        [
            "Bangalore",
            "Chennai",
            "Delhi",
            "Hyderabad",
            "Kolkata",
            "Mumbai"
        ]
    )


# ============================================================
# ROW 2
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    departure_time = st.selectbox(
        "Departure Time",
        [
            "Early_Morning",
            "Morning",
            "Afternoon",
            "Evening",
            "Night",
            "Late_Night"
        ]
    )


with col2:

    arrival_time = st.selectbox(
        "Arrival Time",
        [
            "Early_Morning",
            "Morning",
            "Afternoon",
            "Evening",
            "Night",
            "Late_Night"
        ]
    )


with col3:

    stops = st.selectbox(
        "Number of Stops",
        [
            "zero",
            "one",
            "two_or_more"
        ]
    )


# ============================================================
# ROW 3
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    flight_class = st.selectbox(
        "Class",
        [
            "Business",
            "Economy"
        ]
    )


with col2:

    duration = st.number_input(
        "Flight Duration (Hours)",
        min_value=0.5,
        max_value=50.0,
        value=2.5,
        step=0.1
    )


with col3:

    days_left = st.number_input(
        "Days Left Before Departure",
        min_value=1,
        max_value=365,
        value=15,
        step=1
    )


# ============================================================
# PREDICT BUTTON
# ============================================================

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

predict = st.button(
    "✈️  Predict Ticket Price"
)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    try:

        # ----------------------------------------------------
        # RAW INPUT
        # ----------------------------------------------------

        input_data = pd.DataFrame({
            "airline": [airline],
            "source_city": [source_city],
            "departure_time": [departure_time],
            "stops": [stops],
            "arrival_time": [arrival_time],
            "destination_city": [destination_city],
            "class": [flight_class],
            "duration": [duration],
            "days_left": [days_left]
        })


        # ----------------------------------------------------
        # CATEGORICAL COLUMNS
        # ----------------------------------------------------

        categorical_columns = [
            "airline",
            "source_city",
            "departure_time",
            "stops",
            "arrival_time",
            "destination_city",
            "class"
        ]


        # ----------------------------------------------------
        # ONE-HOT ENCODING
        # ----------------------------------------------------

        input_encoded = pd.get_dummies(
            input_data,
            columns=categorical_columns,
            drop_first=True
        )


        # ----------------------------------------------------
        # MATCH TRAINING FEATURES
        # ----------------------------------------------------

        input_encoded = input_encoded.reindex(
            columns=feature_columns,
            fill_value=0
        )


        # ----------------------------------------------------
        # SCALE NUMERICAL FEATURES
        # ----------------------------------------------------

        input_encoded[["duration", "days_left"]] = scaler.transform(
            input_encoded[["duration", "days_left"]]
        )


        # ----------------------------------------------------
        # PREDICT
        # ----------------------------------------------------

        prediction = model.predict(input_encoded)[0]

        prediction = max(0, prediction)


        # ====================================================
        # RESULT
        # ====================================================

        result_html = dedent(
            f"""
            <div class="result-wrapper">
                <div class="result-card">
                    <div class="result-label">
                        Estimated Ticket Price
                    </div>
                    <div class="result-price">
                        ₹{prediction:,.0f}
                    </div>
                    <div class="result-note">
                        Predicted using the trained Linear Regression model
                    </div>
                </div>
            </div>
            """
        )

        st.markdown(
            result_html,
            unsafe_allow_html=True
        )


        # ====================================================
        # FLIGHT SUMMARY
        # ====================================================

        st.markdown(
            dedent("""
            <div class="section-title">
                📋 Flight Summary
            </div>
            """),
            unsafe_allow_html=True
        )

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)


        with c1:

            st.markdown(
                dedent(
                    f"""
                    <div class="summary-card">
                        <div class="summary-value">
                            {airline}
                        </div>
                        <div class="summary-label">
                            AIRLINE
                        </div>
                    </div>
                    """
                ),
                unsafe_allow_html=True
            )


        with c2:

            st.markdown(
                dedent(
                    f"""
                    <div class="summary-card">
                        <div class="summary-value">
                            {source_city} → {destination_city}
                        </div>
                        <div class="summary-label">
                            ROUTE
                        </div>
                    </div>
                    """
                ),
                unsafe_allow_html=True
            )


        with c3:

            st.markdown(
                dedent(
                    f"""
                    <div class="summary-card">
                        <div class="summary-value">
                            {duration:.1f} hrs
                        </div>
                        <div class="summary-label">
                            DURATION
                        </div>
                    </div>
                    """
                ),
                unsafe_allow_html=True
            )


        with c4:

            st.markdown(
                dedent(
                    f"""
                    <div class="summary-card">
                        <div class="summary-value">
                            {days_left} days
                        </div>
                        <div class="summary-label">
                            DAYS LEFT
                        </div>
                    </div>
                    """
                ),
                unsafe_allow_html=True
            )


    except Exception as e:

        st.error(
            "Unable to generate the prediction."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    dedent("""
    <div class="footer">
        ✈️ AirFare AI &nbsp;•&nbsp;
        Machine Learning Ticket Price Prediction
        <br><br>
        Built with Python • Scikit-learn • Streamlit
    </div>
    """),
    unsafe_allow_html=True
)