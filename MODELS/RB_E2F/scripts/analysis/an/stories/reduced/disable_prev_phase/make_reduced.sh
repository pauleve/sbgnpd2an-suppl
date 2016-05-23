echo "---------------"
echo "G0"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdc25c=a816,cdc2=a791,wee1=sa551,cdc20=a858 --reduce-for-goal e2f4=a6 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_G0_e2f4=a6.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdc25c=a816,cdc2=a791,wee1=sa551,cdc20=a858 --reduce-for-goal e2f4=a359 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_G0_e2f4=a359.reduced.an
echo "---------------"
echo "earlyG0"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f4=a6,e2f4=a359 --reduce-for-goal e2f1=a450 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_earlyG1_e2f1=a450.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f4=a6,e2f4=a359 --reduce-for-goal cdk4=a735 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_earlyG1_cdk4=a735.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f4=a6,e2f4=a359 --reduce-for-goal e2f1=a475 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_earlyG1_e2f1=a475.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f4=a6,e2f4=a359 --reduce-for-goal cdk6=a725 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_earlyG1_cdk6=a725.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f4=a6,e2f4=a359 --reduce-for-goal e2f1=a462 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_earlyG1_e2f1=a462.reduced.an
echo "---------------"
echo "lateG1"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f1=a450,cdk4=a735,e2f1=a475,cdk6=a725,e2f1=a462 --reduce-for-goal e2f1=a524 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_lateG1_e2f1=a524.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f1=a450,cdk4=a735,e2f1=a475,cdk6=a725,e2f1=a462 --reduce-for-goal e2f1=a532 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_lateG1_e2f1=a532.reduced.an
echo "---------------"
echo "earlyS"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable e2f1=a524,e2f1=a532 --reduce-for-goal cdk2=a632 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_earlyS_cdk2=a632.reduced.an
echo "---------------"
echo "lateS"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdk2=a632 --reduce-for-goal cdk2=csa89 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_lateS_cdk2=csa89.reduced.an
echo "---------------"
echo "G2"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdk2=csa89 --reduce-for-goal cdc2=a803 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_G2_cdc2=a803.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdk2=csa89 --reduce-for-goal cdc2=a809 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_G2_cdc2=a809.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdk2=csa89 --reduce-for-goal cdc2=a832 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_G2_cdc2=a832.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdk2=csa89 --reduce-for-goal cdc2=a837 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_G2_cdc2=a837.reduced.an
echo "---------------"
echo "M"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdc2=a803,cdc2=a809,cdc2=a832,cdc2=a837 --reduce-for-goal cdc25c=a816 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_M_cdc25c=a816.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdc2=a803,cdc2=a809,cdc2=a832,cdc2=a837 --reduce-for-goal cdc2=a791 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_M_cdc2=a791.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdc2=a803,cdc2=a809,cdc2=a832,cdc2=a837 --reduce-for-goal wee1=sa551 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_M_wee1=sa551.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/stories/stories.an --disable cdc2=a803,cdc2=a809,cdc2=a832,cdc2=a837 --reduce-for-goal cdc20=a858 -o MODELS/RB_E2F/analysis/an/stories/reduced/disable_prev_phase/stories_M_cdc20=a858.reduced.an
