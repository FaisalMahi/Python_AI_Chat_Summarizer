from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
 
def parse_chat_log(file_path):
    user_messages = []
    ai_messages = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith("User:"):
                user_messages.append(line.replace("User:", "").strip())
            elif line.startswith("AI:"):
                ai_messages.append(line.replace("AI:", "").strip())

    return user_messages, ai_messages
from collections import Counter
import re

def extract_keywords(messages, top_n=5):
    all_text = ' '.join(messages).lower()
    
    words = re.findall(r'\b\w+\b', all_text)
    
    filtered_words = [word for word in words if word not in STOPWORDS]

    most_common = Counter(filtered_words).most_common(top_n)
    return [word for word, _ in most_common]

def generate_summary(user_msgs, ai_msgs, keywords):
    total_exchanges = len(user_msgs) + len(ai_msgs)

    print("\n📄 Conversation Summary:")
    print(f"- Total exchanges: {total_exchanges}")
    print(f"- User messages: {len(user_msgs)}")
    print(f"- AI messages: {len(ai_msgs)}")
    print(f"- Most common keywords: {', '.join(keywords)}")


    topic_keywords = ', '.join(keywords[:3])
    print(f"- The conversation likely focused on: {topic_keywords}")


if __name__ == "__main__":
    user_msgs, ai_msgs = parse_chat_log("chat.txt")

    print("User Messages:")
    for msg in user_msgs:
        print("-", msg)

    print("\nAI Messages:")
    for msg in ai_msgs:
        print("-", msg)


def get_message_stats(user_msgs, ai_msgs):
    return {
        "total": len(user_msgs) + len(ai_msgs),
        "user": len(user_msgs),
        "ai": len(ai_msgs),
    }


    
stats = get_message_stats(user_msgs, ai_msgs)
print("\n📊 Message Statistics:")
print(f"- Total messages: {stats['total']}")
print(f"- User messages: {stats['user']}")
print(f"- AI messages: {stats['ai']}")

all_msgs = user_msgs + ai_msgs
top_keywords = extract_keywords(all_msgs)

print("\n🔑 Top Keywords:")
print(", ".join(top_keywords))
generate_summary(user_msgs, ai_msgs, top_keywords)


