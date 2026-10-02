
 PyMOL(TM) Molecular Graphics System, Version 3.2.0a.
 Copyright (c) Schrodinger, LLC.
 All Rights Reserved.
 
    Created by Warren L. DeLano, Ph.D. 
 
    PyMOL is user-supported open-source software.  Although some versions
    are freely available, PyMOL is not in the public domain.
 
    If PyMOL is helpful in your work or study, then please volunteer 
    support for our ongoing efforts to create open and affordable scientific
    software by purchasing a PyMOL Maintenance and/or Support subscription.
 
    More information can be found at "http://www.pymol.org".
 
    Enter "help" for a list of commands.
    Enter "help <command-name>" for information on a specific command.
 
 Hit ESC anytime to toggle between text and graphics.
 
 Detected OpenGL version 4.6. Shaders available.
 Detected GLSL version 4.60.
 OpenGL graphics engine:
  GL_VENDOR:   Intel
  GL_RENDERER: Intel(R) Iris(R) Xe Graphics
  GL_VERSION:  4.6.0 - Build 32.0.101.6737
 Detected 8 CPU cores.  Enabled multithreaded rendering.
 
PyMOL>viewport 640,480
 parser: matching files:
  CD40L_ef6d8.result.zip                                                    
  CD40L_ef6d8_unrelaxed_rank_001_alphafold2_multimer_v3_model_2_seed_000.pdb
  CD40L_prediction.ipynb                                                    
 parser: no matching files.
 parser: matching files:
  CD40L_ef6d8.result.zip                                                    
  CD40L_ef6d8_unrelaxed_rank_001_alphafold2_multimer_v3_model_2_seed_000.pdb
PyMOL>load CD40L_ef6d8_unrelaxed_rank_001_alphafold2_multimer_v3_model_2_seed_000.pdb, CD40L_prediction
 CmdLoad: "" loaded as "CD40L_prediction".
PyMOL>load 3QD6.cif.gz, CD40-CD40L_crystal
TITLE     Crystal structure of the CD40 and CD154 (CD40L) complex
 ExecutiveLoad-Detail: Detected mmCIF
 CmdLoad: "3QD6.cif.gz" loaded as "CD40-CD40L_crystal".
 You clicked /CD40-CD40L_crystal/I/T/HIS`78/CA
 Selector: selection "sele" defined with 10 atoms.
 You clicked /CD40-CD40L_crystal/E/E/ALA`173/CA
 Selector: selection "sele" defined with 15 atoms.
 You clicked /CD40-CD40L_crystal/F/F/ALA`173/CA
 Selector: selection "sele" defined with 20 atoms.
 You clicked /CD40-CD40L_crystal/D/D/LEU`168/CA
 Selector: selection "sele" defined with 28 atoms.
PyMOL>hide everything, all
 parser: matching selection:
  CD40-CD40L_crystal  CD40L_prediction  
PyMOL>show cartoon, CD40-CD40L_crystal and (chain D or chain E or chain F)
 parser: matching commands:
  extra_fit  extract  
PyMOL>extract CD40L_trimer, CD40-CD40L_crystal and (chain D or chain E or chain F)
 parser: no matching representation.
 parser: no matching representation.
PyMOL>show cartoon, CD40L_prediction
PyMOL>super CD40L_prediction, CD40L_trimer
 MatchAlign: aligning residues (783 vs 447)...
 MatchAlign: score 939.492
 ExecutiveAlign: 2967 atoms aligned.
 ExecutiveRMS: 79 atoms rejected during cycle 1 (RMSD=2.58).
 ExecutiveRMS: 222 atoms rejected during cycle 2 (RMSD=1.27).
 ExecutiveRMS: 191 atoms rejected during cycle 3 (RMSD=0.82).
 ExecutiveRMS: 125 atoms rejected during cycle 4 (RMSD=0.61).
 ExecutiveRMS: 67 atoms rejected during cycle 5 (RMSD=0.53).
 Executive: RMSD =    0.505 (2279 to 2279 atoms)
 Executive: Colored 6162 atoms and 1 object.
 You clicked /CD40L_prediction//A/LEU`100/CA
 Selector: selection "sele" defined with 8 atoms.
PyMOL>ray
 Ray: render time: 4.01 sec. = 898.9 frames/hour (4.01 sec. accum.).
 ScenePNG: wrote 1029x687 pixel image to file "C:/Users/Sébastien/alphafold-training/docs/day1/data/Exercise_5/super_CD40L_trimer_ECD.png".
