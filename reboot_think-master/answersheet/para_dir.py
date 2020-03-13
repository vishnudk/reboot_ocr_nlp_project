def split_paragraph(text_data):
    i=0
    para = ["" for x in range(100)]
    print(para)
    for line in text_data.splitlines():
        #print('---------')
        if line[0].isdigit():
            i=i+1
            #print(line)
            para[i]=" "
        para[i]=para[i]+line
    return para
def print_required_ans(para):   #creates a dir
#     no=str(input())
    j=0
    para_di={}
    for i in para:
        #tmp_txt=i
        if i:
            for j in i:
                if j and j.isdigit():
                    print(j)
                    para_di[j]=i
                    break
    return para_di
                    
def create_dir(text):
    text1=split_paragraph(text)
    for i  in text1:
        print("===================")
        print(i)
    text2=print_required_ans(text1)
    return text2