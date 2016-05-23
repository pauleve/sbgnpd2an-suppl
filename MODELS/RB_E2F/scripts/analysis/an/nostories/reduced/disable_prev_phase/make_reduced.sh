./reducePhases.py --formc --nostories --log logs/nostories/disable_prev_phase/reducePhases.log --dir MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/ -i MODELS/RB_E2F/analysis/an/nostories/nostories.an phases

echo "---------------"
echo "G0"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a791=1,a858=1,a816=1,sa551=1 --reduce-for-goal a359=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_G0_a359=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a791=1,a858=1,a816=1,sa551=1 --reduce-for-goal a6=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_G0_a6=1.reduced.an
echo "---------------"
echo "earlyG0"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a359=1,a6=1 --reduce-for-goal a450=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_earlyG1_a450=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a359=1,a6=1 --reduce-for-goal a735=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_earlyG1_a735=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a359=1,a6=1 --reduce-for-goal a462=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_earlyG1_a462=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a359=1,a6=1 --reduce-for-goal a475=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_earlyG1_a475=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a359=1,a6=1 --reduce-for-goal a725=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_earlyG1_a725=1.reduced.an
echo "---------------"
echo "lateG1"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a450=1,a735=1,a462=1,a475=1,a725=1 --reduce-for-goal a524=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_lateG1_a524=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a450=1,a735=1,a462=1,a475=1,a725=1 --reduce-for-goal a532=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_lateG1_a532=1.reduced.an
echo "---------------"
echo "earlyS"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a524=1,a532=1 --reduce-for-goal a632=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_earlyS_a632=1.reduced.an
echo "---------------"
echo "lateS"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a632=1 --reduce-for-goal csa89=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_lateS_csa89=1.reduced.an
echo "---------------"
echo "G2"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable csa89=1 --reduce-for-goal a803=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_G2_a803=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable csa89=1 --reduce-for-goal a809=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_G2_a809=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable csa89=1 --reduce-for-goal a832=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_G2_a832=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable csa89=1 --reduce-for-goal a837=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_G2_a837=1.reduced.an
echo "---------------"
echo "M"
echo "---------------"
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a803=1,a809=1,a832=1,a837=1 --reduce-for-goal a791=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_M_a791=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a803=1,a809=1,a832=1,a837=1 --reduce-for-goal a858=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_M_a858=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a803=1,a809=1,a832=1,a837=1 --reduce-for-goal a816=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_M_a816=1.reduced.an
pint-export -i MODELS/RB_E2F/analysis/an/nostories/nostories.an --disable a803=1,a809=1,a832=1,a837=1 --reduce-for-goal sa551=1 -o MODELS/RB_E2F/analysis/an/nostories/reduced/disable_prev_phase/nostories_M_sa551=1.reduced.an
