Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insert(filename,*ad):
...     f=open(filename,'a')
...     for i in ad:
...         f.write(str(i)+'\t')
...     f.write('\n')
...     f.close()
... def extract(filename):
...     f=open(filename)
...     z=f.readlines()
...     a=[]
...     n=0
...     for i in z:
...         word=""
...         l=[]
...         for j in i:
...             if j=='\t':
...                 l.append(word)
...                 word=""
...             else:
...                 word+=j
...         a.append(l)
...         n+=1
...     f.close()
...     return a
... def main():
...     print("1.about students:")
...     print("2.about teachers:")
...     print("3.about school faculty:")
...     print("4.about fees:")
...     a=int(input("enter choice:"))
...     if a==1:
...         print("1.registration of a student:")
...         print("2.information of a student:")
...         b=int(input("enter choice:"))
...         if b==1:
...             ID=int(input("ID:"))
...             name=input("NAME:")
...             Class=input("CLASS:")
...             subject=input("SUBJECT:")
...             gender=input("GENDER-M/F:")
...             address=input("ADDRESS:")
...             phone=input("PHONE NO.:")
...             fees=input("FEES DEPOSITED-Rs:")
...             insert("data.txt",ID,name,Class,subject,gender,address,phone,fees)
...             print("information saved:")
...         elif b==2:
...             Id=input("enter ID:")
...             l=extract("data.txt")
...             t=0
...             for i in range(len(l)):
...                 if l[i][0]==Id:
...                     t=1
...                     print("ID:",l[i][0])
...                     print("NAME:",l[i][1])
...                     print("CLASS:",l[i][2])
...                     print("SUBJECT:",l[i][3])
...                     print("GENDER:",l[i][4])
...                     print("ADDRESS:",l[i][5])
...                     print("PHONE NO.:",l[i][6])
...             if t==0:
...                 print("ID not found:")
...     elif a==2:
...         print("1.registration of a teacher:")
...         print("2.information of a teacher:") 
...         c=int(input("enter choice:"))
...         if c==1:
            D=int(input("ID:"))
            NAME=input("NAME:")
            CLASS=input("CLASS:")
            SUBJECT=input("SUBJECT APPOINTED:")
            SEX=input("GENDER-M/F:")
            ADDRESS=input("ADDRESS:")
            PHONE=input("PHONE NO.:")
            insert("teacher.txt",D,NAME,CLASS,SUBJECT,SEX,ADDRESS,PHONE)
            print("information saved:")
        elif c==2:
            Id=input("enter ID:")
            l=extract("teacher.txt")
            s=0
            for j in range(len(l)):
                if l[j][0]==Id:
                    s=1
                    print("ID:",l[j][0])
                    print("NAME:",l[j][1])
                    print("CLASS:",l[j][2])
                    print("SUBJECT APPOINTED:",l[j][3])
                    print("GENDER:",l[j][4])
                    print("ADDRESS:",l[j][5])
                    print("PHONE NO.:",l[j][6])
            if s==0:
                print("ID not found:")
    elif a==3:
        print("1.sports faculty:")            
        print("2.library faculty:")
        print("3.computer lab faculty:")
        d=int(input("enter choice:"))
        if d==1:
            ba=input("no. of good badminton:")
            ba1=input("no. of damaged badminton:")
            b=input("no. of balls:")
            b1=input("no. of damaged balls:")
            t=input("no. of table tennis:")
            t1=input("no. of damaged table tennis:")
            insert("sports.txt",ba,ba1,b,b1,t,t1)
            print("information saved:")
        elif d==2:
            s=input("no. of science books:")
            s1=input("no. of required science books:")
            m=input("no. of maths books:")
            m1=input("no. of required maths books:")
            c=input("no. of computer books:")
            c1=input("no. of required computer books:")
            insert("library.txt",s,s1,m,m1,c,c1)
            print("information saved:")
        elif d==3:
            comp=int(input("no. of systems:"))
            comp1=int(input("no. of damaged systems:"))
            comp2=int(input("no. of required systems:"))
            insert("computer.txt",comp,comp1,comp2)
            print("information saved:")
    elif a==4:
        Id=input("enter ID:")
        p=extract("data.txt")
        e=0
        for k in range(len(p)):
            if p[k][0]==Id:
                e=1
                print("NAME:",p[k][1])
                print("TOTAL AMOUNT-Rs:10000")
                print("AMOUNT DEPOSITED-Rs:",p[k][7])
                z=10000-int(p[0][7])
                print("AMOUNT LEFT-Rs:",z)
        if e==0:
            print("ID not found:")
    ch=input("back/exit:").lower()
    if ch=="back":
        main()
    else:
        exit()
