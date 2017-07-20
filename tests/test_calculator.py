############
# Standard #
############

###############
# Third Party #
###############
import pytest
import numpy as np
##########
# Module #
##########
from transfocate.lens       import Lens
from transfocate.calculator import Calculator
from transfocate.calculator import TransfocatorCombo

@pytest.fixture(scope='module')
def calculator():
    #Define prefocus lenses
    prefocus = [Lens(500., 100.0, 50.),
                Lens(300., 100.0, 25.)]
    #Define transfocator
    tfs = [Lens(500., 275., 25.),
           Lens(500., 280., 55.)]
    #Define Calculator
    return Calculator(xrt_lenses = prefocus,
                      tfs_lenses = tfs,
                      xrt_limit  = 400,
                      tfs_limit  = 750)

def test_calculator_combinations(calculator):
    #Eight possible transfocator combinations
    #Three possible prefocus lens choices
    assert len(calculator.combinations) == 8

def test_calculator_find_combinations(calculator):
    solutions = calculator.find_combinations(312.5, num_sol=1)
    #Assert we found the accurate combination
    assert np.isclose(solutions[0].image(0.0), 312.5, atol=0.1)

def test_TransfocatorCombo(calculator):
    #Define xrt and tfs lists
    xrt=Lens(300.0, 100., 25.)
    tfs=[Lens(500., 275., 25.),
         Lens(500., 280., 55.)]
    #Define TransfocatorCombo
    test_combo=TransfocatorCombo(xrt, tfs)
    assert np.isclose(test_combo.image(200.0), 297.18, atol=0.1)