# 테스트 케이스 13번 16번이 틀림
# 왜 틀린건지 ..??

import re


def solution(word, pages):
    answer = 0
    word = word.lower()

    # 검색어 찾기 - 기본 점수
    score = []
    for i, page in enumerate(pages):
        cnt = re.sub('[^a-zA-Z]', ' ', page).lower().split().count(word.lower())
        score.append([i, cnt, 0, 0])
    print(score)

    # 웹페이지 url 찾기
    url_list = [["", []] for _ in range(len(pages))]
    for i, page in enumerate(pages):
        # url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        # url_list[i][0] = url
        # score[i][0] = url
        for tag in page.split("\n"):
            if "<meta" in tag and "content" in tag:
                start = tag.find("content=") + 9
                end = tag.find("\"/>")
                url_list[i][0] = tag[start:end]
                score[i][0] = tag[start:end]
    print(url_list)
    print(score)
    print()

    # 모든 외부 링크 찾기
    for i, page in enumerate(pages):

        exiosLink = re.findall('<a href="(https://[\S]*)"', page)
        for url in url_list:
            for exlink in exiosLink:
                if url[0] == exlink:
                    score[i][2] += 1
                    url[1].append(i)
    print(url_list)
    print(score)
    print()

    # 링크 점수 계산
    for i in range(len(score)):
        if score[i][2] == 0:
            score[i][3] = 0
        else:
            score[i][3] = score[i][1] / score[i][2]
    print(url_list)
    print(score)

    # 결과
    result = []
    for i in range(len(url_list)):
        link_score = 0
        for j in range(len(url_list[i][1])):
            link_score += score[url_list[i][1][j]][3]
        result.append([i, score[i][1] + link_score])
    print(result)
    result.sort(key=lambda x: (-x[1], x[0]))
    answer = result[0][0]

    return answer


word = "muzi"
pages = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"
]

answer = solution(word, pages)
print("answer:", answer)
