def solution(files):
    print(files)
    answer = []
    num_files = []
    for i in range(len(files)):
        file = files[i]
        file_size = len(file)
        head, number, tail = '', '', ''
        print(file)
        j = 0
        while True:
            print(file[j])
            if not file[j].isdigit():
                head += file[j]
            else:
                number += file[j]
                if j == file_size - 1 or not file[j + 1].isdigit():
                    break
            j += 1
        tail = file[j + 1:]
        print(head, number, tail)
        num_files.append([head.upper(), int(number), tail, i])
        print()
    print(num_files)

    num_files.sort(key=lambda x: (x[0], x[1]))
    print(num_files)

    for nf in num_files:
        answer.append(files[nf[3]])

    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
answer = solution(files)
print("answer:", answer)
