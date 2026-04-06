import nltk
from nltk.tokenize import sent_tokenize
import spacy
from collections import Counter

# 下载NLTK的Punkt句子分词器
nltk.download('punkt')

# 加载spaCy的英文模型
nlp = spacy.load('en_core_web_sm')

def analyze_topic_and_character(text):
    # 分句
    sentences = sent_tokenize(text)
    
    # 预测主题
    predicted_topic = analyze_topic(sentences)  
    
    # 提取主角
    characters = extract_characters(sentences)
    
    # 计数角色出现的次数
    character_counts = Counter(characters)
    
    # 获取戏份最高的前三个角色
    top_characters = character_counts.most_common(3)
    
    return predicted_topic, top_characters

def analyze_topic(sentences):
    predicted_topic = "电影"
    return predicted_topic
    #注：这里也可以自己修改

def extract_characters(sentences):
    characters = []
    
    for sentence in sentences:
        doc = nlp(sentence)
        
        # 提取人物
        for entity in doc.ents:
            if entity.label_ == "PERSON":
                characters.append(entity.text)
    
    return characters

# 要分析的速度与激情9剧情文本
text = "Sean Boswell, who has always been an outsider. A loner at school, his only connection to the indifferent world around him is through illegal street racing -- which has made him particularly unpopular with the local authorities. To avoid jail time, Sean is sent out of the country to live with his Farther in the military, in a cramped apartment in a low-rent section of Tokyo. In the land that gave birth to the majority of modified racers on the road, the simple street race has been replaced by the ultimate pedal-to-the-metal, gravity-defying automotive challenge - drift racing, a deadly combination of brutal speed on heart stopping courses of hairpin turns and switchbacks. For his first unsuccessful foray in drift racing, Shean unknowingly takes on D.K., the Drift King,with ties to the Yakuza, the Japanese crime machine. The only way he can pay off the debt of his loss is to venture into the deadly realm of the Tokyo underworld, where the stakes are life and death."
predicted_topic, top_characters = analyze_topic_and_character(text)

# 打印结果
print("Predicted Topic:", predicted_topic)
print("Top Characters:")
for character, count in top_characters:
    print(character, "-", count)
