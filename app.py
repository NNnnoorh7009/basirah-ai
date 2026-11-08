import streamlit as st
import json
from PIL import Image
from google import genai
from google.genai import types

# ---------------------------------------------------------
# 1. تهيئة الصفحة والنمط البصري (Page Configuration & UI)
# ---------------------------------------------------------
st.set_page_config(
    page_title="بصيرة | BASIRAH AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# نمط CSS مخصص لإعطاء التطبيق هوية تقنية حديثة
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .sub-header {
        text-align: center;
        color: #4B5563;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .stAlert {
        border-radius: 10px;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        border-right: 5px solid #2563EB;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. الهيدر والمقدمة
# ---------------------------------------------------------
st.markdown("<h1 class='main-header'>🛡️ نظام بصيرة | BASIRAH AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>المنظومة الذكية للاستباق وتحليل أدلة الخداع الرقمي وانتحال الهوية</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. الشريط الجانبي (إعدادات مفتاح API والذاكرة المجتمعية)
# ---------------------------------------------------------
with st.sidebar:
    st.header("⚙️ إعدادات النظام")
    api_key = st.text_input("أدخلي مفتاح Gemini API Key:", type="password")
    st.info("💡 يمكنك الحصول على المفتاح مجاناً من Google AI Studio.")
    
    st.divider()
    st.header("🧠 الذاكرة المجتمعية")
    st.caption("أنماط الاحتيال المسجلة حديثاً في قاعدة البلاغات:")
    st.warning("⚠️ انتحال صفة الجهات الرسمية وشركات الشحن")
    st.warning("⚠️ رسائل توظيف وهمية تطلب بيانات حساسة بضغط زمني")
    st.warning("⚠️ روابط مسابقات ومكافآت وهمية")

# ---------------------------------------------------------
# 4. محرك التحليل بالذكاء الاصطناعي (Gemini Analysis Engine)
# ---------------------------------------------------------
def analyze_content(prompt_text, image=None, api_key=None):
    if not api_key:
        return {"error": "يرجى أدخال مفتاح API في الشريط الجانبي لتفعيل التحليل."}
    
    try:
        client = genai.Client(api_key=api_key)
        
        system_instruction = """
        أنت محرك الذكاء الاصطناعي الخاص بنظام "بصيرة" لاكتشاف الاحتيال الرقمي والتلاعب النفسي.
        قم بتحليل النص أو الصورة المرفقة واستخراج مؤشرات الخداع بدقة.
        يجب أن تعيد النتيجة بتنسيق JSON حصراً وتضمن الأجزاء التالية:
        {
            "risk_level": "مرتفع جداً" / "مرتفع" / "متوسط" / "منخفض",
            "summary": "ملخص سريع لتقييم الرسالة",
            "evidence_map": [
                {"indicator": "اسم المؤشر (مثلاً: انتحال صفة)", "details": "تفاصيل ما تم اكتشافه"},
                {"indicator": "التلاعب النفسي", "details": "طريقة الضغط أو الخداع المستخدمة"},
                {"indicator": "فحص الروابط/الوسائط", "details": "تقييم الرابط أو العناصر البصرية"}
            ],
            "official_verification": "إرشادات للتحقق من المصادر والقنوات الرسمية",
            "community_pattern": "هل ينتمي هذا للأنماط الشائعة في الذاكرة المجتمعية؟"
        }
        """
        
        contents = [prompt_text]
        if image:
            contents.append(image)
            
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                temperature=0.2
            )
        )
        return json.loads(response.text)
    except Exception as e:
        return {"error": f"حدث خطأ أثناء التحليل: {str(e)}"}

# ---------------------------------------------------------
# 5. واجهة المدخلات (تعدد الوسائط: نص وصورة)
# ---------------------------------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 1. إدخال المحتوى النصي أو الرابط")
    user_text = st.text_area(
        "ألصقي نص الرسالة، الرابط المشبوه، أو الإعلان هنا:",
        height=180,
        placeholder="مثال: تهانينا! تم قبولك في وظيفة أو برنامج تدريبي، يرجى إدخال بياناتك عبر الرابط لاستكمال الإجراءات خلال 10 دقائق..."
    )

with col2:
    st.subheader("🖼️ 2. رفع صورة (لقطة شاشة للرسالة)")
    uploaded_file = st.file_uploader("ارفعي صورة للرسالة أو المحتوى المشبوه:", type=['png', 'jpg', 'jpeg'])
    img = None
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="الصورة المرفقة للتحليل", use_container_width=True)

# ---------------------------------------------------------
# 6. زر إطلاق التحليل واقتفاء الأدلة
# ---------------------------------------------------------
st.divider()
analyze_btn = st.button("🔍 فحص عبر نظام «بصيرة»", type="primary", use_container_width=True)

if analyze_btn:
    if not user_text and not img:
        st.warning("⚠️ يرجى أدخال نص أو رفع صورة للبدء في الفحص.")
    else:
        with st.spinner("جاري فحص وتفكيك مؤشرات الخداع وتحليل التلاعب النفسي..."):
            prompt_input = user_text if user_text else "قم بتحليل الصورة المرفقة واكتشاف أي مؤشرات احتيال أو انتحال هوية."
            result = analyze_content(prompt_input, img, api_key)
            
            if "error" in result:
                st.error(result["error"])
            else:
                st.success("✅ تم الفحص بنجاح! إليك تقرير الأدلة المسبب:")
                
                # عرض مستوى الخطورة
                risk = result.get("risk_level", "غير محدد")
                if risk in ["مرتفع جداً", "مرتفع"]:
                    st.error(f"🚨 **مستوى الخطورة:** {risk}")
                elif risk == "متوسط":
                    st.warning(f"⚠️ **مستوى الخطورة:** {risk}")
                else:
                    st.info(f"ℹ️ **مستوى الخطورة:** {risk}")
                
                st.markdown(f"**الملخص التنفيذي:** {result.get('summary', '')}")
                
                # خريطة الأدلة الذكية
                st.subheader("🗺️ خريطة الأدلة الذكية (تفكيك أسلوب الخداع)")
                evidence_list = result.get("evidence_map", [])
                for item in evidence_list:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>📌 {item.get('indicator')}</h4>
                        <p>{item.get('details')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # التحقق والتوصيات
                col_a, col_b = st.columns(2)
                with col_a:
                    st.subheader("🏛️ طرق التحقق الموصى بها")
                    st.info(result.get("official_verification", "لا تتوفر إرشادات خاصة."))
                
                with col_b:
                    st.subheader("🧠 مطابقة الذاكرة المجتمعية")
                    st.write(result.get("community_pattern", "تم تسجيل هذا النموذج في الذاكرة لتنبيه المستخدمين الآخرين."))

# ---------------------------------------------------------
# 7. التذييل (Footer) - معلومات المشروع والأسماء
# ---------------------------------------------------------
st.divider()
st.caption("مشروع بصيره - جامعة نجران 2026 | إعداد الطالبات: نورة آل فطيح، خضراء النجراني، هديل الدرسي")
