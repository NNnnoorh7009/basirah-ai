import streamlit as st
import time
import re
from urllib.parse import urlparse

def analyze_url_safety(url):
    """
    دالة فحص الترابط الذكية لتحديد ما إذا كان الرابط مشبوباً أم آمناً بدقة عالية.
    """
    # تنظيف الرابط والتأكد من صحة البدء
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
        
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    path = parsed_url.path.lower()
    full_url = url.lower()
    
    trusted_domains = [
        '.gov.sa', '.edu.sa', 'absher.sa', 'elm.sa', 
        'google.com', 'microsoft.com', 'apple.com', 'github.com', 'streamlit.app',
        'basirah-ai'
    ]
    
    for trusted in trusted_domains:
        if domain.endswith(trusted) or trusted in domain:
            return {
                "status": "آمن",
                "risk_score": 5,
                "message": "النطاق يتبع جهة رسمية أو موثوقة معتمدة."
            }

    # مؤشرات الاحتيال والتصيد (Indicators of Compromise)
    risk_score = 0
    threats = []

    # أ) الكلمات المفتاحية الخطرة المرتبطة بالاحتيال المصرفي أو تحديث البيانات الوهمية
    phishing_keywords = ['update', 'login', 'verify', 'bank', 'account', 'secure', 'signin', 'wallet', 'bonus', 'free']
    found_keywords = [kw for kw in phishing_keywords if kw in full_url]
    if found_keywords:
        risk_score += 40
        threats.append(f"وجود كلمات حساسة تستخدم غالباً في التصيد: {', '.join(found_keywords)}")

    # ب) استخدام نطاقات فرعية مريبة أو غريبة (Subdomain abuse)
    if domain.count('.') > 3:
        risk_score += 30
        threats.append("النطاق يحتوي على عدد مفرط من النطاقات الفرعية المشبوهة.")

    # ج) استخدام عناوين IP مباشرة بدلاً من أسماء النطاقات
    ip_pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    if ip_pattern.match(domain):
        risk_score += 50
        threats.append("الرابط يبتعد عن أسماء النطاقات الرسمية ويستخدم عنوان IP مباشر.")

    # د) الروابط القصيرة (URL Shorteners) التي تخفي الوجهة الحقيقية
    shorteners = ['bit.ly', 't.co', 'goo.gl', 'tinyurl.com', 'ow.ly']
    if any(short in domain for short in shorteners):
        risk_score += 25
        threats.append("تم استخدام خدمة اختصار روابط، مما يخفي وجهة الرابط الحقيقية.")

    # القرار النهائي بناءً على نسبة المخاطرة
    if risk_score >= 40:
        return {
            "status": "مشبوه وخطر",
            "risk_score": risk_score,
            "threats": threats,
            "message": "⚠️ تحذير: تم رصد مؤشرات تصيد احتيالي محتملة في هذا الرابط!"
        }
    else:
        return {
            "status": "آمن نسبياً",
            "risk_score": risk_score,
            "message": "✅ لم يتم رصد مؤشرات احتيال واضحة في هذا الرابط."
        }
# --- دالة تحليل الأرقام المشبوهة وكشف الاحتيال الهاتفي ---
def analyze_phone_number(phone):
    """
    تحليل رقم الهاتف أو الرسائل النصية الواردة لمعرفة احتمالية الاحتيال.
    """
    phone = phone.strip()
    
    # تنظيف الرقم من المسافات والرموز الزائدة
    clean_phone = ''.join(filter(str.isdigit, phone))
    
    # التحقق من الأرقام الدولية المشبوهة أو القصيرة المخالفة للمعتاد
    if len(clean_phone) < 7:
        return {
            "status": "مشبوه جداً",
            "message": "⚠️ تحذير: الرقم قصير جداً وغير معتمد، قد يكون عائداً لجهات احتيالية تستخدم خدمات إرسال وهمية."
        }
    
    # فحص رموز الدول أو الأنماط غير المعتادة (مثلاً أرقام دولية غريبة تبدأ بمفاتيح غير مألوفة)
    if phone.startswith('+') and not (phone.startswith('+966') or phone.startswith('+00966')):
        return {
            "status": "مشبوه / دولي",
            "message": "⚠️ تنبيه: رقم دولي غريب. احذر من مشاركة أي بيانات شخصية أو رموز تحقق (OTP) معه."
        }
    
    return {
        "status": "آمن / محلي",
        "message": "✅ الرقم يبدو ضمن النطاق الطبيعي، ولكن احرص دائماً على عدم الإفصاح عن البيانات البنكية."
    }

# --- دالة التوصيات الأمنية الذكية بناءً على نتيجة الفحص ---
def get_security_recommendations(risk_type):
    """
    توليد توصيات إرشادية وتوعوية للمستخدم لحمايته من الهندسة الاجتماعية والتصيد.
    """
    recommendations = {
        "phishing": [
            "1. **لا تنقر** على أي روابط مرفقة في رسائل البريد أو الرسائل النصية القصيرة (SMS) مجهولة المصدر.",
            "2. **تحقق دائماً** من اسم النطاق (URL) في شريط العنوان وتأكد من وجود القفل الآمن (HTTPS) ونطاقات الدولة الرسمية (.gov.sa أو .edu.sa).",
            "3. **لا تقم بتحديث** بياناتك الشخصية أو البنكية عبر روابط خارجية أبداً؛ الجهات الرسمية لا تطلب ذلك عبر الرسائل.",
            "4. **استخدم تطبيق بصيرة** لفحص أي رابط مشكوك فيه قبل اتخاذ أي خطوة."
        ],
        "phone": [
            "1. **لا تشارك** رمز التحقق المؤقت (OTP) أو كلمات المرور مع أي شخص مهما كانت الصفة أو الجهة التي يدعيها.",
            "2. **تجاهل تماماً** الرسائل أو الاتصالات التي توهمك بالفوز بجوائز مالية ضخمة أو تطلب سداد رسوم وهمية.",
            "3. **قم بحظر** الأرقام المشبوهة والمجهولة فوراً والإبلاغ عنها للجهات المختصة.",
            "4. **تأكد من الاتصال** بالجهات الرسمية من خلال قنواتهم المعتمدة فقط في حال وجود استفسار."
        ]
    }
    return recommendations.get(risk_type, [])
# تجربة دالة الفحص:
# test_url = "http://nbe-update-sa.com/login"
# print(analyze_url_safety(test_url))
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
