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
    chain = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    LSU = 7013 #number of atoms
    SSU = 1594
    LIG = 29
    
    cuts = [4+LSU               , 4+LSU+SSU             , 4+LSU+SSU+LIG,
            4+2*LSU+SSU+LIG     , 4+2*LSU+2*SSU+LIG     , 4+2*LSU+2*SSU+2*LIG,
            4+3*LSU+2*SSU+2*LIG , 4+3*LSU+3*SSU+2*LIG   , 4+3*LSU+3*SSU+3*LIG,
            4+4*LSU+3*SSU+3*LIG , 4+4*LSU+4*SSU+3*LIG   , 4+4*LSU+4*SSU+4*LIG,
            4+5*LSU+4*SSU+4*LIG , 4+5*LSU+5*SSU+4*LIG   , 4+5*LSU+5*SSU+5*LIG,
            4+6*LSU+5*SSU+5*LIG , 4+6*LSU+6*SSU+5*LIG   , 4+6*LSU+6*SSU+6*LIG,
            4+7*LSU+6*SSU+6*LIG , 4+7*LSU+7*SSU+6*LIG   , 4+7*LSU+7*SSU+7*LIG,
            4+8*LSU+7*SSU+7*LIG , 4+8*LSU+8*SSU+7*LIG   , 4+8*LSU+8*SSU+8*LIG]
    
    i = 0           
    for line in pdb:
        if False:
            pass
        
        elif i < cuts[0]:
            replace(chain[0],file, line)
        elif i < cuts[1]:
            replace(chain[1],file, line)
        elif i < cuts[2]:
            replace('X',file, line)

        elif i < cuts[3]:
            replace(chain[2],file, line)
        elif i < cuts[4]:
            replace(chain[3],file, line)
        elif i < cuts[5]:
            replace('X',file, line)

        elif i < cuts[6]:
            replace(chain[4],file, line)
        elif i < cuts[7]:
            replace(chain[5],file, line)
        elif i < cuts[8]:
            replace('X',file, line)

        elif i < cuts[9]:
            replace(chain[6],file, line)
        elif i < cuts[10]:
            replace(chain[7],file, line)
        elif i < cuts[11]:
            replace('X',file, line)

        elif i < cuts[12]:
            replace(chain[8],file, line)
        elif i < cuts[13]:
            replace(chain[9],file, line)
        elif i < cuts[14]:
            replace('X',file, line)

        elif i < cuts[15]:
            replace(chain[10],file, line)
        elif i < cuts[16]:
            replace(chain[11],file, line)
        elif i < cuts[17]:
            replace('X',file, line)

        elif i < cuts[18]:
            replace(chain[12],file, line)
        elif i < cuts[19]:
            replace(chain[13],file, line)
        elif i < cuts[20]:
            replace('X',file, line)

        elif i < cuts[21]:
            replace(chain[14],file, line)
        elif i < cuts[22]:
            replace(chain[15],file, line)
        elif i < cuts[23]:
            replace('X',file, line)
            
        else:
            file.write(line)
        i += 1
file.close()