for num in [10,100]:
    input_filename = "./in"+str(num)+".txt"
    output_filename = "./out"+str(num)+"_sample_actual.txt"
    print(input_filename)
    print(output_filename)
    file = open(input_filename)
    file_out = open(output_filename,'w')
    linesRaw = file.readlines()
    arraySize = int(linesRaw[0])
    A = []
    for i in range(0,arraySize):
        A.append(0)
    lineIndex=1
    while(lineIndex<=(len(linesRaw)-1)):
        nums = linesRaw[lineIndex].split()
        if(len(nums)==0):
            break
        for num in nums:
            A[int(num)] = A[int(num)] + 1
        lineIndex=lineIndex+1
    i=0
    for a in A:
        for j in range(0,a):            
            file_out.write(str(i) + " ")
        i=i+1