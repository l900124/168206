start='hit'
end='cog'
 adict =[ 'hot','dot','dog','lot','log','dit']
 def find_path(start,end,paths):
     if start==end:
        return "start=end"
     else:
        visited=[]
        visited.append(start)
        for word in visited:
            temp=word
            for i in range(len(word)):
                for j in range(ord('a'),ord('z')+1):
                    word=word[:i]+chr(j)+word[i+1:]
                    print(word)
                    if word in paths and word not in visited:
                        visited.append(word)
                    if word==end:
                        visited.append(word)
                        print("The path is :")
                        print (visited)
                        return
                word=temp 
 find_path(start,end,adict)
