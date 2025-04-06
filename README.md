# chain-id
Script for writing chain IDs into PDB files. 
While working with GROMACS, I found that in the conversion bewteen the original .pdb file to the native .gro file the information about the chains was lost. 
This supposed a problem when I needed to display these files and use the chains to label multimeric proteins. 
Initially, I wrote this script to the specific systems I was working with in 2024. Now, I have generalized it so it can work with other proteins with multiple chains. 
The main problem I see with this script is that it needs an auxilliary .txt file specifying the names of the residues that are considered ligands or not a part of the protein chains. This includes traditional ligands, substrates, prostetic groups, coordinated ions, among others.   
There are 3 tests considered: 
    -Test 1 consists of an homooctameric protein (A8) with two ligands, one bifosfate sugar and a magnesium ion.
    -Test 2 consists of an heterohexadecameric protein (A8B8) with two ligands, one bifosfate sugar and a magnesium ion.
    -Test 3 consists of an homotetrameric protein with one ligand, a heme group coordinating with an iron ion.      