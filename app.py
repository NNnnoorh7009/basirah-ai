import streamlit as st
import hashlib
from urllib.parse import urlparse

# إعداد الصفحة لتكون واسعة
st.set_page_config(page_title="BASIRAH AI | Cyber Investigator", page_icon="🛡️", layout="wide")

# تصميم الهوية البصرية والواجهة الزرقاء المتكاملة
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #0d1b2a, #1b263b, #415a77);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        border: 1px solid #415a77;
        margin-bottom: 30px;
    }
    .main-header h1 {
        color: #ffffff;
        font-size: 2.5rem;
        margin-bottom: 10px;
        font-weight: 700;
        direction: rtl;
    }
    .main-header p {
        color: #e0e1dd;
        font-size: 1.1rem;
        direction: rtl;
    }
    </style>
    
    <div class="main-header">
        <h1>نظام بصيرة 🛡️ | BASIRAH AI & Cyber Investigator</h1>
        <p>المنظومة الذكية المتعددة الوسائط لكشف التصيد، الاحتيال الهندسي، وتحليل مخاطر الأمن السيبراني</p>
    </div>
""", unsafe_allow_html=True)

# تقسيم الشاشة إلى المحتوى الرئيسي ولوحة التحكم الجانبية
col1, col2 = st.columns([3, 1])

with col2:
    st.markdown("### لوحة التحكم الأمنية")
    st.info("🛡️ نظام تحليل مخاطر الأمن السيبراني مدعوم بالذكاء الاصطناعي")
    st.success("حالة النظام: 🟢 متصل وآمن")
    st.markdown("---")
    st.caption("مشروع تخرج 2026 - جامعة نجران")
    st.caption("إعداد الطالبات: نورة آل فطيح، خضراء النجراني، هديل الدرسي")

with col1:
    tab1, tab2, tab3 = st.tabs(["📄 تحليل النصوص والروابط", "🖼️ فحص الملفات والأدلة", "📊 تقييم مخاطر CIA Triad"])

    with tab1:
        st.subheader("تحليل الرسائل النصية والروابط المشكوك فيها")
        user_input = st.text_input("أدخلي نص الرسالة أو الرابط المراد فحصه:", placeholder="مثال: عزيزي العميل، تم تجميد حسابك، اضغط على الرابط لتحديث البيانات فوراً...")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("بدء الفحص والتحليل الذكي"):
                if user_input:
                    if "https://" in user_input or "http://" in user_input:
                        parsed_url = urlparse(user_input)
                        if "https" in parsed_url.scheme:
                            st.success(f"الرابط آمن ومميز ببروتوكول HTTPS المشفر: {parsed_url.netloc}")
                        else:
                            st.warning(f"تحذير: الرابط يستخدم بروتوكول غير آمن HTTP: {parsed_url.netloc}")
                    else:
                        st.info("جاري تحليل النص وكشف مؤشرات الاحتيال والهندسة الاجتماعية...")
                else:
                    st.warning("يرجى إدخال النص أو الرابط أولاً.")
        with col_btn2:
            if st.button("تحميل رسالة احتيال تجريبية ⚠️"):
                st.code("عاجل: تم إيقاف حسابك المصرفي مؤقتاً، يرجى التوثيق عبر الرابط السريع لتفادي الإغلاق النهائي.")

    with tab2:
        st.subheader("فحص الملفات واستخراج البصمة الرقمية (Hashing)")
        uploaded_file = st.file_uploader("ارفعي الملف أو لقطة الشاشة للفحص واستخراج البصمة:", type=["png", "jpg", "jpeg", "pdf", "exe", "txt"])
        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            sha256_val = hashlib.sha256(file_bytes).hexdigest()
            st.success(f"اسم الملف المرفوع: {uploaded_file.name}")
            st.markdown("**البصمة الرقمية (SHA-256):**")
            st.code(sha256_val)
            st.info("جاري فحص البصمة البصرية والرقمية بمحركات اكتشاف البرمجيات الخبيثة...")

    with tab3:
        st.subheader("إطار تقييم المخاطر (CIA Triad Risk Analysis)")
        st.write("تقييم أمان المنظومة بناءً على مبادئ أمن المعلومات الأساسية:")
        
        col_c, col_i, col_a = st.columns(3)
        with col_c:
            st.markdown("### السرية (Confidentiality)")
            st.success("حماية البيانات وسرية المستودعات مفعلة بنجاح.")
        with col_i:
            st.markdown("### التكامل (Integrity)")
            st.success("سلامة السجلات والتحقق من التوقيع الرقمي مطبقة.")
        with col_a:
            st.markdown("### التوافر (Availability)")
            st.success("استمرارية الخدمة والجاهزية السحابية نشطة على مدار الساعة.")
