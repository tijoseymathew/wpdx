import pytest
import clean_wpdx_sample_data

# @pytest.mark.skip
def test_clean_col_country_name():
    """
    Test the cleaning for column: "country_name"
    """
    assert clean_wpdx_sample_data.clean_col_country_name('NA') == 'NA'
    
def test_clean_col_adm1():
    """
    Test the cleaning for column: "adm1"
    """
    assert clean_wpdx_sample_data.clean_col_adm1('singapore') == 'SINGAPORE'
    assert clean_wpdx_sample_data.clean_col_adm1(' Singapore ') == 'SINGAPORE'
