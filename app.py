import streamlit as st
import numpy as np
import joblib

st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Home", "Screening Quiz", "More Information", "Donate", "About me + Contact Us", "Q&A"])
data = np.random.randn(10, 1)

@st.cache_resource
def load_model():
	mod = joblib.load('best_random_forest_model.joblib')
	return mod
	
def set_language(tab_number, languages_key):
    if f"selected_language{tab_number}" in st.session_state:
        lang = st.session_state[f"selected_language{tab_number}"]
        st.experimental_set_query_params(**{f"lang{tab_number}": languages_key[lang]})
        return lang
    return "English"
	
with tab1:
	engInfo = "English"
	spanInfo = "Spanish"
	hindiInfo = "Hindi"
	languages = {"English": engInfo, "Spanish": spanInfo, "Hindi": hindiInfo}

	sel_lang1 = st.radio(
        	"Language",
        	options=languages.keys(),
        	horizontal=True,
        	key="selected_language1",
    	)
	selected_language1 = set_language(1, languages)
	
	st.markdown(f"Selected Language: {selected_language1}")
	if selected_language1 == "English":
		st.subheader("What is Obstructive Sleep Apnea?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("Obstructive sleep apnea (OSA) is a prevalent sleep disorder characterized by repeated interruptions in breathing during sleep. These interruptions occur when the muscles in the throat relax excessively, causing the airway to narrow or close partially or completely. As a result, the flow of air into the lungs is restricted, leading to brief pauses in breathing. These pauses can occur numerous times throughout the night, disrupting the normal sleep cycle and leading to fragmented and poor-quality sleep.")
			st.write("")
			st.write("The most common symptom of obstructive sleep apnea is loud and persistent snoring. Other symptoms include pauses in breathing during sleep, often witnessed by a bed partner, and gasping or choking sensations as breathing resumes. Individuals with OSA may also experience daytime symptoms such as excessive daytime sleepiness, morning headaches, difficulty concentrating, and irritability. Furthermore, OSA can lead to nocturnal symptoms such as frequent awakenings, night sweats, and a dry or sore throat upon waking.")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("Untreated, obstructive sleep apnea can have serious health consequences. The repeated interruptions in breathing lead to oxygen desaturation, putting strain on the cardiovascular system and increasing the risk of hypertension, heart disease, and stroke. OSA is also associated with metabolic disorders such as insulin resistance and type 2 diabetes. Additionally, untreated OSA can contribute to daytime fatigue, impairing cognitive function and increasing the risk of accidents while driving or operating machinery. Moreover, the chronic sleep disruption associated with OSA can negatively impact mood, leading to depression and anxiety in some individuals.")
		st.write("---")
	if selected_language1 == "Spanish":
		st.subheader("¿Qué es la apnea obstructiva del sueño?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("La apnea obstructiva del sueño (AOS) es un trastorno del sueño frecuente que se caracteriza por interrupciones repetidas de la respiración durante el sueño. Estas interrupciones ocurren cuando los músculos de la garganta se relajan excesivamente, lo que hace que las vías respiratorias se estrechen o se cierren parcial o completamente. Como Como resultado, el flujo de aire hacia los pulmones se restringe, lo que provoca breves pausas en la respiración. Estas pausas pueden ocurrir numerosas veces durante la noche, interrumpiendo el ciclo normal del sueño y provocando un sueño fragmentado y de mala calidad.")
			st.write("")
			st.write("El síntoma más común de la apnea obstructiva del sueño son los ronquidos fuertes y persistentes. Otros síntomas incluyen pausas en la respiración durante el sueño, a menudo presenciadas por un compañero de cama, y ​​sensaciones de jadeo o asfixia a medida que se reanuda la respiración. Las personas con AOS también pueden experimentar síntomas diurnos como somnolencia diurna excesiva, dolores de cabeza matutinos, dificultad para concentrarse e irritabilidad. Además, la AOS puede provocar síntomas nocturnos como despertares frecuentes, sudores nocturnos y garganta seca o dolor al despertar.")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("La apnea obstructiva del sueño no tratada puede tener graves consecuencias para la salud. Las repetidas interrupciones de la respiración provocan una desaturación de oxígeno, lo que ejerce presión sobre el sistema cardiovascular y aumenta el riesgo de hipertensión, enfermedades cardíacas y accidentes cerebrovasculares. La AOS también se asocia con trastornos metabólicos como la resistencia a la insulina y la diabetes tipo 2. Además, la AOS no tratada puede contribuir a la fatiga diurna, perjudicando la función cognitiva y aumentando el riesgo de accidentes al conducir o utilizar maquinaria. Además, la interrupción crónica del sueño asociada con la AOS puede afectar negativamente el estado de ánimo y provocar depresión y ansiedad en algunas personas.")
		st.write("---")
	if selected_language1 == "Hindi":
		st.subheader("ऑब्सट्रक्टिव स्लीप एपनिया क्या है?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("ऑब्सट्रक्टिव स्लीप एपनिया का सबसे आम लक्षण जोर से और लगातार खर्राटे लेना है। अन्य लक्षणों में नींद के दौरान सांस लेने में रुकावट शामिल है, जिसे अक्सर बिस्तर पर साथी द्वारा देखा जाता है, और सांस फिर से शुरू होने पर हांफने या दम घुटने की अनुभूति होती है। ओएसए से पीड़ित व्यक्तियों को दिन में अत्यधिक नींद आना, सुबह सिरदर्द, ध्यान केंद्रित करने में कठिनाई और चिड़चिड़ापन जैसे लक्षणों का भी अनुभव हो सकता है। इसके अलावा, ओएसए रात में लक्षण पैदा कर सकता है जैसे बार-बार जागना, रात में पसीना आना और जागने पर गला सूखना या दर्द होना।")
			st.write("")
			st.write("ऑब्सट्रक्टिव स्लीप एपनिया का सबसे आम लक्षण जोर से और लगातार खर्राटे लेना है। अन्य लक्षणों में नींद के दौरान सांस लेने में रुकावट शामिल है, जिसे अक्सर बिस्तर पर साथी द्वारा देखा जाता है, और सांस फिर से शुरू होने पर हांफने या दम घुटने की अनुभूति होती है। ओएसए से पीड़ित व्यक्तियों को दिन में अत्यधिक नींद आना, सुबह सिरदर्द, ध्यान केंद्रित करने में कठिनाई और चिड़चिड़ापन जैसे लक्षणों का भी अनुभव हो सकता है। इसके अलावा, ओएसए रात में लक्षण पैदा कर सकता है जैसे बार-बार जागना, रात में पसीना आना और जागने पर गला सूखना या दर्द होना।")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("अनुपचारित, ऑब्सट्रक्टिव स्लीप एपनिया के गंभीर स्वास्थ्य परिणाम हो सकते हैं। सांस लेने में बार-बार रुकावट से ऑक्सीजन की कमी हो जाती है, जिससे हृदय प्रणाली पर दबाव पड़ता है और उच्च रक्तचाप, हृदय रोग और स्ट्रोक का खतरा बढ़ जाता है। ओएसए इंसुलिन प्रतिरोध और टाइप 2 मधुमेह जैसे चयापचय संबंधी विकारों से भी जुड़ा है। इसके अतिरिक्त, अनुपचारित ओएसए दिन के समय थकान, संज्ञानात्मक कार्य को ख़राब कर सकता है और ड्राइविंग या मशीनरी चलाते समय दुर्घटनाओं के जोखिम को बढ़ा सकता है। इसके अलावा, ओएसए से जुड़ी पुरानी नींद की गड़बड़ी मूड पर नकारात्मक प्रभाव डाल सकती है, जिससे कुछ व्यक्तियों में अवसाद और चिंता हो सकती है।")
		st.write("---")
	
with tab2:
	st.header("Get your screening results today!")
	with st.form("my_form"):
		with st.expander("What is your gender by birth?"):
			genre = st.radio("", ["male", "female"])
		age = st.slider('What is your age?', 18, 100)
		oc = st.text_input("What is your occupation?")
		sle = st.slider("On average, what is your daily sleep duration in hours?", 1, 24)
		weight = st.slider("How much do you weigh? in lbs", 80, 300)
		height = st.slider("How tall are you? in inches", 48, 84)
		sbp = st.number_input("What is your Systolic blood pressure?", step=1)
		dbp = st.number_input("What is your Diastolic blood pressure?", step=1)
		hr = st.number_input("What is your heart rate?", step=1)
		steps = st.number_input("On average, how many steps do you take in a day?", step=1)
		physical = st.number_input("On average, how many minutes do you workout in a day?", step=1)

		"""For the following questions, answer on a scale of 0-5 about the last month, where 0 = never, 1 = 1-3 days, 2 = ~1 day per week, 3 = 2-4 nights per week, 4 = 5-6 nights per week, and 5 = almost every night"""
		qs1 = st.slider("Experienced difficulty falling asleep?", 0, 5)
		qs2 = st.slider("Woken up at night and easily fell asleep again?", 0, 5)
		qs3 = st.slider("Woken up and had difficulty falling asleep again / difficulty staying asleep?", 0, 5)
		qs4 = st.slider("Non-restorative sleep? i.e. feeling tired or worn-out after getting a usual amount of sleep", 0, 5)

		"""For the following questions, answer on a scale of 0-4 about the last month, where 0 = never, 1 = almost never, 2 = sometimes, 3 = fairly often, and 4 = very often"""
		sl1 = st.slider("How often have you been upset because of something that happened unexpectedly?", 0, 4)
		sl2 = st.slider("How often have you felt that you were unable to control the important things in your life?", 0, 4)
		sl3 = st.slider("How often have you felt nervous and stressed?", 0, 4)
		sl4 = st.slider("How often have you felt confident about your ability to handle your personal problems?", 0, 4)
		sl5 = st.slider("How often have you felt that things were going your way?", 0, 4)
		sl6 = st.slider("How often have you found that you could not cope with all the things that you had to do?", 0, 4)
		sl7 = st.slider("How often have you been able to control irritations in your life?", 0, 4)
		sl8 = st.slider("How often have you felt that you were on top of things?", 0, 4)
		sl9 = st.slider("How often have you been angered because of things that happened that were outside of your control?", 0, 4)
		sl10 = st.slider("How often have you felt difficulties were piling up so high that you could not overcome them?", 0, 4)
			  
		sub = st.form_submit_button('Submit')
		if sub:
			qs = (qs1+qs2+qs3+qs4)//2
			sl = (sl1+sl2+sl3+(4-sl4)+(4-sl5)+sl6+(4-sl7)+(4-sl8)+sl9+sl10)//4
			bmi = (weight/(height**2)) * 703
			if bmi < 18.5:
				bm = 0
			elif bmi >= 18.5 and bmi < 25:
				bm = 1
			elif bmi >= 25 and bmi < 30:
				bm = 2
			else:
				bm = 3
			if genre == 'female':
				gn = 0
			else:
				gn = 1
			inp = [[gn,age,sle,qs,physical,sl,bm,hr,steps,sbp,dbp]]
			model = load_model()
			new = model.predict(inp)
			if new == 0:
				st.write("You have a healthy sleep")
			elif new == 1:
				st.write("You might have Insomnia, please visit a doctor")
			elif new == 2:
				st.write("You might have Sleep Apnea, please visit a doctor")

with tab3:
	st.subheader("Find out more about OSA")
	col3 = st.columns(2)
	with col3[0]: 	
		st.write("To find out more about OSA, check out our YouTube channel and our FaceBook blog! We post informative videos about all aspects of OSA and hope to spread awareness about this silent killer. ")
		st.video('https://youtu.be/IIKlqbLwS7M')
		st.video('https://youtu.be/KGEKz4r5n8Q?si=thuPAv_9QfiZTaEP')
	with col3[1]:
		post_urls = [
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02tm8fT82sxZorg5KeE4DLSVC4nAM5Z2kFY7vss3R4Z5jtRLet8EJ53xDbbB8mZSuEl%26id%3D61560444242747&show_text=true&width=500" width="500" height="250" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02xn5PEUKkp7UADruTUYGTqYsVSgCPJjsN3Se7ZHPwkjvSoR8NZucpHE5nrSAmUt7el%26id%3D61560444242747&show_text=true&width=500" width="500" height="636" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid065hjmMpZJZqgmd2xsMe4VxPgGbUVD5WAzasrZ6VWWoz7349VByDM4uVUTQbx6qz9l%26id%3D61560444242747&show_text=true&width=500" width="500" height="661" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid0AYK4p3PmqkLpUTaEcgVGL3iDWNgGrSb6FbPVLqZkokWfcZqEG2kTjdypgw9zeqL9l%26id%3D61560444242747&show_text=true&width=500" width="500" height="661" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid0V9JrMdpByR4bmZYR9aCD42gToQjaVgbD5zM8CaGbhgZWcouNFzGZN48FwrpAhdPdl%26id%3D61560444242747&show_text=true&width=500" width="500" height="622" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			# Add more URLs as needed
		]
		
		def embed_facebook_post(post_url):
		    embed_code = post_url
		    st.markdown(embed_code, unsafe_allow_html=True)

		for url in post_urls:
    			embed_facebook_post(url)

with tab4:
	st.header("Join the Against Obstructive Sleep Apnea by Donating Now!")
	col1, col2 = st.columns([0.38, 0.62])
	
	with col1:
		gofundme_url = "https://www.gofundme.com/f/join-the-fight-against-sleep-apnea/widget/medium?sharesheet=CAMPAIGN_PAGE&attribution_id=sl:b1feb9fb-cbab-4945-af87-4c4286a75742"
		
		gofundme_iframe = f'''
		<iframe
		  src="{gofundme_url}"
		  style="height: 180px; width: 100%;"
		  frameborder="0"
		  scrolling="yes"
		></iframe>
		'''
		st.markdown(gofundme_iframe, unsafe_allow_html=True)

		youtube_url1 = "https://www.youtube.com/embed/g665P3z8sGk"
		youtube_iframe1 = f'''
		<iframe
		  width="100%"
		  height="300"
		  src="{youtube_url1}"
		  frameborder="0"
		  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
		  allowfullscreen
		></iframe>
		'''
		st.markdown(youtube_iframe1, unsafe_allow_html=True)
		
	with col2:
		youtube_url2 = "https://www.youtube.com/embed/eKItaKdLxPA?si=VTXdSF4Jmd0XQ5oY"
		youtube_iframe2 = f'''
		<iframe
		  width="100%"
		  height="450"
		  src="{youtube_url2}"
		  frameborder="0"
		  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
		  allowfullscreen
		></iframe>
		'''
		st.markdown(youtube_iframe2, unsafe_allow_html=True)
			  
with tab5:	
	engInfo4 = "English"
	spanInfo4 = "Spanish"
	hindiInfo4 = "Hindi"
	languages4 = {"English": engInfo4, "Spanish": spanInfo4, "Hindi": hindiInfo4}

	sel_lang4 = st.radio(
		"Language",
	        options=languages4.keys(),
	        horizontal=True,
	        key="selected_language4",
	)
	selected_language4 = set_language(4, languages4)
	
	st.markdown(f"Selected Language: {selected_language4}")
	col4 = st.columns(2)
	if selected_language4 == "English":
		with col4[0]:
			st.subheader("About Me")
			st.write("Hello! I am Ananya Aggarwal, a highschooler in Fremont, CA. I started this project to raise awareness about obstructive sleep apnea, an extrmemly widespread sleep disorder around the world. I was shocked by the number of my own family members and friends who were affected by the disorder and realized the problem is much bigger than expected. After doing research about OSA and its treatments, I realized that a big contributing factor to the lack of patient diagnosis for OSA is the expense and inavailblity of its diagnosis options. The most common diagnosis option for OSA, sleep tests, are expensive and not always easy to access, making it hard for possible OSA pateints to seek early diagnosis and therefore more effective treatment. My intelligent OSA screenoing quiz briges this gap between suspecting patients and professional diagnosis. The quiz is free to all and available on all web browsers. It currently predicts whether a user has healthy sleep or is at risk for either OSA or insomnia. I plan to enhance the quiz to also provide users with a prediction of how at-risk/likely they are to have obstructive sleep apnea, informing them of whether they are should get checked for it soon. My goals with this project are to raise the awareness for OSA in general and to gain popularity for my quiz to provide a free first step to OSA patients' diagnosis and treatment journey!")
		with col4[1]:
			st.subheader("Contact Us")
			st.write("Contact us here!")
			st.link_button("Click here to find all my links & forms of contact!", "https://linktr.ee/apneaast")
			st.link_button("YouTube", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
			st.link_button("FaceBook", "https://www.facebook.com/profile.php?id=61560444242747")
			st.link_button("GoFundMe", "https://gofund.me/6858e97d")
			st.write("Email: apneaassist@gmail.com")
	elif selected_language4 == "Spanish":
		with col4[0]:
			st.subheader("Acerca de Mí")
			st.write("¡Hola! Soy Ananya Aggarwal, estudiante de secundaria en Fremont, CA. Comencé este proyecto para crear conciencia sobre la apnea obstructiva del sueño, un trastorno del sueño extremadamente extendido en todo el mundo. Me sorprendió la cantidad de familiares y amigos afectados por el trastorno y me di cuenta de que el problema es mucho mayor de lo esperado. Después de investigar sobre la AOS y sus tratamientos, me di cuenta de que un factor que contribuye en gran medida a la falta de diagnóstico de AOS en los pacientes es el costo y la indisponibilidad de sus opciones de diagnóstico. La opción de diagnóstico más común para la AOS, las pruebas del sueño, son costosas y no siempre de fácil acceso, lo que dificulta que los posibles pacientes con AOS busquen un diagnóstico temprano y, por lo tanto, un tratamiento más eficaz. Mi cuestionario inteligente de detección de AOS cierra esta brecha entre los pacientes sospechosos y el diagnóstico profesional. El cuestionario es gratuito para todos y está disponible en todos los navegadores web. Actualmente predice si un usuario tiene un sueño saludable o si tiene riesgo de sufrir AOS o insomnio. Planeo mejorar el cuestionario para brindarles a los usuarios una predicción sobre el riesgo o la probabilidad de que tengan apnea obstructiva del sueño, informándoles si deben hacerse un examen pronto. Mis objetivos con este proyecto son crear conciencia sobre la AOS en general y ganar popularidad para mi cuestionario para proporcionar un primer paso gratuito en el diagnóstico y tratamiento de los pacientes con AOS.")
		with col4[1]:
			st.subheader("Contacta con Nosotras")
			st.write("Contacta con nosotras aquí!")
			st.link_button("¡Haz click aquí para encontrar todos mis enlaces y formas de contacto!", "https://linktr.ee/apneaast")
			st.link_button("YouTube", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
			st.link_button("FaceBook", "https://www.facebook.com/profile.php?id=61560444242747")
			st.link_button("GoFundMe", "https://gofund.me/6858e97d")
			st.write("Email: apneaassist@gmail.com")
	elif selected_language4 == "Hindi":
		with col4[0]:
			st.subheader("मेरे बारे में")
			st.write("नमस्ते! मैं अनन्या अग्रवाल हूं, फ़्रेमोंट, सीए में हाई स्कूल की छात्रा। मैंने यह परियोजना ऑब्सट्रक्टिव स्लीप एपनिया, एक नींद विकार जो दुनिया भर में बेहद व्यापक है, के बारे में जागरूकता बढ़ाने के लिए शुरू की है। मैं इस विकार से प्रभावित परिवार और दोस्तों की संख्या से आश्चर्यचकित था और मुझे एहसास हुआ कि समस्या अपेक्षा से कहीं अधिक बड़ी है। ओएसए और इसके उपचारों पर शोध करने के बाद, मुझे एहसास हुआ कि रोगियों में ओएसए का निदान न हो पाने का एक बड़ा कारण उनके निदान विकल्पों की लागत और अनुपलब्धता है। ओएसए के लिए सबसे आम निदान विकल्प, नींद परीक्षण, महंगा है और हमेशा आसानी से उपलब्ध नहीं होता है, जिससे संभावित ओएसए रोगियों के लिए शीघ्र निदान और इसलिए अधिक प्रभावी उपचार प्राप्त करना मुश्किल हो जाता है। मेरी स्मार्ट ओएसए स्क्रीनिंग प्रश्नावली संदिग्ध रोगियों और पेशेवर निदान के बीच इस अंतर को बंद कर देती है। क्विज़ सभी के लिए मुफ़्त है और सभी वेब ब्राउज़र पर उपलब्ध है। यह वर्तमान में भविष्यवाणी करता है कि क्या उपयोगकर्ता को स्वस्थ नींद आती है या उसे ओएसए या अनिद्रा का खतरा है। मैं उपयोगकर्ताओं को उनके जोखिम या ऑब्सट्रक्टिव स्लीप एपनिया होने की संभावना के बारे में पूर्वानुमान देने के लिए प्रश्नावली में सुधार करने की योजना बना रहा हूं, जिससे उन्हें पता चल सके कि क्या उन्हें जल्द ही परीक्षण करवाना चाहिए। इस परियोजना के साथ मेरा लक्ष्य सामान्य रूप से ओएसए के बारे में जागरूकता बढ़ाना और ओएसए रोगियों के निदान और उपचार में मुफ्त पहला कदम प्रदान करने के लिए मेरी प्रश्नावली के लिए लोकप्रियता हासिल करना है।")
		with col4[1]:
			st.subheader("संपर्क करें")
			st.write("हमसे यहां संपर्क करें!")
			st.link_button("मेरे सभी लिंक और संपर्क फ़ॉर्म पाने के लिए यहां क्लिक करें!", "https://linktr.ee/apneaast")
			st.link_button("यूट्यूब", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
			st.link_button("फेसबुक", "https://www.facebook.com/profile.php?id=61560444242747")
			st.link_button("गोफंडमी", "https://gofund.me/6858e97d")
			st.write("ईमेल: apneaassist@gmail.com")

with tab6:
	st.subheader("Have questions? Check here!")
	st.write("Find answers to your questions about OSA and about Apnea Assist! If you can't find an answer here, please let me know by typing it in the feedback form below.")
	st.write("General Questions about OSA")
	with st.expander("What is Obstructive Sleep Apnea (OSA)?")
		st.write("OSA is a sleep disorder where the airway becomes blocked during sleep, causing breathing to stop and start repeatedly.")
		


