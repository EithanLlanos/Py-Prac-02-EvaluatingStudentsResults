class StudentsDataException(Exception):
    def __init__(self,message):
        super().__init__(message)

class BadLine(StudentsDataException):
    def __init__(self,line,txt):
        return super().__init__(message=f"There is an error in the format of the line {line}: {txt}")

class FileEmpty(StudentsDataException):
    def __init__(self,name):
        return super().__init__(message=f"The file named {name} has no data")
        
try:
    srcN=input("Enter the source file name:\n")
    srcF=open(srcN,"r")
except Exception as e:
    print(f'Error {e.__class__.__name__}:\nThere is no such a file called "{srcN}" or it cant be opened')
    exit(0)
buffer=524288
dict={}
line=0
readin=srcF.readline(buffer)
try:
    if readin=="":
        raise FileEmpty(srcN)
    while readin!="":
        
        try:
            # readin=str(readin).split(maxsplit=3)
            # val=readin[0]+" " + readin[1]
            # dict[val]=round(dict.get(val,0)+float(readin[2]),1)
            val=str(readin).split(maxsplit=3)
            val[0]=val[0]+" " + val[1]
            dict[val[0]]=round(dict.get(val[0],0)+float(val[2]),1)
        except:
            raise BadLine(line,readin)
        readin=srcF.readline(buffer)
        line+=1
    dict=sorted(dict.items(),key=lambda x: x[0][0])
except FileEmpty as e:
    print("Error: ",e.__class__.__name__)
    print(e)
    exit(0)
except BadLine as e:
    print("Error: ",e.__class__.__name__)
    print(e)
    exit(0)
    
print("Report:")
for k,v in dict:
    print('{:<20}{:0>4.1f}'.format(k,v))