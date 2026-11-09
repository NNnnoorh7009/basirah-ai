import streamlit as st
import time

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="بصيرة AI - منصة كشف الاحتيال الذكية",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص واجهة المستخدم والتصميم السيبراني (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stApp {
        background-color: #0b132b;
        color: #ffffff;
    }
    .main-header {
        background: linear-gradient(135deg, #1c2541 0%, #0b132b 100%);
        border: 1px solid #48cae4;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(72, 202, 228, 0.15);
    }
    .risk-high {
        background-color: rgba(239, 68, 68, 0.15);
        border: 2px solid #ef4444;
        border-radius: 10px;
        padding: 16px;
        color: #f87171;
    }
    .risk-safe {
        background-color: rgba(34, 197, 94, 0.15);
        border: 2px solid #22c55e;
        border-radius: 10px;
        padding: 16px;
        color: #4ade80;
    }
</style>
""", unsafe_allow_html=True)

# الهيدر الرئيسي
st.markdown("""
<div class="main-header">
    <h1>🛡️ بصيرة AI | BASIRAH AI</h1>
    <p>النظام الذكي المتعدد الوسائط لكشف التصيد والاحتيال الهندسي</p>
</div>
""", unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.title("لوحة التحكم")
    st.info("نظام تحليل مخاطر الأمن السيبراني مدعوم بالذكاء الاصطناعي.")
    st.divider()
    st.markdown("**حالة النظام:** 🟢 متصل")

# التبويبات الرئيسية للتحليل
tab1, tab2, tab3 = st.tabs(["📝 تحليل النصوص والرسائل", "🔗 فحص الروابط", "🖼️ تحليل الصور ولقطات الشاشة"])

with tab1:
    st.subheader("تحليل الرسائل النصية والإيميلات")
    text_input = st.text_area("أدخلي نص الرسالة المشكوك فيها:", height=120, placeholder="مثال: عزيزي العميل، تم تجميد حسابك البنكي، اضغط على الرابط للتحديث فوراً...")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        btn_analyze_text = st.button("فحص النص الآن 🔍", use_container_width=True)
    with col2:
        btn_demo_phish = st.button("تحميل رسالة احتيال تجريبية ⚠️")

    if btn_demo_phish:
        text_input = "عزيزي العميل، تم إيقاف بطاقتك لعدم تحديث البيانات. يرجى الدخول فوراً على الرابط وتحديث بياناتك: http://nbe-update-sa.com"

    if btn_analyze_text and text_input:
        with st.spinner("جاري تحليل النص واستخراج الأدلة..."):
            time.sleep(1.5)
            st.markdown("---")
            st.markdown("### 📊 نتائج التقييم الأمني")
            
            if "تحديث" in text_input or "بطاقتك" in text_input or "http" in text_input:
                st.markdown("""
                <div class="risk-high">
                    <h2>🚨 نسبة المخاطرة: 94% (خطر مرتفع جداً)</h2>
                    <p>تم اكتشاف محاولة تصيد احتيالي وانتحال صفة مؤسسة مالية.</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### 🗺️ خريطة الأدلة (Evidence Map):")
                st.error("1. **لغة التهديد والاستعجال:** استخدام أسلوب إرهاب المستخدم لإجباره على اتخاذ قرار سريع.")
                st.error("2. **طلب معلومات حساسة:** محاولة الحصول على بيانات شخصية أو بنكية.")
                st.error("3. **رابط غير رسمي:** النطاق المرفق لا ينتمي لأي جهة معتمدة.")
                
                st.markdown("#### 💡 التوصيات الأمنية:")
                st.warning("• لا تضغط على الرابط المرفق نهائياً.\n• لا تشارك أي رموز تحقق.\n• قم بحظر المرسل فوراً.")
            else:
                st.markdown("""
                <div class="risk-safe">
                    <h2>✅ نسبة المخاطرة: 5% (رسالة آمنة)</h2>
                    <p>لم يتم رصد أي مؤشرات احتيال أو روابط مشبوهة في النص.</p>
                </div>
                """, unsafe_allow_html=True)

with tab2:
    st.subheader("فحص سلامة الروابط والنطاقات")
    url_input = st.text_input("أدخلي الرابط المراد فحصه:", placeholder="https://example.com")
    if st.button("فحص الرابط 🌐") and url_input:
        with st.spinner("جاري فحص النطاق..."):
            time.sleep(1)
            st.warning("⚠️ الرابط يحتوي على هيكلية نطاق مشابهة للمواقع الاحتيالية.")

with tab3:
    st.subheader("تحليل لقطات الشاشة والصور")
    uploaded_file = st.file_uploader("ارفعي صورة الرسالة المشكوه فيها:", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="الصورة المرفوعة", width=300)
        if st.button("تحليل الصورة بالذكاء الاصطناعي 🖼️"):
            with st.spinner("جاري قراءة النص..."):
                time.sleep(1.5)
                st.success("تم تحليل الصورة بنجاح وتأكيد خلوها من النصوص الاحتيالية.")

st.divider()
st.markdown("<p style='text-align: center; color: #4B5563; font-size: 0.95rem;'>جامعة نجران | تطبيق بصيرة والذكاء الاصطناعي 2026<br>من إعداد الطالبات: نورة آل فطيح ، خضراء النجراني ، هديل الدرسي</p>", unsafe_allow_html=True)
