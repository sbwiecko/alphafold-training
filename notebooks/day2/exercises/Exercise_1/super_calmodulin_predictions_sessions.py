
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
  fold_calmodulin.zip             fold_calmodulin_ca_model_0.cif
  fold_calmodulin_ca.zip          fold_calmodulin_model_0.cif   
 parser: matching files:
  fold_calmodulin_ca.zip          fold_calmodulin_model_0.cif   
  fold_calmodulin_ca_model_0.cif
PyMOL>load fold_calmodulin_model_0.cif, calmodulin_prediction
 ExecutiveLoad-Detail: Detected mmCIF
 CmdLoad: "fold_calmodulin_model_0.cif" loaded as "calmodulin_prediction".
 parser: no matching files.
 parser: matching files:
  fold_calmodulin.zip             fold_calmodulin_ca_model_0.cif
  fold_calmodulin_ca.zip          fold_calmodulin_model_0.cif   
 parser: matching files:
  fold_calmodulin_ca.zip          fold_calmodulin_ca_model_0.cif
PyMOL>load fold_calmodulin_ca_model_0.cif, calmodulin_ca_prediction
 ExecutiveLoad-Detail: Detected mmCIF
 CmdLoad: "fold_calmodulin_ca_model_0.cif" loaded as "calmodulin_ca_prediction".
 parser: no matching color.
 parser: no matching color.
 parser: matching selection:
  calmodulin_ca_prediction  calmodulin_prediction   
PyMOL>color firebrick, calmodulin_ca_prediction
 Executive: Colored 1178 atoms and 1 object.
PyMOL>color tomato, calmodulin_ca_prediction
 Error: Unknown color.
PyMOL>color 0xff4c00, calmodulin_ca_prediction
 Executive: Colored 1178 atoms and 1 object.
PyMOL>color 0xff8b00, calmodulin_ca_prediction
 Executive: Colored 1178 atoms and 1 object.
 parser: matching selection:
  calmodulin_ca_prediction  calmodulin_prediction   
PyMOL>color 0x58578c, calmodulin_prediction
 Executive: Colored 1174 atoms and 1 object.
 parser: matching selection:
  calmodulin_ca_prediction  calmodulin_prediction   
 parser: matching selection:
  calmodulin_ca_prediction  calmodulin_prediction   
PyMOL>super calmodulin_prediction, calmodulin_ca_prediction
 MatchAlign: aligning residues (149 vs 149)...
 MatchAlign: score 718.978
 ExecutiveAlign: 1126 atoms aligned.
 ExecutiveRMS: 26 atoms rejected during cycle 1 (RMSD=1.16).
 ExecutiveRMS: 9 atoms rejected during cycle 2 (RMSD=1.03).
 ExecutiveRMS: 5 atoms rejected during cycle 3 (RMSD=1.02).
 ExecutiveRMS: 1 atoms rejected during cycle 4 (RMSD=1.01).
 Executive: RMSD =    1.010 (1085 to 1085 atoms)
PyMOL>ray
 Ray: render time: 1.05 sec. = 3445.0 frames/hour (1.05 sec. accum.).
 ScenePNG: wrote 892x640 pixel image to file "C:/Users/Sébastien/alphafold-training/docs/day2/data/Exercise_1/super_calmodulin_predictions.png".
PyMOL>fetch 1cfd, calmodulin_apo
TITLE     CALCIUM-FREE CALMODULIN
 ExecutiveLoad-Detail: Detected mmCIF
 CmdLoad: ".\1cfd.cif" loaded as "calmodulin_apo".
PyMOL>fetch 1cll, calmodulin_ca
TITLE     CALMODULIN STRUCTURE REFINED AT 1.7 ANGSTROMS RESOLUTION
 ExecutiveLoad-Detail: Detected mmCIF
 CmdLoad: ".\1cll.cif" loaded as "calmodulin_ca".
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>hide everything, calmodulin_ca_prediction
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>hide everything, calmodulin_ca
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
 parser: no matching selection.
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>super calmodulin_apo, calmodulin_prediction
 MatchAlign: aligning residues (148 vs 149)...
 MatchAlign: score 530.853
 ExecutiveAlign: 1058 atoms aligned.
 ExecutiveRMS: 24 atoms rejected during cycle 1 (RMSD=11.13).
 ExecutiveRMS: 24 atoms rejected during cycle 2 (RMSD=10.55).
 ExecutiveRMS: 32 atoms rejected during cycle 3 (RMSD=10.06).
 ExecutiveRMS: 34 atoms rejected during cycle 4 (RMSD=9.41).
 ExecutiveRMS: 30 atoms rejected during cycle 5 (RMSD=8.69).
 Executive: RMSD =    8.075 (914 to 914 atoms)
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>zoom calmodulin_apo
PyMOL>ray
 Ray: render time: 0.85 sec. = 4250.3 frames/hour (1.89 sec. accum.).
 ScenePNG: wrote 892x640 pixel image to file "C:/Users/Sébastien/alphafold-training/docs/day2/data/Exercise_1/super_calmodulin_apo_prediction.png".
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>hide everything, calmodulin_apo
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>show cartoon, calmodulin_ca
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>super calmodulin_ca, calmodulin_prediction
 MatchAlign: aligning residues (148 vs 149)...
 MatchAlign: score 675.617
 ExecutiveAlign: 1110 atoms aligned.
 ExecutiveRMS: 25 atoms rejected during cycle 1 (RMSD=2.68).
 ExecutiveRMS: 14 atoms rejected during cycle 2 (RMSD=2.53).
 ExecutiveRMS: 3 atoms rejected during cycle 3 (RMSD=2.47).
 Executive: RMSD =    2.464 (1068 to 1068 atoms)
 parser: matching selection:
  calmodulin_apo            calmodulin_ca_prediction
  calmodulin_ca             calmodulin_prediction   
PyMOL>zoom calmodulin_prediction
PyMOL>ray
 Ray: render time: 1.04 sec. = 3451.6 frames/hour (2.94 sec. accum.).
 ScenePNG: wrote 892x640 pixel image to file "C:/Users/Sébastien/alphafold-training/docs/day2/data/Exercise_1/super_calmodulin_ca_prediction.png".
 Save: Please wait -- writing session file...
 Save: wrote "C:/Users/Sébastien/alphafold-training/docs/day2/data/Exercise_1/super_calmodulin_predictions.pse".
 Save: Please wait -- writing session file...
 Save: wrote "C:/Users/Sébastien/alphafold-training/docs/day2/data/Exercise_1/super_calmodulin_predictions.psw".
