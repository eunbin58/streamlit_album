import streamlit as st

print("page_reloaded")

st.set_page_config(
    page_title="ALBUM",
    page_icon="🎞️"
)

st.title("streamlit Album")
st.subheader("좋아하는 사진을 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "인물": "👶",
    "풍경": "🌠",
    "여행": "✈️",
    "접사": "🖼️",
    "패션": "🧥",
    "음식": "🍮",
    "거리": "🌉",
    "스포츠": "🏀",
    "연예인": "✨",
    "기타": "🪐",
}

initial_pokemons = [
    {
        "name": "신유",
        "year": "2003.11.07",
        "types": ["연예인","인물"],
        "image_url": "https://i.namu.wiki/i/xg7H1tfTWj7cCCPbTOBbWHHS9jXPS8NtZetRub105icSvUaz_axwg_znyrrTlinRp24Kv3Pync1vLBu2qqPVviEKODGT9e5fu4MdPNQaLmy0a52Oh-AbYn4nw90kLewaFdd309ZvshJSXOL5WmiNrA.webp"
    },
    {
        "name": "도훈",
        "year": "2005.01.30",
        "types": ["연예인","인물"],
        "image_url": "https://i.namu.wiki/i/B-XpEg_dH-3zgjVlG9nbdbCJc4UBvUmSgFm6gF4rPI3jFoRba07qOWECyZpLAEgVChzeYrC6FQ9giNST_oJiGcmU3RUovgXVec2PuEmHU_m_Ks94Rh8bzdBzdUH71KGvK_tGZXZAOeG02ByI9Eux1g.webp",
    },
    {
        "name": "고우석",
        "year": "1998.08.06",
        "types": ["인물"],
        "image_url": "https://i.namu.wiki/i/j9pM_AwVrQW5sItCcXMTWMlUxzPLy7kqLCuM0anTdDdfBmiEmD3KPi8w71kU7nQnsriJ1ch7BkSA7uPxsEbRq457vnjI9TENxs9wv3JvxRE2Tn7TDdvfA8YK0kOhMUGU_bDXfSwZ3a_wDP1qR-K0gg.webp",
    },
    {
        "name": "손흥민",
        "year": "1992.07.08",
        "types": ["인물"],
        "image_url": "https://i.namu.wiki/i/4v0p9UFadP2A0t2yjFRxxbOHXDnI_D10Dbf_4SpASVdO4nxQUjgRbozw4IyRczQtPRGIBHKGAcggnZgI2-nLl0oR65XRkok0vTOe7rhaeejlV_g2ojqy0U9KCW_6nz2--VkGZVMv-u5Dc3paTxkm8A.webp"
    },
]

example_pokemon = {
    "name": "에클레르",
    "year": "2024.05.20",
    "types": ["음식"],
    "image_url": "https://i.namu.wiki/i/8ek2lK8b_e21GP2J6tnzgzN8g_o6jYCcyp5tItg5WA_W9a-a5Ih8JrN2mG-ufESLABsMszLSB5ZmcCa1_U9rthIwzKd2WbFZ6YINRcxYPrJjcIfhtPfhzLAMYyO_DFBTASdmHu09tTyHtVDhiU8zFA.webp"
}

if "pokemons"not in st.session_state:
    st.session_state.pokemons=initial_pokemons


auto_complete =st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)

with st.form(key="form"):
    col1, col2, col3=st.columns(3)
    with col1:
        name=st.text_input(
            label="사진 이름",
            value=example_pokemon["name"] if auto_complete else ""
            )
    with col2:
        year=st.text_input(
            label="사진 연도",
            value=example_pokemon["year"] if auto_complete else ""
            )
    with col3:
        types=st.multiselect(
            label="사진 종류",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
            )
        
    image_url=st.text_input(
        label="사진 URL",
        value=example_pokemon["image_url"] if auto_complete else ""
        )

    submit=st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("사진 이름을 입력해주세요.")
        if not year:
            st.error("사진 연도를 입력해주세요.")
        if len(types)==0:
            st.error("사진 종류를 적어도 한개 선택해주세요")
        else:
            st.success("사진을 추가할 수 있습니다.")
            st.session_state.pokemons.append({
                "name":name,
                "year":year,
                "types":types,
                "image_url":image_url if image_url else "./images/default.png"
            })


for i in range(0,len(st.session_state.pokemons),4):
    row_pokemons =st.session_state.pokemons[i:i+4]
    cols = st.columns(4)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon=row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']} / {pokemon['year']}**", expanded=True):
            # st.subheader(pokemon["name"])
                st.image(pokemon["image_url"],)

                emoji_types =[f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.subheader(" / ".join(emoji_types))
                delete_button =st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i+j]
                    st.rerun()

