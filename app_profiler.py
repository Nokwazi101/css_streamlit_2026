"""
Kwazi's Fiber Bliss Business Profile
Simple Streamlit App
Run with: streamlit run filename.py
"""

import streamlit as st
from datetime import datetime

# ===== PAGE CONFIGURATION =====
st.set_page_config(
    page_title="Kwazi's Fiber Bliss",
    layout="centered"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    .stApp {
        background-color: white;
        color: black;
    }
    .title {
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
    .section {
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ===== BUSINESS INFO =====
BUSINESS_NAME = "Kwazi's Fiber Bliss"
TAGLINE = "Love in every stitch, comfort in every thread"
FOUNDER_NAME = "Nokwazi Prudence Mbhele"
FOUNDED_YEAR = 2017
EMAIL = "KFiberBliss@gmail.com"
INSTAGRAM = "@K_FiberBliss"
WHATSAPP = "0662708613"

# ===== CALCULATIONS =====
current_year = datetime.now().year
business_years = current_year - FOUNDED_YEAR

# ===== HEADER =====
st.markdown(f'<h1 class="title">{BUSINESS_NAME}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="tagline">{TAGLINE}</p>', unsafe_allow_html=True)

# ===== OPTION 1: Use a web image URL (Recommended - no file needed) =====
try:
    # Using a placeholder crochet image from the web
    st.image(
        "https://cdn-media.knitpro.eu/media/mageplaza/blog/post/brand/how-to-crochet-a-sweater-1.webp",
        caption="Handmade with care since 2017"
    )
   #st.caption("*(Placeholder image - replace with your own)*")
except:
    st.write("**Image could not be loaded**")
    st.write("To add your own image:")
    st.write("1. Save your image in the same folder as this script")
    st.write("2. Use: st.image('your_image.jpg', caption='Your caption')")

# ===== OPTION 2: Use your local image file =====
# To use your own image file, comment out Option 1 above and uncomment below:
# st.image("your_image_filename_here.jpg", caption="Handmade with care since 2017")
# Make sure to replace "your_image_filename_here.jpg" with your actual filename

# ===== ABOUT SECTION =====
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("About")
st.write(f"**Founder:** {FOUNDER_NAME}")
st.write(f"**Journey:** Learned crocheting at age 8. Started business in {FOUNDED_YEAR}.")
st.write(f"**Experience:** {business_years} years professional craftsmanship")
st.write("**Specialty:** Handmade fashion and accessories")
st.write("**For:** All ages seeking unique, comfortable fashion")
st.markdown('</div>', unsafe_allow_html=True)

# ===== ARTICLE =====
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Featured Article")
st.write("**From Crochet Hooks to Lab Coats: Nokwazi's Journey**")
st.write("Published July 2025 in Vibe Online")
st.write("")
st.write("Highlights from the article:")
st.write("- First learned crocheting at age 8")
st.write(f"- Started business in {FOUNDED_YEAR}")
st.write("- MSc in Microbiology candidate")
st.write("- Research on water treatment solutions")
st.write("")
st.markdown('[Read full article](https://vibeonline.co.za/academic/from-crochet-hooks-to-lab-coats-nokwazis-journey-is-pure-fire/)')
st.markdown('</div>', unsafe_allow_html=True)

# ===== PRODUCTS & PRICES =====
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Products & Prices")

st.write("**HATS**")
st.write("Ruffle Hats: R250")
st.write("Beanie Hats: R150")
st.write("Sun Hats: R170")

st.write("")
st.write("**BIKINIS**")
st.write("Bikini Sets: R300")
st.write("Mix & Match: R280")

st.write("")
st.write("**TWO-PIECE SETS**")
st.write("Youth Sets: R320")
st.write("Seasoned Sets: R350")

st.write("")
st.write("**HANDBAGS**")
st.write("Crochet Classy Bags: R350")

st.write("")
st.write("**Children's Discount:** R50 OFF for children under 7 years")
st.write("Use code: KIDSBUZZ7")
st.markdown('</div>', unsafe_allow_html=True)

# ===== CONTACT =====
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Contact")
st.write(f"**Email:** {EMAIL}")
st.write(f"**Instagram:** {INSTAGRAM}")
st.write(f"**WhatsApp:** {WHATSAPP}")
st.write("")
st.write("Shop Coming Soon!")
st.markdown('</div>', unsafe_allow_html=True)

# ===== INQUIRY FORM =====
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Send Inquiry")

with st.form("inquiry_form"):
    name = st.text_input("Your Name")
    email_input = st.text_input("Your Email")
    product_interest = st.selectbox(
        "Product Interest",
        ["Hats", "Bikinis", "Two-Piece Sets", "Handbags", "Multiple Items"]
    )
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")
    
    if submit and name and email_input and message:
        st.success(f"Thank you {name}! We'll contact you soon.")
    elif submit:
        st.warning("Please fill in all fields.")
st.markdown('</div>', unsafe_allow_html=True)

# ===== FOOTER =====
st.write("---")
st.write(f"© {FOUNDED_YEAR}-{current_year} Kwazi's Fiber Bliss")
st.write("Crafting since childhood • Business since 2017")

# ===== IMAGE HELP =====
st.write("---")
st.write("**Image Help:**")
st.write("Currently using a web image. To use your own:")
st.write("1. Save your image file (.jpg, .png, .webp) in this folder")
st.write("2. Replace line 69 with: st.image('YOUR_FILENAME', caption='Handmade with care since 2017')")
st.write("3. Make sure the filename is EXACT (including .jpg or .png)")

