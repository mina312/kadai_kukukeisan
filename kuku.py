import random
import streamlit as st
import numpy as np

# 九九の問題セットを定義
kuku2 = {
    "2×1=": "2",
    "2×2=": "4",
    "2×3=": "6",
    "2×4=": "8",
    "2×5=": "10",
    "2×6=": "12",
    "2×7=": "14",
    "2×8=": "16",
    "2×9=": "18"
}

kuku3 = {
    "3×1=": "3",
    "3×2=": "6",
    "3×3=": "9",
    "3×4=": "12",
    "3×5=": "15",
    "3×6=": "18",
    "3×7=": "21",
    "3×8=": "24",
    "3×9=": "27"
}

kuku4 = {
    "4×1=": "4",
    "4×2=": "8",
    "4×3=": "12",
    "4×4=": "16",
    "4×5=": "20",
    "4×6=": "24",
    "4×7=": "28",
    "4×8=": "32",
    "4×9=": "36",
}

kuku5 = {
    "5×1=": "5",
    "5×2=": "10",
    "5×3=": "15",
    "5×4=": "20",
    "5×5=": "25",
    "5×6=": "30",
    "5×7=": "35",
    "5×8=": "40",
    "5×9=": "45",
}

kuku6 = {
    "6×1=": "6",
    "6×2=": "12",
    "6×3=": "18",
    "6×4=": "24",
    "6×5=": "30",
    "6×6=": "36",
    "6×7=": "42",
    "6×8=": "48",
    "6×9=": "54",
}

kuku7 = {
    "7×1=": "7",
    "7×2=": "14",
    "7×3=": "21",
    "7×4=": "28",
    "7×5=": "35",
    "7×6=": "42",
    "7×7=": "49",
    "7×8=": "56",
    "7×9=": "63",
}

kuku8 = {
    "8×1=": "8",
    "8×2=": "16",
    "8×3=": "24",
    "8×4=": "32",
    "8×5=": "40",
    "8×6=": "48",
    "8×7=": "56",
    "8×8=": "64",
    "8×9=": "72",
}

kuku9 = {
    "9×1=": "9",
    "9×2=": "18",
    "9×3=": "27",
    "9×4=": "36",
    "9×5=": "45",
    "9×6=": "54",
    "9×7=": "63",
    "9×8=": "72",
    "9×9=": "81"
}

# クイズデータセット
quiz_data = {
    "2の段": kuku2,
    "3の段": kuku3,
    "4の段": kuku4,
    "5の段": kuku5,
    "6の段": kuku6,
    "7の段": kuku7,
    "8の段": kuku8,
    "9の段": kuku9,
}

# セッション変数の初期化
if 'score' not in st.session_state:
    st.session_state.score = 0

if 'question_count' not in st.session_state:
    st.session_state.question_count = 0

# 正解時と不正解時の画像リスト
correct_images = ["zoro.png", "sogeking.png", "luffy.png", "sanji.png", "nami.png"]
incorrect_images = ["enel.png", "santaisyou.png", "doflamingo.png", "crocodile.png"]

# 正解数に合わせた画像リスト
perfect_image = "omedetou.png"
mousukosi_image = "panda.png"
zannen_image = "zannen.png"

# サイドバーで問題を選択
name = st.sidebar.text_input("名前をいれてね")
level = st.sidebar.radio("問題をえらんでね", ["2の段", "3の段", "4の段", "5の段", "6の段", "7の段", "8の段", "9の段"])
word_pairs = quiz_data[level]

# 2列のカラムを作成
col1, col2 = st.columns([2, 1])

# カラム1: 初期のテキストを表示
with col1:
    st.title("九九を覚えよう！")
    st.header(f"全部で5問だよ")
    st.subheader(f"{name}さんは、何問正解できるかな？")

# 問題を出題するボタンが押されたときの処理
if st.button("もんだい") and st.session_state.question_count < 5:
    index = np.random.randint(0, len(word_pairs))
    question = list(word_pairs.keys())[index]
    st.session_state.current_question = question
    st.session_state.current_answer = word_pairs[question]
    st.markdown(f"## {question}")

# 現在の問題がセッションにある場合は表示する
if "current_question" in st.session_state:
    with col1:
        st.markdown(f"## {st.session_state.current_question}")

        # 答えの入力フィールド
        answer = st.text_input("こたえを書いてね")

        # 答え合わせボタンが押されたときの処理
        if st.button("こたえあわせ"):
            with col2:
                if answer == st.session_state.current_answer:
                    st.session_state.score += 1
                    image = random.choice(correct_images)
                    st.subheader("やったね！せいかいだよ！")
                else:
                    image = random.choice(incorrect_images)
                    st.subheader(f"ざんねん　正解は 「{st.session_state.current_answer}」 です。")
                st.image(image, use_column_width=True)

                # 問題カウンターを更新
                st.session_state.question_count += 1

# 結果発表とリセットボタンを表示する
if st.session_state.question_count == 5:
    st.write("## けっかはっぴょう！")
    if st.session_state.score == 5:
        st.subheader(f"{name}さん、おめでとう！全問正解だよ！")
      
        st.image(perfect_image, use_column_width=True)
    elif st.session_state.score >= 3:
        st.subheader(f"{st.session_state.score} 問正解、がんばれあともうちょっとだよ！")
        st.image(mousukosi_image, use_column_width=True)
    else:
        st.subheader(f"正解は{st.session_state.score} 問だよ。もっとがんばろう！")
        st.image(zannen_image, use_column_width=True)

    if st.button("リセットする"):
        # セッション変数を初期化して、問題を再度出題可能にする
        st.session_state.score = 0
        st.session_state.question_count = 0
        if "current_question" in st.session_state:
            del st.session_state.current_question
            del st.session_state.current_answer
        st.experimental_rerun()
