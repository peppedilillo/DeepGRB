import os
import getpass
from pathlib import Path

user = getpass.getuser()

if user == 'rcrupi':
    PATH_TO_SAVE = "/beegfs/rcrupi/"
elif  user == 'riccardo':
    PATH_TO_SAVE = "C:/Users/riccardo/Documents/GBM_data/"
else:
    # PATH_TO_SAVE = "C:/Users/peppe/Dropbox/Progetti/NN_FOCuS/DeepGRB-master/data/"
    PATH_TO_SAVE = "D:/Dropbox/Progetti/NN_FOCuS/DeepGRB/data/"
FOLD_CSPEC_POS = "cspec"
FOLD_BKG = "bkg"
FOLD_PRED = "pred"
FOLD_NN = "nn_model"
FOLD_TRIG = "trig"
FOLD_PLOT = "plots"
FOLD_POSHIST = 'poshist'
db_path = os.path.dirname(__file__)
PATH_GRB_TABLE = PATH_TO_SAVE + "grb_classification/df_grb.csv"
# TODO: change above to use pathlib
if user == 'rcrupi':
    FOLD_RES = PATH_TO_SAVE + 'results/'
elif user == 'riccardo':
    FOLD_RES = "C:/Users/riccardo/Documents/GBM_data/" + '/results/'
else:
    FOLD_RES = Path(db_path).parent.parent / 'results/'
GBM_BURST_DB = Path(db_path).parent.parent / 'data/gbm_burst_catalog.db'
GBM_TRIG_DB = Path(db_path).parent.parent / 'data/gbm_trig_catalog.csv'
