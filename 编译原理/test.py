# 识别 x > 3.14

def test():
    while True:
        s = input()
        ids = [chr(i) for i in range(97,97+26)] + [chr(i) for i in range(65,65+26)]
        num = [str(i) for i in range(10)]
        relation = [">", "<", "="]
        tmp_id = []
        tmp_relation = []
        tmp_num = []
        for i in s:
            if i in ids:
                tmp_id.append(i)
            elif i in num:
                tmp_num.append(i)
            elif i in relation:
                tmp_relation.append(i)
            
            elif i == " ":
                continue
            elif i != "#":
                print("has err", i)
                break
            else:
                print("识别完成")
                print("id:", tmp_id)
                print("num:", tmp_num)
                print("relation:", tmp_relation)

# test()

def test1():
    while True:
        print("start analysis")
        s = input()
        ids = [chr(i) for i in range(97,97+26)] + [chr(i) for i in range(65,65+26)]
        num = [str(i) for i in range(10)]
        relation = [">", "<", "="]
        tmp_id = []
        tmp_relation = []
        tmp_num = []
        i = 0
        while i < len(s):
            if s[i] in ids:
                tmp_id.append(s[i])
                i += 1
            elif s[i] in num:
                tmp = s[i]
                i += 1
                while i < len(s) and (s[i] == "." or s[i] in num):
                    tmp += s[i]
                    i += 1
                else:
                    print("not have Terminator, please restart input")
                tmp_num.append(tmp)
            elif s[i] in relation:
                tmp_relation.append(s[i])
                i += 1

            elif s[i] == " ":
                i += 1
                continue
            elif s[i] != "#":
                print("has err", s[i])
                break
            else:
                print("识别完成")
                print("id:", tmp_id)
                print("num:", tmp_num)
                print("relation:", tmp_relation)
                break

test1()