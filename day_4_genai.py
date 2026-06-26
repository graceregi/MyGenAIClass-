import streamlit as st
from  google import genai;
import json
from google.genai import types 
from pydantic import BaseModel

st.set_page_config(
    page_title="AI Used Car Advisor",
    page_icon="🚗",
    layout="wide"
)
system_instruction="""You are CarSense AI, an expert Used Car Advisor with over 20 years of experience in the Indian used car market. \
        Your objective is to help users buy the best used car based on their requirements by providing accurate, practical, and unbiased recommendations.\
        Analyze the user's requirements based on: \
        - Budget \
        - City/Location
        - Fuel Type
        - Transmission
        - Family Size
        - Primary Usage (City/Highway/Mixed)
        - Annual Running
        - Mileage Preference
        - Safety Preference
        - Maintenance Budget
        - Resale Value
        - Boot Space
        - Comfort
        - Reliability
        ## Data Requirements
        Always use the latest available market information.
        Prioritize:
        - Current used car market prices
        - Current resale values
        - Current ownership trends
        - Current maintenance estimates
        Recommendations must be relevant to the user's city or nearby cities.
        For example:
        If the user is in Coimbatore, prioritize listings, pricing, and market trends from:
        - Coimbatore
        - Pollachi
        - Tiruppur
        - Erode
        - Salem (if required)
        Do NOT use prices from other states unless no local information is available.
        Mention that prices may vary slightly based on:
        - Variant
        - Year
        - Kilometers driven
        - Service history
        - Number of owners
        ## Trusted Sources
        Prefer information that is commonly available from reputable automobile marketplaces and manufacturers.
        Avoid relying on unreliable classifieds, forums, social media posts, or unverified pricing.
        Do not mention websites unless the user specifically asks where to buy.
        ## Recommendation Rules
        Recommend exactly 3 cars.
        For each recommendation include:
        - Car Name
        - Recommended Model Year
        - Expected Price Range
        - Mileage
        - Maintenance Cost
        - Resale Value
        - Reliability Rating
        - Safety Rating
        - Suitable For
        - Pros
        - Cons
        - Why this car is recommended
        ## Buying Advice
        Mention:
        - Things to inspect before buying
        - Common issues for that model
        - Fair negotiation range
        - Estimated yearly maintenance cost
        ## Response Style
        Be concise.
        Avoid marketing language.
        Be honest.
        If a car has known issues, clearly mention them.
        Never recommend a car that exceeds the users budget unless explicitly requested.
        If no suitable car exists within the budget, explain why and recommend the closest alternatives.
        Always personalize recommendations based on the user city and requirements.
        Never invent specifications or prices.
        If you are uncertain about current market pricing, clearly state that the price is an estimate.
        Always recommend the car you would personally choose and explain why.
        if user has not provided enough information, ask for clarification before making recommendations.
        if anything other than cars is asked tell them  that you are a used car advisor and can only provide information about used cars.
        Dont give any other information other than  cars."""
robo = genai.Client(api_key="MY_API")
mychat = robo.chats.create(
        model="gemini-3.1-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction
        )
    )


# ------------------------
# CSS
# ------------------------

st.markdown("""
<style>

/* ---------- Main Background ---------- */

.stApp{
    background-image: linear-gradient(to bottom, #a8aff9, #8c93f5, #7077ef, #535be8, #2f3ddf);
}

/* ---------- Hide Streamlit Header ---------- */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* ---------- Hero ---------- */

.hero{
    background: linear-gradient(135deg,#0F172A,#2563EB);
    color:white;
    padding:50px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 20px 40px rgba(0,0,0,0.18);
    margin-bottom:30px;
}

.hero h1{
    font-size:52px;
    margin-bottom:12px;
}

.hero p{
    font-size:20px;
    opacity:.9;
}

/* ---------- Sidebar/Form ---------- */

[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius:20px;
}

/* ---------- Input Controls ---------- */

.stTextInput input,
.stNumberInput input,
.stSelectbox div,
.stSlider{
    border-radius:12px !important;
}

/* ---------- Button ---------- */

.stButton button{

    width:100%;
    height:55px;

    border:none;

    border-radius:14px;

    background:linear-gradient(135deg,#2563EB,#1D4ED8);

    color:white;

    font-size:18px;

    font-weight:bold;

    transition:.3s;

    box-shadow:0 10px 25px rgba(37,99,235,.35);

}

.stButton button:hover{

    transform:translateY(-3px);

    box-shadow:0 20px 35px rgba(37,99,235,.45);

}

/* ---------- Recommendation Card ---------- */

.card{

    background:rgba(255,255,255,.75);

    backdrop-filter:blur(14px);

    border-radius:24px;

    padding:25px;

    border:1px solid rgba(255,255,255,.4);

    box-shadow:0 20px 35px rgba(0,0,0,.08);

    transition:.35s;

    min-height:420px;

}

.card:hover{

    transform:translateY(-8px);

    box-shadow:0 30px 45px rgba(0,0,0,.15);

}

/* ---------- Car Name ---------- */

.recommend-title{

    color:#1E40AF;

    font-size:26px;

    font-weight:700;

    margin-bottom:15px;

}

/* ---------- Metrics ---------- */

.metric{

    background:#F8FAFC;

    padding:10px;

    border-radius:12px;

    margin-top:10px;

    font-size:15px;

}

/* ---------- Recommendation Reason ---------- */

.reason{

    margin-top:18px;

    padding:15px;

    border-left:5px solid #2563EB;

    background:#EFF6FF;

    border-radius:10px;

}

/* ---------- Chat ---------- */

[data-testid="stChatMessage"]{

    border-radius:18px;

    padding:12px;

}

/* ---------- Divider ---------- */

hr{

    border:none;

    height:1px;

    background:#E2E8F0;

    margin-top:18px;

    margin-bottom:18px;

}

/* ---------- Section Heading ---------- */

h2,h3{

    color:#1E3A8A;

    font-weight:700;

}

/* ---------- Smooth Animations ---------- */

*{

    transition:.2s ease;

}

</style>
""", unsafe_allow_html=True)

# ------------------------
# Hero
# ------------------------

st.markdown("""
<div class="hero">
<h1>🚗 IntelliCar AI - Used Car Advisor</h1>
<p>Find the perfect used car with AI recommendations.</p>
</div>
""", unsafe_allow_html=True)

# ------------------------
# Layout
# ------------------------

left, right = st.columns([1,2])

# ------------------------
# LEFT PANEL
# ------------------------

with left:

    st.subheader("Tell us your needs")

    budget = st.number_input(
        "Budget (₹)",
        100000,
        5000000,
        700000,
        step=50000
    )

    fuel = st.selectbox(
        "Fuel Type",
        ["Any","Petrol","Diesel","CNG","EV"]
    )

    transmission = st.selectbox(
        "Transmission",
        ["Automatic","Manual"]
    )

    family = st.selectbox(
        "Family Members",
        [2,3,4,5,6,7]
    )

    city = st.text_input(
        "City",
        "Coimbatore"
    )

    usage = st.selectbox(
        "Usage",
        [
            "Mostly City",
            "Mostly Highway",
            "Mixed"
        ]
    )

    mileage = st.slider(
        "Mileage Importance",
        1,
        5,
        4
    )

    recommend = st.button("🚗 Find Cars")

# ------------------------
# RIGHT PANEL
# ------------------------
user_prompt = f"""
    Recommend the best used cars for the following requirements.

    Budget: ₹{budget}

    City: {city}

    Fuel Type: {fuel}

    Transmission: {transmission}

    Family Members: {family}

    Usage: {usage}

    Mileage Importance: {mileage}/5

    Please recommend the top 3 used cars.
    """


class Car(BaseModel):
    car_name: str
    expected_price_range: str
    mileage: str
    maintenance_cost: str
    resale_value: str
    why_this_car_is_recommended: str

with right:

    st.subheader("AI Recommendations")

    if recommend:
        response = robo.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=user_prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                system_instruction=system_instruction,
                response_schema=list[Car]
                )
            )
        cars = json.loads(response.text)

        cols = st.columns(3)

        for col, car in zip(cols, cars):

            with col:

                st.markdown(f"""
                <div class="card">

                <div class="recommend-title">
                🚗 {car['car_name']}
                </div>

                <hr>

                <div class="metric">
                💰 <b>Price:</b> {car['expected_price_range']}
                </div>

                <div class="metric">
                ⛽ <b>Mileage:</b> {car['mileage']}
                </div>

                <div class="metric">
                🔧 <b>Maintenance:</b> {car['maintenance_cost']}
                </div>

                <div class="metric">
                📈 <b>Resale:</b> {car['resale_value']}
                </div>

                <hr>
                <div class="reason">
                <b>Why this car?</b>

                <br><br>

                {car['why_this_car_is_recommended']}
                </div>
                </div>
                """, unsafe_allow_html=True)

        else:

            st.info("👈 Fill in your preferences and click **Find Cars**.")

# ------------------------
# CHAT
# ------------------------

st.markdown("---")

st.subheader("💬 Ask the AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask anything about used cars...")



if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = mychat.send_message(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response.text
        }
    )

    with st.chat_message("assistant"):
        st.write(response.text)
