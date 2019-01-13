import pytest
import clean_wpdx_sample_data

# @pytest.mark.skip
def test_clean_col_country_name():
    """
    Test the cleaning for column: "country_name"
    """
    assert clean_wpdx_sample_data.clean_col_country_name('NA') == 'NA'


def test_clean_col_management():
    """
    Test the cleaning for column: "management"
    """
    assert clean_wpdx_sample_data.clean_col_management('Direct Government Operation?,') == 'Direct Government Operation'
    assert clean_wpdx_sample_data.clean_col_management('management') == 'Direct Government Operation'
