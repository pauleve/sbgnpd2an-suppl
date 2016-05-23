SCRIPTS/sbgnpd2an/sbgnpd2an \
 --initial-state a3,a14,a13,sa854,a45,a40,a212,a39,a634,a35,a41,a36,a37,a38,a211,a633,a1,a4,a18,a5,a2,a815,a765,a678,a590,a651,a700,a760,a682,a691,a278,a613,a673,a665,a185,sa382,a23,sa378,a280,a874,a856,a857,a855,a635,a661,a662,a159,a875,a158,a157,a25,a309,a414,a53,a54,a944,a164,a165,a307,a308,a341,a785,a27\
 --names-are-ids\
 MODELS/RB_E2F/maps/e2f_rb_no_genes.sbgn > MODELS/RB_E2F/analysis/an/nostories/nostories.an
#%s/ STORY \([a-z0-9_]*\)\n\([a-z0-9,]*\)/ --story \1=\2 \\/
