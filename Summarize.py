import streamlit as st
import openai

# StreamlitでAPIキーを入力
api_key = st.text_input("OpenAI APIキーを入力してください")

# OpenAI API認証情報の設定
openai.api_key = api_key
# 文章を要約する関数
def summarize_text(text, max_tokens):
    prompt = f"次の文章を{max_tokens}の文字数で要約してください\n{text}"
    # パラメータの定義
    parameters = {
        'engine': 'gpt-3.5-turbo',
        'max_tokens': 400,
        'stop': None,
    }


    # 温度の定義
    temperatures = [0 , 0.8]

    # ユーザーからの入力を取得
    question = prompt

    # 温度パラメータの更新
    parameters['temperature'] = 0.5

    # APIを呼び出す
    response = openai.ChatCompletion.create(
        model=parameters['engine'],
        messages=[
            {"role": "system", "content": "あなたは助けになるアシスタントです。"},
            {"role": "user", "content": question}
        ],
        max_tokens=parameters['max_tokens'],
        temperature=parameters['temperature'],
        stop=parameters['stop'],
    )
    summarized_text=response['choices'][0]['message']['content']
    st.write(f"{summarized_text}")
    
# 文章を添削する関数
def proofread_text(text):
    prompt = f"次の文章には誤字脱字、文法ミスがあるので正しい文章に直してください\n{text}"
    # パラメータの定義
    parameters = {
        'engine': 'gpt-3.5-turbo',
        'max_tokens': 400,
        'stop': None,
    }


    # 温度の定義
    temperatures = [0 , 0.8]

    # ユーザーからの入力を取得
    question = prompt

    # 温度パラメータの更新
    parameters['temperature'] = 0.5

    # APIを呼び出す
    response = openai.ChatCompletion.create(
        model=parameters['engine'],
        messages=[
            {"role": "system", "content": "あなたは助けになるアシスタントです。"},
            {"role": "user", "content": question}
        ],
        max_tokens=parameters['max_tokens'],
        temperature=parameters['temperature'],
        stop=parameters['stop'],
    )
    proofread_result=response['choices'][0]['message']['content']
    st.write(f"{proofread_result}")

# メイン関数
def main():
    st.title("文章要約・添削アプリ")
    task = st.radio("以下のタスクを選択してください:", ("要約", "添削"))

    if task == "要約":
        text = st.text_area("要約する文章を入力してください:")
        max_tokens = st.number_input("要約する文字数を入力してください:", min_value=1, max_value=400)
        if st.button("要約する"):
            summarized_text = summarize_text(text, max_tokens)
            #st.write("要約された文章:", summarized_text)
    elif task == "添削":
        text = st.text_area("添削する文章を入力してください:")
        if st.button("添削する"):
            proofread_result = proofread_text(text)
            #st.write("添削された文章:", proofread_result)

if __name__ == "__main__":
    main()
