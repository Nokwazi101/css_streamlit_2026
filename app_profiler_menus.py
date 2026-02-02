"""
Kwazi's Fiber Bliss - Recruitment Portal
Streamlit app for showcasing job opportunities and recruitment
Run with: streamlit run kfb_recruitment.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ===== PAGE CONFIGURATION =====
st.set_page_config(
    page_title="KFB Recruitment Portal",
    layout="wide",
    page_icon="🧶"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    .stApp {
        background-color: white;
        color: black;
    }
    .main-title {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .tagline {
        font-size: 1.2rem;
        text-align: center;
        font-style: italic;
        margin-bottom: 1.5rem;
        color: #333;
    }
    .sidebar-title {
        font-size: 1.5rem;
        color: #8b7462;
        font-weight: bold;
    }
    .job-card {
        background-color: #f8f8f8;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 5px solid #8b7462;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .urgent-badge {
        background-color: #ff6b6b;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin-left: 10px;
    }
    .apply-btn {
        background-color: #8b7462;
        color: white;
        border: none;
        padding: 8px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ===== COMPANY INFORMATION =====
COMPANY_NAME = "Kwazi's Fiber Bliss"
TAGLINE = "Love in every stitch, comfort in every thread"
FOUNDER_NAME = "Nokwazi Prudence Mbhele"
FOUNDED_YEAR = 2017
EMAIL = "careers@kfibrebliss.co.za"  # Changed to careers email
INSTAGRAM = "@K_FiberBliss"
WHATSAPP = "0662708613"
ARTICLE_URL = "https://vibeonline.co.za/academic/from-crochet-hooks-to-lab-coats-nokwazis-journey-is-pure-fire/"

# ===== JOB OPENINGS DATA =====
JOB_OPENINGS = {
    "Production & Crafting": [
        {
            "title": "Lead Crochet Artisan",
            "location": "Remote / Dondotha, KZN",
            "type": "Full-time",
            "salary": "R8,000 - R12,000",
            "urgent": True,
            "description": "Lead production of handmade fashion items. Must have 3+ years crochet experience.",
            "requirements": ["Advanced crochet skills", "Pattern creation ability", "Quality control", "Team leadership"]
        },
        {
            "title": "Junior Crochet Assistant",
            "location": "Dondotha, KZN",
            "type": "Part-time/Apprentice",
            "salary": "R3,000 - R5,000",
            "urgent": True,
            "description": "Learn and assist in crochet production. Training provided for beginners.",
            "requirements": ["Willingness to learn", "Basic handcraft skills", "Attention to detail", "Reliable transportation"]
        }
    ],
    "Business & Operations": [
        {
            "title": "Sales & Marketing Coordinator",
            "location": "Remote",
            "type": "Contract",
            "salary": "R6,000 - R9,000",
            "urgent": False,
            "description": "Handle social media, customer inquiries, and sales coordination.",
            "requirements": ["Social media savvy", "Customer service", "Basic admin skills", "Own smartphone/laptop"]
        },
        {
            "title": "Quality Control Specialist",
            "location": "Dondotha, KZN",
            "type": "Part-time",
            "salary": "R4,000 - R6,000",
            "urgent": False,
            "description": "Ensure all products meet quality standards before shipping.",
            "requirements": ["Attention to detail", "Knowledge of textiles", "Organizational skills"]
        }
    ],
    "Growth & Development": [
        {
            "title": "Business Development Intern",
            "location": "Remote",
            "type": "Internship",
            "salary": "Stipend + Commission",
            "urgent": True,
            "description": "Help expand business reach and explore new markets. Great for students.",
            "requirements": ["Business/ Marketing student", "Creative thinking", "Basic computer skills"]
        }
    ]
}

# ===== APPLICATION DATA =====
applications_data = pd.DataFrame({
    "Application ID": [f"KFB-APP{1000+i}" for i in range(8)],
    "Applicant": ["Sarah M.", "Jessica T.", "Emma R.", "Michael B.", "Patricia L.", 
                 "David K.", "Lisa W.", "Grace N."],
    "Position": ["Lead Crochet Artisan", "Sales Coordinator", "Junior Assistant", 
                 "Quality Control", "Business Intern", "Lead Crochet Artisan", 
                 "Junior Assistant", "Sales Coordinator"],
    "Status": ["Under Review", "Interview Scheduled", "New", "Rejected", 
               "Under Review", "New", "Interview Scheduled", "Under Review"],
    "Applied Date": pd.date_range(start="2024-01-01", periods=8, freq='5D')
})

# ===== CALCULATIONS =====
current_year = datetime.now().year
business_years = current_year - FOUNDED_YEAR
total_jobs = sum(len(jobs) for jobs in JOB_OPENINGS.values())
urgent_jobs = sum(1 for category in JOB_OPENINGS.values() for job in category if job.get('urgent', False))

# ===== SIDEBAR NAVIGATION =====
st.sidebar.markdown('<p class="sidebar-title">KFB Recruitment</p>', unsafe_allow_html=True)
st.sidebar.markdown(f'*{TAGLINE}*')

menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Welcome", "📋 Job Openings", "📝 Apply Now", "👥 Our Team", "📊 Applications", "🏢 About KFB"]
)

# ===== HEADER =====
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f'<h1 class="main-title">{COMPANY_NAME}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="tagline">Career Opportunities - Join Our Growing Family</p>', unsafe_allow_html=True)

st.image(
    "https://cdn-media.knitpro.eu/media/mageplaza/blog/post/brand/how-to-crochet-a-sweater-1.webp",
    caption=f"Building careers since {FOUNDED_YEAR}"
)

# ===== WELCOME PAGE =====
if menu == "🏠 Welcome":
    st.header("🚀 Join Kwazi's Fiber Bliss")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Openings", total_jobs)
    with col2:
        st.metric("Urgent Hiring", urgent_jobs)
    with col3:
        st.metric("Years Growing", business_years)
    
    st.subheader("Why Work With Us?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**🎯 Skill Development**")
        st.write("- Learn traditional and modern crochet techniques")
        st.write("- Business training provided")
        st.write("- Career growth opportunities")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**💝 Supportive Environment**")
        st.write("- Women-led business")
        st.write("- Family-friendly policies")
        st.write("- Flexible working arrangements")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**🌱 Community Impact**")
        st.write("- Create beautiful handmade products")
        st.write("- Support rural employment")
        st.write("- Be part of a growing success story")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Our Founder's Vision")
    st.write(f"*{FOUNDER_NAME}, Founder & CEO*")
    st.write("'I started Kwazi's Fiber Bliss not just as a business, but as a platform to empower others. From teaching young girls crochet to providing employment in our community, every stitch represents opportunity and growth.'")
    
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{ARTICLE_URL}" target="_blank">
            <button class="apply-btn">
                📖 Read Founder's Story
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# ===== JOB OPENINGS PAGE =====
elif menu == "📋 Job Openings":
    st.header("📋 Current Job Opportunities")
    
    # Create tabs for each job category
    tabs = st.tabs(list(JOB_OPENINGS.keys()))
    
    for i, (category, jobs) in enumerate(JOB_OPENINGS.items()):
        with tabs[i]:
            st.subheader(f"{category} Positions")
            
            for job in jobs:
                st.markdown('<div class="job-card">', unsafe_allow_html=True)
                
                # Job title with urgent badge
                title_html = f"**{job['title']}**"
                if job.get('urgent', False):
                    title_html += '<span class="urgent-badge">URGENT</span>'
                st.markdown(title_html, unsafe_allow_html=True)
                
                # Job details
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"📍 **Location:** {job['location']}")
                with col2:
                    st.write(f"📄 **Type:** {job['type']}")
                with col3:
                    st.write(f"💰 **Salary:** {job['salary']}")
                
                # Description
                st.write(f"**Description:** {job['description']}")
                
                # Requirements
                st.write("**Requirements:**")
                for req in job['requirements']:
                    st.write(f"- {req}")
                
                # Apply button
                if st.button(f"Apply for {job['title']}", key=f"apply_{job['title']}"):
                    st.session_state['selected_job'] = job['title']
                    st.switch_page = True  # This would navigate to Apply page
                    st.info(f"Scroll down to 'Apply Now' section to apply for {job['title']}")
                
                st.markdown('</div>', unsafe_allow_html=True)

# ===== APPLY NOW PAGE =====
elif menu == "📝 Apply Now":
    st.header("📝 Job Application Form")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Application form
        with st.form("job_application_form"):
            st.subheader("Personal Information")
            
            name = st.text_input("Full Name *")
            email = st.text_input("Email Address *")
            phone = st.text_input("Phone Number *")
            location = st.text_input("Current Location/Town *")
            
            st.subheader("Position Information")
            
            # Get all job titles for dropdown
            all_jobs = []
            for category in JOB_OPENINGS.values():
                for job in category:
                    all_jobs.append(job['title'])
            
            selected_position = st.selectbox(
                "Position Applying For *",
                ["Select a position"] + all_jobs
            )
            
            experience = st.selectbox(
                "Years of Relevant Experience *",
                ["No experience", "Less than 1 year", "1-2 years", "3-5 years", "5+ years"]
            )
            
            st.subheader("Additional Information")
            
            crochet_experience = st.selectbox(
                "Do you have crochet experience? *",
                ["No experience", "Beginner (self-taught)", "Intermediate", "Advanced", "Professional"]
            )
            
            availability = st.selectbox(
                "When can you start? *",
                ["Immediately", "Within 2 weeks", "Within 1 month", "Flexible"]
            )
            
            why_join = st.text_area("Why do you want to join Kwazi's Fiber Bliss? *")
            
            # File upload
            resume = st.file_uploader("Upload Resume/CV (PDF or DOC)", type=['pdf', 'doc', 'docx'])
            
            submitted = st.form_submit_button("Submit Application")
            
            if submitted:
                if name and email and phone and location and selected_position != "Select a position":
                    st.success(f"✅ Thank you {name}! Your application for {selected_position} has been submitted.")
                    st.info("We will contact you within 5-7 business days. For urgent inquiries, WhatsApp: 0662708613")
                else:
                    st.warning("Please fill in all required fields (*)")
    
    with col2:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**📞 Application Tips**")
        st.write("1. **Be specific** about your crochet experience")
        st.write("2. **Mention** if you have your own tools")
        st.write("3. **Share** why our mission resonates with you")
        st.write("4. **Include** portfolio photos if available")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("")
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**⏰ Application Process**")
        st.write("1. Submit this form")
        st.write("2. Initial phone screening")
        st.write("3. Skills assessment")
        st.write("4. Final interview")
        st.write("5. Offer & onboarding")
        st.markdown('</div>', unsafe_allow_html=True)

# ===== OUR TEAM PAGE =====
elif menu == "👥 Our Team":
    st.header("👥 Meet Our Team")
    
    st.subheader("Leadership")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**👑 Founder & CEO**")
        st.write(f"*{FOUNDER_NAME}*")
        st.write("MSc Microbiology Candidate")
        st.write("Crochet Artist since age 8")
        st.write("Business Owner since 2017")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**🎨 Head Artisan**")
        st.write("*Position Available*")
        st.write("Lead our production team")
        st.write("Train new artisans")
        st.write("Quality assurance")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**📱 Marketing Lead**")
        st.write("*Position Available*")
        st.write("Manage social media")
        st.write("Customer relationships")
        st.write("Sales strategy")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("Current Artisans")
    st.write("**Nolwandle Z.** - Ruffle Hat Specialist (2 years with KFB)")
    st.write("**Nqobile T.** - Bikini Sets Expert (1.5 years with KFB)")
    st.write("**Minenhle R.** - Youth Sets Creator (1 year with KFB)")
    st.write("**Sabathelihle Z.** - Beanie Specialist (New Apprentice)")
    
    st.markdown("---")
    st.subheader("Team Benefits")
    st.write("✅ **Flexible hours** - Work around your schedule")
    st.write("✅ **Skill development** - Free crochet training")
    st.write("✅ **Product discounts** - 50% off all KFB products")
    st.write("✅ **Commission bonuses** - Earn extra for high performance")
    st.write("✅ **Community support** - Be part of our family")

# ===== APPLICATIONS PAGE =====
elif menu == "📊 Applications":
    st.header("📊 Application Status Tracker")
    
    st.write("**For Applicants:** Check your application status here")
    
    # Search for application
    app_id = st.text_input("Enter your Application ID (e.g., KFB-APP1001)")
    
    if app_id:
        if app_id in applications_data["Application ID"].values:
            app_info = applications_data[applications_data["Application ID"] == app_id].iloc[0]
            
            st.markdown('<div class="job-card">', unsafe_allow_html=True)
            st.write(f"**Application ID:** {app_info['Application ID']}")
            st.write(f"**Applicant:** {app_info['Applicant']}")
            st.write(f"**Position:** {app_info['Position']}")
            st.write(f"**Status:** **{app_info['Status']}**")
            st.write(f"**Applied Date:** {app_info['Applied Date'].strftime('%d %B %Y')}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Status explanation
            if app_info['Status'] == "New":
                st.info("Your application has been received and is awaiting review.")
            elif app_info['Status'] == "Under Review":
                st.info("Your application is being reviewed by our team.")
            elif app_info['Status'] == "Interview Scheduled":
                st.success("Great news! Check your email for interview details.")
            elif app_info['Status'] == "Rejected":
                st.warning("Thank you for applying. We'll keep your details for future opportunities.")
        else:
            st.error("Application ID not found. Please check and try again.")
    
    st.markdown("---")
    st.subheader("Application Statistics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Applications", len(applications_data))
    with col2:
        under_review = len(applications_data[applications_data["Status"] == "Under Review"])
        st.metric("Under Review", under_review)
    with col3:
        interviews = len(applications_data[applications_data["Status"] == "Interview Scheduled"])
        st.metric("Interviews Scheduled", interviews)

# ===== ABOUT KFB PAGE =====
elif menu == "🏢 About KFB":
    st.header("🏢 About Kwazi's Fiber Bliss")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Our Story")
        st.write(f"Founded in {FOUNDED_YEAR} by {FOUNDER_NAME}, Kwazi's Fiber Bliss began as a passion project that grew into a thriving business. What started with crochet hooks and yarn has become a platform for empowerment, creativity, and community development.")
        
        st.write("**Our Mission:** To create beautiful handmade fashion while providing employment opportunities and skill development in our community.")
        
        st.write("**Our Vision:** To be a leading sustainable fashion brand that empowers artisans across South Africa.")
        
        st.markdown("---")
        st.subheader("What We Offer Employees")
        st.write("• **Fair wages** - Competitive pay for skilled work")
        st.write("• **Flexible work** - Remote and local options available")
        st.write("• **Training** - From beginner to expert level")
        st.write("• **Growth** - Opportunities for advancement")
        st.write("• **Community** - Supportive team environment")
    
    with col2:
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**📍 Location**")
        st.write("Headquarters: Ward 9, Dondotha")
        st.write("uMfolozi Local Municipality")
        st.write("KwaZulu-Natal, South Africa")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="job-card">', unsafe_allow_html=True)
        st.write("**📞 Contact HR**")
        st.write(f"Email: {EMAIL}")
        st.write(f"WhatsApp: {WHATSAPP}")
        st.write("Hours: Mon-Fri, 9am-5pm")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <a href="{ARTICLE_URL}" target="_blank">
            <button class="apply-btn" style="width:100%;">
                🏆 Read Our Feature in Vibe Online
            </button>
        </a>
        """, unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.write(f"© {FOUNDED_YEAR}-{current_year} {COMPANY_NAME}")
with footer_col2:
    st.write("Equal Opportunity Employer")
with footer_col3:
    st.write("Made with ❤️ in South Africa")

# ===== RUN INSTRUCTIONS =====
st.sidebar.markdown("---")
st.sidebar.caption("""
**Contact HR:**
📧 careers@kfibrebliss.co.za
📱 066 270 8613
""")