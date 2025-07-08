# OPTION 1: Streamlit Web App (Recommended - Easiest to Deploy)
# Save this as: advisee_matrix_streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import json

class AdviseeMatrixWeb:
    def __init__(self):
        if 'student_info' not in st.session_state:
            st.session_state.student_info = {
                'first_name': '',
                'middle_initial': '',
                'surname': '',
                'student_id': '',
                'contact_no': '',
                'email': '',
                'academic_year': str(datetime.now().year),
                'semester': 'Fall',
                'graduation_term': ''
            }
        
        if 'current_major' not in st.session_state:
            st.session_state.current_major = None
            
        if 'course_entries' not in st.session_state:
            st.session_state.course_entries = {}
            
        self.setup_course_database()
        self.setup_major_requirements()

    def setup_course_database(self):
        """Initialize the course database"""
        self.course_data = {
            'BIOL1020': {'name': 'Diversity of Life I', 'credits': 3, 'level': 1, 'type': 'core'},
            'BIOL1025': {'name': 'Diversity of Life II', 'credits': 3, 'level': 1, 'type': 'core'},
            'BIOC1015': {'name': 'Intro. To Biochemistry', 'credits': 3, 'level': 1, 'type': 'core'},
            'BIOL1030': {'name': 'Introduction to Genetics', 'credits': 3, 'level': 1, 'type': 'core'},
            'BIOL2373': {'name': 'Skills for Biologists', 'credits': 3, 'level': 2, 'type': 'core'},
            'BIOC2365': {'name': 'Primary Metabolism', 'credits': 3, 'level': 2, 'type': 'elective'},
            'BIOC2366': {'name': 'Protein Biochemistry', 'credits': 3, 'level': 2, 'type': 'elective'},
            'BIOC2370': {'name': 'Cell Signals', 'credits': 3, 'level': 2, 'type': 'elective'},
            'BIOC2371': {'name': 'Molecular Techniques', 'credits': 3, 'level': 2, 'type': 'elective'},
            'BIOL3XXX': {'name': 'Level 3 Biology Elective', 'credits': 3, 'level': 3, 'type': 'elective'},
            'BIOC3XXX': {'name': 'Level 3 Biochemistry Elective', 'credits': 3, 'level': 3, 'type': 'elective'},
            'ECOL3XXX': {'name': 'Level 3 Ecology Elective', 'credits': 3, 'level': 3, 'type': 'elective'},
            'MICR3XXX': {'name': 'Level 3 Microbiology Elective', 'credits': 3, 'level': 3, 'type': 'elective'},
        }

    def setup_major_requirements(self):
        """Setup major requirements structure"""
        self.major_requirements = {
            'BIOL': {
                'name': 'BSc Biology Major',
                'total_credits': 90,
                'requirements': [
                    {
                        'section': 'Level 1 Courses',
                        'required_credits': 24,
                        'courses': [
                            {'code': 'BIOL1020', 'credits': 3, 'required': True},
                            {'code': 'BIOL1025', 'credits': 3, 'required': True},
                            {'code': 'BIOC1015', 'credits': 3, 'required': True},
                            {'code': 'BIOL1030', 'credits': 3, 'required': True},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False}
                        ]
                    },
                    {
                        'section': 'Level 2 Major Courses',
                        'required_credits': 30,
                        'courses': [
                            {'code': 'BIOL2373', 'credits': 3, 'required': True},
                            {'code': 'BIOC2365', 'credits': 3, 'required': False},
                            {'code': 'BIOC2366', 'credits': 3, 'required': False},
                            {'code': 'BIOC2370', 'credits': 3, 'required': False},
                            {'code': 'BIOC2371', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False}
                        ]
                    },
                    {
                        'section': 'Level 3 Major Courses',
                        'required_credits': 36,
                        'courses': [
                            {'code': 'BIOL3XXX', 'credits': 3, 'required': False},
                            {'code': 'BIOL3XXX', 'credits': 3, 'required': False},
                            {'code': 'BIOL3XXX', 'credits': 3, 'required': False},
                            {'code': 'BIOL3XXX', 'credits': 3, 'required': False},
                            {'code': 'BIOC3XXX', 'credits': 3, 'required': False},
                            {'code': 'BIOC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ECOL3XXX', 'credits': 3, 'required': False},
                            {'code': 'MICR3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False}
                        ]
                    }
                ]
            },
            'BIOC': {
                'name': 'BSc Biochemistry Major',
                'total_credits': 90,
                'requirements': [
                    {
                        'section': 'Level 1 Courses',
                        'required_credits': 24,
                        'courses': [
                            {'code': 'BIOL1020', 'credits': 3, 'required': True},
                            {'code': 'BIOL1025', 'credits': 3, 'required': True},
                            {'code': 'BIOC1015', 'credits': 3, 'required': True},
                            {'code': 'BIOL1030', 'credits': 3, 'required': True},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC1XXX', 'credits': 3, 'required': False}
                        ]
                    },
                    {
                        'section': 'Level 2 Major Courses',
                        'required_credits': 30,
                        'courses': [
                            {'code': 'BIOC2365', 'credits': 3, 'required': True},
                            {'code': 'BIOC2366', 'credits': 3, 'required': True},
                            {'code': 'BIOC2370', 'credits': 3, 'required': True},
                            {'code': 'BIOC2371', 'credits': 3, 'required': True},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC2XXX', 'credits': 3, 'required': False}
                        ]
                    },
                    {
                        'section': 'Level 3 Major Courses',
                        'required_credits': 36,
                        'courses': [
                            {'code': 'BIOC3XXX', 'credits': 3, 'required': True},
                            {'code': 'BIOC3XXX', 'credits': 3, 'required': True},
                            {'code': 'BIOC3XXX', 'credits': 3, 'required': True},
                            {'code': 'BIOC3XXX', 'credits': 3, 'required': True},
                            {'code': 'BIOL3XXX', 'credits': 3, 'required': False},
                            {'code': 'BIOL3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False},
                            {'code': 'ELEC3XXX', 'credits': 3, 'required': False}
                        ]
                    }
                ]
            }
        }

    def calculate_quality_points(self, grade, credits):
        """Calculate quality points based on grade and credits"""
        grade_points = {
            'A+': 4.3, 'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D': 1.0, 'F': 0.0, 'P': 0.0, 'R': 0.0
        }
        return grade_points.get(grade, 0.0) * credits

    def run_streamlit_app(self):
        """Main Streamlit application"""
        st.set_page_config(
            page_title="AdviseeMatrix - Degree Planning Tool",
            page_icon="🎓",
            layout="wide"
        )

        st.title("🎓 AdviseeMatrix - Degree Planning Tool")
        st.markdown("---")

        # Sidebar for student information
        with st.sidebar:
            st.header("👤 Student Information")
            
            st.session_state.student_info['first_name'] = st.text_input(
                "First Name", 
                value=st.session_state.student_info['first_name']
            )
            st.session_state.student_info['middle_initial'] = st.text_input(
                "Middle Initial", 
                value=st.session_state.student_info['middle_initial']
            )
            st.session_state.student_info['surname'] = st.text_input(
                "Surname", 
                value=st.session_state.student_info['surname']
            )
            st.session_state.student_info['student_id'] = st.text_input(
                "Student ID", 
                value=st.session_state.student_info['student_id']
            )
            st.session_state.student_info['contact_no'] = st.text_input(
                "Contact Number", 
                value=st.session_state.student_info['contact_no']
            )
            st.session_state.student_info['email'] = st.text_input(
                "Email", 
                value=st.session_state.student_info['email']
            )
            st.session_state.student_info['academic_year'] = st.text_input(
                "Academic Year", 
                value=st.session_state.student_info['academic_year']
            )
            st.session_state.student_info['semester'] = st.selectbox(
                "Semester", 
                ['Fall', 'Winter', 'Spring', 'Summer'],
                index=['Fall', 'Winter', 'Spring', 'Summer'].index(st.session_state.student_info['semester'])
            )
            st.session_state.student_info['graduation_term'] = st.text_input(
                "Expected Graduation", 
                value=st.session_state.student_info['graduation_term']
            )

        # Main content area
        col1, col2 = st.columns([2, 1])

        with col1:
            st.header("📚 Major Selection & Course Planning")
            
            # Major selection
            major_options = ['Select a Major'] + [f"{key} - {value['name']}" for key, value in self.major_requirements.items()]
            selected_major_display = st.selectbox("Choose your major:", major_options)
            
            if selected_major_display != 'Select a Major':
                major_key = selected_major_display.split(' - ')[0]
                st.session_state.current_major = major_key
                
                # Display major requirements
                major_data = self.major_requirements[major_key]
                st.subheader(f"📋 {major_data['name']} Requirements")
                
                # Course planning interface
                for req_section in major_data['requirements']:
                    with st.expander(f"{req_section['section']} (Required: {req_section['required_credits']} credits)", expanded=True):
                        
                        # Create a form for this section
                        for i, course in enumerate(req_section['courses']):
                            col_code, col_name, col_credits, col_grade, col_status = st.columns([2, 3, 1, 1, 2])
                            
                            row_key = f"{req_section['section']}_{i}"
                            
                            # Initialize session state for this course if not exists
                            if row_key not in st.session_state.course_entries:
                                st.session_state.course_entries[row_key] = {
                                    'code': course['code'] if not ('ELEC' in course['code'] or 'XXX' in course['code']) else '',
                                    'credits': course['credits'],
                                    'grade': '',
                                    'status': 'Not Taken'
                                }
                            
                            with col_code:
                                if 'ELEC' in course['code'] or 'XXX' in course['code']:
                                    st.session_state.course_entries[row_key]['code'] = st.text_input(
                                        "Course Code", 
                                        value=st.session_state.course_entries[row_key]['code'],
                                        key=f"code_{row_key}",
                                        placeholder="Enter course"
                                    )
                                else:
                                    st.text_input(
                                        "Course Code", 
                                        value=course['code'],
                                        key=f"code_{row_key}",
                                        disabled=True
                                    )
                                    st.session_state.course_entries[row_key]['code'] = course['code']
                            
                            with col_name:
                                course_code = st.session_state.course_entries[row_key]['code']
                                course_name = self.course_data.get(course_code, {}).get('name', 'Custom Course')
                                st.text_input(
                                    "Course Name", 
                                    value=course_name,
                                    key=f"name_{row_key}",
                                    disabled=True
                                )
                            
                            with col_credits:
                                st.session_state.course_entries[row_key]['credits'] = st.number_input(
                                    "Credits", 
                                    min_value=0,
                                    max_value=6,
                                    value=st.session_state.course_entries[row_key]['credits'],
                                    key=f"credits_{row_key}"
                                )
                            
                            with col_grade:
                                grade_options = [''] + ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F', 'P', 'R']
                                st.session_state.course_entries[row_key]['grade'] = st.selectbox(
                                    "Grade", 
                                    grade_options,
                                    index=grade_options.index(st.session_state.course_entries[row_key]['grade']) if st.session_state.course_entries[row_key]['grade'] in grade_options else 0,
                                    key=f"grade_{row_key}"
                                )
                            
                            with col_status:
                                status_options = ['Not Taken', 'Completed', 'In Progress']
                                st.session_state.course_entries[row_key]['status'] = st.selectbox(
                                    "Status", 
                                    status_options,
                                    index=status_options.index(st.session_state.course_entries[row_key]['status']),
                                    key=f"status_{row_key}"
                                )

        with col2:
            st.header("📊 Progress Summary")
            
            if st.session_state.current_major:
                # Calculate progress
                major_data = self.major_requirements[st.session_state.current_major]
                overall_credits = 0
                overall_qp = 0
                
                for req_section in major_data['requirements']:
                    section_credits = 0
                    section_qp = 0
                    
                    st.subheader(req_section['section'])
                    
                    for i in range(len(req_section['courses'])):
                        row_key = f"{req_section['section']}_{i}"
                        if row_key in st.session_state.course_entries:
                            entry = st.session_state.course_entries[row_key]
                            if entry['status'] == 'Completed' and entry['grade']:
                                credits = entry['credits']
                                qp = self.calculate_quality_points(entry['grade'], credits)
                                section_credits += credits
                                section_qp += qp
                    
                    section_gpa = section_qp / section_credits if section_credits > 0 else 0.0
                    progress = (section_credits / req_section['required_credits']) * 100
                    
                    st.metric(
                        label="Credits", 
                        value=f"{section_credits}/{req_section['required_credits']}",
                        delta=f"{progress:.1f}% complete"
                    )
                    st.metric(
                        label="Section GPA", 
                        value=f"{section_gpa:.2f}"
                    )
                    
                    overall_credits += section_credits
                    overall_qp += section_qp
                    
                    st.markdown("---")
                
                # Overall summary
                overall_gpa = overall_qp / overall_credits if overall_credits > 0 else 0.0
                total_required = major_data['total_credits']
                overall_progress = (overall_credits / total_required) * 100
                
                st.subheader("🎯 Overall Summary")
                st.metric(
                    label="Total Credits", 
                    value=f"{overall_credits}/{total_required}",
                    delta=f"{overall_progress:.1f}% complete"
                )
                st.metric(
                    label="Overall GPA", 
                    value=f"{overall_gpa:.2f}"
                )
                
                # Progress bar
                st.progress(overall_progress / 100)
                
                if overall_progress >= 100:
                    st.success("🎓 Congratulations! Degree requirements completed!")
                elif overall_progress >= 75:
                    st.info(f"📚 Almost there! {total_required - overall_credits} credits remaining.")
                else:
                    st.warning(f"📖 Keep going! {total_required - overall_credits} credits remaining.")

        # Declaration form section
        st.markdown("---")
        if st.button("📄 Generate Declaration Form", type="primary"):
            if st.session_state.current_major:
                self.generate_declaration_form()
            else:
                st.error("Please select a major first!")

    def generate_declaration_form(self):
        """Generate declaration form"""
        st.subheader("📄 Declaration of Major Form")
        
        with st.container():
            st.markdown(f"""
            <div style='border: 2px solid #333; padding: 20px; margin: 20px 0;'>
                <h3 style='text-align: center; margin-bottom: 30px;'>DECLARATION OF MAJOR FORM</h3>
                
                <p><strong>Academic Year:</strong> {st.session_state.student_info['academic_year']}</p>
                <p><strong>Semester:</strong> {st.session_state.student_info['semester']}</p>
                <p><strong>Student ID:</strong> {st.session_state.student_info['student_id']}</p>
                <p><strong>Name:</strong> {st.session_state.student_info['first_name']} {st.session_state.student_info['middle_initial']} {st.session_state.student_info['surname']}</p>
                <p><strong>Contact No:</strong> {st.session_state.student_info['contact_no']}</p>
                <p><strong>Email:</strong> {st.session_state.student_info['email']}</p>
                
                <br>
                <p><strong>I intend to graduate at the end of:</strong> {st.session_state.student_info['graduation_term']}</p>
                <p><strong>Declaring Major in:</strong> {self.major_requirements[st.session_state.current_major]['name']}</p>
                
                <br><br>
                <p>Student Signature: ___________________________ Date: ___________</p>
                <br>
                <p>Academic Advisor Signature: ___________________________ Date: ___________</p>
                <br>
                <p>Department Approval: ___________________________ Date: ___________</p>
                
                <p style='text-align: center; margin-top: 30px; font-size: 12px;'>
                    Generated by AdviseeMatrix on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                </p>
            </div>
            """, unsafe_allow_html=True)

# Initialize and run the app
def main():
    app = AdviseeMatrixWeb()
    app.run_streamlit_app()

if __name__ == "__main__":
    main()

# =============================================================================
# DEPLOYMENT INSTRUCTIONS
# =============================================================================

"""
OPTION 1: Streamlit Cloud (FREE & EASIEST)
==========================================

1. Save the code above as 'advisee_matrix_streamlit.py'

2. Create a requirements.txt file with:
   streamlit
   pandas
   numpy

3. Upload both files to a GitHub repository

4. Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path to: advisee_matrix_streamlit.py
   - Click "Deploy"

5. Your app will be live at: https://[username]-[repo-name]-[branch]-[hash].streamlit.app/

6. Share this URL with anyone!

To run locally first:
pip install streamlit pandas numpy
streamlit run advisee_matrix_streamlit.py

=============================================================================

OPTION 2: Google Colab with Ngrok (Quick sharing from Colab)
===========================================================

# Run this in Google Colab for temporary public URL:

!pip install streamlit pyngrok
!ngrok authtoken YOUR_NGROK_TOKEN  # Get free token from ngrok.com

# Save the streamlit code to a file
with open('app.py', 'w') as f:
    f.write('''[PASTE THE STREAMLIT CODE HERE]''')

# Run the app with public URL
import subprocess
from pyngrok import ngrok
import threading

def run_streamlit():
    subprocess.run(['streamlit', 'run', 'app.py', '--server.port', '8501'])

thread = threading.Thread(target=run_streamlit)
thread.start()

# Create public URL
public_url = ngrok.connect(8501)
print(f"Public URL: {public_url}")

=============================================================================

OPTION 3: Heroku (More permanent, free tier available)
=====================================================

1. Create these files:

   app.py (the streamlit code above)
   
   requirements.txt:
   streamlit
   pandas
   numpy
   
   setup.sh:
   mkdir -p ~/.streamlit/
   echo "[server]" > ~/.streamlit/config.toml
   echo "port = $PORT" >> ~/.streamlit/config.toml
   echo "enableCORS = false" >> ~/.streamlit/config.toml
   echo "headless = true" >> ~/.streamlit/config.toml
   
   Procfile:
   web: sh setup.sh && streamlit run app.py

2. Deploy to Heroku:
   - Install Heroku CLI
   - heroku create your-app-name
   - git add .
   - git commit -m "Deploy AdviseeMatrix"
   - git push heroku main

3. Your app will be at: https://your-app-name.herokuapp.com

=============================================================================

OPTION 4: Replit (Easiest for beginners)
========================================

1. Go to replit.com
2. Create new Python project
3. Paste the streamlit code
4. Add to requirements.txt: streamlit, pandas, numpy
5. Click "Run"
6. Click "Open in new tab" to get shareable URL

=============================================================================

RECOMMENDED: Start with Option 1 (Streamlit Cloud) - it's free, reliable, 
and gives you a permanent URL to share!
"""