import streamlit as st
import requests
import datetime

# =====================================================================
# ⚙️ কনফিগারেশন: এখানে তোমার টেলিগ্রাম বটের তথ্যগুলো বসাও
# =====================================================================
TELEGRAM_BOT_TOKEN = "8678628836:AAFmjPTFKlEraZt4Ul3zyHnlMoGpEaTHLE4"  # @BotFather থেকে পাওয়া টোকেন
TELEGRAM_CHAT_ID = "7371365329"      # তোমার টেলিগ্রাম চ্যাট বা চ্যানেল আইডি

# তোমার লোগোর ইমেজ লিংক (Imgur বা যেকোনো ডিরেক্ট ইমেজ লিংক দিতে পারো)
# বর্তমানে এটি খালি থাকলে বা লিংক কাজ না করলে কোডটি স্বয়ংক্রিয়ভাবে টেক্সট হেডার দেখাবে
LOGO_URL = "https://i.imgur.com/your_uploaded_logo_link.png" 

def send_telegram_alert(message):
    """টেলিগ্রামে লাইভ ডেটা পাঠানোর ব্যাকএন্ড ফাংশন"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": 7371365329,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        pass

# =====================================================================
# 📱 অ্যাপের পেজ সেটআপ এবং ইন্টারফেস (Streamlit)
# =====================================================================
st.set_page_config(
    page_title="Cyber Sentinel Academic",
    page_icon="🛡️",
    layout="centered"
)

# সিএসএস (CSS) দিয়ে অ্যাপটিকে আরও আকর্ষণীয় ডার্ক ও নিয়ন লুক দেওয়া হলো
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #00ffcc !important;
    }
    .stButton>button {
        background-color: #00ffcc !important;
        color: #0b0f19 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100%;
    }
    .developer-footer {
        text-align: center;
        padding: 20px;
        color: #8a99ad;
        font-size: 14px;
        border-top: 1px solid #1f2937;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_boxes=True, unsafe_allow_html=True)

# ১. সেশন স্টেট ব্যবহার করে প্রথমবার অ্যাপ ওপেন ট্র্যাকিং (যাতে বারবার রিফ্রেশে মেসেজ না যায়)
if 'user_tracked' not in st.session_state:
    st.session_state['user_tracked'] = True
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send_telegram_alert(f"🚀 *নতুন হ্যাকার অ্যালার্ট!*\n\n👤 একজন ইউজার *Cyber Sentinel Academic* অ্যাপে প্রবেশ করেছেন।\n⏰ সময়: {current_time}")

# --- অ্যাপের হেডার ও লোগো সেকশন ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # এখানে তোমার দেওয়া লোগোটি শো করবে (তুমি পিসিতে রান করার সময় ফাইলের নামও দিতে পারো)
    try:
        st.image("IMG_20260512_085524_953.jpg", use_container_width=True)
    except:
        # যদি ফাইলটি একই ফোল্ডারে না থাকে তবে নিচের অনলাইন লিংকটি ট্রাই করবে
        try:
            st.image(LOGO_URL, use_container_width=True)
        except:
            st.title("🛡️ CSB")

st.markdown("<h1 style='text-align: center;'>CYBER SENTINEL ACADEMIC</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a99ad;'>Your A to Z Guide to Coding & Cyber Security</p>", unsafe_allow_html=True)
st.write("---")

# --- স্বাগত বার্তা ---
st.markdown("### 💻 Hello, Hacker!")
st.write("সাইবার সিকিউরিটি এবং প্রোগ্রামিংয়ের দুনিয়ায় তোমাকে স্বাগতম। নিচে তোমার জন্য নির্ধারিত লার্নিంగ్ পাথ সাজানো হলো:")

# --- কোর্স ডাটাবেজ ও ফাংশনালিটি ---
courses = [
    {"title": "👨‍💻 C Programming (A to Z)", "desc": "লজিক বিল্ডিং, অ্যালگরিদম, লুপ এবং কন্ডিশনাল স্টেটমেন্ট এর বিস্তারিত গাইড।"},
    {"title": "🐍 Python for Cyber Security", "desc": "পাইথন স্ক্রিপ্টিং, নেটওয়ার্ক অটোমেশন এবং অ্যাডভান্সড টেলিগ্রাম বট মেকিং।"},
    {"title": "🌐 Frontend Web Development", "desc": "HTML5, CSS3, JavaScript এবং চমৎকার ডার্ক-নিওন পোর্টফোলিও ডিজাইন।"},
    {"title": "🛡️ Ethical Hacking & Linux", "desc": "Linux কমান্ড লাইন, নেটওয়ার্কিং ফান্ডামেন্টালস, OSI মডেল এবং OWASP Top 10 সিকিউরিটি।"},
]

for index, course in enumerate(courses):
    with st.container():
        st.markdown(f"#### {course['title']}")
        st.write(course['desc'])
        
        # প্রতিটি কোর্সের আলাদা বাটন
        if st.button("কোর্স শুরু করো ➔", key=f"btn_{index}"):
            st.info(f"✨ {course['title']} কোর্সটি খুব শীঘ্রই লাইভ করা হবে!")
            
            # ইউজার কোন কোর্সে ক্লিক করল তা টেলিগ্রামে লাইভ ট্র্যাকিং পাঠানো
            click_time = datetime.datetime.now().strftime("%H:%M:%S")
            send_telegram_alert(f"🖱️ *ইউজার অ্যাক্টিভিটি!*\n\n📚 কোর্স: {course['title']}\n⏰ সময়: {click_time}\n💡 ইউজার এই কোর্স মডিউলটি ওপেন করার চেষ্টা করছেন।")
    st.write("---")

# --- ডেভেলপার ফুটার সেকশন ---
st.markdown(f"""
    <div class="developer-footer">
        🔴 Live Tracking Active via Telegram Bot<br><br>
        <b>Developer:</b> CSB MAHIR AHMED
    </div>
""", unsafe_allow_html=True)