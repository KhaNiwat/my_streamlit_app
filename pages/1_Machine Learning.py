import streamlit as st

st.set_page_config(page_title="Machine Learning Model", layout="wide")

# ปรับสไตล์ให้เรียบง่าย (Dark Mode)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    h1 { color: #00d4ff; }
    h2 { color: #75e6da; margin-top: 30px; }
    h3 { color: #4db8ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("Machine Learning: Ensemble Learning Model")
st.write("การวิเคราะห์และทำนายปัจจัยเสี่ยงโรคหัวใจ")
st.markdown("---")

# --- ส่วนที่ 1: การเตรียมข้อมูล ---
st.header("1. การเตรียมข้อมูล (Data Preparation)")
st.write("กระบวนการจัดการข้อมูลในไฟล์ IS_ML.ipynb เริ่มต้นจากการนำเข้าชุดข้อมูล และดำเนินการดังนี้:")
st.write("ขั้นตอนแรกคือการจัดการค่าที่หายไป (Missing Values) โดยใช้ค่ามัธยฐาน (Median) ของแต่ละคอลัมน์เพื่อรักษาการกระจายตัวของข้อมูลให้ใกล้เคียงเดิมมากที่สุด จากนั้นจึงทำการแปลงข้อมูลหมวดหมู่ให้เป็นตัวเลขด้วยวิธี One-Hot Encoding เพื่อให้โมเดลคณิตศาสตร์สามารถนำไปประมวลผลได้")
st.write("นอกจากนี้ยังมีการใช้ StandardScaler เพื่อปรับสเกลของข้อมูล (Feature Scaling) ให้มีค่าเฉลี่ยเป็น 0 และส่วนเบี่ยงเบนมาตรฐานเป็น 1 ซึ่งจำเป็นอย่างยิ่งสำหรับโมเดลประเภท Logistic Regression")

st.code("""
# ตัวอย่างขั้นตอนจากโค้ด
df[col] = df[col].fillna(df[col].median())
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
""", language='python')

st.markdown("---")

# --- ส่วนที่ 2: ทฤษฎีอัลกอริทึม ---
st.header("2. ทฤษฎีของอัลกอริทึม (Algorithm Theory)")
st.write("โมเดลที่พัฒนาขึ้นใช้เทคนิค Voting Classifier แบบ Soft Voting ซึ่งเป็นการรวบรวมผลทำนายจาก 3 อัลกอริทึมหลัก:")
st.write("- Logistic Regression: ใช้สำหรับหาความสัมพันธ์เชิงเส้นเพื่อระบุโอกาสการเกิดโรค")
st.write("- Random Forest: ใช้วิธีสร้างต้นไม้ตัดสินใจหลายต้นเพื่อลดความคลาดเคลื่อนและป้องกันการเรียนรู้ที่จำเพาะเกินไป")
st.write("- Gradient Boosting: พัฒนาประสิทธิภาพผ่านการสร้างโมเดลใหม่เพื่อลดข้อผิดพลาดจากโมเดลก่อนหน้า")

st.markdown("---")

# --- ส่วนที่ 3: ขั้นตอนการพัฒนาโมเดล ---
st.header("3. ขั้นตอนการพัฒนาโมเดล (Model Development)")
st.write("เริ่มต้นจากการแบ่งข้อมูลเป็นส่วนสำหรับฝึกฝนและส่วนสำหรับทดสอบ จากนั้นสร้าง Pipeline เพื่อเชื่อมต่อขั้นตอนการแปลงข้อมูลเข้ากับตัวโมเดล Ensemble โดยกำหนดน้ำหนักการตัดสินใจแบบ Soft Voting ซึ่งจะนำความน่าจะเป็น (Probability) จากทุกโมเดลมาหาค่าเฉลี่ยเพื่อผลลัพธ์ที่ดีที่สุด")

st.code("""
# โครงสร้างการรวมโมเดล
models = [('lr', model_lr), ('rf', model_rf), ('gb', model_gb)]
ensemble = VotingClassifier(estimators=models, voting='soft')
ensemble.fit(X_train, y_train)
""", language='python')

st.markdown("---")

# --- ส่วนที่ 4: แหล่งอ้างอิงข้อมูล ---
st.header("4. แหล่งอ้างอิงข้อมูล (References)")
st.write("ชุดข้อมูลปัจจัยเสี่ยงโรคหัวใจ (Heart Disease Synthetic Dataset) ถูกสร้างขึ้นโดย Generative AI (ChatGPT) เพื่อใช้ประกอบการศึกษาวิจัย")
st.write("กระบวนการทางคณิตศาสตร์และอัลกอริทึมได้รับการพัฒนาโดยใช้ไลบรารี Scikit-learn (Pedregosa et al., 2011)")