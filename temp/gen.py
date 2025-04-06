import sys

# This script generates a PDB file with specific chain IDs based on the input specifications.

# Define a function to display the help message
help_message = """
    This script generates a PDB file with specific chain IDs based on the input specifications.

    Usage:
        python gen.py -i <input.pdb> -o <output.pdb> -l <ligand_file.txt>

    Arguments:
        <input.pdb>      : The input PDB file.
        <output.pdb>     : The output PDB file with updated chain IDs. 
        <ligand_file.txt> : A text file containing ligand names (optional).

    Options:
        -h, --help       : Display this help message and exit.
    """
correct_usage = "Correct usage: python gen.py -i <input.pdb> -o <output.pdb> -l <ligand_file.txt>"
# Check for help flag
if '-h' in sys.argv or '--help' in sys.argv:
    print(help_message)
    sys.exit(0)
elif len(sys.argv) > 7 or len(sys.argv) < 5: #Check if the correct number of arguments is provided
    print("Incorrect number of arguments!")
    print(correct_usage)
    sys.exit(1)

# Read files from command line arguments
if '-i' in sys.argv: #Check if the input file flag is present
    input_index = sys.argv.index('-i') + 1
    if input_index < len(sys.argv):
        input_File = sys.argv[input_index]
    else:
        print("Input file not provided!")
        print(correct_usage)
        sys.exit(1)
if '-o' in sys.argv: #Check if the output file flag is present
    output_index = sys.argv.index('-o') + 1
    if output_index < len(sys.argv):
        output_File = sys.argv[output_index]
    else:
        print("Output file not provided!")
        print(correct_usage)
        sys.exit(1)
if '-l' in sys.argv: #Check if the ligand file flag is present
    ligands_index = sys.argv.index('-l') + 1
    if ligands_index < len(sys.argv): #Check if the ligand file is provided
        ligands_File = sys.argv[ligands_index]
        with open(ligands_File, 'r') as file: #Read the ligand file
            ligands = file.read().splitlines()
        file.close()
else: 
    print("Ligand file not provided. Defaulting to no ligands.")
    ligands = ""

ligands_number = len(ligands) #Extract the ligand number from the first line of the specifications
if ligands_number > 0: #Check if ligands are present
    print(f"Found {ligands_number} ligands in the specifications file.")
    for i in range(ligands_number):
        print(f"Found ligand number {i+1}: {ligands[i]}")
else: #If no ligands are present, set the variable to False
    ligands = ""
    print("Found no ligands.")

# Read the input PDB file
with open(input_File, 'r') as file:
    pdb = file.read().splitlines()
file.close()

pdb_split = [] 
for line in pdb:
    if line.startswith("ATOM"):
        pdb_split.append(line.split())

lig_ID = []
for line in pdb_split:
    for lig in ligands:
        if lig in line[3]:
            lig_ID.append(line[4])
lig_ID = list(set(lig_ID)) #Get the unique ligand IDs

atom_type = []
atom_type_with_lig = []
for line in pdb_split:
    atom_type_with_lig.append(line[2])
    if line[4] not in lig_ID: 
        atom_type.append(line[2]) #Extract the atom type from the PDB file


counter = 0
chain_atomID = [0]
for i in atom_type:
    counter += 1
    if i == 'OXT':
        chain_atomID.append(counter) 
counter = 0
chain_atomID_with_lig = [0]
for i in atom_type_with_lig:
    counter += 1
    if i == 'OXT':
        chain_atomID_with_lig.append(counter) 
print(f"Found {len(chain_atomID)-1} chains in the PDB file.")
chain_len = []
for i in range(len(chain_atomID)-1):
    chain_len.append(chain_atomID[i+1] - chain_atomID[i]) #Calculate the length of each chain
    print(f"Chain {i+1} length: {chain_len[i]} atoms")

unique_chain_len = list(set(chain_len)) #Get the unique chain lengths
print(f"Found {len(unique_chain_len)} unique chains in the PDB file.")
for i in range(len(unique_chain_len)):
    print(f"Unique chain {i+1} length: {chain_len[i]} atoms")

letter = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'

with open(output_File, 'w') as file:
    print(f"Writing to {output_File}...")
    counter = 0
    for line in pdb:
        if line.startswith("ATOM"):
            counter += 1
            l = line.split()
            if l[3] not in ligands:
                for i in range(len(chain_atomID_with_lig)-1):
                    if counter >= chain_atomID_with_lig[i]+1 and counter < chain_atomID_with_lig[i+1]+1:
                        new_line = line[:21] + letter[i] + line[22:]
                        file.write(new_line + '\n')
            else:
                new_line = line[:21] + 'X' + line[22:]
                file.write(new_line + '\n')

        else:
            file.write(line + '\n')