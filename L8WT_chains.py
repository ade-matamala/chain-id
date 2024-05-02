import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile, 'r') as file:
    pdb = file.readlines()
file.close()

def replace(chain_ID,file, line):
    if line.startswith("ATOM"):
        l = line[:21] + chain_ID + line[22:]
        file.write(l)
    else:
        file.write(line)

with open(outFile, 'w') as file:
    chain = ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'O']
    LSU = 7013 #number of atoms
    LIG = 29
    
    cuts = [4+LSU, 4+LSU+LIG,
            4+2*LSU+LIG, 4+2*LSU+2*LIG,
            4+3*LSU+2*LIG, 4+3*LSU+3*LIG,
            4+4*LSU+3*LIG, 4+4*LSU+4*LIG,
            4+5*LSU+4*LIG, 4+5*LSU+5*LIG,
            4+6*LSU+5*LIG, 4+6*LSU+6*LIG,
            4+7*LSU+6*LIG, 4+7*LSU+7*LIG,
            4+8*LSU+7*LIG, 4+8*LSU+8*LIG,]
    
    i = 0           
    for line in pdb:
        if False:
            pass
        
        elif i < cuts[0]:
            replace(chain[0],file, line)
        elif i < cuts[1]:
            replace('X',file, line)

        elif i < cuts[2]:
            replace(chain[1],file, line)
        elif i < cuts[3]:
            replace('X',file, line)

        elif i < cuts[4]:
            replace(chain[2],file, line)
        elif i < cuts[5]:
            replace('X',file, line)

        elif i < cuts[6]:
            replace(chain[3],file, line)
        elif i < cuts[7]:
            replace('X',file, line)

        elif i < cuts[8]:
            replace(chain[4],file, line)
        elif i < cuts[9]:
            replace('X',file, line)

        elif i < cuts[10]:
            replace(chain[5],file, line)
        elif i < cuts[11]:
            replace('X',file, line)

        elif i < cuts[12]:
            replace(chain[6],file, line)
        elif i < cuts[13]:
            replace('X',file, line)

        elif i < cuts[14]:
            replace(chain[7],file, line)
        elif i < cuts[15]:
            replace('X',file, line)
            
        else:
            file.write(line)
        i += 1
file.close()