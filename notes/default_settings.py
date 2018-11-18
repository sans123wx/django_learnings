from .forms import *

CUSTOMER_FORM_DICT = {
                'dj':CustomerForm_dj(initial={'group':1}),
                'wl':CustomerForm_wl(initial={'group':2}),
    }

CUSTOMER_FORM_CLASS_DICT = {
                'dj':CustomerForm_dj,
                'wl':CustomerForm_wl,
    }

UNIT_TYPE_FORM_DICT = {
                'dj':Unit_typeForm_dj(),
                'wl':Unit_typeForm_wl(),
    }

UNIT_TYPE_FORM_CLASS_DICT = {
                'dj':Unit_typeForm_dj,
                'wl':Unit_typeForm_wl,
    }

UNIT_MODEL_FORM_DICT = {
                'dj':Unit_modelForm_dj(),
                'wl':Unit_modelForm_wl(),
    }

UNIT_MODEL_FORM_CLASS_DICT = {
                'dj':Unit_modelForm_dj,
                'wl':Unit_modelForm_wl,
    }


OTHERS_LIST = (CUSTOMER_FORM_DICT , UNIT_TYPE_FORM_DICT , UNIT_MODEL_FORM_DICT)
