
import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

.main {
    padding-top: 20px;
}

.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    margin-bottom: 30px;
}

.section {
    font-size: 22px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
}

.result-box {
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    margin-top: 20px;
}

.placed {
    background-color: #d4edda;
    border: 2px solid #28a745;
}

.not-placed {
    background-color: #f8d7da;
    border: 2px solid #dc3545;
}

.result-title {
    font-size: 28px;
    font-weight: 700;
}

.probability {
    font-size: 19px;
    margin-top: 10px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# LOAD MODEL AND PREPROCESSOR
# ---------------------------------------------------------
try:
   model = joblib.load("models/placement_model.pkl")
   preprocessor = joblib.load("models/placement_preprocessor.pkl")
except Exception as e:
    st.error("Model files could not be loaded.")
    st.write(e)
    st.stop()


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="title">🎓 Student Placement Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict whether a student is likely to be placed based on academic and skill-related information.</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------------------------------------------------
# STUDENT DETAILS
# ---------------------------------------------------------
st.markdown(
    '<div class="section">👤 Student Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    student_id = st.number_input(
    "Student ID",
    min_value=1,
    value=1,
    step=1
)
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=30,
        value=20,
        step=1
    )

    degree = st.selectbox(
        "Degree",
        ["BCA", "BE", "BSc", "BTech"]
    )

with col2:
    branch = st.selectbox(
        "Branch",
        ["AI", "CS", "DS", "Electrical", "IT", "Mechanical"]
    )

    backlogs = st.number_input(
        "Number of Backlogs",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    internships = st.number_input(
        "Number of Internships",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )


# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------
st.markdown(
    '<div class="section">💡 Skills & Experience</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    certifications = st.number_input(
        "Number of Certifications",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )

    coding_skills = st.slider(
        "Coding Skills (1–10)",
        min_value=1,
        max_value=10,
        value=7
    )

with col2:
    communication_skills = st.slider(
        "Communication Skills (1–10)",
        min_value=1,
        max_value=10,
        value=7
    )

    projects = st.number_input(
        "Number of Projects",
        min_value=0,
        max_value=20,
        value=2,
        step=1
    )


# ---------------------------------------------------------
# ACADEMIC DETAILS
# ---------------------------------------------------------
st.markdown(
    '<div class="section">📚 Academic Performance</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    aptitude_score = st.number_input(
        "Aptitude Score",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=1.0
    )

with col2:
    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=8.0,
        step=0.01
    )


st.divider()


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
if st.button(
    "🔮 Predict Placement",
    use_container_width=True
):

    # Create input dataframe
    input_data = pd.DataFrame({
        "student_id": [student_id],
        "gender": [gender],
        "age": [age],
        "degree": [degree],
        "branch": [branch],
        "backlogs": [backlogs],
        "internships": [internships],
        "certifications": [certifications],
        "coding_skills": [coding_skills],
        "communication_skills": [communication_skills],
        "projects": [projects],
        "aptitude_score": [aptitude_score],
        "cgpa": [cgpa]
    })

    try:

        # Apply same preprocessing used during training
        input_processed = preprocessor.transform(input_data)

        # Prediction
        prediction = model.predict(input_processed)[0]

        # Probability
        probabilities = model.predict_proba(input_processed)[0]

        probability_not_placed = probabilities[0] * 100
        probability_placed = probabilities[1] * 100


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        st.markdown(
            '<div class="section">📊 Prediction Result</div>',
            unsafe_allow_html=True
        )

        if prediction == 1:

            st.markdown(
                f"""
                <div class="result-box placed">
                    <div class="result-title">
                        ✅ PLACED
                    </div>
                    <div class="probability">
                        The student is predicted to be <b>PLACED</b>.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="result-box not-placed">
                    <div class="result-title">
                        ❌ NOT PLACED
                    </div>
                    <div class="probability">
                        The student is predicted to be <b>NOT PLACED</b>.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # -------------------------------------------------
        # PROBABILITY
        # -------------------------------------------------

        st.subheader("Placement Probability")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Probability of Placement",
                f"{probability_placed:.2f}%"
            )
            st.progress(
                int(probability_placed)
            )

        with col2:
            st.metric(
                "Probability of Not Placement",
                f"{probability_not_placed:.2f}%"
            )
            st.progress(
                int(probability_not_placed)
            )


        # -------------------------------------------------
        # INPUT SUMMARY
        # -------------------------------------------------

        st.subheader("Student Summary")

        summary = pd.DataFrame({
            "Parameter": [
                "Gender",
                "Age",
                "Degree",
                "Branch",
                "Backlogs",
                "Internships",
                "Certifications",
                "Coding Skills",
                "Communication Skills",
                "Projects",
                "Aptitude Score",
                "CGPA"
            ],
            "Value": [
                gender,
                age,
                degree,
                branch,
                backlogs,
                internships,
                certifications,
                coding_skills,
                communication_skills,
                projects,
                aptitude_score,
                cgpa
            ]
        })

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error("Prediction failed.")

        st.write(
            "Please check that the input columns match the model's training columns."
        )

        st.exception(e)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        🎓 Student Placement Prediction System<br>
        Machine Learning Project using Random Forest
    </div>
    """,
    unsafe_allow_html=True
)
