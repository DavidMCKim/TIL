# 051 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
print('051')
movie_rank =['닥터 스트레인지', '스플릿', '럭키']
print("---------------------------------")
print()

# 052 movie_rank 리스트에 "배트맨"을 추가하라.
print('052')
movie_rank.append("배트맨")
print(movie_rank)
print("---------------------------------")
print()

# 053 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. '슈퍼맨'을 '닥터 스트레인지'와 '스플릿'사이에 추가하라. **
# 리스트의 insert(인덱스, 원소) 메서드를 사용하면 특정 위치에 값을 끼어넣기 할 수 있습니다.
print('053')
movie_rank = ['닥터스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)
print("---------------------------------")
print()

# 054 movie_rank 리스트에서 '럭키'를 삭제하라. **
print('054')
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
del movie_rank[3]
print(movie_rank)
print("---------------------------------")
print()


# 055 movie_rank 리스트에서 '스플릿'과 '배트맨'을 삭제하라. **
print('055')
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# movie_rank.remove('스플릿')
# movie_rank.remove('배트맨')
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
print("---------------------------------")
print()

# 056 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
print('056')
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
print("---------------------------------")
print()

# 057 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
print('057')
nums = [1, 2, 3, 4, 5, 6, 7]
MAX = max(nums)
MIN = min(nums)
print('max : %s' % MAX)
print('min : %s' % MIN)
print("---------------------------------")
print()

# 058 다음 리스트의 합을 출력하라.
print('058')
nums = [1, 2, 3, 4, 5]
s = sum(nums)
print(s)
print("---------------------------------")
print()

# 059 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
print('059')
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
print("---------------------------------")
print()

# 060 다음 리스트의 평균을 출력하라.
print('060')
nums = [1, 2, 3, 4, 5]
s = sum(nums)
l = len(nums)
avg = s / l
print(avg)
print("---------------------------------")
print()
